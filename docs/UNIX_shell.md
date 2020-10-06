UNIX Shell
==========

What is UNIX
------------

When people say UNIX they normally mean the family of UNIX-like operating systems that derive from 
the original AT&T UNIX operating system. The original UNIX was written (along with the C
programming language) in the 1970s by Ken Thompson, Dennis Ritchie and others. There are many 
UNIX-like operating systems - macOS and Linux being the two most popular for desktop, with iOS and 
Android dominating the mobile market.

UNIX-like systems are characterised by a modular design where functionality is made up of simple 
tools. Each tool performs a well defined function, and can be combined with other tools to together 
become more complex. UNIX-like operating systems consist of many libraries and utilities along with
a master control program - the kernel. The kernel handles starting and stopping programs, the file 
system, and other low level tasks that programs share.

UNIX was instrumental in the development of the internet and still comprises the vast majority of
the machines that make up the internet.

What is the shell?
------------------

The shell is the command line interpreter for UNIX-like operating systems. Users can control the 
operating system through the shell. The shell is both a command language and scripting language. 
Users tend to interact with the shell through a terminal emulator. As the name suggests, this 
emulates old style computer terminals. This is normally the "Terminal" app on your computer.

In essence, the shell is the language and syntax you use to input commands and scripts into the 
terminal emulator. The terminal emulator then sends those commands to the UNIX operating system 
which either runs installed libraries or utilities from the kernel. The output is then sent 
back to the terminal emulator and displayed.

The most common shell is the **B**ourne **A**gain **Sh**ell, or bash for short, but shells like the 
**Z Sh**ell (zsh) and the **F**riendly **I**nteractive **Sh**ell (fish) are gaining popularity. 
We'll be using bash.

How to install a UNIX-like command line on your computer
--------------------------------------------------------

For Mac and Linux users this answer is very simple. You are already running a UNIX-like operating 
system! Install the terminal emulator of your choice (or use the pre-installed options) and you're 
ready.

For Windows the answer is more complicated. As Windows is not a UNIX-like operating system it 
doesn't use a UNIX shell. Instead, it uses PowerShell, which isn't very widely used and is 
incompatible with most UNIX tools.

However, all is not lost! With Windows 10 Microsoft added a full Windows subsystem for Linux, which 
allows Windows users to use a UNIX shell (like bash) and almost all of the GNU utilities that make 
up Linux, just without the Linux kernel. 

To install go to [this 
page](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/) 
which gives instructions on installing a bash shell, then almost everything should be the same from 
there on out.

How to use the UNIX shell
-------------------------

When you open the terminal you will be presented with a **prompt**, which will look something like:

```
user:~$
```

This will be where you write commands. The dollar symbol tells you that you are not the root user, 
but we'll get to that later.

There are a few things to be aware of when using a UNIX shell: where you are and who you are. 

### Where

The **where** is what directory you are in. In a UNIX shell you always have a working directory. To 
find your current working directory use the command "print working directory" which is abbreviated 
to `pwd`.

![PWDImage](Assets/UNIX_Shell/PWDCommand.png)

You can see the shell returns the current directory. If you've just started the shell you'll be 
in your user's **home directory**. In UNIX you can always find the home directory, as `~` represents 
the current user's home directory - that's why it's in the prompt (`user:~$`).

To change the working directory use the `cd` ("change directory") command followed by where you want 
to go.

![CDCommandImage](Assets/UNIX_Shell/CDCommand.png)

You can either use local file paths (from your current directory), or use the absolute path from 
the base directory.

![CDRelativeCommandImage](Assets/UNIX_Shell/CDRelativeCommand.png)

To list all the directories and files in the working directory use the `ls` command, short for 
"list".

![LSCommandImage](Assets/UNIX_Shell/LSCommand.png)

In UNIX any directories starting with a fullstop are hidden by default. To show these hidden files 
add the `-a` flag to the `ls` command.

![LSACommand](Assets/UNIX_Shell/LSACommand.png)

There you can see some unexpected entries. What are `.` and `..`? In every directory in UNIX there 
is `.` to represent the current directory, and `..` to represent the parent directory.

Combining this with `cd` and relative paths we can use `cd ..` to navigate to the parent directory.

![CDUPCommand](Assets/UNIX_Shell/cdupCommand.png)

### Who

All UNIX-like systems have a user system, and different users can access different files and 
different commands.

You can check what user you are with the `whoami` command.

![WhoCommand](Assets/UNIX_Shell/whoCommand.png)

You can then change users by using the `su` command followed by the user you want to switch to. 
"root" is the super user in UNIX and so has all privileges. You shouldn't work as "root", because 
you might do something destructive by accident. The shell makes it clear you're root as the `$` is 
replaced by a `#`, and the prompt may change also.

![WhoCommand](Assets/UNIX_Shell/suCommand.png)

If you want to run just one command as the `root` user (a very common occurence), you can use the 
`sudo` command followed by the command you want to run. This will normally prompt you for an 
administrator's password or the root user password.

Basics of UNIX
--------------

Now you know the basics of getting around and how to change user, let's start using some commands!

In the UNIX shell, a command is structured with the name of the command followed by some arguments.

![UnixCommandExample](Assets/UNIX_Shell/CommandExample.png)

Here in red you can see the **Command**, in this case `git` (the subject of a future lab), followed 
by a list of arguments in blue. 

The command can fall into a few categories:

1. **Internal commands** - Certain commands fall into the remit of the operating system, like 
   managing the file system. These commands are managed by the OS 'kernel' and don't rely on any 
   executables.
2. **Included commands** - Some executables come included with and are considered part of the 
   operating system.
3. **External commands** - Executables the user has installed.

If the command comes in the first category then the shell hands the job straight off to the kernel 
to handle. Otherwise, the shell has to find the command you want to run. To do this, it goes and 
looks for executables with the name you specified in special directories. These directories are 
specified by the PATH variables, which will be covered later. 

Parameters are separated by spaces, unless multiple are surrounded in speech marks. In this case, 
they are treated as one parameter. One common style of parameter is a "flag". Flags look like the 
`-a` and `-m` above and generally alter the command's behaviour in some way.

Different commands take different parameters in different orders. How are you meant to know these 
parameters? You can look at the `man` pages.

Man Pages
---------

Man is short for manual, as the man pages are the manual for each command. Man pages contain 
information like how to use a command, what it does, what parameters it requires, along with the 
command's optional parameters and flags.

To look up the man page for a command use: 

```bash
man <command>
```

Scroll through the manual with the arrow keys (or `d` and `u` for down and up), and press the `q` 
key to exit the man page.

Man pages are an essential resource for learning UNIX, and a great quick reference if you forget 
parameters or flags for a command.

You can also use man pages to find commands, by using:

```bash
man -k <keyword>
```

You will be presented with a list of commands that use that keyword in their description.

Additionally, bash has `help` pages for built-in commands, for example `help pwd` gives you help on 
the `pwd` comamnd.

File management in UNIX
-----------------------

One of the first things you may want to do is manage files and directories. This can be done with 
the UNIX shell.

### Making directories

Making a directory is as simple as `mkdir <directory name>`

![mkdir example](Assets/UNIX_Shell/mkdirExample.png)

### Moving and renaming files and directories

The `mv` command has multiple uses. It allows you to move a file or directory from one file path to 
another. 

You can change the directory a file is in: 
```bash
mv <current directory path>/<file name> <new directory path>
```

You can also move a directory to another directory: 
```bash
mv <current directory path> <path of directory to move it to>
```

You can also use it to rename a file or directory: 
```bash
mv <file name> <new file name>
```

![mv example](Assets/UNIX_Shell/mvExample.png)

### Deleting files and directories

To delete a file use the `rm <file path>` command.

To delete a directory use the `rmdir <file path>` command. This can only be done on empty 
directories.

To delete a directory and its contents use the `rm` command with the `-r` flag to delete 
recursively.

***Warning:*** In UNIX there is no "trash" directory where deleted files go. When you delete a file 
it is gone. 

![rm example](Assets/UNIX_Shell/rmExample.png)

### Copying files and directories

Copying is handled by the `cp` command, which is the same as the `mv` command but moves a copy of 
the file or directory to the new file path.

Environment Variables
---------------------

Earlier we said the shell was a scripting language, and like any other programming language it can 
make use of variables. The command `export <variable name>="<data>"` defines a variable.

Then by writing `$<variable name>`, bash unpacks the variable to its string.

![ExportingVariables](Assets/UNIX_Shell/exportCommand.png)

The `echo <argument>` command simply prints the parameter given to `stdout`.

All the variables together make up the "environment". Programs can read the environment variables 
as well as any values passed into them. So, changing these environment variables can change the
behaviour of programs.

### Path Variables

The "PATH variable" is a special variable in the environment. We can get the value with `echo 
$PATH`.

![PATHVariables](Assets/UNIX_Shell/PathVariables.png)

Here you can see a big list of file directories. This is where the shell goes looking for the 
executables you want to run. You can look in the directories themselves to find a path, but if you 
need to find one particular executable you can use the `which <command>` command.

![WhichCommand](Assets/UNIX_Shell/whichCommand.png)

You can also run executables directly with their absolute path or local path - this is how you could 
run executables you make yourself without putting them in the path directories!

![RunningExecutablesWithPath](Assets/UNIX_Shell/RunningBinaries.png)

Connecting programs together
----------------------------

UNIX programs can take input and return output through two primary streams: the input 
stream and the output stream. By default, the input stream is what you type into the terminal 
emulator and the output stream is printed to the terminal emulator. 

If you've ever written a Python program the `input()` statement reads the input stream and the 
`print()` statement writes to the output stream. 

The streams don't need to be the standard input and output streams.
You can use the `>` operator after a command to save the result to a file.

![SaveToFileOperator](Assets/UNIX_Shell/SaveToFileOperator.png)

The `cat <file path>` command reads a file and outputs it to the standard output stream.

You can use the `<` operator to read a file as the input stream for a command.

![ReadFromFileOperator](Assets/UNIX_Shell/ReadFromFileOperator.png)

The `tail -n1` command returns the last line of the input stream.

Lastly, you can connect one program to another with a pipe: `|`. With a pipe you can take the 
output of one program and feed it into another.

![PipeExample](Assets/UNIX_Shell/pipeExample.png)

Here the `ip a` command lists lots of networking information, but I only want the line about the IP 
address starting "127.". So, I can use the `grep <string>` command that lets you search the standard 
input stream for strings and outputs the lines containing the strings.

Going forwards
--------------

Hopefully you now know how to move around the shell, change users, manage files, and accomplish 
basic tasks with the UNIX shell. Hopefully this introduction allows you to learn more from other 
online resources, as you'll understand what's going on. 

There's a lot more you can do with the shell - if we covered it all it would take the whole year! 
Some more will be covered in future Technical Labs but this should give you a good base to work 
from. Man pages are your friend - if you don't understand a command never be afraid to use them.

Exercises
---------

If you want to work on your UNIX skills here are some good practise exercises:

1. Install and open a UNIX shell!
2. Navigate to your home folder and then explore the file system. Use `cd`, `ls`, and `pwd` to get 
   around.
3. Create a new directory.
4. Rename a directory.
5. Look up the `touch` command.
6. Make some files!
7. Look into UNIX permission system and change some permissions!
8. Try playing around with `<`, `>`, and `|`.
9. Look at your PATH variables and try to find the executable of a command you know.

Credit
======

Written by [Alfie Richards](mailto:alfierchrds@gmail.com).

Editing by Joseph Cryer(mailto:jcryer1234@gmail.com).

Thanks to:

- Dr Russell Bradford
- Bence Babrián

For additional help

Please sent any corrections [here](mailto:alfierchrds@gmail.com).
