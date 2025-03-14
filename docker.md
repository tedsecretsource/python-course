# Overview

Docker is, for me, the easiest way to bring up a python environment for fooling around. If you have Docker installed, you can run the following command to bring up a python environment:

```bash
docker run -it --rm python:3.13 bash
```

It's that simple. Also, you can modify the version number to use the exact version you are interested in. If you want to be able to run python scripts, you can mount a volume to the container like this:

```bash
docker run -it --rm -v $(pwd):/app python:3.13 bash
cd /app
ls -lha
```

