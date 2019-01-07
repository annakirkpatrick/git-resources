# Overview
The script compute_time.py allows students and mentors to easily track time spent on code development projects through git commit messages.
This document describes script installation, provides instructions for students on properly tracking their time in commit messages, and provides instructions on script use along with some suggestions for automation.

# Script download, installation, and first-use configuration

Experienced Linux users will note that there are many ways to manage scripts and that the method used here (linking from your ~/bin directory) is only one strategy.
If you are one of those experienced Linux users, you can skip this section.

These instructions have been tested on a School of Math Red Hat machine, but they should work on most Mac and Linux systems, provided that prerequisites been installed. 
This code should also run on Windows, but you will need to modify the setup instructions.


## Prerequisites
Before running the script, you will need to install git and Python (version 2 or 3 should be fine). 
These prerequisites are already met on School of Math Red Hat machines.
On other Linux systems, you should install using your package manager.
On Mac, Homebrew is suggested.


## Download
If you have not already, navigate to your desired location and clone this repository:
```
cd ~/gtDMMB/Code
git clone git@github.gatech.edu:akirkpatrick3/git-resources.git
```

## Make executable and create symbolic link
Navigate into the repository to find the Python script:
```
cd git-resources/time-tracking
ls
```
Verify that you see the file `compute_time.py` in the output of `ls`.

Set permissions to make sure the script is marked as executable.
```
chmod u+x compute_time.py
```

If you already have a bin directory and have already added it to your path, then you can skip the following.
Otherwise, we need to create ~/bin and add it to PATH.
```
cd ~
mkdir bin
echo -e "export PATH=$(PATH):~/bin" >> ~/.bashrc
```
In order for the changes we just made to PATH to take effect, you need to close and reopen your terminal emulator (if using a graphical Linux or Mac desktop environment) or log out of the machine and log back in (if using SSH).

Finally, we can make a symbolic link.
In the second command, substitute the actual location of the script.
```
cd ~/bin
ln -s ~/gtDMMB/Code/git-resources/time-tracking/compute-time.py compute_git_time
```

## Test your configuration
The git-resources repository contains time tracking codes in (newer) commit messages, so we can use it for a quick test.
Navigate back to the git-resources repository.
```
cd ~/gtDMMB/Code/git-resources
```
And now run the script.
```
compute_git_time "Anna Kirkpatrick" "Jan 1, 2019"
```
The script should output the total time logged since January 1.
It will also generate a log file with extension `tlog` listing all commit messages that contributed to that total time.

Optionally, remove the `tlog` file just generated before proceeding.
```
rm *.tlog
```

# Recording your time

## Technical instructions

The time spent working on a commit is recorded at the end of the commit message.
After the normal commit message describing changes made, type [num hours]h[num mins]m (e.g. `1h25m` for one hour, 25 minutes.)
Make sure this string is separated from the rest of your commit message by at least one white space character (e.g. space, tab, newline) and that it occurs at the very end of your commit message.
Here is a sample complete commit message.
```
fix bug causing segfault when opening second file 1h10m
```

It is also acceptable to omit either the hours or minutes section of the string. 
For example, `10m` and `1h` are both valid strings.

## Expectations for use in gtDMMB

All students writing code with gtDMMB are expected to organize all code in git repositories and use this system to track their time.
Time tracking does not need to be used with weekly updates repositories.
Instead, time spent on tasks described in the weekly update should be noted in that update.

A few additional expectations:
1. The time spent on a single commit should not exceed two hours. If a task takes more than two hours, break it into subtasks and/or stop at the two-hour mark to make a commit and document your progress to this point.
2. Changes should be pushed to Github at least once a day, more frequently if you are actively collaborating on code. This allows mentors to track your progress and creates a backup of your work.
3. Git should be properly configured with the author name property set on each computer where code development is completed. Each student should use the same author name consistently across all computers so that all of his or her commits may be easily located. (See the main [git tutorial](https://github.gatech.edu/akirkpatrick3/git-resources/blob/master/git_tutorial.md), or the [workflow for setting up git on a new computer](https://github.gatech.edu/akirkpatrick3/git-resources/blob/master/git_workflows.md#setting-up-git-on-a-new-computer), for more details.)

##If you mess up

If you make a mistake in your commit message (e.g., forgetting to include your time tracking, or simply making a typo) and you have *not* yet pushed to Github, you can use `git commit --amend` to revise your commit message.

The `--amend` option has many uses, but in this case you want to use it to change the commit message.
This is easy; just run
```
git commit --amend
```
Then enter your revised commit message, and save as usual to complete the commit.

Note that using the `amend` option is a form of rewriting history.
Please do not rewrite history on any commits that have already been pushed to Github, as this can cause significant issues for your collaborators.
If you notice a mistake on a commit that has already been pushed, simply make a note in your weekly report so that your mentors can properly account for your time.

# Computing Time Spent

## Script arguments
The script has 2 required positional arguments and one optional argument.
Namely:
- The *author name* is the first positional argument. It will almost always be enclosed in quotes because it will contain a space.
- The time *since* over which to search for commits is the second positional argument. This can be specified either as an absolute date and (optionally) time, e.g. "January 2, 2019" or as a relative date (examples below).
- The optional argument *repository path* allows you to specify a repository. If not given, the script will use your current working directory.

## Examples
We will use the 'git-resources' repository as an example.

From inside the repository, compute Anna's time contributions from the past week:
```
cd git-resources
compute_git_time "Anna Kirkpatrick" 1.week
```
Or since the beginning of the year:
```
compute_git_time "Anna Kirkpatrick" "Jan 1, 2019"
```

Or, from the home directory, compute Anna's time spent on this project in the last two weeks:
```
cd ~
compute_git_time --repository_path ~/gtDMMB/Code/git-resources/ "Anna Kirkpatrick" 2.weeks
```
Or, from the last 3 days
```
compute_git_time --repository_path ~/gtDMMB/Code/git-resources/ "Anna Kirkpatrick" 3.days
```

## Time log files
Each time you run the script, a time stamped file with extension `tlog` is created in your repository.
These collect the commits which contributed to the total time output by the program and can be used by students and mentors to further investigate where time was spent.
If you don't need this information, you may simply delete the files.

It is helpful to include `*.tlog` in your `.gitignore` file to avoid accidentally including one of these time log files in a commit.
