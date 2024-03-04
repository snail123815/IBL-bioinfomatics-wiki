# SSH access tutorial

*By C.Du [@snail123815](https://github.com/snail123815), Edder Bustos Diaz [@EdderDaniel](https://github.com/EdderDaniel)*

```{contents}
---
depth: 3
---
```

To use our Linux servers, you'll need access to a command line interface (CLI). There is also possibility to use graphical user interface (GUI) to make connections. In any case, you need to first:

## Determine your network location

The IBL servers are setup inside Leiden University's [Research Network](./Intro.md#what-is-research-network), which means intranet. To protect intranet from internet, gateway servers are hosted by Leiden University. Connecting IBL servers from internet can be done only through connecting to the gateway first and then from gateway to IBL servers. Of course, if you are inside our Leiden University intranet, you can make direct connections to IBL servers.

Go to this link [determine your network location](./Intro.md#determine-your-network-location) for how.

If you are working on your own computer, even if it is an university managed laptop, no matter you can connected to the Research Network or not, it is always good to [setup connection using ssh through SSH gateway](#setup-connection-using-ssh-through-ssh-gateway)

Otherwise, from an university managed desktop, you can [connect with a direct SSH connection](#make-direct-ssh-connection).

For GUI setup, [follow this tutorial](./ssh%20access%20winscp.md).

## Start a command line interface

Here's how to get a CLI started on different operating systems:

- For MacOS (Apple operating system) users, open the "Terminal" application by typing "Terminal" in the spotlight.
- For Linux users, open the "Terminal" application (sometimes it is also called "shell").
- For Windows users, there are several options:
  - WSL (Windows Subsystem for Linux) with the default Linux distribution. You can find more detailed instructions on how to install it [here](https://learn.microsoft.com/en-us/windows/wsl/install).
  - GitBash provides a shell environment similar to Linux systems, and the settings will be the same.
  - PowerShell comes by default with Windows. The latest version comes with the software "ssh". However, we do not recommend using this method, as it may cause unforeseen problems and the commands to set up may be slightly different.

```{admonition} Do not copy directly
:class: warning
**DOUBLE CHECK COMMANDS BEFORE EXECUTING THEM**

Please note that in this tutorial, we do not know the IP address you are connecting to, your `USERNAME`, or your `ULCN`. Please carefully check the commands you copy and adjust them accordingly.
```

## Setup connection using ssh through SSH gateway

We recommend you use [Leiden University general purpose gateway](./Intro.md#leiden-university-general-purpose-gateway). Using ALICE gateway is not recommended. If you use, you need to use ALICE gateway URL and your ALICE account for the gateway. !!Use ALICE gateway at your own risk!!

URL of general purpose gateway is `sshgw.leidenuniv.nl`. Once you are able to log in to the gateway following [this tutorial (login needed)](https://helpdesk.universiteitleiden.nl/tas/public/ssp/content/detail/knowledgeitem?unid=4b176453-ad3f-418f-9c15-40a11471de5f), you can proceed with the following setups. It's perfectly safe to access the servers through the gateway, even if you're already within Research Network.

GOAL: Once you've completed this setup, you can access our servers (e.g., BLIS) from your computer with a single command: `ssh blis`, `ssh frodo`, or `ssh bilbo`.

Depends on the operating system you use, you might choose command line interface (CLI, follow the instruction on this page) or [graphical user interface (GUI)](./ssh%20access%20winscp.md#ssh-connection-through-gui).

## SSH connection through CLI

CLI on all system shares the same commands except in PowerShell on Windows systems. The major difference is how to represent a file or directory (folder) path.

```{admonition} Representation of Path
Windows systems uses `DriveLetter:\path\to\your\file`, for example `"C:\Users\Public\Documents\"`. This is the same for Microsoft programs including CMD and PowerShell. The path starts with a drive letter followed by a colon, then uses "**backslash**", `\`, to separate directory hierarchy.

Linux/MacOS/GitBash however, only uses "**forwardslash**", `/`, to separate directory hierarchy. The **full path** always starts from the "**root**" directory represented by a single `/`. For example, the GitBash representation of the above mentioned directory will be `/c/Users/Public/Documents/`.

(A standing pipe "|" that will fall to the right side "/" (forward) is a "forwardslash")
```

There are four steps:

1. [Creeate ssh key pair](#create-ssh-key-pair)
2. [Let server recognise your key](#let-server-recognise-your-key)
3. [Configure local machine to use a correct key](#configure-local-machine-to-use-a-correct-key)
4. [Connect](#connect)

(create-ssh-key-pair)=
### 1. Create ssh key pair

In your terminal do:

```shell
mkdir -p ~/.ssh
ssh-keygen -t ed25519 -C "From my PC" -f ~/.ssh/iblservers
```

When you execute this command, you'll be prompted to enter a "passphrase". You can simply press ENTER to proceed. Otherwise this passphrase will be asked every time you use this key, (too) much  safer.

You should see some output looks like this:

```text
Generating public/private ed25519 key pair.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in iblservers
Your public key has been saved in iblservers.pub
The key fingerprint is:
SHA256:M2238Cx5UCQgGivrRI5gtay92U3QULSQtTneghU2kO8 From my PC
The key's randomart image is:
+--[ED25519 256]--+
|   ..+OB... .    |
|  o .*=.*  o     |
|..ooo..B    .    |
|o+oo  =.o. .     |
|..+. ..+S.= .    |
| o  + oE.+ B .   |
|  .o . .  o =    |
|           o     |
|                 |
+----[SHA256]-----+
```

By running this command, you have actually created a pair of files that we refer to as a "key pair":

```sh
~/.ssh/iblservers
~/.ssh/iblservers.pub
```

![ssh key pair illustration](../_static/images/ssh_keygen_drawing.svg)

The file `~/.ssh/iblservers` is your private key. Be sure not to share its contents with anyone;  
The `~/.ssh/iblservers.pub` file is your public key, which you will add to the `~/.ssh/authorized_keys` file of all servers using the `ssh-copy-id` command.

You can use the same key pair to access all servers. However, it's safer to create a separate key pair for accessing the gateway. We highly recommend following this practice, and the rest of this tutorial will assume that you have created a separate key pair for accessing the gateway:

```shell
ssh-keygen -t ed25519 -C "From my PC" -f ~/.ssh/sshgwLeidenuniv
```

(let-server-recognise-your-key)=
### 2. Let server recognise your key

However, you also need to inform the servers that these keys belong to you and that you should be allowed to use them when logging in. This process involves entering passwords, so it's important to be extremely careful with the passwords you use.

- For the gateway connection, enter your ULCN password when the prompt says `ULCN@sshgw.leidenuniv.nl's` password:.
- For the BLIS server connection, enter the password you received via email when the prompt says `USERNAME@999.999.999.999's password:`. You will be prompted with `Password expired. Change your password now.`, so you will need to enter your old password again, followed by your new password twice. Be sure to remember your new password! Once succeeded, your old password is not valid anymore.

There is a difference using PowerShell on Windows compared to MacOS / Linux / GitBash / Cygwin. Please refer to the correct section for your setup.

#### 2.1 On Windows using PowerShellA

As the `ssh-copy-id` program is not available in Windows PowerShell, an alternative method is required to configure the server to recognize the generated keys.

Compose the following one line command with your ULCN username:

```PowerShell
type $env:USERPROFILE\.ssh\sshgwLeidenuniv.pub | ssh ULCN@sshgw.leidenuniv.nl "cat >> .ssh/authorized_keys"
```

Type your **ULCN** password to complete the operation. Now you have copied the corresponding public key `sshgwLeidenuniv.pub` to our university Gateway server. **Note** here in PowerShell, `$env:USERPROFILE` is a replacement of `~` for the "HOME" directory.

Now copy the corresponding public key `iblservers.pub` to our IBL servers using the following 3 commands. Do change the IP address 999.999.999.999 to the IP of BLIS, FRODO, BILBO:

```PowerShell
type $env:USERPROFILE\.ssh\iblservers.pub | ssh USERNAME@999.999.999.999 "mkdir -p .ssh && cat >> .ssh/authorized_keys"
type $env:USERPROFILE\.ssh\iblservers.pub | ssh USERNAME@999.999.999.999 "mkdir -p .ssh && cat >> .ssh/authorized_keys"
type $env:USERPROFILE\.ssh\iblservers.pub | ssh USERNAME@999.999.999.999 "mkdir -p .ssh && cat >> .ssh/authorized_keys"
```

#### 2.2 On MacOS, Linux, GitBash, Cygwin

`ssh-copy-id` program exists on these systems. The command to add the `sshgwLeidenuniv` key pair to the Gateway and upload the corresponding public key file is:

```shell
ssh-copy-id -i ~/.ssh/sshgwLeidenuniv.pub ULCN@sshgw.leidenuniv.nl
```

Remember to replace `ULCN` with your actual ULCN username in the command. After running the command, you will be prompted to enter your ULCN password. When succeeded, you should see output containing:

```text
...
Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'ULCN@sshgw.leidenuniv.nl'"
and check to make sure that only the key(s) you wanted were added.
```

Do not try it just yet (or if you tried, remember to `exit` back to your local machine). Now, from your local machine, add the other key to BLIS.

```shell
ssh-copy-id -i .ssh/iblservers.pub -o ProxyJump=ULCN@sshgw.leidenuniv.nl USERNAME@999.999.999.999 # BLIS
ssh-copy-id -i .ssh/iblservers.pub -o ProxyJump=ULCN@sshgw.leidenuniv.nl USERNAME@999.999.999.999 # BILBO
ssh-copy-id -i .ssh/iblservers.pub -o ProxyJump=ULCN@sshgw.leidenuniv.nl USERNAME@999.999.999.999 # FRODO
```

Remember to replace `ULCN` with your ULCN username, `USERNAME` with the username provided in the email, and `999.999.999.999` with the actual IP address provided in the email. Pay attention to which password it asks for. After your password is accepted, the command should finish with output containing:

```text
...
Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -o 'ProxyJump=ULCN@sshgw.leidenuniv.nl' 'USERNAME@999.999.999.999'"
and check to make sure that only the key(s) you wanted were added.
```

You can try it by following the instructions, but now you should be able to connect from your local machine using a easier command.

(configure-local-machine-to-use-a-correct-key)=
### 3. Configure local machine to use a correct key

After above steps, you still cannot access the gateway and our servers with the ssh keys, ie, you still need to use your password every time you connect. To make our efforts yield valuable results, ou need to add the correct configuration to your `~/.ssh/config` file on your local machine. This is the configuration file for `ssh` program to know which key to use when connecting to a specific server.

You must have noticed that in previous steps, we have generated two key pairs for "gateway" and "IBL servers" (BLIS, FRODO, BILBO). This is because we have the following infrastructure setup as indicated in the section [Set up connection using ssh through SSH gateway](#setup-connection-using-ssh-through-ssh-gateway).

![IBL server infrastructure](../_static/images/ssh_jump_drawing.svg)

Follow the steps below. (Note that the command below uses >> to append text to the file, even if it does not exist; if you already have the config file, do not use a single > as it will overwrite the existing file.)

```{code-block} shell
---
emphasize-lines: 3, 7, 8, 9, 16, 17, 18, 25, 26, 27
caption: Do not forget to change USERNAME and IP address
---
echo "
Host sshgw.leidenuniv.nl
    User ULCN
    HostName sshgw.leidenuniv.nl
    IdentityFile ~/.ssh/sshgwLeidenuniv

Host blis
    User USERNAME
    HostName 999.999.999.999
    # Use BLIS IP address in the above line
    ProxyCommand ssh -A sshgw.leidenuniv.nl -p 22 -q -W %h:%p
    IdentityFile ~/.ssh/iblservers
    ServerAliveInterval 60
    ServerAliveCountMax 10

Host bilbo
    User USERNAME
    HostName 999.999.999.999
    # Use BILBO IP address
    ProxyCommand ssh -A sshgw.leidenuniv.nl -p 22 -q -W %h:%p
    IdentityFile ~/.ssh/iblservers
    ServerAliveInterval 60
    ServerAliveCountMax 10

Host frodo
    User USERNAME
    HostName 999.999.999.999
    # Use FRODO IP address
    ProxyCommand ssh -A sshgw.leidenuniv.nl -p 22 -q -W %h:%p
    IdentityFile ~/.ssh/iblservers
    ServerAliveInterval 60
    ServerAliveCountMax 10
" >> .ssh/config
```

```{note}
Please note that the command above appends text to the config file. **Do not run it again** if you need to make changes to the configuration. Instead, open the file directly using a text editor such as nano or gedit on Linux or WSL, nano in GitBash, or Notepad on Windows.

It's important to note that the .ssh/ directory is usually hidden. To find it, configure your file explorer to show hidden files.
```

(connect)=
### 4. Connect

You have successfully generated and stored the keys on your local computer, and configured your computer to use these keys when connecting to the gateway and the BLIS server. Now you should be able to login BLIS with one command from your local machine:

```sh
ssh blis
```

This command will use the configuration you added to your `.ssh/config` file for the `Host blis` section to connect to the BLIS server. It will connect with your provided `USERNAME` and to the specific host, which in our case is provided as an IP address. The command is `ssh blis`.

For detailed instruction and explanation of how ssh works, please refer to How to login to [ALICE or SHARK - HPC wiki](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37748771/How+to+login+to+ALICE+or+SHARK).

We use "environments" to manage softwares on all systems. On BLIS, we use `micromamba`, a `conda` replacement, for [environment management](../basic_tools/micromamba.md#blis-users).

## Make direct SSH connection

If you have a desktop computer that is connected to a Ethernet socket on the wall, you don't need to jump from the University's SSH-gateway. You can omit key generation steps for `sshgwLeidenuniv`. Only create `iblservers`, `iblservers.pub` key pair and copy `iblservers.pub` directly to our server. The `config` file in `~/.ssh/` directory can also be simplified.

Following are full steps (work in GitBash for Windows machines), please check corresponding section in [Set up connection using ssh through SSH gateway](#setup-connection-using-ssh-through-ssh-gateway):

```shell
# Create ssh key pair
mkdir -p ~/.ssh
ssh-keygen -t ed25519 -C "From my PC" -f ~/.ssh/iblservers

# Confige your local machine to use the keys
echo "
Host blis
    User USERNAME
    HostName 999.999.999.999
    # Use BLIS IP address in the above line
    IdentityFile ~/.ssh/iblservers
    ServerAliveInterval 60
    ServerAliveCountMax 10

Host bilbo
    User USERNAME
    HostName 999.999.999.999
    # Use BILBO IP address
    IdentityFile ~/.ssh/iblservers
    ServerAliveInterval 60
    ServerAliveCountMax 10

Host frodo
    User USERNAME
    HostName 999.999.999.999
    # Use FRODO IP address
    IdentityFile ~/.ssh/iblservers
    ServerAliveInterval 60
    ServerAliveCountMax 10
" >> .ssh/config

# Add keys to the server
# You can omit the servers you don't use
ssh-copy-id -i .ssh/iblservers.pub USERNAME@999.999.999.999 #BLIS
ssh-copy-id -i .ssh/iblservers.pub USERNAME@999.999.999.999 #BILBO
ssh-copy-id -i .ssh/iblservers.pub USERNAME@999.999.999.999 #FRODO

# Connect
ssh blis
```
