from pathlib import Path
from logging import getLogger

from mkdocs.structure.files import File
from mkdocs.plugins import BasePlugin
import nbconvert
from nbconvert.preprocessors import ExtractOutputPreprocessor
from traitlets.config import Config
import jupytext
import os

log = getLogger("mkdocs.plugins.execute")
log.setLevel("INFO")

output_extractor = ExtractOutputPreprocessor()
output_extractor.extract_output_types = (
    output_extractor.extract_output_types
    | {'application/vnd.plotly.v1+json'}
)


class AlreadySavedFile(File):
    def copy_file(self, dirty=False):
        pass


exporter = nbconvert.TemplateExporter(
    config=Config(dict(
        TemplateExporter=dict(
            preprocessors=[
                nbconvert.preprocessors.ExecutePreprocessor,
                output_extractor,
            ],
            exclude_input=False,
            extra_template_basedirs=[str(Path(__file__).parent / "templates")],
            template_file='mkdocs_markdown/index.md.j2',
        ),
        NbConvertBase=dict(
            display_data_priority=[
                'application/vnd.plotly.v1+json',
                'text/html',
                'text/markdown',
                'image/svg+xml',
                'text/latex',
                'image/png',
                'image/jpeg',
                'text/plain'
            ]
        ),
    ))
)
writer = nbconvert.writers.FilesWriter(build_directory=str())


class Plugin(BasePlugin):
    def __init__(self):
        self.output_map = {}

    # This function has been changed to allow a bypass for code blocks, which allows the code to be rendered
    def on_page_read_source(self, page, config, **kwargs):
        os.environ["PLOTLY_RENDERER"] = "plotly_mimetype"
        src_path = page.file.abs_src_path
        notebook = jupytext.read(src_path)
        log.info(f"Processing {src_path}")

        # Custom logic to bypass execution for certain code blocks
        source = jupytext.writes(notebook, fmt="md")
        lines = source.splitlines()
        new_lines = []
        skip_execution = False

        for line in lines:
            if line.startswith("~~~python"):
                skip_execution = True
                line = "```python"  # Convert back to normal code block for rendering
            elif line.startswith("```python"):
                skip_execution = False

            if skip_execution:
                new_lines.append(line)
            else:
                new_lines.append(line)

        # Re-create the notebook from the modified source
        modified_source = "\n".join(new_lines)
        notebook = jupytext.reads(modified_source, fmt="md")

        if not skip_execution:
            output, resources = exporter.from_notebook_node(
                notebook,
                resources={
                    "unique_key": page.file.src_path,
                    "output_files_dir": "_execute_outputs",
                    "metadata": {
                        "path": Path(src_path).parent
                    }
                }
            )
            build_directory = Path(config["site_dir"])
            nbconvert.writers.FilesWriter(
                build_directory=str(build_directory)
            ).write(output, resources, "out.md")
            out = build_directory / "out.md"
            source = out.read_text()
            out.unlink()
        else:
            source = modified_source

        self.output_map[src_path] = list(resources.get("outputs", {}).keys())
        return source

    # def on_page_read_source(
    #     self, page, config, **kwargs
    # ):
    #     os.environ["PLOTLY_RENDERER"] = "plotly_mimetype"
    #     src_path = page.file.abs_src_path
    #     notebook = jupytext.read(src_path)
    #     log.info(f"Executing {src_path}")
    #     output, resources = exporter.from_notebook_node(
    #         notebook,
    #         resources={
    #             "unique_key": page.file.src_path,
    #             # Compute the relative URL
    #             "output_files_dir": "_execute_outputs",
    #             "metadata": {
    #                 "path": Path(src_path).parent
    #             }
    #         }
    #     )
    #     build_directory = Path(config["site_dir"])
    #     nbconvert.writers.FilesWriter(
    #         build_directory=str(build_directory)
    #     ).write(output, resources, "out.md")
    #     out = build_directory / "out.md"
    #     source = out.read_text()
    #     out.unlink()
    #     self.output_map[src_path] = list(resources["outputs"].keys())
    #     return source

    def on_page_markdown(self, markdown, page, config, files):
        src_path = page.file.abs_src_path
        for file in self.output_map.pop(page.file.abs_src_path):
            files.append(
                AlreadySavedFile(
                    str(file),
                    config['docs_dir'],
                    config['site_dir'],
                    config['use_directory_urls']
                )
            )


plugin_instance = Plugin()
on_page_read_source = plugin_instance.on_page_read_source
on_page_markdown = plugin_instance.on_page_markdown
