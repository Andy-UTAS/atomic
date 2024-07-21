# Course information

## Administration

The atomic physics component of the [atomic and nuclear physics](https://www.utas.edu.au/courses/cse/units/kya323-atomic-and-nuclear-physics) course will run for six weeks, beginning in week one and concluding at the end of week six. In previous years, the quantum mechanics covered advanced wave mechanics in the context of single-particle systems and a subsequent discussion of quantum mechanical systems. In contrast, this course begins with the foundations of quantum mechanics, taking an axiomatic approach to QM theory and using the wavefunction as a tool to model physical phenomena, and the latter part of the course devoted to quantum measurement and a generalised description of quantum states.

!!! Danger "Prerequisite knowledge"

    The content covered in atomic physics is testing, and without the firm bedrock of requisite knowledge and associated competencies, attempts to construct additional structures may be compromised. It is critical that one is comfortable with the following:

    - The principles and machinery of wave mechanics. Explicitly, an understanding of how physical systems and their evolution are modelled using the wave equation, along with a fluency in common examples (plane-wave solutions, travelling waves, etc.).
    - The foundations of quantum mechanics, including the (time dependent) Schrödinger equation and its solutions for common physical systems, and importantly, you must be comfortable with the physical concepts which underpin the mathematics. Fortunately, you have just completed an introductory quantum mechanics course, and it will be assumed that you are comfortable with the content.

    It is my intention that *you will be required* to call upon many of the other tools from the toolbox that you have been developing during your studies, with the explicit aim of further honing these tools, and maybe adding a few to the kit.

!!! info "This looks familiar"

    If you are experiencing a sense of _déjà vu_, that might be because you have encountered one of the other websites which are part of the quantum family of sites:
    - [Quantum mechanics](https://qm.utasphys.cloud.edu.au/)
    - [Solid-state physics](https://ssp.utasphys.cloud.edu.au/)

    In particular, much of the content from the [quantum site](https://qm.utasphys.cloud.edu.au/) is directly relevant to this course, and it could well be considered a sister site.


### Delivery of content

The course will be run in a traditional.

### Subject matter

The content for this course draws heavily from off the excellent text [Quantum Mechanics, A Paradigms Approach (2nd edition)](https://www.cambridge.org/wf/academic/subjects/physics/quantum-physics-quantum-information-and-quantum-computation/quantum-mechanics-paradigms-approach?format=AR) by [David H. McIntyre](https://science.oregonstate.edu/directory/david-h-mcintyre), and the book is a prescribed text for the course, that is, it is assumed that you will have access to this book. This particular text was chosen because of its considered approach to the ordering of content, its accessible rigour, and its delightful quirks and humour. It is also one of the best introductory texts on the subject, so whether you fall deeply into the quantum rabbit hole or pack it all in to cultivate vanilla in Madagascar, your will be able to polish up on the basics thanks to the text[^1].  

!!! question "Wait, are you actually prescribing a textbook?"

    Yes. And no, you haven't just been transported to 1993; I endeavour to employ evidence-based, best-practice methods for teaching, and this includes deploying many modern teaching aids, and also includes ensuring a glorious reference is prescribed. I will be working from the hardcopy, and I encourage you to do the same, although softcopies can be a more cost effective option.

#### Course outline

!!! summary "Course summary"

    This subject is designed to be a thorough introduction to quantum mechanics. As an experiment, cast your mind back to when you first started learning (classical) physics. Now, how many years has it been since you started? How much content have you learned? This course seeks to introduce you to the theory which supplants classical physics, which by its very nature means there is an enormous amount of content, and necessarily it is both more refined and complex. Therefore, the course really will be an introduction, a taster for what is out there in the quantum world; in the context of study at UTAS, the endpoint of this course will serve as the starting point of both the  atomic physics[KYA323](https://www.utas.edu.au/courses/cse/units/kya323-atomic-and-nuclear-physics) and solid-state physics [KYA322](https://www.utas.edu.au/courses/cse/units/kya322-statistical-physics-and-solid-state-physics) units, which are in essence, applications of quantum mechanics. The building blocks we shall study are the principles of nonrelativistic quantum theory and applications, starting with spin and quantum measurement in a state vector formalism and broadly moving onto implications and applications of quantum mechanics.

A rough outline of the course is as follows:

  1. The Stern-Gerlach experiment, state vectors, and Dirac (bra-ket) notation
  2. Matrix notation, general quantum systems
  3. Operators, Measurement, Spin 1 system
  4. Time evolution with Dirac - precession, neutrino oscillations, magnetic resonance (2-level atom)
  5. EPR paradox, Bell's inequalities, Schrödinger's Cat
  6. Applications

with approximately one week devoted to each topic, but with the natural ebb and flow ultimately dictating the timeline.

#### The notes

The notes are designed to be consumed in concert to the video content, with certain aspects highlighted differently in the different media, and in extreme cases with different paths used to arrive at the same destination. One of my aims is to expose you to different ways of thinking about problems, not just have the same method and then just "press play".

!!! danger  "Expected competencies"

    Content has been constructed with the assumption that the material is consumed sequentially, with sections often explicitly relying on results from previous work. I have also to placed _expected competency_ markers at the beginning of each section, outlining knowledge that I expect you to have seen in other areas of study, and importantly, **these are cumulative** from section to section.

!!! note  "Text reference"

    You will also encounter _text references_ at the beginning of each section, relating to the relevant content in the course text [Quantum Mechanics, A Paradigms Approach (2nd edition)](https://www.cambridge.org/wf/academic/subjects/physics/quantum-physics-quantum-information-and-quantum-computation/quantum-mechanics-paradigms-approach?format=AR)

!!! info "Computational content"

    Computational content, which is normally just the jupyter notebook associated with the section, also appears at the top of the page, but may also contain links to other software or pertinent computational material.

#### Slides



---

## Support

<figure>
  <img src="../images/battle-hogwarts.jpg">
  <figcaption> You are not on this journey alone: there are many avenues available to you to help you on the journey (depending on your inclination to watch fantasy movies in the 2000s, you may or not take comfort in the support Harry Potter received by those around him).</figcaption>
</figure>

The course materials as consumed through the _content download_ components are necessarily an individual effort, but in all other facets I strongly encourage collaboration. The structure of _content unpacking_ sessions is deliberately geared towards discussion, the exchange of ideas, and collective problem solving moreso than the execution of a solution finding program.  

!!! quote
    > ... there's something in science like the shine of the Patronus Charm, driving back all sorts of darkness and madness ...

    <p align=right> Eliezer Eudkowsky (Less Wrong), Harry Potter and the methods of rationality

### Computational resources

[:fontawesome-brands-python:](https://jove2021.cloud.edu.au/){ .md-button .md-button--primary class="text-center" style="margin-left: 45%; font-size:60px"}

As part of the course, it will be expected that you perform calculation and computations. You are welcome to do this in which ever language you prefer, but it is __strongly__ recommended that you use `Python`, and indeed, this is the only language that will be supported. In order to ensure equitable and easy access to Python computing resources, a [Jupyter Notebook](https://jupyter.org/) server has been established, which allows for one to write and execute code via a web browser. The server is named Jove[^2], and access is through the [JupyterHub portal](https://jove2021.cloud.edu.au/). You will need to create an account to start using the server, but beyond this is should be click and go. Should you experience any problems getting this up and running, please see the _computation_ section of [POLUS](https://polus.utasphys.cloud.edu.au/reference/computation/#cloud-usage).

Should you have a machine upon which you already have, or you wish to deploy, your own instance of `Python`, this is perfectly acceptable, but note that you will have to manually import the distributed materials into Jupyter. This can be effectively accomplished using the [clone functionality of GitHub](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) as  this is where the [course content](https://github.com/Andy-UTAS/qm) is hosted.

[^1]: No, I am not a [shill](#fnref:1 "I think we call them influencers now?"), I just really endorse the book. Although David, if you see this, contact me for my bank deets.
[^2]: For those wondering, [Jove is an alternate name](https://en.wikipedia.org/wiki/Jupiter_(mythology)) for the Roman god Jupiter.

---

## Bug catcher

![](images/Spr_RG_Bug_Catcher.png){align=left} Finally, this is more of a request than anything else, but should you find any errors in the content - this site, the distributed notebooks, the content download sessions, whatever - please let me know so I can correct the content, which is a major boon for everyone involved. Thanks!

--8<-- "includes/abbreviations.md"
