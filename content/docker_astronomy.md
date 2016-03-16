Title: Docker in Astronomy
Category: blog
Tags: software
Slug: docker-in-astronomy
Email: caseyjlaw@gmail.com

###tl;dr

Installing software is a pain, especially for astronomers dealing with legacy or poorly-supported code. Docker instantly gives astronomers access to a large and growing set of packages (e.g., the 'astrostack') on any OS, environment, or even in the cloud.

### The Problem: We're Not Programmers

Astronomy, as in many academic fields, is plagued by poorly maintained software. I've made [my own contributions](http://github.com/caseyjlaw/rtpipe) to that category and I totally understand why it happens. We have science to do and papers to write. Maintaining software (let alone making it [documented](http://collectiveidea.com/blog/archives/2014/04/21/on-documentation-driven-development) and [tested](https://en.wikipedia.org/wiki/Test-driven_development)) takes time.

But the consequences of that problem become so much clearer when we need to use someone *else's* software. Excited about doing a new kind of analysis or using a new telescope? You will inevitably be using someone else's software to make the leap. As astronomers increasingly become interdisciplinary, we are increasingly obliged to use code of unknown provenance. This is particularly true of older telescopes, since the code was probably written back when Fortran was cool.

I came across this problem when I got excited about reproducing the analysis of pulsar data from the [Parkes radio observatory](http://www.parkes.atnf.csiro.au). This venerable instrument has made a fantastic contribution to the study fast radio transients, including most recently the discovery of [Fast Radio Bursts](http://www.astronomy.swin.edu.au/pulsar/frbcat). The Parkes teams leading this effort have done a nice job of [making their data public](http://supercomputing.swin.edu.au/data-sharing-cluster/parkes-frbs-archival-data) to enable others to reproduce and extend on their analysis. So why not give it a try?

It turns out that a basic exploration of pulsar data analysis requires half a dozen packages, written in a variety of languages and requiring a range of dependencies. Even experts in the field have stories about installing from scratch and losing days of work chasing compilation errors. It is so bad in pulsar astronomy that someone has written a [pulsar software installer](http://www.pulsarastronomy.net/wiki/Software/PSRSoft) that manages dependencies, build order, etc.. Ironically, the download link was broken when I first visited it last month (I contacted them and it has since been fixed).

### The Solution: Build Once, Share in Docker

Thankfully, some smart people have built an open, free tool that I think could make a big impact on the way astronomers work. That tool is [Docker](http://docker.com).

At its simplest, Docker is like a virtual machine; it creates portable operating systems that you can run your code in. Docker describes itself as a technology for building "containers", which are like a lightweight instance of a virtual machine with a process running inside (nice discussion [here](http://stackoverflow.com/questions/16047306/how-is-docker-different-from-a-normal-virtual-machine)). From the academic astronomer's perspective, we can just think of a container as being a frictionless way of running pre-built code. It is so easy that you can create a whole OS in a few seconds just to run a single command.

Docker is available on all operating systems and has [simple, well-documented installation instructions](https://docs.docker.com/engine/installation). Docker also hosts a "hub" service for sharing images; it functions much as github does for git code repositories. Docker is also based on [open standards](https://github.com/opencontainers), so there isn't so much worry about being locked into proprietary technology.

So, while I may have struggled to install the standard set of pulsar analysis softare packages, you will never need to! I have created a Docker image called ["pulsar-stack"](https://hub.docker.com/r/caseyjlaw/pulsar-stack) that includes the core libraries and dependencies for pulsar data analysis. Anyone with Docker can now access that image and run basic analysis steps. Currently, I'm pointing my students to [this demo](http://www.cv.nrao.edu/~sransom/PRESTO_search_tutorial.pdf) as an introduction.

Of course, Docker does require that the software in question be built once. But, then again, maybe someone else has already done that for you? [Peter Williams](https://twitter.com/pkgw) has already built the ["astro stack"](https://hub.docker.com/r/pkgw/jupyter-py2-astrostack). That Docker image includes a great sample of the most common astronomy software along with Jupyter (nee IPython) ready to go as an interactive computing environment.

### Introducing: dodo

In my own applications of Docker to astronomy, I've found it useful to abstract out the docker layer as much as possible. Astronomers don't want to learn Docker; they want to learn how to use some new astronomy software. In an effort to ease access, I've written "dodo" (as in "Docker do"; see [the repo](https://github.com/caseyjlaw/sidomo)). Think of dodo as being like "sudo" for docker images. You can run any command-line tool available in a Docker image from your current environment by prefixing the command with "dodo".

For example, to 'echo hello world' in the standard ubuntu image, type:

    > dodo -i ubuntu echo hello world
    Image ubuntu not found locally. Pulling ubuntu:latest from docker hub.
    ubuntu:latest:	  hello world
    
    
    Shutting down ubuntu:latest container

If you run that command a second time without specifying the image, it will take the first available locally. That is handy if you are running commands in an image like 'pulsar-stack'. As another example, if you'd like to inspect some pulsar data:

    > dodo -i caseyjlaw/pulsar-stack -- readfile GBT_Lband_PSR.fil
    Image caseyjlaw/pulsar-stack not found locally. Pulling from docker hub.
    caseyjlaw/pulsar-stack:	      Assuming the data is a SIGPROC filterbank file.


    1: From the SIGPROC filterbank file 'GBT_Lband_PSR.fil':
                  Telescope = GBT
                Source Name = Mystery_PSR
                    Backend = BPP
            Obs Date String = 2004-01-06T11:38:09
             MJD start time = 53010.48482638889254
                   RA J2000 = 16:43:38.1000
             RA J2000 (deg) = 250.90875        
                  Dec J2000 = -12:24:58.7000
            Dec J2000 (deg) = -12.4163055555556
    ...
    
    Shutting down caseyjlaw/pulsar-stack:latest container

This example shows how to use '--' to force the end of command-line options parsing for dodo.

dodo is just a wrapper of the Python API for Docker, but it uses a syntax that makes Docker feel like a part of your operating system, just like sudo. You can set environment variables to define a standard image to use or X11 display (some setup required for that). Your local directory is mounted in the Docker container by default, so data is seamlessly passed to/from the container.

### Use Cases

When barriers to using new and/or creaky software are removed, then new use cases emerge. I'm excited about applying docker and dodo to common problems like:

* How to run software demos for large groups.
* Packaging software and environments for 100% reproducible science.
* How to port your analysis to the cloud.

What use cases might come from putting your code in Docker? I'm eager to hear what software problems are limiting astronomers and thinking about how Docker can help.