# Softwares

*By C.Du [@snail123815](https://github.com/snail123815)*

(Avaliable softwares can be found in directory `/vol/local/conda_envs/`, use by [activating](#run-a-program) corresponding environment)

We manage our softwares using [conda](https://docs.conda.io/en/latest/) virtual environments, which have become a standard tool in the field and many other tools are compatible with its standard. To avoid confusion, we will use the term "environment" to refer specifically to conda-compatible virtual environments. By using environments, we can easily manage software dependencies and avoid conflicts between different software versions.

On BLIS, we use a tool called **[micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html)**, a lightweight and efficient alternative to conda, to manage these environments. A shared directory dedicated to storing, sharing, and modifying environments is created on BLIS. By default, all users on BLIS should be in a premission group called "condablis". This group grant users access to our shared environments.

Please make sure you are in "condablis" group by running `groups` command. You should see "condablis" in the output of this command. If not, please contact server admin.

```sh
$ groups
sgr condablis
```

## Run a program

Before working with virtual environments, it is highly recommanded to setup a `~/.mambarc` file follow [setting up config file](#setting-up-config-file) down below.

Since all softwares are installed in an environment, you have to activate it first. For example, to use a local version of AntiSMASH:

```sh
# 0. Make sure you have your shell initiated with micromamba (skip if done before)
[user@blis ~]$ micromamba shell init -s bash -p ~/micromamba-base
# 1. Activate environment
(base) [user@blis ~]$ micromamba activate /vol/local/conda_envs/antismash
# 2. Check if antismash is avaliable
(/vol/local/conda_envs/antismash) [user@blis ~]$ antismash --help

########### antiSMASH 6.1.1 #############

usage: antismash [-h] [options ..] sequence


arguments:
  SEQUENCE  GenBank/EMBL/FASTA file(s) containing DNA.

--------
Options
--------
...
```

Note that if you setup the config file as [described](#setting-up-config-file), you may see all environments by `micromamba env list`. But activating an environemnt by its name does not work:

```sh
(base) [user@blis ~]$ micromamba env list

  Name           Active  Path
─────────────────────────────────────────────────────────
  base           *       /home/duc_test1/micromamba-base
  quasan                 /vol/local/conda_envs/quasan
  rrefinder              /vol/local/conda_envs/rrefinder
(base) [user@blis ~]$ micromamba activate quasan
critical libmamba Cannot activate, prefix does not exist at: /home/user/micromamba-base/envs/quasan
# Meaning you can only activate shared environments using their path
(base) [user@blis ~]$ micromamba activate /vol/local/conda_envs/quasan
(/vol/local/conda_envs/quasan) [user@blis ~]$
```

You can make this process less painful by creating a soft link in your home directory:

```shell
cd ~
ln -s /vol/local/conda_envs/ genvs
# Then you can skip the long path in you command while activating an environment
micromamba activate ~/genvs/antismash
```

## Install a program

Before working with virtual environments, it is highly recommanded to setup a `~/.mambarc` file follow [setting up config file](#setting-up-config-file) down below.

Install a program using `sudo` by many users will lead to disaster. Thus all programs needs to be in a contained environment. Compatible programs that might be used by a pipeline can be installed together in one environment.

Create an environment to host the software or a pipe line you want to run. Then you have all control over the environment you created.

```sh
# 0. Make sure you have your shell initiated with micromamba (skip if done before)
[user@blis ~]$ micromamba shell init -s bash -p ~/micromamba-base
# 1. Create environment called multi-omics and activate it
(base) [user@blis ~]$ micromamba create -p /vol/local/conda_envs/multi-omics
(base) [user@blis ~]$ micromamba activate /vol/local/conda_envs/multi-omics
# 2. Install software, eg. python
(/vol/local/conda_envs/multi-omics) [user@blis ~]$ micromamba install -c conda-forge python
```

### Do not follow tutorial with yml file

Many times you will find a tutorial to setup a conda environemnt by `conda env create -f minimotif.yml minimotif`. Please **DO NOT** follow this by simply replacing `conda env` with `micromamba`.

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

Please remove the `name:` line and save the file. (The line is telling conda or micromamba to install the environment with `-n` switch, it is not compatible with `-p` switch.)

Then:

```sh
# 1. Create environment using -p
(base) [user@blis ~]$ micromamba create -p /vol/local/conda_envs/MiniMotif
(base) [user@blis ~]$ micromamba activate /vol/local/conda_envs/MiniMotif
# 2. Install all dependencies using the .yml file
(/vol/local/conda_envs/MiniMotif) [user@blis ~]$ micromamba install -f minimotif.yml
```

Now it should do the job.

## Location of shared environments

All our shared environments are stored in `/vol/local/conda_envs/`, and all cache files are stored in `/vol/loca/.conda_cache/USERNAME`.

Please follow the turtoral below to config your `.condarc`. All cache files will then be stored in a shared location: `/vol/local/.conda_cache/USERNAME` for easier cleanup.

### Setting up config file

The program micromamba uses a config file located in your home folder: `~/.mambarc` to store your specific configurations. Well `micromamba` *not only* check `~/.mambarc` file, but also uses `~/.condarc`, one of them is enough. (The later is used by conda)

The config file has few convenient options. On BLIS, please put these contents in the config file:

```YAML
envs_dirs:
  - /vol/local/conda_envs
pkgs_dirs:
  - /vol/local/.conda_cache/USERNAME
```

- `env_dirs` will allow `micromamba env list` command to list all environments inclduing our shared environments.
- `pkgs_dirs` set the cache dir, it is a easy-to-clean location.

You can also add:

```YAML
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
```

- `channels` will allow you to skip -c option when installing packages
- `auto_activate_base` will activate your base environment, by this, you will be using eg. python from your base environment rather than a system one.

The following commands will create a soft link (shortcut) in your home directory for easier accessing the shared environments.

```shell
cd ~
ln -s /vol/local/conda_envs/ genvs
# Then you can skip the long path in you command while activating an environment
micromamba activate ~/genvs/antismash
```

If you need more information on how to use micromamba, please refer to our [micromamba instruction](../basic_tools/micromamba.md#blis-users).

## Premissions of shared environments on BLIS

All environments created in `/vol/local/conda_envs/` are by default belongs to the group `condablis`, all group members can activate these environments. **Only** the owner who created the environment can add or remove package. If you want to let others change your environment, you need to specifically change the premission:

```sh
chmod -R g+w /vol/local/conda_envs/yourEnvironment
```

**Anyone who changed this environment should do this *again*** for others to change it. Or, the owner can remove this premission after changing:

```sh
chmod -R g-w /vol/local/conda_envs/yourEnvironment
```

This restriction is due to the limitations of the Linux file system, which are intentional for safety reasons.
