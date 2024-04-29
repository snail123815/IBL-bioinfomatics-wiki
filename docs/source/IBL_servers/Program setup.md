# Program setup

*By C.Du [@snail123815](https://github.com/snail123815)*

This tutorial provides guidance of creating environments and install programs in the created environments using `micromamba`. To install programs that are not available in any conda repositories, please ask administrators for help.

## What is an environment

An environment created by conda, micromamba, or pyvenv is essentially just a folder/directory on the disk. This directory contains configuration files and dependency programs. It has a special structure to allow environment manager programs (conda/micromamba/pyvenv) to read. Do not change any content in an environment directory manually, except you understand how environment manager works and know what you are doing.

## Install a program

Please make sure you have [micromamba ready to use](./Execute%20programs.md#prepare-micromamba). Before setting up virtual environments, it is highly recommended to setup a `~/.mambarc` file with the following content. It is explained in the later [section](#setting-up-config-file).

```YAML
envs_dirs:
  - /vol/local/conda_envs
pkgs_dirs:
  - /vol/local/.conda_cache/[USERNAME]
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
```

Create an environment to host the software or a pipe line you want to run. Then you have all control over the environment you created.

```{code-block} shell
---
caption: This block includes prompt, select command to copy
---
# 0. Make sure you have your shell initiated with micromamba (skip if done before)
[user@blis ~]$ micromamba shell init -s bash -p ~/micromamba-base
[user@blis ~]$ source ~/.bashrc
[user@blis ~]$ micromamba activate
(base) [user@blis ~]$

# 1. Create environment called multi-omics and activate it
(base) [user@blis ~]$ micromamba create -p /vol/local/conda_envs/multi-omics
(base) [user@blis ~]$ micromamba activate /vol/local/conda_envs/multi-omics

# 2. Install software, eg. python
(/vol/local/conda_envs/multi-omics) [user@blis ~]$ micromamba install -c conda-forge python
```

:::{tip}
I usually create a "soft link" to `/vol/local/conda_envs/` in home directory for easier access to all the environments. For example,

```sh
ln -s /vol/local/conda_envs/ ~/genvs
```

Then I can replace all `/vol/local/conda_envs/` with `~/genvs`, much simpler.

Advanced method (**do not do** if you don't know what `ln -s` means and its restrictions) is to soft link the shared environment directory to micromamba base directory:

```sh
ln -s /vol/local/conda_envs/ ~/micromamba-base/envs
```

This needs to be done when the target directory does not exist (before creating any "named" environment). The advantage of this method is that you can create environment in the shared environment directory using `-n` and may be more compatible with most program tutorial (the old ones usually assume you have sudo rights and unlimited HOME directory, which is not the case in any of the server systems.) Use this method with caution!
:::

### Do not follow tutorial with yml/yaml file

`.yml` or `.yaml` file format is usually configuration files written with a variant of markup language, describing the required programs and usually their versions, i.e. *dependencies*.

Many times you will find a tutorial to setup a conda environment by `conda env create -f minimotif.yml minimotif`. Please **DO NOT** follow this by simply replacing `conda env` with `micromamba`.

In these cases, the `.yml` file usually looks like:

```YAML
name: MiniMotif
channels:
  - conda-forge
  - bioconda
  - defaults
dependencies:
  - _libgcc_mutex=0.1
  - _openmp_mutex=4.5
  - alsa-lib=1.2.8
  - attr=2.5.1
  - biopython=1.81
  - ...
```

You need to open this file using a text editor, remove the `name:` line and save the file. The `name:` line is telling conda or micromamba to install the environment with `-n` switch, or install the dependencies it is not compatible with `-p` switch.

Then create the environment:

```{code-block} shell
---
caption: This block includes prompt, select command to copy
---
# 1. Create environment using -p
(base) [user@blis ~]$ micromamba create -p /vol/local/conda_envs/MiniMotif
(base) [user@blis ~]$ micromamba activate /vol/local/conda_envs/MiniMotif
# 2. Install all dependencies using the .yml file
(/vol/local/conda_envs/MiniMotif) [user@blis ~]$ micromamba install -f minimotif.yml
```

Now it should do the installation, follow the screen to continue.

Why not combine into one single command? Because `-p` and `-f` parameters are not compatible.

After installation, you can try your program to see if the help function works:

```{code-block} shell
---
caption: This block includes prompt, select command to copy
---
(/vol/local/conda_envs/MiniMotif) [user@blis ~]$ python minimotif.py -h
usage:
-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
Generic command:
     minimotif.py -i [binding_profiles] -G [genome] -O [outdir]
_____________________________________________________________________________________________
Mandatory arguments:
    -G  Provide a genbank file of the genome of interest for TFBS scanning
    ...
```

Do not forget to **deactivate** your environment before doing anything else, unless you know what you are doing. Your current activated environment is shown in the parenthesis before your command line. To deactivate:

```{code-block} shell
---
caption: This block includes prompt, select command to copy
---
(/vol/local/conda_envs/MiniMotif) [user@blis ~]$ micromamba deactivate
(base) [user@blis ~]$
```

## Setting up config file

The program micromamba uses a config file located in your home folder: `~/.mambarc` to store your specific configurations. Well `micromamba` *not only* check `~/.mambarc` file, but also uses `~/.condarc`, one of them is enough. (The later is used by conda)

The config file has few convenient options. On BLIS, please put these contents in the config file:

```YAML
envs_dirs:
  - /vol/local/conda_envs
pkgs_dirs:
  - /vol/local/.conda_cache/USERNAME
```

- `env_dirs` will allow `micromamba env list` command to list all environments inclduing our shared environments. (ignore this line if you have soft linked it to `~/micromamba_base/envs`)
- `pkgs_dirs` set the cache dir, it is a easy-to-clean location.

You can also add after the above contents:

```YAML
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
```

- `channels` will allow you to skip -c option when installing packages
- `auto_activate_base` will activate your base environment, by this, you will be using eg. python from your base environment rather than a system one.

If you need more information on how to use micromamba on your own machine, please refer to our [micromamba instruction](../basic_tools/micromamba.md).

## Premissions of shared environments on BLIS

All files generated by `micromamba`, including all environments created are by default belongs to the group `condablis`, all group members can activate these environments. **Only** the owner who created the environment can add or remove package. If you want to let others change your environment, you need to specifically change the premission:

```sh
chmod -R g+w /vol/local/conda_envs/yourEnvironment
```

**Anyone who changed this environment should do this *again*** for others to change it. Or, the owner can remove this premission after changing:

```sh
chmod -R g-w /vol/local/conda_envs/yourEnvironment
```

This restriction is due to the limitations of the Linux file system, which are intentional for safety reasons.
