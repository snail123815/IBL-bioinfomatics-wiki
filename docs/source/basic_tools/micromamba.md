# Setup `micromamba`

*By C.Du [@snail123815](https://github.com/snail123815)*

```{contents}
---
depth: 3
---
```

`micromamba` is a standalone `conda` replacement. About what is micromamba and how to use: https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html

## BLIS users

BLIS have `micromamba` in your PATH, but if you are using it for the first time, you need to run the following command and **restart your shell** after it finishes:

(Assuming you are using **bash**)

```shell
micromamba shell init -s bash -p ~/micromamba-base
```

After a shell restart, run the following command to check:

```shell
micromamba info
```

Output should be

```
                                          __
         __  ______ ___  ____ _____ ___  / /_  ____ _
        / / / / __ `__ \/ __ `/ __ `__ \/ __ \/ __ `/
       / /_/ / / / / / / /_/ / / / / / / /_/ / /_/ /
      / .___/_/ /_/ /_/\__,_/_/ /_/ /_/_.___/\__,_/
     /_/
...
```

Now, please create a `.mambarc` file: (assuming you do not have this file)

```shell
echo "envs_dirs:
  - /vol/local/conda_envs
pkgs_dirs:
  - /vol/local/.conda_cache/USERNAME" > ~/.mambarc
# Remember to change USERNAME to your login ID
```

This will do the following two things:

1. Setting `envs_dirs` will add shared environments folder to your micromamba, now when you do `micromamba env list`, it will show all environments installed on BLIS

2. Setting `pkgs_dirs` will let it use the general cache location for easier clean up.

```{note}
Commands above are also means of recovery when you encounter problems.
```

## Why choose micromamba instead of conda on BLIS?

`micromamba` is a standalone reimplementation of conda package manager in C++. It provides same command line interface as conda. In addition to conda:

1. Parallel downloading of repository data and package files using multi-threading
2. `libsolv` for much faster dependency solving, a state of the art library used in the RPM package manager of Red Hat (base of our Rocky linux 8), Fedora and OpenSUSE. This is extremely apparent when encountering some large repositories such as conda-forge.
3. Maintained actively by community, **NOT** Anaconda Inc.
4. Not python dependent. So 1, an environment without python is by default; 2, upgrade python version inside environment is easier.
5. `micormamba` executable relays only the one executable file itself, very easy to maintain.

## Install micromamba from scratch

ref. https://mamba.readthedocs.io/en/latest/installation.html#automatic-installation

### Install micromamba on Linux

Run this command in your terminal:

(Assuming you are using bash)

```shell
curl micro.mamba.pm/install.sh | bash
```

Prompt will ask you if you want to “Init shell?”, Please answer “Y” for yes, then restart your shell.

After a shell restart, run the following command to check:

```shell
micromamba info
```

Output should be:

```
                                          __
         __  ______ ___  ____ _____ ___  / /_  ____ _
        / / / / __ `__ \/ __ `/ __ `__ \/ __ \/ __ `/
       / /_/ / / / / / / /_/ / / / / / / /_/ / /_/ /
      / .___/_/ /_/ /_/\__,_/_/ /_/ /_/_.___/\__,_/
     /_/
...
```

### Install micromamba on Windows

Assuming you have Gitbash installed.

ref. https://mamba.readthedocs.io/en/latest/installation.html#windows

1. Download latest micromamba using this [link](https://micro.mamba.pm/api/micromamba/win-64/latest).
   - Assume you downloaded "micromamba-1.4.0-0.tar.bz2", please change the name according to your downloads
2. In Gitbash, `cd` to the download folder, do `bzip2 -d micromamba-1.4.0-0.tar.bz2`. You should see the file micromamba-1.4.0-0.tar now and `.bz2` suffix disappeared.
3. In Gitbash, do:

   ```shell
   mkdir micromamba-1.4.0
   cd micromamba-1.4.0
   tar xf ../micromamba-1.4.0-0.tar
   cp Library/bin/micromamba.exe /usr/bin/
   ```

4. Now micromamba.exe is in your PATH, you can initiate your shell with the following command:

   ```shell
   micromamba.exe shell init -s bash -p ~/micromamba
   ```

   Note you need to answer "y" for long path name support if you have administrator rights. Else "n" to skip it. Now **restart** your shell, do the following:

   ```shell
   micromamba info
   ```

   Output should be:

   ```
                                             __
            __  ______ ___  ____ _____ ___  / /_  ____ _
           / / / / __ `__ \/ __ `/ __ `__ \/ __ \/ __ `/
          / /_/ / / / / / / /_/ / / / / / / /_/ / /_/ /
         / .___/_/ /_/ /_/\__,_/_/ /_/ /_/_.___/\__,_/
        /_/
   ...
   ```

   Note in GitBash, python will not run directly as a console. If you want to do that, either install ipython or do the following and restart GitBash:

   ```shell
   echo 'alias python="winpty python"' >> ~/.bash_profile
   ```

   This will use "[winpty](https://github.com/rprichard/winpty)" to supply python with a Unix pty-master for communicating with Windows console. It works by starting a hidden console window and bridging between the console API and terminal input/output escape codes.