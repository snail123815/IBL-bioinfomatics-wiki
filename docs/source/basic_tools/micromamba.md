# `micromamba` is a standalone `conda` replacement

*Tutorial by C.Du*

About what is micromamba and how to use: https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html

## BLIS users

BLIS have `micromamba` in your PATH, but if you are using it for the first time, please initiate your shell using the following command and **restart your shell** after it finishes:

(Assuming you are using bash)

```shell
micromamba shell init -s bash -p ~/micromamba
```

After your shell has been restarted, please run the following command to check:

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
  - /vol/local/.conda_cache" > ~/.mambarc
```

This will do the following two things:

1. Setting `envs_dirs` will add shared environments folder to your micromamba, now when you do `micromamba env list`, it will show all environments installed on BLIS

2. Setting `pkgs_dirs` will let it use the general cache to reduce time needed for downloading packages and save disk space.

## Install micromamba from scratch

ref. https://mamba.readthedocs.io/en/latest/installation.html#automatic-installation

### Install micromamba on Linux

Run this command in your terminal:

(Assuming you are using bash)

```shell
curl micro.mamba.pm/install.sh | bash
```

Prompt will ask you if you want to “Init shell?”, Please answer “Y” for yes. After this is done, please restart your shell.

To check if micromamba has been successfully installed, please check using this command:

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

