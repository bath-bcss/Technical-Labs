
Git
===

Git is the most popular version control tool for Computer Scientists and is
used extremely widely. We're going to run through the very basics of git so you
can use it for your own projects and can learn the more yourself!

This is inspired by the series of lectures "Missing Semester" ran by MIT. They
run much more in depth then we will. If you're interested in learning more then
I recommend you look there.
[Missing Semester](https://missing.csail.mit.edu/2020/version-control/)

Version control generally
----------------------------

Version control systems are used to track changes in files as you work on them.

Why are they useful? 
- You can look at older versions of your projects to see what has changed.
- It lets you revert sections of your project back to older versions if something goes wrong.
- It lets you work collaboratively with other people.

Installing git
-----------------

### Windows:
Download git bash from the link below, and follow the install process. When selecting the 'default text editor' for git bash, select 'nano' or your preferred text editor. The default (vim) is powerful, but has a very steep learning curve and so we don't recommend it for beginners.

[Windows Installer](https://git-scm.com/download/win)
    
Once installed, you should be able to open the "Git Bash" application, or right click on any folder and click "Git Bash Here" to open a git bash terminal at that location.
    
### macOS:
From macOS version 10.9 onwards, running the command `git --version` in Terminal should prompt you to install git if you don't already have it installed, and give you a version number if you do. Follow the prompts, and git should be installed on your system within minutes.
    
If this does not work, there is an installer linked below.

[Mac Installer](https://sourceforge.net/projects/git-osx-installer/)
    
Once installed, open Terminal and run the command `git --version` to confirm that git is installed successfully.
    
### Linux/Unix:
These instructions are highly dependent on your distro of Linux, so have a google around for platform-specific instructions. The link below contains commands for many of the most common Linux distros.

[Linux Install Commands](https://git-scm.com/download/linux)


Making a git repository
-----------------------

In git all projects have a local repository, which represents the project.

To make a local repository make a folder for it then navigate to it in your
terminal shell. Then run `git init`.

To make a repository make a folder for it then navigate your CLI (Command Line Interface) shell to
it. Then run `git init`.

The repository is a folder with a .git folder in it, which stores all the
information git needs.

You can then run `git status` to see the status of your empty repository.


Staging files
-------------

Before git does anything to your files you need to "stage" them to make git
aware of them.

So if you make a file, say "text.txt", then run the command `git add text.txt`
and git will start tracking that file.

Git Commits
-----------

Once you've staged a file you need to commit it.
This will make git aware of the a few changes:

- The addition of "text.txt"
- The addition of text into "text.txt"

To commit the changes to the repository run `git commit -m "Added text.txt"`, where "Added test.txt" 
is a message describing the changes youve made in this commit.

Git status
----------

To see whats happening in your local repository you can run `git status`.
This lists the commits you've made and what happened in each commit along with the 

Git Diff
-----------

Git Checkout
------------

Git Branching
----------------

Git Merging
--------------

.git folder
-----------




