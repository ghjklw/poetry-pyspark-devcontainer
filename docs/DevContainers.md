# Development Containers

! To get started using the Dev Container, refer to the [getting started documentation](Getting-started.md).

Development Containers is an open specification for defining reproducible and quick to setup dev
environments. The project originates from Microsoft and is now strongly supported by several
partners. At this time, it is very well integrated with VS Code as well as a couple of other
services like Jetpack.io Devbox and GitHub Codespaces.

 > A Development Container (or Dev Container for short) allows you to use a container as a
 > full-featured development environment. It can be used to run an application, to separate tools,
 > libraries, or runtimes needed for working with a codebase, and to aid in continuous integration
 > and testing. Dev containers can be run locally or remotely, in a private or public cloud.

 This project uses 3 files to configure the development container:

- `Dockerfile`: this defines a custom dev container Docker image for this project. This image is
   designed to:
  - Provide the expected version(s) of Python (using PyEnv)
  - Install Apache Spark and Hadoop with the right version
  - Install Tox and Pre-Commit
  - Install Poetry
- `initialize.sh`: it runs on each container startup and checks:
  - Git configuration
  - Initialisation of Poetry project
  - Pre-commit hooks installation
- `devcontainer.json`: it ties it all together and:
  - Defines VS Code extensions to be installed automatically.
  - Defines VS Code settings to be implemented on container startup.
