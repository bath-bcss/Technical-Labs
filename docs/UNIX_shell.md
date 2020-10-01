
UNIX Shell
==========

What is UNIX
------------

When people say UNIX they noramlly mean the family of UNIX-like operating systems that derive from 
the original AT&T UNIX operating system. The original UNIX was written, along with the C programming 
language, in the 1970's by Ken Thompson, Dennic Ritchie and others. There are a lot of UNIX-like 
operating systems, MacOS and Linux being the two most popular for dektop along with iOS and Android 
for mobile.

UNIX is characterised by its modular design where functionality is made up by simple tools, each of 
which perform well defined functions, and can be combined to together become more complex.
UNIX operating systems consist of many librarys and utilities along with a master control program, 
the kernal, which handles starting and stopping programs, handles the file system, and other low 
level tasks that programs share.

UNIX was instrumental in the development of the intenet and still makes up the vast majority of the 
machines that make up the internet.

What is the shell?
------------------

The shell is the command-line interpreter for UNIX-like operating systems. Users can control the 
operating system through the shell which is both a command language and a scripting language. Users 
tend to interact with the ith shell through a terminal emulator. Which, as the name suggests, 
emulate old style computer terminals. This is normally the "Terminal" app on your computer.

In essense, the shell is the language and syntax you use to input commands and scripts into the 
terminal emulator. The terminal emulator then sends those commands to the unix operating system 
which either runs librarys installled or runs utilities from the kernal. then the output is sent 
back to the terminal emulator and displayed.

The most common shell is the Bourne Again SHell, or bash for short, but shells like the Z SHell 
(zsh) and the Friendly Interactive SHell (fish) are gaining in popularity.

How to install a UNIX like command line on your computer
--------------------------------------------------------

For mac and linux users this answer is very simble. You are already running on a UNIX-like operating 
system, Install the terminal emulator of your choice (or use the pre installed options) and you're 
ready.

For Windows the answer is more complicated. As windows is not a UNIX-like operating system it doesnt 
use a UNIX shell, instead it uses powershell, which isnt very widely used and is incompatible with 
most UNIX tools.

However all is not lost! With Windows 10 Microsoft added a full Windows subsystem for Linux, which 
allows Windows users to use a UNIX shell, like bash, and most all of the GNU utilities that make up 
linux, just without the linux kernal! 

To install go to [this 
page](https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/) 
which gives instructions on installing a bash shell, then most everything should be the same from 
there on out.

How to use the UNIX shell
-------------------------

There are a few things to be aware of when using a UNIX shell, where you are and who you are. 

### Where

The where is what directory are you in? In a unix shell you are always have a working directory. To 
find your current working directory use the command "print working directory" which is abbreviated 
to `pwd`.

![PWDImage](Assets/UNIX_Shell/PWDCommand.png)

Then you can see the shell returns the current directory.

To change the working directory use the `cd` (change directory) command followed by where you want 
to go.

![CDCommandImage](Assets/UNIX_Shell/CDCommand.png)

You can also either use local file paths, from your current directory, or use the absolute path from 
the base directory.

![CDRelativeCommandImage](Assets/UNIX_Shell/CDRelativeCommand.png)

To list all the directories and files in the working directory use the `ls` command, short for 
"list".

![LSCommandImage](Assets/UNIX_Shell/LSCommand.png)

In unix any directories starting with a full-stop are hidden by default, to show these hidden files 
add the `-a` flag to the `ls` command.

![LSACommand](Assets/UNIX_Shell/LSACommand.png)

There you can see some unexpected entries, what are `,` and `..`? (There may be other hidden folders 
also). In UNIX in every directory there is `.` to represent the current directory, and `..` to 
represent the parent directory.

Combining this with cd and relative paths we can use `cd ..` to mavigate to the parent directory.

![CDUPCommand](Assets/UNIX_Shell/cdupCommand.png)

### Who

UNIX has a user system, and different users can access different files and different commands.

You can check what user you are with the `who` command.

![WhoCommand](Assets/UNIX_Shell/whoCommand.png)

