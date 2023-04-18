# Install software, manage environments

*By C.Du [@snail123815](https://github.com/snail123815)*

```{contents}
---
depth: 3
---
```

## Why install in environments

Although it seems not reasonable for many beginners, but NO software can run by themselves. First and foremost, they require a good system to support their execution. The system will interpret the commands from the software and translate them to machine specific languages. For example the same command `1+1` will use different circuits on ARM and x86 CPUs. Usually these interpreters (which are also programs) have different versions and provide different access ports. What makes it more complex is that most programs also rely on specific versions of other programs to run. All of the other programs that one program depends on are called "dependencies".

With the increasing complexity of programs, it may develop into a status that only a very specific set of dependencies are needed and only these versions can run these programs. When one dependency is wrong, the dependencies of that dependency might also be wrong for some other dependencies. This will cause a chain reaction and lead us into a near un-resolvable situation, which we call it "[dependency hell](https://en.wikipedia.org/wiki/Dependency_hell)".

Well, this is very annoying. But to keep track of and also to develop new technologies, it is a very essential price we have to pay. Windows or MacOS have less of this issue because you have paid for the system provider to solve these issues for you. But on Linux, we rely on the community contributors, which are mostly volunteers. Thus, we are, by ourselves, responsible for managing all the dependencies to run a software. This is where `conda`, `mamba` and `micromamba` comes in handy.

[Conda](https://docs.conda.io/en/latest) is a software (sometimes also referred as package), dependency and environment management tool. [Mamba](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html) is a program helps conda to do the management faster, it requires conda to run. Well [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) is a tiny and ***standalone*** version of mamba. If you would like to understand how it works, it is best to understand some important [concepts](https://mamba.readthedocs.io/en/latest/user_guide/concepts.html) first, and then do some study. But if you want to get to work fast, here is some basics you need to know.

To install a software using one of the tools, you first need to create an environment for your software. During installation, the following things will be executed automatically.

1. Query online databases (we call these database "[channels](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html#conda-channels)") for your software
2. Get a list of all dependencies and check if the specific versions which match your current system architecture exists.
3. Download all programs and install them in the correct location **within the environment**.
4. If the programs installed need specific commands to be run after installation (eg. download a database), execute those commands.

Now your program is ready, but it will only work in this specific environment that you created. You can, of course, install as many programs you like in a single environment. But when the package management tool cannot resolve dependencies because of some cross dependency locks, it is good time to start a new environment.

## Multi-user system

Systems like [ALICE](../alice/alice_ibl.md) and our [IBL servers](../IBL_servers/Intro.md) are multi-user Linux systems. One challenge of managing multi-user systems is to provide all the softwares that everybody needs. It is very common that users need softwares that requires different versions of same software in the system. It becomes impossible to solve the issue without an environment manager. ALICE uses both [Environment Modules](https://modules.readthedocs.io/en/latest/index.html) and Conda environment manager; while for IBL servers, we use the later.

## Install an environment manager

Here I will only mention basic commands to manage Conda environments, for how to use Environment Modules on ALICE or other HPC systems, please check [this guide](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37749316/Using+available+software+-+Environment+Modules).

[This tutorial](./micromamba.md) will guide you to install or run `micromamba` on IBL Server BLIS and your computer. For conda (miniconda for minimal install of conda) and mamba install, please refer to [this link](https://docs.conda.io/en/latest/miniconda.html#) or [this link](https://mamba.readthedocs.io/en/latest/installation.html). Note, unless instructed (like [here](./micromamba.md)), please do not install any of this in a multi-user system.

## Basic commands

Once you have `conda`/`mamba`/`micromamba` configured, you can start using them. Note all commands are the same for the three programs, eg.:

`micromamba create ...` can be directly replaced by `conda create ...`, same for `mamba create ...`. All three commands will do the same thing. Which one to use depends on which software is installed in your system, use only one on the same system. Following instructions will use `micromamba` as example.

### Create an environment

To create an environment in the desired path (location):

```sh
micromamba create -p path/to/the/environment
```

You can also do:

```sh
micromamba create -n NAME_OF_ENVIRONMENT
```

It will create an environment with a name in your default environment directory, which is usually in your "HOME" directory. Note `-n` and `-p` cannot be used together, ie. you cannot have a "named" environment with non-default path. In HPC systems like ALICE, there is a specific quotation in your "HOME" directory, setting an environment up in your "HOME" directory will consume your quota very fast.

Note for `conda`, it used to be `conda env create ...`, but it is not used now.

### Activate an environment

```sh
micromamba activate path/to/the/environment
```

Or

```sh
micromamba activate NAME_OF_ENVIRONMENT
```

### Install software

After activating your desired environment, you can install a software (or in an other word package):

```sh
micromamba install -c CHANNEL_NAME SOFTWARE_NAME
```

`-c CHANNEL_NAME` means you tell `micromamba` to search this channel first. Some times your environment manager software is set to search for a certain set of channels, then `-c CHANNEL_NAME` can be escaped. You can configure this by your self.

Common channels are: `conda-forge`, `defaults`, `bioconda`. You can use many channels in one install command:

```sh
micromamba install -c conda-forge -c defaults -c bioconda SOFTWARE_NAME
```

You can also install many softwares in one command:

```sh
micromamba install -c CHANNEL_NAME SOFTWARE_NAME_A SOFTWARE_NAME_B SOFTWARE_NAME_C
```

Or a specific version of software:

```sh
micromamba install -c CHANNEL_NAME SOFTWARE_NAME=1.1
micromamba install -c CHANNEL_NAME SOFTWARE_NAME>1.0
micromamba install -c CHANNEL_NAME SOFTWARE_NAME>=1.0
```

Or combination:

```sh
micromamba install -c CHANNEL_NAME SOFTWARE_NAME_A=1.1 SOFTWARE_NAME_B>=3.0 SOFTWARE_NAME_C
```

When you get a specification `.yml` file, you can install all softwares described in it using:

```sh
micromamba install -f path/to/yml/file.yml
```

### Update a software 

To update a software to the latest version:

```sh
micromamba update -c CHANNEL_NAME SOFTWARE_NAME
```

Note it is not always possible to bring a software version to latest within an existing environment. Sometimes there are dependency locks that prevents you to update. If this happens, it is easier to create a new environment.

### Create environment and install software at the same time

```sh
micromamba create -p path/to/the/environment SOFTWARE_NAME_A SOFTWARE_NAME_B=3.2
```

You can also create an environment using specification `.yml` file:

```sh
micromamba create -f path/to/yml/file.yml
```

Note, depends on the specification file, your environment may be created in "HOME" directory. To avoid this, you need to create an environment first, then install all softwares using `micromamba install -f path/to/yml/file.yml` command.

\[ADVANCED:\] To understand how `.yml` file is made, check [this link](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually).