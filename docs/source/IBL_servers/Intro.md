# IBL Linux Servers

*By C.Du [@snail123815](https://github.com/snail123815)*

IBL now have 3 workstation level PCs setup to server bioinformatics requirements within IBL. Every one is welcome to use and share their expertise within our community!

## Servers and specs

We give names to our servers: BLIS, FRODO, BILBO. All of them are powered by [Rocky linux 8](https://rockylinux.org/about), a production-ready downstream version of Red Hat Enterprise Linux.

### BLIS

- Intel(R) Core(TM) i9-10980XE
  - @ 3.00GHz
  - 36 cores
- 256 GiB memory
- NVIDIA Quadro RTX 4000
  - 8 GiB memory
- 2 TB SSD
- 7 TB HDD

### FRODO

- AMD Ryzen Threadripper PRO 5975WX
  - @ 3.6GHz
  - 32 cores
- 64 GiB memory
- NVIDIA Quadro RTX A4500
  - 20 GiB memory

### BILBO

- AMD Ryzen Threadripper PRO 5955WX
  - @ 4.0GHz
  - 16 cores
- 32 GiB memory
- NVIDIA T1000
  - 8 GiB memory

## Basic knowledge of using linux shell

It is easy to find information and basic training on line. If you do not know which to follow, we recommend you to follow this to start: 

[The Unix Shell for novice](https://swcarpentry.github.io/shell-novice/)

## Get access

You can access all three servers directly within Leiden University [Research Network](#what-is-research-network). From outside of Research Network, you need to jump through Leiden University ssh gateway, for this, you need your ULCN account.

Please fill in the form "Request access SSH-gateway" on [this page](https://www.staff.universiteitleiden.nl/ict/help-and-support/application-forms/application-forms/service-units/ict-shared-service-centre) and wait for approval. Then you can set it up follow [this tutorial](https://www.staff.universiteitleiden.nl/binaries/content/assets/ul2staff/ict/handleidingen/manual-setting-up-ssh-gateway-2017-eng.pdf).

To ask for access to all servers, please send email to me (c.du\[at\]biology.leidenuniv.nl) or Edder Bustos Diaz (for Paco Lab only, e.d.bustos.diaz\[at\]biology.leidenuniv.nl). Please let us know the following info:

- The user name you want to use for login. Only lower case letters and numbers allowed, start with letters. It is OK that you use the same user name as your ULCN account.
- Your first name
- Your last name
- The group you come from (your supervisor)
- The analysis you want to do (generally)

We will provide you information needed for accessing our servers.

Currently we are using Slack group "IBL-Bioinformatic" for discussion and most importantly, send notifications about all servers. Please ask for access.

## What is "Research Network"

If you are unable to connect to the servers using the provided IP addresses in the email, it's likely because you are **not connected** to Leiden University's internal network, known as the "Research Network." These IP addresses are not accessible from the World Wide Web for security reasons.  

Without being on the Research Network, your computer cannot locate our servers using the given IP addresses.

### Am I connected to "Research Network"?

YES: One of the following circumstances means you are ***inside*** Research Network:

- You have wired ethernet connection directly through a socket in Leiden University buildings
- You are wireless connected through WiFi to the “NUWD-Laptop” network

NO: One of the following circumstances means you are ***outside*** Research Network:

- At home
  - Even if you are using "eduVPN"
- In Leiden University building but:
  - Connected to WiFi access point "eduroam"
  - Connected to WiFi access point "Leiden University"
  - Also including using "eduVPN"