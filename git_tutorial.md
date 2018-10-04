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

So far this tutorial has covered only have to view and search the contents and history of repositories, but somebody has to actually create that repository content.
In this section, you will create a small repository from scratch, make a few commits, and backup your work to github.

## Creating a repository from scratch
On disk, a git repository consists of a directory and all of its subdirectories (recursively).
You can create a repository in an empty directory or and one which already contains code.
This makes it easy to add version control to an existing project.
Note that git will not provide backup and version control for your files simply because you create a repository in the directory. 
You must also add those files to a commit!

For this tutorial, we will create a repository in an empty directory.
You can place this directory anywhere you like, as long as it is not inside of another git repository.
For simplicity, the commands given in this section will assume that you have placed your new repository directory in your home directory , but you can adjust file paths if you choose to place your repository elsewhere.

Navigate to home, create a new directory, navigate into that directory, and create a repository:

```
cd ~
mkdir hello-git
cd hello-git
git init
```

The command `git init` creates a hidden directory `.git` which marks this directory as a git repository and stores history information (among other things).
So, we now have a git repository with no files and no history.


## Making your first commit

Now, let's create a file.
The details of your file are not important for this tutorial, but here's my file `hello.py`.

```
print("Hello, Git!")
```

If you are still getting familiar with using a commandline text editor, now is a good opportunity to practice.
You will also need to use your text editor to write commit messages.

For example, using nano:
``` 
nano hello.py
```
will open the editor with a new (empty) file.
You can then type the file contents.
When finished, press CTRL+w to save and then CTRL+x to exit the editor.

You have now created a file, but we have not yet asked git to record the fact that you created a file.
In order to tell git about this file, we need build a commit containing the file.

Before we build our first commit, we need to understand a little bit about how git manages files and commits.
There are three primary locations that git uses to build and organize commits: the working directory, the staging area, and the commit history.
You should think of each locations is containing a snapshot (or set of snapshots) of the status of all tracked files.
The working directory is the directory as it actually exists on disk.
As you actually write code, you are changing the content of the working directory.
The staging area is where you assemble your commits.
You can think of the staging area as containing a set of changes to files.
Once you have assembled all of the necessary changes in the staging area, you actually make a commit, at which point git generates a timestamp and a hash used to identify the commit and adds the commit to the history.

We've already made changes to the working directory, but we have not yet added those changes to the staging area.
We can see this by running `git status`.
To add our changes to the staging area, run
``` 
git add hello.py
```

Now that we've added a file, we can see the contents of the staging area by again running `git status`.
Since we don't have any other changes to add, we will go ahead and make a commit.
Run
```
git commit
```
Git will open your text editor so that you can write a commit message.
The commit message should generally be used to summarize the changes that were made in this commit.
Write a commit message, save the file and exit the editor.
Git will print some summary information about your commit, such as how many lines were added and removed.

If you want to see your commit, you can run `git log`.

## Backing up your work and collaborating on Github

So far, all of your work in this section has been local.
That is, you have only made changes to files on your own hard drive.
Now, we will learn how to upload your new repository to github.

First, we need to make github aware that you have a new repository.
Open your web browser and navigate to github.gatech.edu.
If you are not already logged in, do so now.

From your (logged in) homepage on github, find the green button labeled New repository.
There should be a list of your repositories on the right-hand side of the screen, and the new repository button is located at the top of that list.
Click on the new repository button.

Github should now present you with a page where you can create your repository.
The first two fields ask you to give your repository name and description.
For name, type `hello-git`.
The description field is optional and appears only on github.
It is generally good practice to fill out the description, so I'm going to say `test repository for learning git`.

Next you are asked to pick whether your repository should be public or private.
Public repositories are viewable by everyone who has an account on github.gatech.edu.
(If you are using github.com, then public repositories are viewable to anyone with Internet access.)
Private repositories are viewable only by you and collaborators that you add.
For the sake of this educational example, select private.

The final section of the repository creation form asks you to decide whether or not you would like to initialize the repository with the readme and/or a .gitignore file.
Both of these files are important to have in most repositories, and will be discussed later.
For the sake of this example, leave the check box asking if you want to create a readme unchecked and leave the .gitignore drop-down box set to None.
Click the green button at the bottom of the page to create your repository.

The next page gives you quick setup instructions for your new repository.
We will want the instructions titled `... Or push an existing repository from the command line.`
Following those instructions, return to your terminal and run the following 2 commands, substituting your actual username for [username].
```
git remote add origin git@github.gatech.edu:[username]/hello-git.git
git push -u origin master
```

Note: the two commands above assume you have configured SSH keys. 
If you are instead choosing to use HTTPS, the first command will have a different address. 
Just follow the instructions given to you by Github.

If everything is working correctly, you should be prompted for your SSH key passphrase.
Git will then print some status information to your terminal.
Assuming this command completes without errors, you have successfully uploaded your work to Github!
You can further verify this fact by returning to your web browser and refreshing the page.
You should now see your file posted on Github.

## Making some more changes
We've now seen how to create a repository, make an initial commit, and upload the repository to Github.
All that remains is to make further commits and continue to keep your local repository in sync with the remote copy hosted on Github.

In most cases, keeping your local repository in sync with the remote repository is very simple.
Just run
```
git pull origin master
```
before you start work for the day and whenever you need to download the latest work from your colleagues.
In many cases, the above command can be abbreviated by simply
```
git pull
```
As long as you are not working with multiple branches, it is safe to just run `git pull`. 
However, depending on the configuration details of your local repository, the shortened form of the command might not work.
Discussing those configuration details is beyond the scope of this tutorial, but git does generate intelligent error messages that should point you in the right direction if you want to investigate.

Making and synchronizing further commits is also easy.
Let's work through two more related examples: adding a readme to your project and editing your existing file 'hello.py'.

We'll start by adding a readme.
From your terminal, navigate to your repository and create a file `README.txt` using your commandline text editor.
The contents of that file really are arbitrary, but mine simply reads
```
A test repository for learning about git.
```
Add your new file to the staging area by running
```
git add README.txt
```
Now create a commit by running 
```
git commit
```
Enter a commit message, and now you've successfully made your second commit!

Now let's look at the process for modifying an existing file.
With your text editor, open 'hello.py' and add a comment line to the top of that file.
```
#Hello World program in my first git repo
```
Save the file and exit your text editor.
Now we will add our changes to the staging area by running
```
git add hello.py
```
Check that everything looks in order by running
```
git status
```
You should see that the changes you just made to 'hello.py' are now listed as staged changes.
That's what we wanted, so let's go ahead and commit.
```
git commit
```
As before, use your commandline text editor to enter a commit message.

Before pushing your changes to github, optionally run `git log` to see a record of the commits you have just made.
Finally, run
```
git push origin master
```
to backup your work.



### Some additional options for `git commit`

# Best practices

## Setting up a new project and repository

### README

###.gitignore

### Keeping things organized

## Some notes on adding version control to an existing project

## Managing projects with code and data

## Using version control with your LaTeX documents













