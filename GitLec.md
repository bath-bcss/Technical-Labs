
Git
===

Git is the most popular version control tool for Computer Scientists and is
used extremely widely. We're going to run through the very basics of git so you
can use it for your own projects and can learn the more yourself!

This is inspired by the series of lectures "Missing Semester" ran by MIT. They
run much more in depth then we will. If youre interested in learning more then
I recommend you look there.
[Missing Semester](https://missing.csail.mit.edu/2020/version-control/)

Version control generally
----------------------------

Version control systems are used to track changes in files as you work on them.

Why are they useful? Its very useful to be able to look at older versions of
your projects and look what youve changed. And to be able to revert sections
back. Also they can be used for working with other people.

Installing git
-----------------

- Windows:
- For MacOS if you don't yet have XCode command line tools installed open 
    terminal and run
    `xcode-select --install`
    Then running `git --version` should produce something like:
    `git version 2.24.3 (Apple Git-128)`
- If you run Linux google for your specific distro

Making a git repository
-----------------------

In git all projects have a local repository, which represents the project.

To make a local repository make a folder for it then navigate to it in your
terminal shell. Then run `git init`

To make a repository make a foder for it then navigate your terminal shell to
it. Then run `git init`.

The repository is a folder with a .git folder in it, which stores all the
information git needs.

You can then run `git status` to see the status of your empty repository.

Staging files
-------------

Before git does anything to your files you need to "stage" them to make git
aware of them.

So if you add a file, say "text.txt", then run the command `git add text.txt`
and git will start tracking that file.

Git Commits
-----------



Git Diff
-----------

Git Branching
----------------

Git Merging
--------------

.git folder
-----------



