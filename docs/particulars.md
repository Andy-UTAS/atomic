# Course information

## Administration

The atomic physics component of the [atomic and nuclear physics](https://www.utas.edu.au/courses/cse/units/kya323-atomic-and-nuclear-physics) course will run for six weeks, beginning in week one and concluding at the end of week six. In previous years, atomic physics acted to reenforce the content discussed in the advanced wave mechanics and quantum mechanics course, spending time on trying to understand atomic structure in a piecewise manner. In contrast, this course begins where the quantum mechanics course left off: the conclusion for most introductory quantum courses is the full solution to the Schrödinger equation for the hydrogen atom, and poking at the structure of helium. We take these foundations, and construct a framework for understanding and predicting the structure of more complex systems, and importantly, the kind of systems would encounter in wild. Moreover, we will explicitly discuss how one designs and executes experiments in a real-world context with the aim to cultivate an appreciation for quantum systems actually being accessible, and not just problems which appear on whiteboards.

!!! Danger "Prerequisite knowledge"

    The content covered in atomic physics is testing, and without the firm bedrock of requisite knowledge and associated competencies, attempts to construct additional structures may be compromised. It is critical that one is comfortable with the following:

    - The principles and machinery of wave mechanics. Explicitly, an understanding of how physical systems and their evolution are modelled using the wave equation, along with a fluency in common examples (plane-wave solutions, travelling waves, etc.).
    - The foundations of quantum mechanics, including the (time dependent) Schr$\"{o}$dinger equation and its solutions for common physical systems, and importantly, you must be comfortable with the physical concepts which underpin the mathematics. Fortunately, you have just completed an introductory quantum mechanics course, and it will be assumed that you are comfortable with the content.

    It is my intention that *you will be required* to call upon many of the other tools from the toolbox that you have been developing during your studies, with the explicit aim of further honing these tools, and maybe adding a few to the kit.

!!! info "This looks familiar"

    If you are experiencing a sense of d&#xE9j&#xE0 vu, that might be because you have encountered one of the other websites which are part of the quantum family of sites:

    - [Quantum mechanics](https://qm.utasphys.cloud.edu.au/)
    - [Solid-state physics](https://ssp.utasphys.cloud.edu.au/)

    In particular, much of the content from the [quantum site](https://qm.utasphys.cloud.edu.au/) is directly relevant to this course, and it could well be considered a sister site.


### Delivery of content

The course will be run in a traditional.

### Subject matter

The content for this course draws heavily from a set of reference texts:

1. The excellent text [Quantum Mechanics, A Paradigms Approach (2nd edition)](https://www.cambridge.org/wf/academic/subjects/physics/quantum-physics-quantum-information-and-quantum-computation/quantum-mechanics-paradigms-approach?format=AR) by [David H. McIntyre](https://science.oregonstate.edu/directory/david-h-mcintyre)
2. The go-to reference for basic atomic physics, aptly named [Atomic Physics](https://academic.oup.com/book/52827) by [Christopher J. Foot](https://www.physics.ox.ac.uk/our-people/foot)
3. The intensely thorough [Quantum and Atom Optics](https://atomoptics.uoregon.edu/~dsteck/teaching/quantum-optics) by [Daniel A. Steck](https://steck.us/academic.html)

With Foot being the prescribed text for the course, that is, it is assumed that you will have access to this book. This was chosen as McIntyre is the prescribed text for [Quantum mechanics](https://qm.utasphys.cloud.edu.au/), and the two are somewhat complimentary. Steck is a glorious reference - and freely available - but our atomic physics journey only scratches the surface of the material covered in these notes, and as such it is not appropriate as a prescribed text. With this trilogy of titles, you will be well placed to understand why atoms are the way they are, and how to make them do what you want them to do. It is also one of the best introductory texts on the subject, so whether you fall deeply into the quantum rabbit hole or pack it all in to cultivate vanilla in Madagascar, your will be able to polish up on the basics thanks to the text.  

!!! question "Wait, are you actually prescribing textbooks?"

    Yes. And no, you haven't just been transported to 1993; I endeavour to employ evidence-based, best-practice methods for teaching, and this includes deploying many modern teaching aids, and also includes ensuring a glorious reference is prescribed. I will be working from hardcopies, and I encourage you to do the same, although softcopies can be a more cost-effective option.

#### Course outline

Make yourself at home for our journey into atomic and nuclear physics. In this course we are going to study fundamental physical systems, which, on their surface can often appear simple, but are delightfully rich, engaging, and powerful. A testament to the foundational nature, utility, and continuing importance of the topics covered in this course is that during the period between 1995 - 2017, the fields of atomic and particle physics accounted for [25% of all Nobel prizes in science that were awarded](https://www.nature.com/nature-index/news/these-five-scientific-fields-win-the-most-nobel-prizes). It is with this backdrop that we shall set out and seek to understand the fundamental properties and interactions of atoms and nuclei.

!!! summary "Course summary"

    This subject is designed to be a meaningful introduction to atomic physics. Hopefully your foray into the world of quantum mechanics was enjoyable, but it is almost inevidable that it left you with more questions than answers. Notably, most introductory quantum mechancis courses finish at the same spot: with the full-blown calculation of the energy eigenstates of the Hamiltonian for the hydrogen atom (in the nonrelativistic case). Whilst such a calculation is a triumph in its own right, the first question that you may ask is: "does the hydrogen emission spectrum match my prediction". The answer is no, and there are many distinct ways in which it does not match, due to different phenomena which arise from considering the atom in more detail. It is not the intention of this course the completely describe the hydrogen atom, on the contrary, we want to be able to describe all the atoms! This will mean developing theories and methods of calculation for multielectron systems, ensembles of atoms, and even touching on what happens with multiple nuclei. If your quantum mechanics course was a taster for what is out there in the quantum world; atomic physics narrows the focus of quantum mechanics to the measurement, manipulation, and evolution of atoms and their internal electronic transitions, our understanding of which provides our best tests of how the universe works, along with tests of how well we can predict how the universe works. The building blocks we shall study are basic atomic physics, angular momentum coupling, systems of indistinguishable particles, enesmbles of atoms, modern applications of atomic physics and molecular physics. It is worth noting that I am an experimental physicist by training, and it is my duty to ensure that experimental details permiate all that we study, because at the end of the day, we do need to actually make measurements to test our scientific theories: without this, one lives in a world of fiction.

A rough outline of the course is as follows:

1. Early atomic physics, the hydrogen atom, computational methods
2. Hyperfine structure, angular momentum coupling
3. Identical particles, transitions
4. The density matrix
5. Applications
6. Molecular physics

with approximately one week devoted to each topic, but with the natural ebb and flow ultimately dictating the timeline.

#### The notes

The notes on this site are designed to be consumed in concert the content from class, with certain aspects highlighted differently in the different media; in extreme cases, different paths are used to arrive at the same destination. One of my aims is to expose you to different ways of thinking about problems, not just have the same method and then just "press play".

!!! danger  "Expected competencies"

    Content has been constructed with the assumption that the material is consumed sequentially, with sections often explicitly relying on results from previous work. I have also to placed _expected competency_ markers at the beginning of each section, outlining knowledge that I expect you to have seen in other areas of study, and importantly, **these are cumulative** from section to section.

!!! note  "Text reference"

    You will also encounter _text references_ at the beginning of each section, relating to the relevant content in the [course texts](#subject-matter)

!!! info "Computational content"

    Computational content, which is normally just the jupyter notebook associated with the section, also appears at the top of the page, but may also contain links to other software or pertinent computational material.

#### Slides

In the first iteration of this class, content will be deliverd with a mixture of curated presentation material and whiteboarding. Below you can find slides for the in-class presentations, but note that content is delibrately missing from these collections - usually many whole slides or sections - and this content will be covered in class.

<div class="grid cards" markdown>

-   :fontawesome-solid-atom:{ .lg .middle } __Week 1__

    ---

    Introductory atomic physics, the hydrogen atom, and computational methods for real systems

    [:material-microsoft-powerpoint: Week 1](../hosted/Week1.pdf)

-   :fontawesome-solid-arrows-spin:{ .lg .middle } __Week 2__

    ---

    Hyperfine structure, angular momentum, and the coupling of angular momentum

    [:material-microsoft-powerpoint: Week 2](../hosted/Week2.pdf)


-   :material-content-copy:{ .lg .middle } __Week 3__

    ---

    Identical particles, multielectron atoms, and atomic transitions

    [:material-microsoft-powerpoint: Week 3](../hosted/Week3.pdf)

-   :material-matrix:{ .lg .middle } __Week 4__

    ---

    The density matrix, the optical bloch equations, Rabi oscillations

    [:material-microsoft-powerpoint: Week 4](../hosted/Week4.pdf)

-   :octicons-clock-16:{ .lg .middle } __Week 5__

    ---

    Atomic timekeeping, quantum sensing, mechanical effects of quantum interactions

    [:material-microsoft-powerpoint: Week 5](../hosted/Week5.pdf)

-   :material-beaker:{ .lg .middle } __Week 6__

    ---

    Molecular physics, quantum chemistry

    [:material-microsoft-powerpoint: Week 6](#)

</div>

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

As part of the course, it will be expected that you perform calculation and computations. You are welcome to do this in which ever language you prefer, but it is __strongly__ recommended that you use `Python`, and indeed, this is the only language that will be supported. In order to ensure equitable and easy access to Python computing resources, a [Jupyter Notebook](https://jupyter.org/) server has been established, which allows for one to write and execute code via a web browser. The server is named Jove[^1], and access is through the [JupyterHub portal](https://jove2021.cloud.edu.au/). You will need to create an account to start using the server, but beyond this is should be click and go. Should you experience any problems getting this up and running, please see the _computation_ section of [POLUS](https://polus.utasphys.cloud.edu.au/reference/computation/#cloud-usage).

Should you have a machine upon which you already have, or you wish to deploy, your own instance of `Python`, this is perfectly acceptable, but note that you will have to manually import the distributed materials into Jupyter. This can be effectively accomplished using the [clone functionality of GitHub](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) as this is where the [course content](https://github.com/Andy-UTAS/atomic-physics) is hosted.

[^1]: For those wondering, [Jove is an alternate name](https://en.wikipedia.org/wiki/Jupiter_(mythology)) for the Roman god Jupiter.

---

## Bug catcher

![](images/Spr_RG_Bug_Catcher.png){align=left} Finally, this is more of a request than anything else, but should you find any errors in the content - this site, the distributed notebooks, whatever - please let me know so I can correct the content, which is a major boon for everyone involved. Thanks!

--8<-- "includes/abbreviations.md"
