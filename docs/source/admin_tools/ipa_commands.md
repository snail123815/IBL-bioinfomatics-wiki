# Useful IPA commands

```{contents}
---
depth: 3
---
```

## User management

Everything can be done only after you do a

```sh
kinit [USERNAME]
```

with your login username. Assuming you have the right to manage users.

### Add user

To add a user, you have to have a group for this user, else IPA will create a user with GID\==UID. This may cause umask to be set to 002, which may lead to security issue.

```shell
ipa group-show [GROUP-NAME]
# Copy GID of this group
ipa user-add [USERNAME] \
    --first [FIRST-NAME] \
    --last [LAST-NAME] \
    --random \
    --gid [GID] \ # This will set users primary group
    --shell /usr/bin/bash

# Then add this user to group, there is no way of adding to multiple groups
# Even when gid is set, you still need to add user to that group
ipa group-add-member [GROUP-NAME-1] --users [USERNAME-1] --users [USERNAME-2]
ipa group-add-member [GROUP-NAME-2] --users [USERNAME-1] --users [USERNAME-2]
```

Each new user should belong to:

1. Their lab group

Make sure the lab group is in condablis group.

Change default shell

```shell
ipa user-mod [USERNAME] --shell=/usr/bin/zsh
```

### Find user

```sh
ipa user-find --gid [GID] # find users with this primary group
```

## Group

### Add group

```sh
ipa group-add --desc="Explain why this group exists" [GROUP-NAME]
ipa group-add-member [GROUP-NAME] --users [USERNAME-1] --users [USERNAME-2]
ipa group-add-member [GROUP-NAME] --groups [GROUP-NAME-1]
```

Information of groups

```sh
ipa group-find [GROUP-NAME]
```

Information of groups that a user belongs to

```sh
ipa group-find --user=[USERNAME]
```

## Password policy

Show current policy

```sh
ipa pwpolicy-show
```

change password expiration to 730 days

```sh
ipa pwpolicy-mod --maxlife=730
```