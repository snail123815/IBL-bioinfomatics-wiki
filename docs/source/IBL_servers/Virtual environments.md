# Virtual environments

*by Chao DU*

```{toctree}
---
#caption: Table of contents
maxdepth: 3
---
```

We manage our softwares using virtual environments, these environments are usually created by [conda](https://docs.conda.io/en/latest/). Now that "conda environments" become standards and many other tools can be used to create and manage the environments.

On BLIS, we have a shared space where we store, share, and tweak these environments, and we use [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html) as a conda alternative to manage these environments.

For more instructions on micromamba, please check [micromamba instruction](../basic_tools/micromamba.md#blis-users).

## Location of shared environments

All our shared environments are stored in `/vol/local/conda_envs/`, and all cache files are stored in `/vol/loca/.conda_cache/`

The following commands will create a soft link (shortcut) in your home directory to easier access the shared environments.

```shell
cd ~
ln -s /vol/local/conda_envs/ genvs
```

### Config file `.mambarc`

`.mambarc` has few convenient options. My `.mambarc` looks like:

(you can also use `.condarc` as file name, it can be recognised by both conda, mamba, and micromamba. `.mambarc` can only be recognised by mamba and micromamba)

```
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
show_channel_urls: true
envs_dirs:
  - /home/[USERNAME]/micromamba/envs
  - /vol/local/conda_envs
pkgs_dirs:
  - /vol/local/.conda_cache
```
 
- `channels` will allow you to skip -c option when installing packages
- `auto_activate_base` will activate your base environment, by this, you will be using eg. python from your base environment rather than a system one.
- `env_dirs` will allow conda env list command to list all environments from these dirs. A must have in our shared environment work flow.
- `pkgs_dirs` set the cache dir. With this we save disk space by using a general cache.
