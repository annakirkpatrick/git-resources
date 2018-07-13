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
Mac users can install from a variety of sources, but the official builds can be found on [here](https://git-scm.com/download/mac).
Linux users should install through your package management system.

# Initial git setup
This is a set up that you will need to complete for each computer on which you want to use git.
(Note: you only need to do this once inside of the School of Math network. Since all of this configuration data is saved to your home directory, it can be accessed whenever you are logged in to a School of Math machine.)

First, we will set your name and email address.
This information will be included in every commit you make and is also used by github to figure out who has contributed to a project.
Since we are working with Georgia Tech Enterprise Github, you will want to use your `username@gatech.edu` email address.
Open a terminal and enter
```
git config --global user.name "Anna Kirkpatrick"
git config --global user.email "akirkpatrick3@gatech.edu"
```
substituting your own name and email address.
(The `--global` option in these commands is global to the user, meaning that it applies to all of the repositories you might work with. 
Git also has options to set your name and email on a per-repository basis.)

Next, we will configure your default text editor.
This is the (commandline) text editor that git will automatically open to allow you to write messages (mainly commit messages, which accompany changes/additions to the contents of the repository).
Some examples of commandline editors probably installed on your system are: vi, vim, emacs, and nano.
If you're familiar with these tools, then you probably already have a favorite; if not, I would suggest choosing nano as it is comparatively simple and easy to use.
```
git config --global core.editor nano
```

Git supports many other configuration options, but the above will be sufficient for most casual users.

