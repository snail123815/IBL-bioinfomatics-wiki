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

## Files transfer

Assume you have already setup ssh connection to ALICE (`hpc1`) and BLIS (`blis`).

### scp

SCP for secure copy, or ssh cp, or safe cp...

When you have few files to copy, this is a good tool. But if you have a directory to transfer, then rsync is much better.

```shell
scp [OPTIONS] [[user@]src_host:]file1 [[user@]dest_host:]file2
# A file
scp path/to/file blis:/vol/local/username
# A dir
scp -r path/to/dir hpc1:data/
```

### rsync

```shell
rsync [OPTION...] SRC... [USER@]HOST:DEST
# A dir
rsync -aP path/to/dir hpc1:data/
```

## How to run long jobs

When you want to run a long job, longer than your ssh connection, then you can use `screen`. When you execute `screen`, a new bash will open, it is actually another shell that runs through the program screen. You can do anything here. When it starts doing things, press **ctrl + a** then **d** to detach from the shell. The program you run inside screen shell will still be running in the background. You can check the status by `htop` or `top`. Now it is safe to exit ssh connection. When you want to come back to your job, check the output etc., you can execute `screen -r`, this operation is called "attaching".

This also works on ALICE, but please do not use this for super long jobs, they should only run in slurm queue.