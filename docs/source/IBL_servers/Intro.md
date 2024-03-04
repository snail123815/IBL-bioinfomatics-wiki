# IBL Linux Servers

*By C.Du [@snail123815](https://github.com/snail123815)*

IBL now have 3 workstation level PCs setup to server bioinformatics requirements within IBL. Every one is welcome to use and share their expertise within our community!

## Servers and specs

We give names to our servers: BLIS, FRODO, BILBO. All of them are powered by [Rocky linux 8](https://rockylinux.org/about), a production-ready downstream version of Red Hat Enterprise Linux.

### BLIS

This is our main server, it has a shared local storage and use [conda environments (managed by `micromamba`)](Softwares.md) to manage softwares. Home directory has a quota of 20 GB for each user, no quota on shared local storage.

- Intel(R) Core(TM) i9-10980XE
  - @ 3.00GHz
  - 36 cores
- 256 GB memory
- NVIDIA Quadro RTX 4000
  - 8 GB memory
- `/home` 1.8 TB SSD; Quota for each user: 20 GB
- `/vol/local` 7 TB HDD

### DINGLAB01

Recently added. Home directory quota, shared local storage, and `micromamba` are setup the same as [BLIS](#blis). Note, if you run your program using an environment on BLIS and want to use DINGLAB01, you need to setup the environment again. The architecture of the two machines are not completely the same.

- Intel(R) Core(TM) i9-10900 CPU 
  - @ 2.80GHz
  - 10 cores (20 with Hyper-Threading, on)
- 32 GB memory
- `/home` 390 GB SDD; Quota for each user: 20 GB
- `/vol/local` 1 TB HDD

### BILBO

Managed by [Paco lab](https://www.universiteitleiden.nl/en/staffmembers/paco-barona-gomez)

- AMD Ryzen Threadripper PRO 5955WX
  - @ 4.0GHz
  - 16 cores
- 32 GB memory
- NVIDIA T1000
  - 8 GB memory

### FRODO

Managed by [Paco lab](https://www.universiteitleiden.nl/en/staffmembers/paco-barona-gomez)

- AMD Ryzen Threadripper PRO 5975WX
  - @ 3.6GHz
  - 32 cores
- 64 GB memory
- NVIDIA Quadro RTX A4500
  - 20 GB memory

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