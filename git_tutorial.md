This is a brief introduction to git and github, intended mainly for users who need to access only the most common program functionality. 
A few notes are also included specifically for users working inside of the Georgia Tech School of Math computer network. 

# A note to Windows users
If you use Windows as your primary operating system, then this tutorial may be a little more challenging for you, both because you will need to install git yourself and because you are likely to be less familiar with the command line.
You will need to begin by installing [Git for Windows](gitforwindows.org). 
Git for Windows is bundled with a utility called git bash.
Though you can also use git from Windows Power Shell (or indeed the plain Windows command prompt), this tutorial will work best using git bash.
Whenever the tutorial directs you to a command prompt/terminal, you should open git bash.


# Prerequisites
This tutorial covers using git from the command line (also called the terminal, terminal emulator, or shell).
You don't need extensive knowledge in order to follow this tutorial, but you should be familiar with basic commands like cd, ls, mkdir, rm, rmdir, cp, and mv. 
If these commands are not familiar to you, please take a few minutes to work through a basic bash or Linux command line tutorial.

First, we will check that git is installed on your system. Open a terminal and type
```
git version
```
If you get the output `git version #.#.#` or similar, then you are good to go.
Otherwise, if you get a message like `command not found `, you will need to install git.
Instructions for Windows users are above.
Mac users can install from a variety of sources, but the official builds can be found on [here] (https://git-scm.com/download/mac).
Linux users should install through your package management system.