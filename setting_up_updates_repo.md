This document gives step-by-step instructions for creating a repository on Github to store weekly research updates.
These repositories are used by junior researchers in the Heitsch research group to keep more senior researchers apprised of their progress and maintain a record of research work completed.

This document assumes no knowledge of git or Github but does assume that you have very basic knowledge of a Linux or UNIX-style command line.
If you are using a Linux or Mac system, you will want to use your system terminal.
If you regularly use Windows, I would recommend installing [git for Windows](https://gitforwindows.org/) which includes the utility git bash.
Git bash behaves like a terminal in Linux and can be used to follow the steps given in this document.

Unlike the full [git tutorial](https://github.gatech.edu/akirkpatrick3/git-resources/blob/master/git_tutorial.md), this document does not attempt to explain why these steps are given.
If you want to understand git, please consult the full tutorial or other resources.

# 1. Make sure that git is installed on your computer

Open a terminal and type
```
git version
```
If you get the output `git version #.#.#` or similar, then you are good to go.

Otherwise, if you get a message like `command not found `, you will need to install git.
Windows users should install [git for Windows](https://gitforwindows.org/).
Mac users can install from a variety of sources, but the official builds can be found [here](https://git-scm.com/download/mac).
Linux users should install through your package management system.
If you have any questions or concerns about installing software, please seek advice from a team member with more computer science experience or ask the School of Math computer support team.

# 2. One-time git configuration

If you have previously used git on this computer, then you can skip this step.

If you also intend to use git for code development in the near future, please read and follow the instructions in the git tutorial section [Initial git setup](https://github.gatech.edu/akirkpatrick3/git-resources/blob/master/git_tutorial.md#initial-git-setup).

Otherwise, if you don't intend to use git for code management in the near future, then run the following commands in your terminal.
Substitute your own first and last name, and your @gatech.edu email address in the following commands.
```
git config --global user.name "First Last"
git config --global user.email "FLast#@gatech.edu"
git config --global core.editor nano
```

# 3. Sign in to Github

Open your web browser and navigate to `github.gatech.edu`.
If you are not already logged in, you will need to login with your Georgia Tech username and password.
(Yes, the login prompt looks different than the single sign-on prompts you are used to seeing. It's still legitimate; I promise.)
After logging in, github will probably offer you a tutorial (which you can ignore/close).

# 4. Set up an ssh key

Return to your terminal, and run
```
ssh-keygen
```
The program will prompt you to enter a file in which to save your new key.
Press enter to accept the default location and file name.

It will then prompt you twice for a passphrase.
This is a password that you will need to type each time you want to use your SSH key.
You can choose to leave the passphrase blank, but do know that this presents a small security risk, as anyone who gains access to your hard drive could then access anything protected by your SSH keys.

Return to your web browser and navigate to `github.gatech.edu`. 

Click on the small profile picture icon in the upper right-hand corner of the screen.

In that menu, click on *Settings*.

In the left hand menu, click on *SSH and GPG keys*.

Then, click the green *New SSH key* button.

You should now be looking at a form which asks you for a title and a key.

For the title, you want to enter a brief description of the computer associated with the key (e.g. "School of Math Network", "Personal MacBook", "Ubuntu Desktop").

For the key, open the file `~./ssh/id_rsa.pub` with a text editor, copy the entire contents of the file, and paste into the key field.

Click "Add SSH key", and you're done.
(Github may prompt you for your password to confirm this new key actually belongs to you.)

# 5. Create your updates repository on Github

In your web browser, return to `github.gatech.edu`.
On the right-hand side of your screen, locate the green button labeled *New repository* and click on it.
You should be presented with a form containing several fields for you to fill out.

In *Repository name* type "[your name]-weekly-updates".
(So, for example, my repository name is "anna-weekly-updates".)

In *Description* type "[your name]'s weekly research progress update."

Click the radio button labeled *Private*.

Check the box labeled *Initialize this repository with a README*.

Leave the *Add .gitignore* option set to *None*.

Click *Create repository*.

# 6. Give repository access to your supervisor(s)

If you just finished the previous step, then you should currently be looking at your new repository.
If not, return to the homepage of github.gatech.edu and then click on your repository name in the right hand column.

Click on the *Settings* tab.

From the left-hand menu, click *Collaborators*.

You should see a message telling you that the repository does not yet have any collaborators.
Github should also present you with a form to search for users to add as collaborators.
Click on this text field.

Enter the name or username of your supervisor(s).
Select the correct person from the list of matches and then click *Add collaborator*.

It is generally easier to search by username.
Christine Heitsch has username "cheitsch3".
Anna Kirkpatrick has username "akirkpatrick3".

Generally speaking, graduate students and postdocs should add Christine Heitsch as a collaborator on updates repositories.
Undergraduate students should add the graduate student or postdoc supervising them as well as Christine Heitsch.

You can add additional collaborators, if needed, by returning to this page in the future.

# 7. Clone your repository to your computer

In your terminal, navigate to the location where you would like to keep a local copy of your updates repository.

In your web browser, return to the *Code* tab of your repository.
Find the green button labeled *Clone or download* on the right-hand side of your screen, and click on this button.

A small box should appear underneath the green button.
If that box says *Clone with HTTPS*, then click the small blue text *Use SSH*.
You should now be looking at a box titled *Clone with SSH*.

Click the copy-to-clipboard button to copy the address provided.

Return to your terminal and run
```
git clone [address you copied]
```
Then run
```
ls
```
to verify that git has created a new directory for your local repository.
Navigate into your new repository with
```
cd [your name]-weekly-updates
```

# 8. Fill out your README and make a commit

In your terminal, navigate into your repository directory.
(If you just finished the previous step, you should already be there.)

To demonstrate the use of the command line text editor `nano`, we will use it to fill out the README file.
```
nano README.md
```
You should see a file containing only one line, namely
```
# [your name]-weekly-updates
```
You can delete this line using the arrow keys to move your cursor and the backspace or delete keys to delete characters.
Replace this line with a description of this repository.
You may borrow mine, if you want:
```
This repository stores [your name]'s weekly research progress reports.
Each directory is dated yyyy-mm-dd with the anticipated meeting date.
A plain text file and each directory gives the exposition of the weekly report.
Additional figures or data may be included in this directory or in additional subdirectories if needed for organization.
Updates accompanied by large datasets or complex code will instead contain a pointer to a project directory or github repository.

Weekly reports have been written beginning in [date]. 
Some documents summarizing progress before this point are also included.
```

When you have finished typing your README, press control + X to exit nano.

Nano will ask you if you would like to "Save modified buffer."

Press Y to save your changes and then press enter to keep the same file name.
Nano will close and you will be returned to your terminal.

Now we make a commit.
Run
```
git add README.md
git commit
```
When you run the second command, nano (or whichever text editor you configured when setting up git) will open again so that you can write a commit message.
In this case, a simple commit message will suffice.
Type 
```
create README
```
and then press control + X to exit nano.

As before, press Y to save your changes and enter to accept the default filename.
Git will display a message summarizing your changes.

Push your changes to Github
```
git push
```
Enter your passphrase, and you've successfully backed up your work!

# 9. Set up Slack notifications

Weekly updates repositories should post notification messages to the *updates* channel.
Complete instructions for setting up these notifications can be found in a separate file: [slack_notifications_github_enterprise_instructions.txt](https://github.gatech.edu/akirkpatrick3/git-resources/blob/master/slack_notifications_github_enterprise_instructions.txt)

For details on how to post your weekly update reports, see [section Maintaining a log of weekly research progress updates in file git_workflows.md](https://github.gatech.edu/akirkpatrick3/git-resources/blob/master/git_workflows.md#maintaining-a-log-of-weekly-research-progress-updates).
