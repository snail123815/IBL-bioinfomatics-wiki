# Setup `micromamba`

*By C.Du [@snail123815](https://github.com/snail123815)*

```{contents}
---
depth: 3
---
```

`micromamba` is a standalone `conda` replacement. About what is micromamba and how to use, [follow this link](https://mamba.readthedocs.io).

## IBL server users

The program is available, but please follow [execute programs tutorial](../IBL_servers/Execute%20programs.md) for how to use.

## Why choose micromamba instead of conda on BLIS?

[Instructions on how micromamba works](../IBL_servers/Program%20setup.md) on BLIS.

`micromamba` is a standalone reimplementation of conda package manager in C++. It provides same command line interface as conda. In addition to conda:

1. Parallel downloading of repository data and package files using multi-threading
2. `libsolv` for much faster dependency solving, a state of the art library used in the RPM package manager of Red Hat (base of our Rocky linux 8), Fedora and OpenSUSE. This is extremely apparent when encountering some large repositories such as conda-forge.
3. Maintained actively by community, **NOT** Anaconda Inc.
4. Not python dependent. So 1, an environment without python is by default; 2, upgrade python version inside environment is easier.
5. `micormamba` executable relays only the one executable file itself, very easy to maintain.

## Install micromamba from scratch

**Do NOT do this on any of our servers!** This tutorial is for you to install this in your own computer (**not** university/company owned).

[Ref.](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)

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

```sh
                                          __
         __  ______ ___  ____ _____ ___  / /_  ____ _
        / / / / __ `__ \/ __ `/ __ `__ \/ __ \/ __ `/
       / /_/ / / / / / / /_/ / / / / / / /_/ / /_/ /
      / .___/_/ /_/ /_/\__,_/_/ /_/ /_/_.___/\__,_/
     /_/
...
```

### Install micromamba on Windows

[ref.](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)

#### Gitbash install micromamba

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
   micromamba.exe shell init -s bash -p $env:HOME/micromamba-base
   ```

   Note you need to answer "y" for long path name support if you have administrator rights. Else "n" to skip it. Now **restart** your shell, do the following:

   ```shell
   micromamba info
   ```

   Output should be:

   ```sh
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

#### Gitbash install PowerShell

Modified from [ref.](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html#windows)

```PowerShell
# Download
Invoke-Webrequest -URI https://micro.mamba.pm/api/micromamba/win-64/latest -OutFile micromamba.tar.bz2
```

Now you need to find the downloaded micromamba.tar.bz2 file, extract the archive use [7-Zip](http://www.7-zip.org/download.html) or any other program that can extract `.tar.bz2` file. (Windows 11 file explorer can directly open this file)

Now inside extracted directory, find `Library\bin\micromamba.exe` file, move it to your current directory or a programs directory you define by yourself. If you did the later, you need to navigate to the target directory. Then

```PowerShell
# You should be able to run the program now.
.\micromamba.exe --help

# You can use e.g. $HOME\micromamba-base as your base prefix
$Env:MAMBA_ROOT_PREFIX=$HOME+"\micromamba-base"

# Initialize the shell
.\micromamba.exe shell init -s powershell -p $Env:MAMBA_ROOT_PREFIX
```

After **restarting** your PowerShell, you can start using it:

```PowerShell
micromamba create -n test
micromamba activate test
micromamba install -c defaults python
```