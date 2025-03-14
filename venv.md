# venv

`venv` is a tool that allows you to create isolated Python environments for your projects. This means that each project can have its own dependencies, regardless of the dependencies of other projects. `venv` is commonly used by Python developers who are working on Python projects that are not (normally) web applications to manage dependencies, versions, and environments. This could be for a pipeline, a data analysis project, or a machine learning model.

## Pros

- **Isolation**: Each project can have its own dependencies, regardless of the dependencies of other projects.
- **Dependency management**: You can install and uninstall dependencies without affecting other projects.
- **Version management**: You can have different versions of Python installed on your system and use them in different projects.
- **Environment consistency**: You can ensure that all developers working on a project have the same environment.

## Cons

- **Complexity**: It can be difficult to set up and manage virtual environments, especially for beginners.
- **Disk space**: Each virtual environment takes up disk space, which can add up if you have many projects.
- **Activation**: You need to activate the virtual environment before you can use it, which can be cumbersome.
- **Compatibility**: Virtual environments can sometimes cause compatibility issues with certain packages.

## Practical example

Let's say you have two projects: Project A and Project B. Project A requires `numpy` version 1.19.2, while Project B requires `numpy` version 1.20.0. If you use a virtual environment for each project, you can install the required version of `numpy` in each environment without conflicts.

In the following examples it is highly likely you will see some errors. Explaining why these errors occur is way beyond the scope of this lesson but should illustrate one reason why venvs should not be your first choice.

### Project A

```bash
# Create a virtual environment for Project A
python3 -m venv project_a # Creates a virtual environment in a new directory called project_a

# Activate the virtual environment
source project_a/bin/activate

# Install numpy version 2.2.1
pip install numpy==2.2.1

# verify the numpy version
pip freeze | grep numpy

# Deactivate the virtual environment
deactivate
```

### Project B

```bash
# Create a virtual environment for Project B
python3 -m venv project_b # Creates a virtual environment in a new directory called project_b

# Activate the virtual environment
source project_b/bin/activate

# Install numpy version 2.2.3
pip install numpy==2.2.3

# verify the numpy version
pip freeze | grep numpy

# Deactivate the virtual environment
deactivate
```

In this example, Project A and Project B have their own isolated environments with the required dependencies installed. This prevents conflicts and ensures that each project runs correctly.

These days Python is much more stable than it was prior to version 2.6 but just to demonstrate how cool venvs can be, let's recreate the projects above and install Python 3.9 in project A and Python 3.13 in project B.

### Project A

```bash
# Create a virtual environment for Project A
python3.9 -m venv project_a

# Activate the virtual environment
source project_a/bin/activate

# Install numpy
pip install numpy

# Verify the Python version
python --version

# verify the numpy version
pip freeze | grep numpy

# Deactivate the virtual environment
deactivate
```

### Project B

```bash
# Create a virtual environment for Project B
python3 -m venv project_b

# Activate the virtual environment
source project_b/bin/activate

# Install numpy
pip install numpy

# Verify the Python version
python --version

# verify the numpy version
pip freeze | grep numpy

# Deactivate the virtual environment
deactivate
```