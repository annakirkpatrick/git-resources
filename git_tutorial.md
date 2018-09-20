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
Mac users can install from a variety of sources, but the official builds can be found [here](https://git-scm.com/download/mac).
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

# Get acquainted with Github
Github provides a few important functions beyond what you can accomplish with git alone.
Most importantly, it allows you to back up and share repositories with collaborators.
It also provides an environment where you can view the contents of repositories, albeit with some limitations.

For the moment, we will just focus on getting logged in to github.gatech.edu and understanding where you can find and view repositories.

Open your web browser and navigate to ```github.gatech.edu```.
If you are not already logged in, you will need to login with your Georgia Tech username and password.
(Yes, the login prompt looks different than the single sign-on prompts you are used to seeing. It's still legitimate; I promise.)

After logging in, github will probably offer you tutorial (which you can ignore/close), and it will bring you to your personal newsfeed (which is probably empty).
On the right-hand side of your homepage, you will see a list of your repositories and repositories where you are collaborator.
Clicking on any one of these repositories will bring you to a page showing the contents of the repository, and you can navigate through this view like you would any file explorer.
Most source files can be viewed inside of github by clicking on them.

At any time, you can click on the github icon in the upper left corner of the screen to return to your newsfeed.
You can also open a navigation menu by clicking on your profile picture in the upper right-hand corner.
From that menu, you can explore your personal profile, including a list of all of your repositories.
(Note that this list only contains repositories that you have created, not repositories where you are a collaborator.)

Take a few minutes to try it out.
Click on one of those repositories and see what it contains.
If you do not currently have access to any repositories, you can always have a look at the one which contains this tutorial.
This repository is public, so all you have to do is navigate to ```https://github.gatech.edu/akirkpatrick3/git-resources```.


# Optional configuration: SSH keys
**Note:  you must set up SSH keys in order to use git with private repositories from inside the School of Math computer network.**
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
In that menu, click on *Settings*.
In the left hand menu, click on *SSH and GPG keys*.
Then, click the green *New SSH key* button.

You should now be looking at a form which asks you for a title and a key.
For the title, you want to enter a brief description of the computer associated with the key (e.g. "School of Math Network", "Personal MacBook", "Ubuntu Desktop").
For the key, open the file `~./ssh/id_rsa.pub` with a text editor, copy the entire contents of the file, and paste into the key field.
Click "Add SSH key", and you're done.
(Github may prompt you for your password to confirm this new key actually belongs to you.)

# Getting copies of existing repositories: clone and pull
## Copying a repository: clone
We have already seen that we can view existing repositories online through the github interface.
Even if you are not contributing code to a project, it probably won't take long to discover the limitations of this approach.
As soon as you want to download many files at once, use tools like grep, or view history in a sensible way, you will need to clone the repository.

The command `git clone` creates a local copy of the repository you specify and sets up appropriate *remotes* so that you can easily download updates to the repository and make contributions to the repository (if you have permission).

For example, if you wanted to clone the repository containing this tutorial, then run
```
git clone git@github.gatech.edu:akirkpatrick3/git-resources.git
```
if you have set up SSH keys. Otherwise, if you are using HTTPS, run
```
git clone https://github.gatech.edu/akirkpatrick3/git-resources.git
```
(Unless the repository you're cloning is public, git will prompt you to authenticate with either your password or your SSH key and passphrase.)
Either command will create a new directory called `git-resources` in your current working directory. 
The directory `git-resources` will contain all of the files and directories in this repository, along with a hidden directory named `.git`. 
This hidden directory holds all of the information about the repository, including all of the history information.
You will most likely never need to even look inside of this directory, but you should know that it exists in case you ever need to move a repository manually (that is, putting it on physical media instead of using a service like Github).

Great, so the command to download a repository for the first time is `git clone`, but how did I come up with the address?
Well, I just asked Github, of course!
When viewing any repository, make sure that you are on the *Code* tab, and look for a green button with the text *Clone or Download*.
It should be towards the upper right-hand side of your screen.
When you click this button, a small box appears containing an address along with a button to copy it to your clipboard.
Note the small blue text that allows you to toggle between SSH and HTTPS addresses.
(Remember: you must use SSH on School of Math computers when you want to access private repositories or push to public repositories.)

## Updating a repository: pull
Once you have used the `clone` command to create a copy of a repository, git provides an efficient way to update your local copy of the repository to reflect remote changes.

In most cases, this is as simple as executing
```
git pull
```
with your working directory anywhere inside of the repository.
(As with `clone`, you will need to authenticate unless the repository is public.)

Pulling becomes more complicated if you have set multiple *remotes* or are working with multiple *branches*.
Neither of these topics will be covered in depth in this tutorial.

If you are not contributing code to the repository (and therefore have not made any commits to your local repository), then you should always be able to pull the latest changes without any conflicts.
If you have made commits locally, then your commits could conflict with other commits made to the remote repository.
In this case, manual merging of the relevant files will be required.
Merging will be covered in a later section.

Note: if you are not attempting to contribute to the repository but have locally edited some files in the repository, you may get an error message when attempting to run `git pull`.
As long as you do not want to keep your changes, you can easily reset the state of your working directory by running
```
git reset --hard
```
This command will undo all changes you have made to your local copy of the repository, so use with caution!
After running reset, you should be able to run `git pull` without conflicts or errors.


# Viewing history
## Viewing the commit log
One very important function of git is to maintain a record of changes to your code, along with information about who modified it, at what time, for what purpose.
Git maintains this history as a set of *commits*. 
Each commit is a set of changes made by a single person to some files in the repository.
Commits also contain a *commit message* written by the person who made the changes and a timestamp indicating when the changes were made.

To see the most recent commits, navigate to a directory in your repository and run
```
git log
```
As an example, we can look at this repository.
Here is a fragment of the output generated by `git log`.
```
commit e78f2394597360c29dc8fa82cdec62d17d0d86c2
Author: Anna Kirkpatrick <akirkpatrick3@gatech.edu>
Date:   Mon Jul 16 17:12:18 2018 -0400

    formatting fixes, clarification on authentication

commit 09c5e0913b1388dd96e88ca0f9fe7cf2af83a0b0
Author: Anna Kirkpatrick <akirkpatrick3@gatech.edu>
Date:   Mon Jul 16 17:07:07 2018 -0400

    formatting fixes

commit c536777e02b1d0c0eb1eaf739d9e4bf318419afb
Author: Anna Kirkpatrick <akirkpatrick3@gatech.edu>
Date:   Mon Jul 16 17:03:49 2018 -0400

    add sections on clone and pull

```

We are looking at the basic information for 3 recent commits.
The first line of each gives the *hash* of the commit.
(This is in fact a hash of the changes together with the author's name and email, the timestamp, and the commit message.)
Git uses this hash as a unique identifier for the commit.
In some other settings, such as on Github, you may see a shortened form of the hash, usually the first 7 digits, used to improve human readability.
The second line gives the author and email address, and the third line contains the timestamp.
Below the third line, set off with an indentation, is the commit message written by the author when the commit was created.
You can think of the commit message as a comment field for the commit.

The command `git log` supports a variety of options which allow you to search the commit history and change the presentation of the output.
The full list is vast, so we will mention just a couple of common options.

To specify the number of commits to output, we can simply specify that number as an option.
```
git log -2
```
returns
```
commit e78f2394597360c29dc8fa82cdec62d17d0d86c2
Author: Anna Kirkpatrick <akirkpatrick3@gatech.edu>
Date:   Mon Jul 16 17:12:18 2018 -0400

    formatting fixes, clarification on authentication

commit 09c5e0913b1388dd96e88ca0f9fe7cf2af83a0b0
Author: Anna Kirkpatrick <akirkpatrick3@gatech.edu>
Date:   Mon Jul 16 17:07:07 2018 -0400

    formatting fixes
```

Note: the option to specify a number of commits is useful in some circumstances (such as if you want to write log info to a file), but you probably will not use it much on a daily basis. 
By default, `git log` sends its output to a pager, like `less`, and so you can simply navigate through his many commits as you want using the arrow keys. 
To exit the pager, just type `q`.

If we actually want to see the changes that occurred in each commit, we can use the option `-p` or `--patch`.
Note the following example combines `-p` with the option `-1` explained above to limit the size of the output.

```
git log -p -1
```

The *patch* output tends to be long, so we will not include an example here, but you should try it in your own repositories.
In the patch output, lines beginning with a `-` were removed in this commit, and lines beginning with `+` were added in this commit.
Lines which instead begin with a space are included for context.

The `--stat` option presents a level of detail intermediate between the plain `git log` and the much more detailed `git log --patch`.
It presents information about which files were modified and how many lines were inserted and deleted from each file.

```
git log --stat -3
```
gives output
```
commit e78f2394597360c29dc8fa82cdec62d17d0d86c2
Author: Anna Kirkpatrick <akirkpatrick3@gatech.edu>
Date:   Mon Jul 16 17:12:18 2018 -0400

    formatting fixes, clarification on authentication

 git_tutorial.md |   10 +++++-----
 1 files changed, 5 insertions(+), 5 deletions(-)

commit 09c5e0913b1388dd96e88ca0f9fe7cf2af83a0b0
Author: Anna Kirkpatrick <akirkpatrick3@gatech.edu>
Date:   Mon Jul 16 17:07:07 2018 -0400

    formatting fixes

 git_tutorial.md |   10 +++++-----
 1 files changed, 5 insertions(+), 5 deletions(-)

commit c536777e02b1d0c0eb1eaf739d9e4bf318419afb
Author: Anna Kirkpatrick <akirkpatrick3@gatech.edu>
Date:   Mon Jul 16 17:03:49 2018 -0400

    add sections on clone and pull

 git_tutorial.md |   46 ++++++++++++++++++++++++++++++++++++++++++++++
 1 files changed, 46 insertions(+), 0 deletions(-)
```

## Searching the commit history

## Turning back time: viewing old versions of files

# Contributing code to a project

## Creating a repository from scratch

## Making your first commit

## Backing up your work and collaborating on github











