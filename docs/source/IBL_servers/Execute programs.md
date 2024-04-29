# Execute programs

*By C.Du [@snail123815](https://github.com/snail123815)*

We manage our softwares using [conda](https://docs.conda.io/en/latest/) virtual environments, which have become a standard tool in the field and many other tools are compatible with its standard. To avoid confusion, we will use the term "environment" to refer specifically to conda-compatible virtual environments. By using environments, we can easily manage software dependencies and avoid conflicts between different software versions.

On BLIS, we use a tool called **[micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html)**, a lightweight and efficient alternative to conda, to manage these environments. A shared directory dedicated to storing, sharing, and modifying environments is created on BLIS. By default, all users on BLIS should be in a premission group called "condablis". This group grant users access to our shared environments.

Please make sure you are in "condablis" group by running `groups` command. You should see "condablis" in the output of this command. If not, please contact server admin.

```sh
$ groups
sgr condablis
```

To manage software used by different users on BLIS, we use virtual environments located at `/vol/local/conda_envs`. You can check if the environment for the software you want to use already exists at this location. If not, you may need to create one and install the software yourself. For detailed instructions on how to create virtual environments and install software, please finish [program setup](./Program%20setup.md) guide.

## Prepare micromamba

The program `micromamba` is already installed on the server, but you need to do some configuration before you can activate and create environments.

Note, you only need to do this **once** on **one** server.

Here is how (assuming you are using default shell `bash`):

```sh
micromamba shell init -s bash -p ~/micromamba-base
```

Above command will create a "base" environment at your home directory. Then a script will be put into your `~/.bashrc` file. Now you need to run the script by:

```sh
source ~/.bashrc
```

Next time when you start your `bash` shell (at login), the script will be automatically executed.

Now you should be able to run this command:

```sh
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

If you see something else, please try to restart your shell and repeat the above steps. Contact for help if still no success.

## Plan and notify others before execute long program

Once you have done [program setup](./Program%20setup.md), it is time to plan a real job. Please follow these steps:

1. Check the "jobs-on-servers" channel in our Slack group for pinned messages.
2. Log in to the system and use htop or top to check for heavily running processes. Notify the channel if you see any anomalies.
3. Run your job. If it will take a long time, run it in a `screen` session and check its status.
4. Inform everyone else in the "jobs-on-servers" channel using this format:  
   "{Job type} on {SERVER} is using {number} cores, (approximately, optional) {number} ram, until ~(approximately) {time}."  
   For example, "phylophlan on BLIS is using 8 cores, 100 GB ram, until ~20 Nov 9:00." Pin this message if the job list is a bit long.
5. Once your job is done, edit the message to include a big "DONE" at the beginning and unpin it.

```{admonition} Rule of thumb
- For any job, leave at least 2 cores free.
- For short jobs, use as many cores as possible.
- For long jobs, use maximum half of the avaliable cores. If more cores are needed, notify everyone at least half hour in advance.
  For example, "PLANNING phylophlan on BLIS, is using 18 cores, 160 GB ram, from 19 Nov 20:00 till ~20 Nov 9:00."  
```

## File transfer

If you're planning to work with your own dataset on the servers, you'll need to transfer it first. To do this, you need to have already set up an SSH connection BLIS (`blis`).

For WinSCP+PuTTY users, just use the GUI to transfer.

Please bare in mind that there is a quota system for your home directory `/home/USERNAME`. It should mainly be used to store settings, code, own apps. Not for data.

To check how much quota has left for you:

```sh
quota -s
Disk quotas for user duc (uid 148600000):
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
/dev/mapper/rl-home
                 16073M  20480M  25600M            154k       0       0
# Meaning you have used 16GB of the 20GB.
# You can store up to 25GB but after exceeding 20GB,
# you will be given a grace time of few days, then
# your home directory will be locked until you remove excess data
```

Two programs you can use to transfer data: `scp` and `rsync`

### scp

SCP for <u>s</u>ecure <u>c</u>o<u>p</u>y, or ssh cp, or safe cp...

When you have few files to copy, this is a good tool. It **cannot** resume transfer after transfer failure.

The syntax for `scp` is

```shell
scp [OPTIONS] [[user@]src_host:]file1 [[user@]dest_host:]file2
```

Same as command `ssh`, since you have already a config with user name and IP address for `Host blis` and `Host hpc1`, then the `[[user@]dest_host:]` part can be replaced with `blis:` or `hpc1:`.

```shell
# A file
scp path/to/file blis:/vol/local/username/
# Multiple files
scp path/to/fileA path/to/fileB blis:/vol/local/username/
# A directory, -r for recursive
scp -r path/to/dir blis:/vol/data/username
```

### rsync

`rsync` is a more reliable tool for copying large datasets. It can continue the transfer from where it left off in case of interruption. (PowerShell does not have this program, use `scp` or WinSCP instead.)

The syntax for `rsync` is almost the same as `scp`:

```shell
rsync [OPTION...] SRC... [USER@]HOST:DEST
```

```shell
# Copy a directory to your own folder in the shared storage on BLIS
rsync -aP path/to/dir blis:/vol/data/username/
```

`-a` means archiving the directory, it will copy everything associated with the file, including its creation time, permissions etc. It implies `-rlptgoD`.  
`-P` to show progress.

## How to run long jobs using `screen`

If you need to run a long job that exceeds the duration of your SSH connection, you can use `screen`. This program creates a new Bash shell that runs within the `screen` program, allowing you to run commands even if your SSH connection is interrupted. To use `screen`, simply execute the command, and a new shell will open. From here, you can execute commands as usual. To detach from the shell and leave the program running, press **Ctrl + a**, release the buttones, then press **d**. You can check the status of the program using `htop` or `top`. Once detached, you can safely exit the SSH connection. To come back to your running job, check its output, etc., you can execute `screen -r` to attach to the shell that have your running program.

When multiple `screen` is needed and you find it hard to track which is doing which job, you can use `screen -S [session name]` command to give each screen a name. Then use `screen -r [session name]` to resume to that session.

`screen` might also works on ALICE, but please do not use `screen` for super long jobs on ALICE. Long jobs should only run in a slurm queue.