# Run jobs on Linux servers

*by Chao DU*

```{toctree}
---
#caption: Table of contents
maxdepth: 3
---
```

## Schedule your jobs

1. Check pinned messages "jobs-for-blis-frodo-bilbo" channel in our Slack group.
2. Log in the system, use `htop` or `top` to check if any processes are running heavily. Notify in the channel if there is any anomaly.
3. Run your job. If it will take long, run it in a `screen` session, check its status.
4. Tell everyone else in the "jobs-for-blis-frodo-bilbo" channel using the this format: "{Job type} is using {number} cores, (approximately, optional) {number} ram, till ~(approximately) {time}."  
  eg. "phylophlan is using 8 cores, 100 GB ram, till ~20 Nov 9:00."

```{admonition} Rule of thumb
- For any job, leave at least 2 cores free.
- For short jobs, use as many cores as possible.
- For long jobs, use maximum half of the cores. If more cores are needed, notify everyone in advance.
```

## File transfer

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

## How to run long jobs using `screen`

When you want to run a long job, longer than your ssh connection, then you can use `screen`. When you execute `screen`, a new bash will open, it is actually another shell that runs through the program screen. You can do anything here. When it starts doing things, press **ctrl + a** then **d** to detach from the shell. The program you run inside screen shell will still be running in the background. You can check the status by `htop` or `top`. Now it is safe to exit ssh connection. When you want to come back to your job, check the output etc., you can execute `screen -r`, this operation is called "attaching".

This also works on ALICE, but please do not use this for super long jobs, they should only run in slurm queue.