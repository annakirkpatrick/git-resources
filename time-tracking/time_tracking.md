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
