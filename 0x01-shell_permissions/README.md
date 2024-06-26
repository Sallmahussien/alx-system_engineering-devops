# Project: 0x01. Shell, permissions

## Resources

#### Read or watch:

* [Permissions](https://linuxcommand.org/lc3_lts0090.php)
## Learning Objectives

### General

* What do the commands <code>chmod</code>, <code>sudo</code>, <code>su</code>, <code>chown</code>, <code>chgrp</code> do
* Linux file permissions
* How to represent each of the three sets of permissions (owner, group, and other) as a single digit
* How to change permissions, owner and group of a file
* Why can’t a normal user <code>chown</code> a file
* How to run a command with root privileges
* How to change user ID or become superuser<br>
## Tasks

* **0. My name is Betty**
  * [0-iam_betty](./0-iam_betty): Bash script that changes the user ID to `betty`.

* **1. Who am I**
  * [1-who_am_i](./1-who_am_i): Bash script that prints the effective userid of the
  current user.

* **2. Groups**
  * [2-groups](./2-groups): Bash script that prints all the groups the
  current user is a part of.

* **3. New owner**
  * [3-new_owner](./3-new_owner): Bash script that changes the owner of the
  file `hello` to the user `betty`.

* **4. Empty!**
  * [4-empty](./4-empty): Bash script that creates an empty file called `hello`.

* **5. Execute**
  * [5-execute](./5-execute): Bash script that adds execute permissions to the owner
  of the file `hello`.

* **6. Multiple permissions**
  * [6-multiple_permissions](./6-multiple_permissions): Bash script that adds
  execute permission to the owner and the group owner, and read permission to
  other users, for the file `hello`.

* **7. Everybody!**
  * [7-everybody](./7-everybody): Bash script that adds execution permission to the owner,
  the group owner and the other users, for the file `hello`.

* **8. James Bond**
  * [8-James_Bond](./8-James_Bond): Bash script that sets the permission for the file
  `hello` as follows:
    * Owner - no permission at all
    * Group - no permission at all
    * Other users - all permissoins

* **9. John Doe**
  * [9-John_Doe](./9-John_Doe): Bash script that sets the mode of the file
  `hello` to -rwxr-x-wx.

* **10. Look in the mirror**
  * [10-mirror_permissions](./10-mirror_permissions): Bash script that sets the mode
  of the file `hello` the same as the file `olleh`.

* **11. Directories**
  * [11-directories_permissions](./11-directories_permissions): Bash script that adds execute
  permission to all subdirectories of the current directory for the owner, the group owner
  and all other users. Regular files are not changed.

* **12. More directories**
  * [12-directory_permissions](./12-directory_permissions): Bash script that creates a
  directory `dir_holberton` with permissions 751 in the working directory.

* **13. Change group**
  * [13-change_group](./13-change_group): Bash script that changes the group owner to
  `holberton` for the file `hello`.

* **14. Owner and group**
  * [100-change_owner_and_group](./100-change_owner_and_group): Bash script that changes the
  owner to `betty` and the group owner to `holberton` for all the files and directories
  in the working directory.

* **15. Symbolic links**
  * [101-symbolic_link_permissions](./101-symbolic_link_permissions): Bash script that changes
  the owner and the group owner of the file `hello` to `betty` and `holberton`, respectively.

* **16. If only**
  * [102-if_only](./102-if_only): Bash script that changes the owner of the file `hello`
  to `betty` only if it is owned by the user `guillaume`.

* **17. Star Wars**
  * [103-Star_Wars](./103-Star_Wars): Bash script that plays Star Wars Episode IV
  in the terminal.
