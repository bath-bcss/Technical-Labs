
# Git, the sequel

## Table of Contents

## Git remotes

Having a repository for storing your work is only half the story, you may want
to backup your work, or share your work with others. For this purpose Git has
"remotes". Any Git repository can be a remote or have remotes it connects to, or 
both at the same time. Git's remote system is very flexible. 

### What is a remote

A remote is simply git repository accessible from the current repository that 
your local repository is configured to send and receive commits to and from. This 
may be another repository on the same system, or on another computer on the 
local network, but most commonly it's on a server accessed over the internet. 

This is a one way relationship, the local keeps track of the remote but a remote 
is completely oblivious of what locals are tracking it.

A local repository can "push" commits to the remote, or "fetch" commits from the 
remote.

There are many methodologies for structuring remotes, but the most common is to 
have each developer in a team have a local repository on their devices and one 
bare remote repository for them to collate their work on.

*Terminology:* Git doesn't care about the structure of remotes, but by 
convention we say the flow of changes, from development machines, to the remote 
repository is "upstream". Then the flow of changes from the shared remote back 
to the development machine is "downstream". In this way we can say a development 
machine is downstream of the remote.

### How does interacting with a remote work

When you set up a remote on your local repository you give it a name, to 
distinguish it as the repository can have multiple remotes. The most common name 
is "origin". The state of the remote is then represented on "remote tracking 
branches". 

To get a local repository with a remote you must either clone an existing remote 
repository or add a remote to an existing repository. To clone a remote 
repository use the command `git clone <remote repo URL> [name]`. This will make 
a new folder called `[name]` containing the copied repository. To add a remote 
to an existing local repository use the command 
`git remote add <remote name> <remote URL>`.

To retrieve commits from a remote to your repository you use 
`git fetch [remote_name]` (the remote can be omitted if its the only one 
configured in the local repository). This command will retrieve the objects from 
the remote repository and represent the commits on remote tracking branches. 

Remote tracking branches are functionally the same as remote branches except 
they are named like `remotes/<remote name>/<remote branch name>` and they are 
automatically generated on a fetch to represent the state of the branches on the 
remote. Bring changes into your local repository branches you merge the remote 
tracking branches into your local branches. 

**Note:** You should never work directly on the remote tracking branches, it 
causes lots of headaches.

To push your work to a remote, you use the command `git push [remote]` which 
will push the current branch to the configured remote branch.

However, if you've made a new branch in your local Git repository Git will not 
know which branch on the remote to add your changes into, or it may need to make 
a new one. To correlate local branches with branches on remotes git uses 
something called a "refspec". These are configurations within your Git 
repository which tells Git what remote branch you wish for the local branch to 
update and pull from. The most common way to add a refspec is to add the `-u` 
flag to your push command. This will add a refspec for your checked out local 
branch to a remote branch of the same name. The whole command is then 
`git push -u <repository> <branch>`.

After refpecs have been configured you can use the `git pull [remote]` command 
which will fetch all commits from the remote, add them to the remote tracking 
branches, then merge them into the local branches specified in the refspecs.

## GitHub example

GitHub is the most popular host for remotes. GitHub hosts remote git 
repositories and manages access to them. With GitHub you can control which users 
can pull your repository and which can push changes to it.

For example lets use a local Technical Labs repository, here you can see it with 
a long history. 

![technical Labs repo](assets/GitPt2/01GitRepo.png)

The command `git remotes` lists the current remotes. Here you can see there are 
no current remotes (I removed them for this example).

![No initial remotes](assets/GitPt2/02NoRemotes.png)

We then need to set up a repository on GitHub. To do this first setup an account 
if you don't already have one. Then you need to click the plus button at the top 
right, and then "New Repository" in the drop down. 

You will be presented with some options for setting up a new repository, here 
I'm going to enter details for a new GitHub repository for Technical Labs.

![Technical labs new repo screen](assets/GitPt2/03GitHubMakeRepo.png)

Then click confirm and you will be presented with the following screen showing 
your new empty repository.

![Technical labs new empty repository](assets/GitPt2/04NewRepoScreen.png)

The address at the top is the address for the remote that has just been set up 
and it is now hosting. Then we can add the remote to the local repo.

![Adding new repo](assets/GitPt2/05AddRemote.png)

Now the Git remote is added. But the remote is empty so we need to push to the 
remote, which means sending all the commits in our history to the remote, which, 
thankfully, Git can do easily and efficiently.

![Initial push](assets/GitPt2/06initialPush.png)

If we now look at the remote on GitHub we will now see the files of our most 
recent commit on the main branch, and we can go through and see all the commits 
making up or history.

![GitHub repo initialised](assets/GitPt2/07InitialisedRepo.png)

Then if we add some new changes to our local repository we can push the new 
commit. 

![Pushing new changes to remote](assets/GitPt2/08GitAddNewChanges.png)

And if we look at GitHub you will see the new file.

![New changes in git repository](assets/GitPt2/09GitUpdatedRepo.png)

Now imagine we're working on this project with others, they may have have cloned 
the repository and have submitted changes of their own, or alternatively you may 
have made changes with a different machine. Here, I have added changes from 
another clone I made.

We can then use `git fetch` to pull the changes into the remote tracking 
branches on our local repo.

![Git fetch example](assets/GitPt2/10GitFetch.png)

And then we can look at the remote tracking branches to see what branches there 
are.

![Checking branches after a fetch](assets/GitPt2/11Gitbranches.png)

Here you can see, the developer (me) did work on the branch `differentDeveloper` 
and then pushed that branch to the remote. In this instance I want to merge the 
other developers changes into my main branch, then push the merged branch with 
the changes to the remote.

![Git merge other developers 
changes](assets/GitPt2/12GitMergeOtherDevelopersWork.png)

### Cloning a repository

If a remote repository already exists you may want to clone that repository, to 
get a local repository copy of that repository.

To do this we will need to issue the command 
`git clone <Git url> [directory name]`. Where the Git URL is the same as before, 
and the directory name is the name of the directory you want the repository to 
be put into.

Here we will clone the same remote into a new local repository.

![Git clone example](assets/GitPt2/13CloneEx.png)

And with the `git clone` command Git automatically adds the remote it was copied 
from as the `origin` remote.

## Collaboration best practices and techniques

Now you have seen how to make a repository, push your changes to it, and pull 
other peoples changes to your repo we will run through some basic rules for 
using Git remotes and some common techniques you can use in your repositories to 
keep everything organised and save you some headaches.

### Some basic rules

1. Don't work on the same branch as other people-
    If you and a collaborator work on the same remote branch you will quickly 
    start having issues. This is because one of you will submit some commits, 
    then another will try submit commits, but they will get rejected because 
    your commits were supposed to attach to an earlier commit. Thus you must 
    pull the changes before you can commit. This leads to you having to do a 
    merge almost every time you want to push changes, which is tiresome.
2. Don't alter history already committed - It is possible to change commits in 
   your history. Some common ways are `git commit --ammend` to add changes to 
   your last repository, or `git rebase` which isn't covered in this series. 
   However, if you do this after having pushed those changes it is possible 
   another developer could have fetched your changes already. Then you are 
   changing the history they have already pulled, and when they next try push 
   all sort of conflicts will happen and headaches will follow.
3. No development on the main (or master) branch - The majority of repos keep 
   the master branch strictly for working commits. This means you can always 
   find a working version of the project in the main branch. If someone were to 
   work on the main branch it is likely they would have a few commits with bugs 
   and unfinished code, which would mean other developers wouldn't have any 
   version they could use if they need to deploy a working version or check 
   something.

### Some basic techniques

There are also some common techniques for managing your git repositories and 
keeping them organised. Here we'll just run through a few, there are many more 
you'll find people arguing about online.

Firstly, each bug fix and feature should have its own branch, and the name of 
the branch should start with "feat/<feature_name>" and "bug/<bug_name>" 
respectively. This allows for much easier tracking of bugs and features, stops 
development happening on the same branch, and facilitates concurrent 
development.

Secondly, each commit is encouraged to represent an atomic change. You should 
try avoid having multiple changes within one commit.

Thirdly, it is extremely helpful for anyone glancing at the commit graph for the 
commits to all have messages that are descriptive or the changes made within it. 

Lastly, in many repositories it in encouraged that before you push to the 
remote you make sure your current commit works. You might want to avoid pushing 
half finished work.

## Resolving merges

You may have noticed we talked a lot about merges, and indeed in most Git work 
flows merges are common. So lets briefly cover how to so a merge and how to 
resolve them.

Ideally with merges the two sets of changes will nicely separate, and git will 
be able to automatically combine them. However this is often not the case, if 
the two sets of changes have edited the same functions or the same lines this 
will result in merge conflicts. 

You start a merge with the command `git merge <branch_name>`, and if it can be 
completed automatically git will give a success message and prompt you for a 
message for the new commit merging the two branches. However, often instead it 
will return a message stating the commit can't be completed. Git will have added 
"conflict markers" to the conflicting files. At this point you can either use 
the command `git merge --abort` to abort the commit and return to your previous 
commit. Alternatively you can go into the conflicting files and resolve the 
conflicts.

Conflict markers will look something like this: 

```
<<<<<<< HEAD
The lines from the branch currently checked out
=======
The lines from the branch being merged in
>>>>>>> branch_being_merged_in
```

Where the lines with the `>`, `=`, and `<` are the conflict markers. Here you 
must choose the remove the lines with the markers and change the resulting lines 
to have the desired behaviour, often this means all the lines from one of the 
block or all the code from both.

After removing the conflict markers you can stage the file again with 
`git add <file>`. Then once you have done this for all conflicting files you run 
`git commit`, it will prompt you for a message, and then the merge is complete.

## Pull requests

With GitHub especially there is a very popular system for managing 
collaboration- Forks and Pull requests. In this system there will be a remote 
repository on GitHub which someone maintains. 

If you wanted to make some changes to the repository the repository owner could 
add me as a contributor, so you could submit changes directly to the repository, 
which they would be unwise to do in case you make changes they don't like. 
Instead, more often you will "fork" the repository, which means GitHub will make 
an identical repository in your account. You can then make my changes in this 
repository. 

When you have finished my changes on my fork you can submit a "Pull request", 
which is a request for the main repository to pull from your forked repository, 
which, if accepted, will add all my changes to the main repository. The 
maintainers of the main repository can then look through my changes, alter them 
if they need, and add them in as they desire. 

This is a very common workflow in Git and is how we handled getting 
collaborators suggesting changes to these notes for example.

## Exercises

1. Make a GitHub account.
2. Add some of your local repositories to your GitHub account.
3. Clone the repositories of some projects on GitHub, for instance [this 
   project](https://github.com/AlfGalf/TechnicalLabs) or 
   [Jekyll](https://github.com/jekyll/jekyll) the tool used to build the website 
   for these notes.
4. Try collaborating using git on your next group project! Try use good 
   practices and encourage others to do the same.
5. Practice good Git practices while working in your private repositories. Not 
   only is it good practice but you'll thank yourself later.

## References and resources

These notes are the second of two notes on git. The first can be found 
[here](https://bath-bcss.github.io/Technical-Labs/git.html).

A lot of this information comes directly from [this O'Reilly 
book](https://learning.oreilly.com/library/view/version-control-with/9781449345037/) 
which is available as part of the O'Reilly subscription all students at the 
University of Bath have access to.

Additionally there are some great resources for finding out more:

- [This 
    article](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/use-git-microsoft) 
    by Microsoft explaining their Git workflow.
- [Another 
    article](https://docs.microsoft.com/en-us/azure/devops/repos/git/git-branching-guidance?view=azure-devops) 
    by Microsoft explaining more about Git.
- [GitHub's best practices 
    article](https://resources.github.com/videos/github-best-practices/)
- [Oh Shit, git!?!](https://ohshitgit.com) is a great resource explaining many 
    common Git pitfalls and how to get out of them
- [Pro Git](https://git-scm.com/book/en/v2) is a free book explaining a lot more 
    of git in much more detail, including distributed Git and Github.

## Thanks

These notes were written by [Alfie Richards](https://www.alfierichards.com).

Edited by [Joe Cryer](mailto:jcryer1234@gmail.com)

With additional additions and corrections by:

