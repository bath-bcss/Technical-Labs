# Debugging

## Table of Contents

## Introduction

Debugging is the process of fixing bugs in software. It may sound uninteresting 
but developers and computer scientists often spend the same amount of time 
debugging as they do writing code, so getting proficient at debugging and the 
comfortable with the tooling for it is important.

Debugging techniques fall into two categories. The first and most common is 
logging.

Logging is a technique that, if you've written much code at all, you're probably 
already familiar with. It involved littering your code with print statements, 
running the program over and over again, until eventually you track down your 
issue.

Logging is tried and tested, and always works.

"The most effective debugging tool is still careful thought, coupled with 
judiciously placed print statements” — Brian Kernighan, Unix for Beginners.

But when logging isn't enough, you can turn to debuggers, which will be the 
subject of this lab.

### What is a debugger

A debugger is a program that gives you control over another program that you are 
trying to test or debug, allowing you to:

- Halt the execution of a program
- Step through a program line by line
- Inspect values of variables at any point
- Alter the execution of a program
- Many more advanced features

There is a massive selection of debuggers. Many of languages provide their own. 
However, most debuggers have a similar command line interface. Also, most 
languages that are supported by a Jetbrains IDE have an almost identical GUI in 
within the IDE.

To show you both sides we are going to cover the command line application in 
these notes, and the Jetbrains interface in the recorded live session.

For this lab we're going to be using [The GNU Project 
Debugger](https://www.gnu.org/software/gdb/) (GDB for short). GDB works with a 
number of languages; with C, C++, Pascal, and Rust being some of the most 
popular. Here we will be using C as its part of the Bath CS course.

### Installing GDB

Unfortunately due to the privileges debuggers need in order to control another 
program installation can be complicated. For Python and Java installation will 
come with the installation of the language development kits, which no doubt you 
will have done already. For C debuggers it's more complicated, I recommend 
searching for instructions for your OS and desired debugger. However CLion will 
come with one installed already.

## Opening GDB

Before you start up GDB you need to compile the C code and include the `symbols 
table`. In brief the symbols table correlates commands and addresses in the 
compiled binary with lines of source code and the names of variables in the 
source code. To do this specify the `-g` flag in the compiler.

To open a binary with GDB use the command `gdb [binary file]`. GDB will open and 
present a prompt for your commands. The prompt will normally look like `(gdb)`.

In these examples I will be using this C file: 

`detab.c`:

```C
#include <stdio.h>

#define TAB_WIDTH 4

#define IN_SPACES 1
#define NOT_SPACES 0

int main() {
    
    int curLineLength = 0;
    int curChar;
    int spaceLength = 0;
    int state = 0;
    
    while((curChar = getchar()) != EOF) {
        curLineLength++;
        if (state == NOT_SPACES) {
            if (curChar == ' ') {
                state = IN_SPACES;
                spaceLength = 1;
            } else if (curChar == '\n') {
                curLineLength = 0;
                printf("\n");
            } else {
                printf("%c", curChar);
            }
        } else {
            if (curChar == ' ') {
                spaceLength++;
            } else {
                int curIndex = curLineLength - spaceLength;
                int numTabs = 0;
                int numSpaces = spaceLength;
                
                spaceLength = 0;
                state = NOT_SPACES;

                while (numSpaces > (TAB_WIDTH - curIndex % TAB_WIDTH)) {
                    numSpaces -= (TAB_WIDTH - curIndex % TAB_WIDTH);
                    curIndex += (TAB_WIDTH - curIndex % TAB_WIDTH);
                    numTabs++;
                }

                for (int i = 0; i < numTabs; i++) {
                    printf("\t");
                } 

                for (int i = 0; i < numSpaces; i++) {
                    printf(" ");
                }
                printf("%c", curChar);
            }
        }
    }
    return 0;
}
```

This program converts input with spaces for indentation to one that uses tabs. I 
wrote it a long time ago while learning C. As a result it's not very well 
written, but it will work as an example here.

### `r(un)` command`

After loading a binary into GDB the `r [arguments]` command will start the 
program.

## Break points

To get GDB to halt at a certain line you need to insert a *break point*. A break 
point tells GDB to stop whenever it reaches a certain line. Then once GDB has 
halted, you can enter commands to inspect or alter the program.

To insert a break point use the command `b [line number]`.

GDB will then print the name of the new break point you've created. You can look 
at the list of current break points with `info breakpoints`.

You can also enable and disable the break point with 
`enable [break point number]` and `disable [break pint numebr]` respectively.

When you next call `r` and the program gets to this line it will halt and the 
GDB prompt will open up, and it will let you know it's hit the break point.

You can look at the code around the break point with the `l` command, which 
lists 11 lines of code centred on the current line.

## Resuming execution

Once in a break point you may want to continue some execution, and there are 
option for ways to do this.

The `r` command will run until the next break point is hit.

The `n` (/`next`) command will run until the line below the current line runs in 
the code. Often called *step over*.

The `s` (`/skip`) command will run until the next line of code is reached. If 
the current line contains a function this will then stop on the first line of 
that function. That is why this is often called *step into* as it will go into 
functions.

The `f` (/`finish`) command will run until the end of the current function, then 
will break and print the result.

The `until [line number]` command will run until execution reaches a certain 
line.

## Examining the stack

In C and most programming languages each time you perform a function call 
information about the call is stored. This includes the location of the call, 
the arguments of the call, and the local variables of the function being called. 
This data is stored in a block called a *stack frame*. Stack frames together 
make up *the stack*.

### `bt (backtrace)` command

After you've halted in GDB you probably want to know is where you are and how 
you go there. When you reach a break point GDB will automatically select the 
executing stack frame. The `bt` command will then print all the stack frames up 
until the main stack frame.

You can specify a `-[number]` flag to only print `number` stack frames.

### The frame command

With the `frame [frame number]` command you can then select any frame you want.
Or use `up` to go up one frame and `down` to go down one.

### Printing the contents of a frame

The `frame` command with no parameters prints a description of the frame. 

`info frame` prints a more verbose description.

### Finding variable values

You can also inspect the contents of variables at any point with 
`print [variable]`.

## Altering execution

You can now run through a program in a controlled way. But you may want to 
change the course of execution. There are a couple ways to alter the path of 
execution in your program. 

### `j(ump)` command

The first way is with the `j [line number]` command will will jump to another 
line and resume execution there.

### `return` command

With the command `return [value]` GDB will return from the current function with 
`value`. 

### Assigning values to variables

You can alter execution be assigning different values to functions. To do this 
use the command `call [expr]` where the expression is an assignment to a 
variable. For instance, you could use the command `call foo=2` to set `foo` to 
2.

## Checkpoints

A more advanced feature that not all debuggers have is the ability to use 
checkpoints. The concept of checkpoints may be familiar from video games, 
essentially you can save the state of the program to later return to and try 
again. In this way if you have a specific part of the program you wish to debug, 
you can save a checkpoint before it occurs, try it, if it fails return to the 
checkpoint, change some state, and try again.

To save a checkpoint use the command `checkpoint`. You can see a list of 
checkpoints with `info checkpoint` and restore to a checkpoint with `restart 
[checkpoint number]`.

## Watchpoints

Another more advanced feature some debuggers support is the concept of *watch 
points*. Watchpoints are similar to breakpoints but instead of breaking whenever 
a execution reaches a line of code, a watchpoint breaks every time a variable is 
changed.

To set a watchpoint use the command `watch [variable]`. Watch points can be 
enabled, disabled and deleted in the same way as breakpoints.

## Exceptions and crashes

One of the main uses of GDB and other C debuggers specifically is to allow a 
little more insight into C's errors and crashes. When running in GDB if your 
program receives a signal, a `segfault` signal for example, the program will 
halt execution allowing you to examine where execution is at the point which 
your program is erroring. 

## Summary

Hopefully, you've seen some features of GDB that would have been useful in your 
debugging, or that you could imagine being useful in future debugging. On top of 
that GDB has a massive number of features we couldn't cover here. I want to 
emphasise that while this lab used GDB, most languages have a variety of 
debuggers that work with them, and they will have a similar feature set, 
normally with similar commands and interface.

Additionally, in the video for this week I have gone through the same feature 
set using the Jetbrains GUI in CLion, which may be easier if this is your first 
experience debugging.

## Sources

The bulk of the research for this lab was from the GDB manual which is open 
source and can be found [here](http://www.gnu.org/software/gdb/documentation/).

There will be good tutorials and introductions to any compiler you wish to learn 
online. You can also learn a lot from use.

## Credit and thanks

Written by [Alfie Richards](https://www.alfierichards.com)

Edited by [Joe Cryer](mailto:jcryer1234@gmail.com)

Additional help from:
