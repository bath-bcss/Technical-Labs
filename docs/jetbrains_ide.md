
# IDEs and Jetbrains

## Table of Contents

## Introduction 

An IDE (or **I**ntegrated **D**evelopment **E**nvironment) is a GUI application 
that provides a comprehensive suite of tools for programmers. This is in 
contrast to the alternative of using separate programs for each task. However 
IDEs gentler learning curve and wide spread usage makes them a easier choice for 
less experienced programmers. In this lab we will aim to show the basics of the 
Jetbrains IntelliJ IDE and to introduce IDE concepts and context. Hopefully, 
then this can be transferred to other IDEs in the Jetbrains family and other 
IDEs generally. Jetbrains has a large number of IDEs with support for the vast 
majority of popular languages.

IntelliJ is Jetbrains' first and largest IDE, and it is one of the most popular 
IDEs in the world. Initially it was only for Java development, but since then 
has added support for a [large number of 
languages](https://en.wikipedia.org/wiki/IntelliJ_IDEA#Supported_languages) and 
you can use modules to add support for even more. 

Additionally [android studio](https://developer.android.com/studio/) is built 
atop IntelliJ. Most techniques learnt for IntelliJ can be used directly for 
android studio.

### Installing IntelliJ

You can download IntelliJ from the Jetbrains website 
[here](https://www.jetbrains.com/idea/), and as a student you can get the 
"Ultimate edition" for free 
[here](https://www.jetbrains.com/community/education/#students).

Installation varies platform to platform but is normally straight forward. 
Follow the instructions on IntelliJ's site.

When you first start IntelliJ you will be asked what theme you want to use and 
when plugins you want to install. I recommend you keep the number of plugins 
low, turning off some of the included ones. You can add plugins back later and 
this reduces the number of features you're presented with when starting.

## IntelliJ

IntelliJ is massively configurable. Nearly all the behaviours and keyboard 
shortcuts can be configured. For this reason we're going to be looking at 
IntelliJ as it comes out the box, and we'll be giving the default keyboard 
shortcuts for Windows and macOS, but you could change these as you wish.

IntelliJ is incredibly feature rich, which can be intimidating. But if you get 
to know how to do the basics you can start using it and learn the rest of the 
features as you need them.

## IntelliJ Basics

Lets run through some of the basics of IntelliJ before we start looking at some 
more advanced features.

### Making a project and project templates

When you start up IntelliJ for the first time you will be presented with a 
screen to create a new project or import a project. If you have already used 
IntelliJ on some projects you will see a list of the projects IntelliJ knows 
about on the left.

In the create project screen you will be presented with the **Templates** 
IntelliJ has installed. Templates are merely an initial set of project 
configurations and files to get you started with specific platforms. But 
projects are not set in stone by their template, you can add all the features 
and platforms you like to your project by changing the settings and files. A lot 
of developers avoid templates entirely.

You then have to give the project a name and tell IntelliJ where you want to put 
the project. Then press create and IntelliJ will make a project with the files 
and settings from the template chosen.

With only the plugins I need installed and with no template installed my 
IntelliJ looks like this.

![Blank IntelliJ](assets/JetbrainsIDE/IntelliJ_blank.png)

If you have more plugins installed your IntelliJ may look significantly busier.

### IntelliJ Layout

IntelliJ's layout is made up of **Tool windows** around a central editor, what 
those windows contain and where they are is very flexible. Plugins can provide 
tool panes in addition to the panes that come by default with IntelliJ. Also,
you can add, remove, minimize, and move panes as you desire. 

However the standard is to have navigation on the left with an editor central 
and panes regarding running programs, such as logs and debugging, at the bottom. 
By default IntelliJ uses this layout.

### Navigation

There are many ways to get around in IntelliJ, but the most basic is the 
**Project** pane on the far left. There is a drop down at the top to select which 
view you want to use. 

- The **Project** view shows the structure of your program
    by each files dependencies. However this wont reflect the actual file 
    structure of your project. 
- The **File Structure** view shows the actual file structure of your project.
- The **Problems** view shows the problems IntelliJ has found in your project. 
    For instance the errors and warnings generated when the project attempts to 
    compile.

Double clicking any item in the project navigation pane will open it in a tab in 
the editor window.

Another way to get around is search - to open the search press `Shift` twice, in 
the search window enter whatever file or item you're searching for then press 
enter to open a tab at that item.

There are many other ways to get around in IntelliJ, but they're outside of the 
scope of this lab.

### Editing

Editing text and code in IntelliJ can be much like any other text editor you've 
used. But IntelliJ has lots of smart ways to make writing code a little easier.

IntelliJ has syntax highlighting by default, which can make understanding code a 
lot easier.

Also, IntelliJ will constantly inspect your code while you write it and find 
where your code doesn't match the configured code style options or is unlikely 
to compile. It will annotate with warnings and errors to show this.

#### Some simple tricks

##### Live templates 

IntelliJ has a bunch of shortcuts to writing lines that you have to type over 
and over again, it calls these "Live Templates". For instance when writing Java 
you can type `sout` to make a `System.out.println();` statement. Other snippets 
like this can be found and configured in `IntelliJ prefrences > Editor > Live 
templates`

##### Code generation

Often when writing Java you will find yourself writing code blocks like access 
methods or interface implementations, which are fairly simple. IntelliJ can 
write some code for you! Press `Alt+Insert` on Windows or `⌘N` on macOS to enter 
the code generation window. Then you can select what code you want IntelliJ to 
generate.

##### Quick fixes 

A lot of code problems, like typos, access modifier mismatches or
missing imports can be fixed pretty easily. At any point when editing IntelliJ 
you can open the **Quick Fixes** panel to show the what solutions IntelliJ 
thinks it can provide in the code where the cursor is. To open the panel use the 
shortcut `Alt+Enter` on windows and `⌥⏎` on macOS. Then preview any fix with 
`Ctrl+Shift+I` on Windows and `⌥Space` on macOS. Then press `Enter` to apply the 
change.

##### Code formatting

A lot of Computer Scientists have strong opinions over how code should look. 
IntelliJ can keep your code consistent to a set of rules. You can get IntelliJ 
to reformat your code with `Ctrl+Alt+L` on Windows and `⌥⌘L` on macOS.

You can set your code style preferences in the IntelliJ preferences menu.

##### Renaming and refactoring

One of the most tiresome and error prone things to do when programming is to 
rename something or, more generally, to refactor code; fortunately IntelliJ will 
help you out with its extensive reformatting tools. You can find these in the 
`Refactor` section in the menu bar.

##### Generating documentation

IntelliJ can do some of the grunt work in writing JavaDocs, simply type `/**` in 
front of a class or function and IntelliJ will add lines for all the public 
fields or parameters.

### File management

File management can be done in the Project pane. To move files simply drag and 
drop them into place, as the result of a move you may be prompted to refactor 
code. To make new files you can right click in the Project pane and select 
`new`, it will then let you choose from a variety of supported file types. 

### Building, Compiling and Running

IntelliJ has a very flexible system for configuring build systems. Build systems 
will be the topic of a future lab so we wont cover them in depth here. However 
the gist of build systems is they can be used to automate the tasks required to 
build and compile a project. This could include tasks like finding and compiling 
dependencies, running tests on the code, compiling the code and running the 
compiled output.

The IntelliJ build configurations cover a large range. You can use build systems 
like Maven or Ant, or simply compile and run your code. Either way it all starts 
in the `Run/Debug Configuration` window you get to from the configuration 
button/ drop down in the top right. From this screen you can add as many 
configurations as you like. 

Here we will set up a simple configuration to run this command line application.

![Simple command line application](assets/JetbrainsIDE/Project_example.png)

We want to make a configuration to compile and run this code. To do this go to 
the configuration plane again, and click the add button in the top left. Here we 
can choose what template we want the run configuration to use, in this case the 
"Application" template does everything we want. We give the config a name and we 
specify the class we want the program to start with. We can specify options for 
the Java virtual machine, specify parameters for out program, and even specify 
environment variables. For this program we just need to specify the Main class 
and add some program arguments.

![IntelliJ run config](assets/JetbrainsIDE/Run_Config.png)

You could also select "Allow parallel run" if we need to run the same program 
multiple times. For example, if you were testing multiple clients for a server.

Now we have a configuration we can select it in the run config drop down in the 
top right, and the play button will then appear. Upon pressing that button 
IntelliJ will compile and run the program. You can also use `Shift+F10` on 
Windows and `⌃R` on macOS. 

After pressing the Run button IntelliJ will open the build and run panes in the 
bottom window. The build pane shows the output of the build config, and the Run 
pane shows the `stdout` of the program and allows input into `stdin`.

#### Compiler output

By default all your source code should go in a directory called `src` and 
IntelliJ will output the compiled code into a folder called `out`. This keeps 
your file structure clean of binaries. Additionally you shouldn't include the 
`out` directory in any Version control.

### Java docs

IntelliJ comes with an easy way to generate JavaDocs, you can find the tool in 
the menu bar:

`Tools > Generate Java Doc`

## Plugins

IntelliJ and all Jetbrains IDEs have very flexible and powerful plugin systems. 
Plugins can add an incredible amount including support for other languages, 
different build tools, themes, version control, and even a plugins to assist 
with the development of plugins.

### Adding and removing plugins

You can enable, disable and remove remove plugins through a page in the 
preferences window

`IntelliJ prefrences > Plugins > Installed` 

You can find new plugins and install them from the Marketplace tab.

Plugins often add extra pages to the preferences window to alter the behaviour of 
the plugin.

### Version Control

One of the most popular category of plugins on Jetbrains IDEs are version 
control plugins. Git was the subject of the 2nd and 3rd technical labs and so 
won't be covered here. However the version control plugin and the Git and GitHub 
plugins allow you to run many Git commands directly from IntelliJ and present 
information about your repository in a GUI.

However, you do not need to use the plugins, if you are more comfortable with 
using Git in the command line, or with another Git interface you can.

### Deployment plugins

There are lots of plugins to facilitate deployment and continuous integration. 
Both of which will be the subjects of future labs.

### IDE feature trainer

IntelliJ has a plugin available called IDE Feature Trainer that will walk you 
through a lot of the features of IntelliJ.

## Debugging

IntelliJ supports a powerful debugging and profiling suite. However debugging 
will be the subject of a future technical labs so we will not cover it in this 
lab. 

## `.idea` folder

IntelliJ stores all its settings and information about a project in the `.idea` 
folder within the project. For any project in which you are using version 
control you should make the decision whether or not you will include it. In the 
repository.

## Summary

We've tried to show here how to get around in IntelliJ, and tried to break down 
some of the scarier things IntelliJ will do. But more importantly we want to 
communicate that IDEs are tools for you, and you are in control of them. You can 
customise it to your liking and change its behaviour to match your tastes and 
needs. You do not need to keep all the plugins you are not using that add bloat. 
and you can add plugins and tools for whatever you want, to make the tool better 
for you.

Additionally, we focussed on IntelliJ a lot here, but all other Jetbrains IDEs 
are built on the same platform, and cover a massive range of languages. For 
instance you can use Pycharm for python and CLion for C and have a consistent 
experience between all of them.

There are also lots of other great tools and IDEs out there. They all have 
differences but almost everything gone through here is applicable to the 
majority of IDEs, be that with different shortcuts, different looks and 
different design choices.

Also, all of these features can be found in separate tools, you do not need to 
use an IDE, it simply gathers all the tools together under one consistent 
program. But what you prefer to use is up to you.

## Exercises

1. Get a Jetbrains student account and download the ultimate edition of 
   IntelliJ.
2. Make an empty project in IntelliJ
3. Make a basic main function and configure IntelliJ to run compile and run the 
   program
4. Find some plugins you like, try Rainbow brackets
5. Look into the version control plugin for IntelliJ
6. Get a Jetbrains IDE for a different language you use
7. Change the appearance and behaviour of IntelliJ to your liking
8. Open other Java projects in IntelliJ, set is up to run properly.
9. Install and use the IDE feature trainer plugin.

## Thanks and credit

The vast majority of the information for these notes comes from the 
[Jetbrains help 
articles](https://www.jetbrains.com/help/idea/discover-intellij-idea.html#developer-tools).

Written by [Alfie Richards](https://www.alfierichards.com/).

Edited by [Joe Cryer](mailto:jcryer1234@gmail.com)

Additional thanks to:

