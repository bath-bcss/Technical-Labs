---
layout: note
title: Command line basics
date: 2020-10-12 #2021-10-12
---

{% include toc.md %}

## Introduction

Welcome to the notes for Technical Labs 2021. In this series we will aim to 
introduce you to some tools and ideas that will be useful for any computer 
scientist and anyone who uses computers regularly for complex tasks.

This first lab will focus on **Command Line Interfaces** (CLI). We will start 
here as the rest of this series will interact with tools through CLI's.

The vast majority of computing is done through graphical user interfaces. For 
99% of tasks these are great. But often user interfaces are fundamentally 
restricted. Sometimes you need to go old school and drop down to a command line 
interface. By learning about tools through the command line interface you should 
have a better fundamental understanding of the tool and how it works from seeing 
how it works at a lower level. Then you can apply that knowledge to make better 
use of graphical interfaces.

## What is a command line?

While most of computing is dominated by graphical user interfaces, command line 
tools stand apart by using a text based interface. In order to interact with the
computer you type commands. Programs display results, not by altering complex 
graphics, but by outputting lines of text.

### What is the shell?

The shell is the program that runs the interface, there are many shells but they 
all share the fundamentals. They allow you to give them input, they run 
programs, and they allow you to inspect the output.

These labs will be using the **b**ourne **a**gain **sh**ell (bash) [^1], which 
is the most popular shell.

### Getting started with the command line

With Macs and linux machines getting started with bash is very simple. You will 
need a "terminal emulator" which is the application that allows you to interact 
with a shell. 

On windows machines its more complicated. Bash is a shell for Unix based 
operating systems, which windows isn't. You can use "Windows Powershell" which 
is a different shell but it will be significantly different and use different 
programs. We recommend, for following along with these labs, using the [Windows 
Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install) (WSL) 
which is a system made by Microsoft to use a Unix shell on Windows. WSL will 
also be useful for the tools in the other labs and useful in general as most 
development tools are primarily Unix based.

## Using a command line

There are some basic concepts to be aware of when using any shell.

### The prompt

Once you open the command line you will be presented with the "prompt". Which 
will look like this:

```bash
technical-labs:~$
```

The text in the prompt can be customised so may vary user to user. To break down 
this prompt, 

- `technical-labs` is the current user
- `~` is the "current working directory" or where you are, `~` means the "home" 
    directory.
- `$` means you are not the root user, which will be covered more later

### Working directory

A shell is always at a position in your computers file 

[^1]:
    After this lab we will use the **Z sh**ell (zsh) which is backwards 
    compatible with bash with slightly more features.
