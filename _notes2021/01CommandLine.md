---
layout: note
title: Command line basics
date: 2021-10-12
---

{% include toc.md %}

## Introduction

Welcome to the notes for Technical Labs 2021. In this series we will aim to
introduce you to some tools and ideas that will be useful for any computer
scientist and anyone who uses computers regularly for complex tasks.

This first lab will focus on **Command Line Interfaces** (CLI). We will start
here as the rest of this series will interact with tools through CLIs.

The vast majority of computing is done through graphical user interfaces (GUIs). For 99% of tasks these are great. However, these user interfaces are regularly restrictive, so sometimes we need to go old school and drop down to a command line level. Learning about a tool through the command line interface gives you a better, more fundamental understanding of that tool and how it works, and lets you more easily apply that knowledge to make good use of graphical interfaces.

## What is the command line?

While most of computing is dominated by graphical user interfaces, command line
tools stand apart by using a text based interface. In order to interact with the
computer you type commands. Programs display results, not by altering complex
graphics, but by outputting lines of text.

### What is the shell?

The shell is the program that runs the interface. There are many different shells available, but they
all share the same basics. They allow you to give them input, they run
programs, and they allow you to inspect the output.

These labs will be using the **B**ourne **A**gain **SH**ell (bash) [^1], which
is the most popular shell.

### Getting started with the command line

With Mac and Linux machines, getting started with **bash** is very simple. You will
need a **terminal emulator**, which is the application that allows you to interact
with a shell.

On Windows machines it can be more complicated. **Bash** is a shell designed for 
Unix-based operating systems, which Windows isn't. You can use **Windows 
Powershell** instead, however it will be significantly different to **bash** and 
will use different programs.. We recommend, for following along with these labs, 
using the [Windows
Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) (WSL)
which is a system made by Microsoft to use a Unix shell on Windows. WSL will be 
useful in general, as most mature and well-known development tools are primarily 
Unix-based. Using WSL will also allow you to follow along with future labs more 
easily.

## Using a command line

There are some basic concepts to be aware of when using any shell.

### The prompt

Once you open the command line you will be presented with the **prompt**, which
will look something like this:

```
alfierichards:~$
```

The text in the prompt can be customised so may vary from user to user. Let's break down
this prompt:

- `technical-labs` is the current user
- `~` means the **home** directory. This section displays the **current working 
    directory** (cwd), or where you currently are within the file system.
- `$` means you are not the root user, which will be covered more later

### Command structure

In most shells the commands are structured in the same way. For a command like:

```
alfierichards:~$ ping -c 3 www.google.com
PING www.google.com (216.58.213.4): 56 data bytes
64 bytes from 216.58.213.4: icmp_seq=0 ttl=116 time=12.248 ms
64 bytes from 216.58.213.4: icmp_seq=1 ttl=116 time=11.851 ms
64 bytes from 216.58.213.4: icmp_seq=2 ttl=116 time=11.617 ms

--- www.google.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 11.617/11.905/12.248/0.260 ms
```

There are some sections we can break down:

- `ping` - this is the **name of the command** to run. In this example `ping` is a
  program that sends echo packets to a server to test if it's accessible.
- `www.google.com` - is an **argument**. This string is passed to the program.
  Here it's the address you want to send the packets to.
- `-c 3` is also an argument, but a special one called a `flag`. A flag is
  always a hyphen followed by a character. Often, as in this case, the next argument
  is associated with the flag.

### Working with the file system

A shell always has a position within your computer's file system, much like a
file browser has a current open directory. This is often displayed in
your prompt. To view the active working directory you can use the **p**rint
**w**orking **d**irectory command, `pwd`[^2].

```
alfierichards:~$ pwd
/Users/alfierichards
```

You can list all the files in your current directory with the `ls` command.

```
alfierichards:~/Desktop$ ls
Compilers		Individual Project	Technical Labs		untitled text.txt
```

You can display your files in a list with the `-l` flag, and show hidden files 
with the `-a` flag.

```
alfierichards:~/Desktop$ ls -al
total 32
drwx------@   8 alfierichards  staff   256 Oct  6 16:53 .
drwxr-xr-x+ 113 alfierichards  staff  3616 Oct  7 14:09 ..
-rw-r--r--@   1 alfierichards  staff  8196 Oct  6 16:53 .DS_Store
-rw-r--r--    1 alfierichards  staff     0 Jun 17  2019 .localized
drwxr-xr-x    4 alfierichards  staff   128 Oct  6 17:35 Compilers
drwxr-xr-x@   5 alfierichards  staff   160 Oct  5 17:15 Individual Project
drwxr-xr-x@   2 alfierichards  staff    64 Oct  4 10:14 Technical Labs
-rw-r--r--@   1 alfierichards  staff   267 Oct  5 17:15 untitled text.txt
```

In Unix-based systems, entities that start with a full stop (`.`) are **hidden**.

Other information such as file permissions, file owners, date added, and size
are also included but we will not cover them in detail here.

Additionally, `.` represents the current directory and `..` represents the
parent directory.

#### Moving around

You can navigate to different working directories with the **c**hange
**d**irectory command, `cd`.

```
alfierichards:~$ pwd
/Users/alfierichards
alfierichards:~$ cd Desktop/
alfierichards:~/Desktop$ pwd
/Users/alfierichards/Desktop
```

Note that the directory in the prompt changes.

Combining `cd` with `..` means `cd ..` will always take you to the parent
directory.

#### Interacting with the file system

There are other commands such as:

- `cp` to copy entities
- `mv` to move entities
- `rm` to delete entities
- `mkdir` to make a directory
- `chown` to change which user owns an entity
- `chmod` to change the permissions on an entity

You can learn how to use these commands from their **man pages** or by looking at
their **tldr page**.

### File paths in Unix

File paths are often a point of confusion for command line beginners. This is
because the same path can be entered in several different ways.

For instance, if the working directory is `/Users/alfierichards/` and I want to
print the contents of `/Users/alfierichards/Desktop` I could enter that several
ways:

- Relative path: `ls Desktop` or `ls ./Desktop` - this can become more
  explicit if there is a conflict.
- Absolute path: `ls /Users/alfierichards/Desktop` - this is useful if you want
  the command to always access the same file no matter the current working
  directory.
- Home directory path: `ls ~/Desktop` - this is very similar to the absolute path
  except it uses the current user's home directory (in this case
  `/Users/alfierichards`). This will point to a different location when logged in as another user.

#### Wild cards

Most **bash** commands accept wild cards, which are characters that meet certain
strings.

The `*` character matches every file name.

```
alfierichards:~/Desktop$ cat TechnicalLabs/_notes2020/*
```

The `cat` command outputs the contents of a file.

The above command will then output the content of every file in the `_notes2020`
directory.

### Command History

Bash stores the executed commands, to get the previous commands press the up 
arrow.

### Tab completion

Program names and certain arguments can be automatically filled by bash. To use 
this type the start of the word you need and press the tab key.

### Exiting commands

There are certain key combinations that mean certain things on the command line:

- `Ctrl-C` - sends an `abort` signal to the operating system. This usually exits 
    the current program
- `Ctrl-D` - sends an end of file character. This often causes programs that 
    expect a file to be piped to it (which we will cover later) to output the 
    result.

#### Exiting Vim

Vim is a very common command line text editor, its famously unintuitive to exit 
and many people have the experience of getting trapped in Vim.

To exit vim you need to enter the key sequence `ESC` then `:q`.


## man pages

Commands normally come with a manual, or **man page** as they are known. To view a
**man page** use the `man` command.

```
alfierichards:~/Desktop$ man ls -P cat

LS(1)                     BSD General Commands Manual                    LS(1)

NAME
     ls -- list directory contents

SYNOPSIS
     ls [-ABCFGHLOPRSTUW@abcdefghiklmnopqrstuwx1%] [file ...]

...
```

Here we have used `-P cat` to override the default behaviour which opens a
"pager" - we have overridden it to make it easier to display. To exit a pager
press `:` then `Q`.

### Finding commands

**Man pages** are great if you know what command you need, however that may not
always be the case. You can search for a command with the `-k` flag, which searches for given specific keywords.

```
alfierichards:~/Desktop$ man -k directory -P cat
basename(1), dirname(1)  - return filename or directory portion of pathname
bundle-clean(1)          - Cleans up unused gems in your bundler directory
bundle-init(1)           - Generates a Gemfile into the current working directory
bundle-open(1)           - Opens the source directory for a gem in your bundle
cd(ntcl)                 - Change working directory
chroot(8)                - change root directory
```

(again ignore the `-P cat`)

### tldr pages

For a quicker, more lightweight alternative to **man pages** you can use a tool called
**tldr**. It's available through a website at [tldr.sh](https://tldr.sh/), or by installing a command called `tldr`.

```
alfierichards:~/Desktop$ tldr cp

cp

Copy files and directories.
More information: <https://www.gnu.org/software/coreutils/cp>.

- Copy a file to another location:
    cp path/to/source_file.ext path/to/target_file.ext

- Copy a file into another directory, keeping the filename:
    cp path/to/source_file.ext path/to/target_parent_directory

...
```

## Environment variables

A command line environment needs contextual information - which user
is logged in, the current working directory, what terminal emulator is being used, what
shell is being used and much more. When commands run they need access to that
information, as it would be tiresome to always pass them in. As such, programs have access to
**environment variables**.

The `env` command prints all the current environment variables.

```
alfierichards:~$ env
TERM_PROGRAM=iTerm.app
TERM=xterm-256color
SHELL=/bin/bash
...
```

**Bash** will substitute any environment variable into a command if you use the
dollar symbol `$`.

```
alfierichards:~$ echo $USER
alfierichards
```

The `echo` command is one which simply returns what was given to it. In this
case bash substituted `$USER` with my username.

The `export` command can be used to define your own environment variables or
edit existing ones.

```
alfierichards:~$ export MY_VAR="variable content"
alfierichards:~$ echo $MY_VAR
variable content
```

Environment variables only exist for the current session. If you close the
terminal and reopen a new session any changed variables will be back to their
default values.

### PATH variables

When **bash** executes a command it needs to find the program to run. The command
contains the name of the program but not the directory where the program is. To
find the program, **bash** searches in a list of directories known as the **path**.
**Bash** gets the list from an environment variable called `PATH`.

```
echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/alfierichards/.cargo/bin:/Library/Frameworks/Python.framework/Versions/3.9/bin
```

Looking in these directories we find the binaries for the commands we run.
[^internal_commands]

```
ls /usr/bin
2to3-					ditto					jvisualvm				perlthanks				splain5.30
2to3-2.7				dmc					kcc					perlthanks5.18				split
...
```

When you install a new program you may want to update the environment variables
to include the new program. Most operating systems have subsystems for updating
your environment variables so you don't have to update them manually every time.

## Scripting

The real power of the command line is in how it allows you to write scripts and
combine commands. **Bash** is itself a programming language.

### Saving output

You can use the `>` operator to save the output of a command to a file and `>>`
to append the output to the end of a file.

```
alfierichards:~$ ifconfig
lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
... (100 lines or so)
alfierichards:~$ ifconfig > log.txt
```

After this operation the contents of the command is saved to a new file called
`log.txt`.

```
alfierichards:~$ touch file.txt
alfierichards:~$ echo "Line 1" >> file.txt
alfierichards:~$ cat file.txt
Line 1
alfierichards:~$ echo "Line 2" >> file.txt
alfierichards:~$ echo "Line 3" >> file.txt
alfierichards:~$ cat file.txt
Line 1
Line 2
Line 3
```

There are a few new commands in this example:

- `touch` - creates an empty file

### Inputting a file

Certain programs take input while they are running. Often beginner programming
projects use this standard input for games or similar.

```
alfierichards:~$ dc
5
5
+
p
10
```

`dc` is a reverse polish calculator that takes input through the standard input.

The `>` operator allows the use of a file as input.

```
alfierichards:~$ grep "shell" < Unix_Shell.md
title: Command line shell
2. [What is the shell?](#what-is-the-shell)
4. [How to use the Unix shell](#how-to-use-the-unix-shell)
## What is the shell?
The shell is the command line interpreter for Unix-like operating systems, used to control the
computer. The name "shell" refers both to the language you use to input commands and write scripts,
...
```

`grep` is a command to search a file. Here is it is finding every instance of
"shell" in last year's notes on the command line.

### Combining programs

One of the most powerful things you can do with a command line is combine
programs to make a single command that does a complex task.

The pipe operator `|` takes the output of one command and inputs it into the
next command.

```
alfierichards:~$ ifconfig | grep "127."
    inet 127.0.0.1 netmask 0xff000000
```

`ifconfig` outputs the details of your machine's network configuration.

This can unlock enormous flexibility and power.

```
alfierichards:~$ curl https://www.technical-labs.link --silent | grep --ignore-case "lab" | wc -l
      11
```

This gets the content of the website for Technical Labs, finds every instance of
"lab" then counts how many there are.

### Scripting

The power of the command line is massive - this lab has only touched a fraction of what can
be achieved. If you are interested in going beyond this lab and learning more we
recommend [The Linux Command Line and Shell Scripting
Bible](https://www.wiley.com/en-gb/Linux+Command+Line+and+Shell+Scripting+Bible%2C+4th+Edition-p-9781119700937).

## Super User

Some commands will need access rights higher than your user has access to. This
is normally a sign that it could break things or be damaging, so make sure you
know what you are doing when executing one of these commands.

The command **s**uper **u**ser **do** or `sudo` takes a command and executes that command
as the root user. It will normally need an administrator password to do this
(often your own password).

```
alfierichards:~$ sudo systemctl restart nginx
[sudo] password for alfierichards:
```

The password will always be hidden.

In this example the nginx service is being restarted. Interacting with a
background service normally requires super user rights.

## Thanks

Written by: Alfie Richards
Edited by: Joe Cryer

Additions and fact checking by:
- [Steven Borrie](https://backslash.build/)
- Professor Russel Bradford

[^1]:
    After this lab we will use the **Z sh**ell (zsh), which is backwards
    compatible with bash with slightly more features.

[^2]: Not all commands have a logical naming structure.
[^internal_commands]:
    Some commands are bash commands which it interprets internally so do not
    have binaries.
