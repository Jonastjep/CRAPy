# Remotely controlling a Raspberry Pi

The most direct way to connect to any remote server, be it a RPi or just another server for your work or research, is through SSH (Secure SHell). This method creates a secure tunnel between you and the remote address you are trying to connect to. Once you have ssh installed (generally comes pre-installed on GNU/Linux and MacOS; needs to be installed through PuTTY or similar for windows) you can just open the terminal and create the connection.

The command to connect is simply `ssh user@ip_address -p port_nb`. This should make a connection and you can enter the password. So for example if your remote server has the ip address 127.0.0.1:5000 with you user named Alice, you should type in `ssh Alice@127.0.0.1 -p 5000`. 

#### Controlling the remote system

Now that you are connected, you need to be able to do things with the connection. Here I assume you have a Linux/Debian based system (like Ubuntu or Raspbian). The most important commands are:

- `cd directoryName` for changing directory. You can have multiple directories separated by `/` , moving back one directory you'll use `..` and the directory you are in is represented by a single `.`
- `ls` to list the items in the current directory
- `pwd` to print the current (called working) directory
- `cp dirFrom/filename dirTo` to copy a file to a directory. If you want to copy a file to the current dir, you have to put a dot instead of the `dirTo`. If you want to copy a directory that has files insde and maybe subdirectories, you have to use `cp -r` that stands for recursive copying.
- `mv dirFrom/filename dirTo` to move a file. This can also be used to rename files, by moving them and having the new name as final destination.
- `rm filename` to remove a file. You can also remove a directory recursively by adding `-r`
- `nano filename` to modify the text content of a file. If the file doesn't exist it will create it. There are other editors available like vim or emacs, but I use nano personally.

Of course dempending on the software you have you will have many more commands that you have to use, like `python3 filename.py` to run a python script etc... All these commands have alot of different options, too many to summarize here, so if you need more out of a command you  can always call `command --help` and this will list the different possibilities. Equally useful is testing if some command exists, which I generally do by checking for the version with `command --version` as it doesn't do anything else than return the version number.

Depending on the location of the files you want to modify, you might not have enough priviledge as a simple user. This can be modified with the `chmod` command, but I will let you explore all this by yourself. This command comes with a catch however, as it relies on you having enough priviledge to make that change, which you don't have. This means that you need to define yourself as the superuser of the system, by adding `sudo` in front of the command ou want to take. This gived you the right do do basically anything on the computer, granting you with great power, but just as much responsability, as this will allow you to, for example, delete files that are necessary for the normal function of the system you are on.

#### Installing software

This `sudo` command is also necessary for you to install new software on your machine. The simplest way to download anything is using the packet managet apt, with `sudo apt install packageName`. There are more convoluted ways to install software that is not available on apt, by downloading a compressed .deb file or building the package from source, but this will not be covered here. Doing this also ensures that the software is the latest/specific version that you want, as apt is only updated infrequently. The deletion of software is done with `sudo apt remove packageName`. 

#### Transfering files from remote desktop

The process to send files from the remote system to the local one is the same as the simple `cp` but is done through ssh. The command is `scp -p port user@ipaddress:remoteDirectory/filename localDirectory`. With this you can also send files by just inverting the recieving and sender ends.
