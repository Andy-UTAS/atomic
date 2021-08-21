# Course information

## Administration

The solid-state component of the course will run for seven weeks, beginning in week 7 and concluding at the end of semester. In previous years, the solid-state physics and semiconductor physics components of the course have been explicitly differentiated; however, in this iteration, the two will be more closely intertwined, with semiconductors being considered a flourish to the foundations that we shall construct during our adventures in describing matter.

!!! Danger "Prerequisite knowledge"

    The content covered in this course is complicated, and without the frim bedrock of requisite knowledge and associated competencies, attempts to construct additional structures may be compromised. It is critical that one is comfortable with the following:

    - The principles and machinery of quantum mechanics. Explicitly, an understanding of how physical systems and their evolution are modelled using the Schrödinger equation, along with a fluency in common examples (e.g. particle in a box, harmonic oscillator, the hydrogen atom), and a vague familiarity with Dirac notation is assumed.
    - Thermodynamic quantities and concepts abound, with statistical mechanics looming large in the background. Conveniently, you have just completed a course in statistical mechanics, but it will be assumed that you are comfortable with the content

    It is my intention that you will be required to call upon many of the other tools from the toolbox that you have been developing during your studies, with the explicit aim of further honing these tools, and maybe adding a few to the kit.

### Delivery of content

The course will operate in a flipped-mode configuration, whereby the undergirding principle is that your out-of-class time is used to consume prepared content (e.g. _lectures_) and scheduled times are used for discussions in a problem-based learning framework. I prefer to refer to the lecture-style material as the _content download_, and interactive, active-learning sessions as the _content unpacking_ component.

### Subject matter

The content for this course draws heavily from off the excellent text [The Oxford Solid State Basics](https://global.oup.com/academic/product/the-oxford-solid-state-basics-9780199680771?cc=au&lang=en&) by [Steven H. Simon](https://www-thphys.physics.ox.ac.uk/people/SteveSimon/), and the book is a prescribed text for the course, that is, it is assumed that you will access to this book. This particular text was chosen because of its concise discussion of the content, its accessibility, and the wry whit which permeates the content, in concert with the availability of [freely distributed pre-print of the book](http://www-thphys.physics.ox.ac.uk/people/SteveSimon/condmat2012/LectureNotes2012.pdf). I will be working from the printed text, and I encourage you to do the same.

!!! warning "Unsupported material"

    Steven himself has said that the preprint is roughly 85% of the book; however, if you elect to work from the preprint, you do so at your own risk.

#### Course outline

!!! summary "Course summary"

    This subject is designed to serve as _an introduction_ into the field of solid-state physics. Solid-state physics is the largest field of condensed matter physics, which itself is the largest branch of physics, and so there is only so material we will cover. The trajectory we shall take begins with _bulk_ descriptors of solids, into considering the fundamental nature of solids, collective behaviour within solids, and the place of these systems in the real world.

A rough outline of the course is as follows:

  1. An introduction to solid-state physics
  2. The structure of materials
  3. Solids in one dimension
  4. The geometry of solids
  5. Electrons in solids
  6. Magnetism

with approximately one week devoted to each topic, but with the natural ebb and flow ultimately dictating the timeline.

??? abstract "_Content download_"

    A brief summary of the topics discussed in the _content download_ sessions is shown below:

    | Video       | Topic(s) discussed                   |
    | ----------- | ------------------------------------ |
    | w0v1        | An introduction to solid-state physics |
    | w1v1        | The Einstein model of solids  |
    | w1v2        | The Debye model of solids  |
    | w1v3        | The Drude model of metals |
    | w2v1        | The Sommerfeld free-electron model |
    | w2v2        | Chemistry 101 |

---

## Support

<figure>
  <img src="../images/zelda.png">
  <figcaption> You are not on this journey alone: there are many avenues available to you to help you on the journey (depending on your inclination to play antiquated video games, you may recognise this as a scene from <a href="https://en.wikipedia.org/wiki/The_Legend_of_Zelda">The Legend of Zelda</a>).</figcaption>
</figure>

### "_We are all in this together_"

The course materials as consumed through the _content download_ components are necessarily an individual effort, but in all other facets I strongly encourage collaboration. The structure of _content unpacking_ sessions is deliberately geared towards discussion, the exchange of ideas, and collective problem solving moreso than the execution of a solution finding program.  

### Computational resources

[<i class="fab fa-python fa-5x"></i>](https://jove2021.cloud.edu.au/){ .md-button .md-button--primary class="text-center" style="margin-left: 45%"}

As part of the course, it will be expected that you perform calculation and computations. You are welcome to do this in which ever language you prefer, but it is __strongly__ recommended that you use `Python`, and indeed, this is the only language that will be supported. In order to ensure equitable and easy access to Python computing resources, a [Jupyter Notebook](https://jupyter.org/) server has been established, which allows for one to write and execute code via a web browser. The server is named Jove[^1], and access is through the [JupyterHub portal](https://jove2021.cloud.edu.au/). You will need to create an account to start using the server, but beyond this is should be click and go.

Should you have a machine upon which you already have, or you wish to deploy, your own instance of `Python`, this is perfectly acceptable, but note that you will have to manually import the distributed materials into Jupyter. This can be effectively accomplished using the [clone functionality of GitHub](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) as  this is where the [course content](https://github.com/Andy-UTAS/Solid-state) is hosted.

[^1]: For those wondering, [Jove is an alternate name](https://en.wikipedia.org/wiki/Jupiter_(mythology)) for the Roman god Jupiter.

---

## Bug catcher

Finally, this is more of a request than anything else, but should you find any errors in the content - this site, the distributed notebooks, the content download sessions, whatever - please let me know so I can correct the content, which is a major boon for everyone involved. Thanks!

--8<-- "includes/abbreviations.md"
