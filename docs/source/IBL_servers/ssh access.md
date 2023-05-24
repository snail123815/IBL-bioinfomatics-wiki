# Access with ssh

*By C.Du [@snail123815](https://github.com/snail123815), Edder Bustos Diaz [@EdderDaniel](https://github.com/EdderDaniel)*

```{contents}
---
depth: 3
---
```

To use our Linux servers, you'll need access to a command line prompt. Here's how to get started on different operating systems:

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

## Set up connection using ssh through SSH gateway

To access our server from outside Leiden University's [Research Network](./Intro.md#what-is-research-network), you need to tunnel through a gateway called sshgw.leidenuniv.nl. Once you are able to log in to the gateway using your ULCN username and password, you can proceed with the setup.

It's perfectly safe to access the servers through the gateway, even if you're already within Research Network. For the purposes of this tutorial, we'll assume that you'll always use the gateway.

Once you've completed the setup, you can access our servers (e.g., BLIS) from your computer with a single command: `ssh blis`, `ssh frodo`, or `ssh bilbo`.

### Create ssh key pair

In your terminal do:

```shell
mkdir -p ~/.ssh
ssh-keygen -t ed25519 -C "From my PC" -f ~/.ssh/iblservers
```

When you execute this command, you'll be prompted to enter a "passphrase". If you don't want to have to enter this passphrase every time you access our servers, you can simply press ENTER to proceed. Alternatively, you can choose your own passphrase and enter it twice.

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

The file `~/.ssh/iblservers` is your private key. Be sure not to share its contents with anyone;  
The `~/.ssh/iblservers.pub` file is your public key, which you will add to the `~/.ssh/authorized_keys` file of all servers using the `ssh-copy-id` command.

You can use the same key pair to access all servers. However, it's safer to create a separate key pair for accessing the gateway. We highly recommend following this practice, and the rest of this tutorial will assume that you have created a separate key pair for accessing the gateway:

```shell
ssh-keygen -t ed25519 -C "From my PC" -f ~/.ssh/sshgwLeidenuniv
```

### Config your local machine to use the keys

You need to add the correct configuration to your `~/.ssh/config` file on your local machine. Follow the steps below. (Note that the command below uses >> to append text to the file, even if it does not exist; if you already have the config file, do not use a single > as it will overwrite the existing file.)

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

### Add keys to the servers

You have successfully generated and stored the keys on your local computer, and configured your computer to use these keys when connecting to the gateway and the BLIS server. However, you also need to inform the servers that these keys belong to you and that you should be allowed to use them when logging in. This process involves entering passwords, so it's important to be extremely careful with the passwords you use.

- For the gateway connection, enter your ULCN password when the prompt says `ULCN@sshgw.leidenuniv.nl's` password:.
- For the BLIS server connection, enter the password you received via email when the prompt says `USERNAME@999.999.999.999's password:`. You will be prompted with `Password expired. Change your password now.`, so you will need to enter your old password again, followed by your new password twice. Be sure to remember your new password! Once succeeded, your old password is not valid anymore.

The command to add the `sshgwLeidenuniv` key pair to the Gateway and upload the corresponding public key file is:

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
ssh-copy-id -i .ssh/iblservers.pub -o ProxyJump=ULCN@sshgw.leidenuniv.nl USERNAME@999.999.999.999
ssh-copy-id -i .ssh/iblservers.pub -o ProxyJump=ULCN@sshgw.leidenuniv.nl USERNAME@999.999.999.999 #BILBO
ssh-copy-id -i .ssh/iblservers.pub -o ProxyJump=ULCN@sshgw.leidenuniv.nl USERNAME@999.999.999.999 #FRODO
```

Remember to replace `ULCN` with your ULCN username, `USERNAME` with the username provided in the email, and `999.999.999.999` with the actual IP address provided in the email. Pay attention to which password it asks for. After your password is accepted, the command should finish with output containing:

```text
...
Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -o 'ProxyJump=ULCN@sshgw.leidenuniv.nl' 'USERNAME@999.999.999.999'"
and check to make sure that only the key(s) you wanted were added.
```

You can try it by following the instructions, but now you should be able to connect from your local machine using a easier command.

### Connect

Now you should be able to login BLIS with one command from your local machine:

```sh
ssh blis
```

This command will use the configuration you added to your `.ssh/config` file for the `Host blis` section to connect to the BLIS server. It will connect with your provided `USERNAME` and to the specific host, which in our case is provided as an IP address. The command is `ssh blis`.

For detailed instruction and explanation of how ssh works, please refer to How to login to [ALICE or SHARK - HPC wiki](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37748771/How+to+login+to+ALICE+or+SHARK).

We use "environments" to manage softwares on all systems. On BLIS, we use `micromamba`, a `conda` replacement, for [environment management](../basic_tools/micromamba.md#blis-users).

## Connect directly from inside Research Network

If you have a desktop computer that is connected to a Ethernet socket on the wall, you don't need to jump from the University's SSH-gateway. You can omit key generation steps for `sshgwLeidenuniv`. Only create `iblservers`, `iblservers.pub` key pair and copy `iblservers.pub` directly to our server. The `config` file in `~/.ssh/` directory can also be simplified.

Following are full steps (work in GitBash for Windows machines), please check corresponding section in [Set up connection using ssh through SSH gateway](#set-up-connection-using-ssh-through-ssh-gateway):

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
