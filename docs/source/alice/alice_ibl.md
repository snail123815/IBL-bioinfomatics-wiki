# ALICE server from Leiden University

```{toctree}
---
#caption: Table of contents
maxdepth: 3
---
```

## How to

[https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/)

## IBL on ALICE
 
### Group shared dir

Please use a folder of your user name in our group shared folder for your data.

`/data1/projects/pi-vriesendorpb/<ULCN_USERNAME>`

This is Project directories on ALICE, [rules apply](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519552/Storage+on+ALICE#Project-directories).

The directory is backed up. Please only store data that you think very important to keep. Otherwise, use

`/data1/<ULCN_USERNAME>`

or simply use the soft link

`~/data`

As the quota is much higher according to [ALICE WIKI](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519552/Storage+on+ALICE#The-scratch-shared-file-system-on-%2Fdata1).
 
We cannot overwrite data that others created.
 
### Group shared Conda environments

Load Conda module:

```shell
module load Miniconda3
```

Your `HOME` dir is limited to a quota of 15 GB, as a result, we created a shared dir for our group and we can use and create shared Conda environments, just like [on BLIS](../blis/blis_usage.md#conda-environments).

`/data1/projects/pi-vriesendorpb/condaEnvs`

TEMP/CACHE dir for pkgs:

`/data1/projects/pi-vriesendorpb/.condaTemp`

Want others to change your environment? Do

`chmod g+w -R [ENVDIR] # Not tested`

Generate a yaml file when you think your environment is working.
 
Example `.condarc` file

```
channels:
  - bioconda
  - conda-forge
  - defaults
auto_activate_base: true
show_channel_urls: true
envs_dirs:
  - /data1/projects/pi-vriesendorpb/condaEnvs
pkgs_dirs:
  - /data1/projects/pi-vriesendorpb/.condaTemp
```
 
Be cautious if your environment involves R and R packages. Do some extra tests.

### Storage Quota

To get your quota on SCRATCH, use

`beegfs-ctl --getquota --uid <ULCN_USERNAME>`

To get status of group quota, use

`beegfs-ctl --getquota --gid pi-vriesendorpb`

Yes, we only have 600GB, and it is almost full. Please do not store data on our shared space unless you want to share it.

## Transfer data

Refer to [BLIS usage](../blis/blis_usage.md#files-transfer).