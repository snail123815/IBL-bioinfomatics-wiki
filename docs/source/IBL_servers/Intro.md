# IBL Linux Servers

*By C.Du [@snail123815](https://github.com/snail123815)*

IBL now have 3 workstation level PCs setup to server bioinformatics requirements within IBL. Every one is welcome to use and share their expertise within our community!

## Servers and specs

Except FRODO, all of servers are powered by [Rocky linux 8](https://rockylinux.org/about), a production-ready downstream version of Red Hat Enterprise Linux. FRODO is now [Rocky linux 9](https://rockylinux.org/news/rocky-linux-9-3-ga-release/). In the future, all servers will be upgraded to Rocky linux 9 to keep up with [ALICE](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519378/About+ALICE). Ethernet connection of all servers have a speed of 1000 Gb/s. There is no sub-network for the servers.

:::{NOTE}
Not all servers have [ECC memory](https://serverfault.com/questions/5887/what-is-ecc-ram-and-why-is-it-better), if you plan to run long analysis (>10 hours) on no-ECC-memory servers, be prepared for some random error even if your program is perfect.
:::

### BLIS

This is our main server, it has a shared local storage and use [conda environments (managed by `micromamba`)](Program%20setup.md) to manage softwares. Home directory has a quota of 20 GB for each user, no quota on shared local storage.

- Intel(R) Core(TM) i9-10980XE
  - @ 3.00GHz
  - 36 cores
- 256 GB memory (ECC)
- NVIDIA Quadro RTX 4000
  - 8 GB memory
- `/home` 1.8 TB SSD; Quota for each user: 20 GB
- `/vol/local` 7 TB HDD

### FRODO

The only Rocky linux 9 server. Shared local storage and `micromamba` enviroment are in line with BLIS. Home directory on SSD and has a quota of 20 GB for each user.

- AMD Ryzen Threadripper PRO 5975WX
  - @ 3.6GHz
  - 32 cores
- 64 GB memory (ECC)
- NVIDIA Quadro RTX A4500
  - 20 GB memory
- `/home` 1.8 TB SSD; Quota for each user: 20 GB
- `/vol/local` 10 TB HDD

### BILBO

Managed by [Paco lab](https://www.universiteitleiden.nl/en/staffmembers/paco-barona-gomez). No quota, no `micromamba` setup.

- AMD Ryzen Threadripper PRO 5955WX
  - @ 4.0GHz
  - 16 cores
- 32 GB memory (ECC)
- NVIDIA T1000
  - 8 GB memory

### DINGLAB01

Home directory quota, shared local storage, and `micromamba` are setup the same as [BLIS](#blis). Note, if you run your program using an environment on BLIS and want to use DINGLAB01, you need to setup the environment again. The architecture of the two machines are not completely the same.

- Intel(R) Core(TM) i9-10900 CPU
  - @ 2.80GHz
  - 10 cores (20 with Hyper-Threading, on)
- 32 GB memory (no ECC)
- `/home` 390 GB SSD; Quota for each user: 20 GB
- `/vol/local` 1 TB HDD

### VBLIS

Home directory quota, shared local storage, and `micromamba` are setup the same as [BLIS](#blis). Note, if you run your program using an environment on BLIS and want to use VBLIS, you need to setup the environment again. The architecture of the two machines are not completely the same.

- Intel(R) Core(TM) i9-10900 CPU
  - @ 2.80GHz
  - 10 cores (20 with Hyper-Threading, on)
- 32 GB memory (no ECC)
- `/home` 390 GB SSD; Quota for each user: 20 GB
- `/vol/local` 7 TB HDD
- `/vol/local1` 1 TB SSD

## Basic knowledge of using linux shell

It is easy to find information and basic training online. If you do not know which to follow, we recommend you to follow this to start:

[The Unix Shell for novice](https://swcarpentry.github.io/shell-novice/)

## Get access

You can access all three servers directly within Leiden University [Research Network](#what-is-research-network). From outside of Research Network, you need to jump through one of Leiden University ssh gateways. Please prepare your access to gateway before you make actual connections.

To ask for access to all servers, please send email to me (c.du\[at\]biology.leidenuniv.nl). Please let me know the following info:

- The user name you want to use for login. Only lower case letters and numbers allowed, start with letters. It is OK that you use the same user name as your ULCN account.
- Your first name
- Your last name
- The group you come from (your supervisor)
- The analysis you want to do (generally)

We will provide you information needed for accessing our servers.

Currently we are using Slack group "IBL-Bioinformatic" for discussion and most importantly, send notifications about all servers. You will get invitation link with your username and password.

## Leiden University gateways

Leiden University has two different gateway servers which uses different account systems.

### Leiden University general purpose gateway

You need your ULCN account.

Please fill in the form "Request access SSH-gateway" on [this page](https://www.staff.universiteitleiden.nl/ict/help-and-support/application-forms/application-forms/service-units/ict-shared-service-centre) and wait for approval. Then you can set it up follow [this tutorial (login needed)](https://helpdesk.universiteitleiden.nl/tas/public/ssp/content/detail/knowledgeitem?unid=4b176453-ad3f-418f-9c15-40a11471de5f).

### ALICE gateway

Leiden University super computer cluster has its own gateway server, can be used also to connect Research Network. Please refer to [this page](../alice/alice_ibl.md#how-to-get-an-account) for more details. In principle, you still needs to be working or studying in Leiden University or have projects collaborating with us.

```{note}
The access to Research Network is not officially supported and you need to use it with your own risk!
```

## What is "Research Network"

The IBL servers are setup inside Leiden University's [Research Network](./Intro.md#what-is-research-network), which means intranet. To protect intranet from internet, gateway servers are hosted by Leiden University. Connecting IBL servers from internet can be done only through connecting to the gateway first and then from gateway to IBL servers. Of course, if you are inside our Leiden University intranet, you can make direct connections to IBL servers.

Without being on the Research Network, your computer cannot connect our servers using the given IP addresses.

### Determine your network location

If you are unable to connect to the servers using the provided IP addresses in the email, it is likely because you are **not** connected to Research Network. How to determine?

INSIDE:

- You have wired ethernet connection directly through a socket in Leiden University buildings. Note: using your own device does not guarantee a Research Network connection.
- You are wireless connected through WiFi to the “NUWD-Laptop” network

OUTSIDE:

- At home
- In Leiden University building but:
  - Connected to WiFi access point "eduroam"
  - Connected to WiFi access point "Leiden University"
- All locations that require "eduVPN". Note that "eduVPN" does not help you to connect IBL servers because this specific case is not setup in "eduVPN" setup.

## Data and backup

As a small server cluster intended for testing and teaching, we **do not** plan to backup any data you upload to the servers. Please remove your data when it is not needed.

## Home directory quota explained

Except BILBO, you will have limited storage space in your `/home/user` directory. This is meant for supporting as much users as possible. The `/home` directory is located in SSD and should be fast, it is intended to store scripts that you made, programs that you compile that do not fit for sharing, or some temporary files generated by your program.

Find how much you have used using the following commands:

```sh
[username@blis ~]$ quota -s
Disk quotas for user username (uid 168888888):
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
/dev/mapper/rl-home
                   785M  20480M  25600M           14081       0       0

[username@blis ~]$ du -d 0 -h ~/
785M    /home/username/

```

Please do not try to overload the quotation even if you find out that you are not listed in the quotation system. It may be a mistake that might be fixed at anytime.

You can overrun the system to "limit", but cannot exceed it. The file system will block you from writting any new stuff in. If this happened during your job which writes to `~` directory, the job will fail. You need to run all data IO heavy jobs from the shared storage. For that, please check carefully the program you want to use for its temporary and output data location.

Contact server adminstrators in our SLACK group if you really need larger `~` directory.

## Jump within servers

You can jump using `ssh [servername (lowercases)]` to any of the above listed servers.

### Check os version

```sh
$ cat /etc/os-release
NAME="Rocky Linux"
VERSION="9.3 (Blue Onyx)"
ID="rocky"
ID_LIKE="rhel centos fedora"
VERSION_ID="9.3"
PLATFORM_ID="platform:el9"
PRETTY_NAME="Rocky Linux 9.3 (Blue Onyx)"
ANSI_COLOR="0;32"
LOGO="fedora-logo-icon"
CPE_NAME="cpe:/o:rocky:rocky:9::baseos"
HOME_URL="https://rockylinux.org/"
BUG_REPORT_URL="https://bugs.rockylinux.org/"
SUPPORT_END="2032-05-31"
ROCKY_SUPPORT_PRODUCT="Rocky-Linux-9"
ROCKY_SUPPORT_PRODUCT_VERSION="9.3"
REDHAT_SUPPORT_PRODUCT="Rocky Linux"
REDHAT_SUPPORT_PRODUCT_VERSION="9.3"
```
