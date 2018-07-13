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
git config --global user.name "First Last"
git config --global user.email "FLast#@gatech.edu"
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

# Optional configuration: SSH keys
**Note:  you must set up SSH keys in order to use git from inside the School of Math computer network.**
Whenever you exchange information with github, you must authenticate your identity.
With the newer versions of git, you can use a https protocol which allows you to authenticate using your github password (which, for Georgia Tech github, is your Georgia Tech password).
For older versions of git, including the version currently running on School of Math machines, you must instead authenticate using SSH keys.
(Newer versions of git can also be used with SSH keys, and some people choose to do so for convenience.
Because SSH uses a public-private key pair, it is completely safe to use the same key to authenticate with multiple services, e.g. Georgia Tech's github.gatech.edu and the public-facing github.com.)

First, you will need to generate an SSH key pair, unless you already have one.  
If you're not sure whether or not you have generated a key previously, it is safe to just generate a new key.
We will use the program ssh-keygen.
```
ssh-keygen
```
The program will prompt you to enter a file in which to save your new key.
You can just press enter to accept the default location and file name.
It will then prompt you twice for a passphrase.
This is a password that you will need to type each time you want to use your SSH key.
(Basically, it is a small encryption key that unlocks a big encryption key.)
You can choose to leave the passphrase blank, but do know that this presents a small security risk, as anyone who gains access to your hard drive could then access anything protected by your SSH keys.

When the program finishes, you will have a pair of files. 
By default, these are `~/.ssh/id_rsa` (your private key) and `~./ssh/id_rsa.pub` (your public key).

You now need to provide your public key to github so that you can use your private key to authenticate.
Open web browser and navigate to `github.gatech.edu`. 
(The same process applies for `github.com`.)
Login if you have not already done so, and then click on the small profile picture icon in the upper right-hand corner of the screen.
This click should open a menu.
In that menu, click on Settings.
This will bring you to a settings page.
In the left hand menu, click on SSH and GPG keys.
Then, click the green New SSH key button.

You should now be looking at a form which asks you for a title and a key.
For the title, you want to enter a brief description of the computer associated with the key (e.g. "School of Math Network", "Personal MacBook", "Ubuntu Desktop").
For the key, open the file `~./ssh/id_rsa.pub` with a text editor, copy the entire contents of the file, and paste into the key field.
Click "Add SSH key", and you're done.
(Github may prompt you for your password to confirm this new key actually belongs to you.)


