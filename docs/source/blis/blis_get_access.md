# How to get access to BLIS

```{toctree}
---
#caption: Table of contents
maxdepth: 3
---
```

BLIS is currently a semi-managed computer by University ISSC. It is connected to the ULCN account system. As a result, your username = ULCN user name, password = ULCN password, and the password will change as you change your ULCN password.

## Request for access

Write an email to Vriesendorp, B. (Bastienne).

## Set up ssh agent

Similar to ALICE, we also need to tunnel through a gateway, which is `sshgw.leidenuniv.nl`, to access our server. Once you can login using your user name and password to the gateway and then from gateway to BLIS, you can setup ssh login from your computer for easier access with one command: `ssh blis`.

You need to add ssh keys to both the gateway and to BLIS in order to use it without entering passwords from terminal.

Assume you already created key pairs: `to_gw_leidenu` for access the gateway, and `to_blis` for accessing BLIS. You then need to login to the gateway, add public key `to_gw_leidenu.pub` to `~/.ssh/authorized_keys` file, then from gateway, login to BLIS, add `to_blis.pub` to `~/.ssh/authorized_keys`:

```{code-block} shell
---
emphasize-lines: 6, 8
caption: Highlighted will be the key hashes that will vary.
---
# On local machine
# Create ssh keys, "user@host" is just a string to identify your self from the host, change to [your_name@your_computer], eg. du@office_pc
ssh-keygen -t ed25519 -C user@host -f ~/.ssh/to_gw_leidenun
ssh-keygen -t ed25519 -C user@host -f ~/.ssh/to_blis
cat ~/.ssh/to_gw_leidenu.pub
> ssh-ed25519 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX user@host
cat ~/.ssh/to_blis.pub
> ssh-ed25519 YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY user@host
# copy the output lines to replace the same content in the following commands.
# now login gateway
ssh sshgw.leidenuniv.nl
mkdir -p ~/.ssh
echo "
ssh-ed25519 XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX user@host" >> ~/.ssh/authorized_keys
# now login BLIS from gateway, you can get BLIS IP address when you are applying access. (ask if you don't) Change 999.999.999.999 to BLIS IP.
ssh 999.999.999.999
mkdir -p ~/.ssh
echo "
ssh-ed25519 YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY user@host" >> ~/.ssh/authorized_keys
```

Note: This is essentially the same operation which can be done by `ssh-copy-id`. You can choose to use the same key pair (not recommended) for both. 

Then exit to your local machine, add the following lines to your `~/.ssh/config` file (create one if not exist):

```
Host sshgw.leidenuniv.nl
    User [ULCN_USER_NAME]
    HostName sshgw.leidenuniv.nl
    IdentityFile ~/.ssh/to_gw_leidenu

Host blis
    User [ULCN_USER_NAME]
    HostName 132.229.246.243
    ProxyCommand ssh -A sshgw.leidenuniv.nl -p 22 -q -W %h:%p
    IdentityFile ~/.ssh/to_blis
    ServerAliveInterval 60
    ServerAliveCountMax 10
```

Now you should be able to login BLIS with one command from your local machine: `ssh blis`

Note:
One identity file on both machines should be good, but it is safer to have two different ones.
BLIS will ask for password once a week even when you have ssh keys setup correctly.
 
For detailed instruction and explanation of how ssh works, please refer to How to login to [ALICE or SHARK - HPC wiki](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37748771/How+to+login+to+ALICE+or+SHARK) for now.
