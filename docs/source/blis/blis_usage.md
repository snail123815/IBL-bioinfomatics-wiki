# BLIS - Usage how-to

```{toctree}
---
#caption: Table of contents
maxdepth: 3
---
```

## Schedule your jobs

1. Check pinned messages "blis-jobs" channel in our Slack group.
2. Log in the system, use `htop` or `top` to check if any processes are running heavily. Notify in the channel if there is any anomaly.
3. Run your job in a `screen` session, check its status.
4. State in the "blis-jobs" channel: "{Job type} is using {number} cores, (approximately) {number} ram, till (approximately) {time}."  
  eg. "phylophlan is using 8 cores, 100 GB ram, till 20 Nov 9:00."

```{admonition} Rule of thumb
- For short jobs, use as many cores as possible, but leave at least 2 cores free.
- For long jobs, use maximum half of the cores. If more cores are needed, notify everyone in advance, also leave at least 2 cores free.
```

## Conda environments

We use conda environments for almost all bioinformatics works.

### Location of shared environments

All our conda environments are stored in
`/opt/anaconda3/envs/`
For example, the phylophlan environment is stored in
`/opt/anaconda3/envs/phylophlan`
To activate phylophlan:
`conda activate /opt/anaconda3/envs/phylophlan`
 
I (DU) recommend you to do

```shell
cd ~
ln -s /opt/anaconda3/envs/ genvs
conda activate ~/genvs/phylophlan
```

### Conda config file `.condarc`

`.condarc` has few convenient options. My (DU) `.condarc` looks like:

```
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
show_channel_urls: true
envs_dirs:
  - /home/[USERNAME]/micromamba/envs
  - /opt/anaconda3/envs
pkgs_dirs:
  - /vol/local/conda_cache
```
 
- `channels` will allow you to skip -c option when installing packages
- `auto_activate_base` will activate your base environment, by this, you will be using eg. python from your base environment rather than a system one.
- `env_dirs` will allow conda env list command to list all environments from these dirs. A must have in our shared environment work flow.
- `pkgs_dirs` set the cache dir. With this we save disk space by using a general cache.

### micromamba
 
`micromamba` is neat ;-)