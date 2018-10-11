This document gives instructions for a few simple workflows using git and github.
In all cases, these instructions assume that you have already set up git on your computer and that you have already created or cloned a repository and have correctly set it up to interface with github.
For instructions on setting up git on a new computer or creating or cloning a repository, please see the full [git tutorial](https://github.gatech.edu/akirkpatrick3/git-resources/blob/master/git_tutorial.md).

These instructions also assume that you are working with only one remote and only one branch.
(If you don't know what those words mean, don't worry.
If you don't know what these things are, then you probably aren't using multiple!)

All of the commands given should be executed in a bash command line environment.
On Mac or Linux, this is just your system terminal.
If you are using Windows, I would recommend using git bash, which is available as part of [git for Windows](https://gitforwindows.org/).

# Contributing code to a collatorative project

## When you sit down to start work

1. Navigate to the repository.
```
cd path/to/repository
```

2. Pull down the latest changes from your collaborators.
```
git pull
```
In the vast majority of cases, this command will succeed without incident, and git will give you a message saying that it has made a merge by a recursive method. 
(Or your repository was already up to date in which case no merge was necessary.)
If git informs you that a manual merge is required and you are not comfortable with the merge process, please seek advice from a more experienced team member.

## After each hour (approximately) of work and when you finish any major tasks

1. Review the changes that you have made.
```
git status
```

2. Add files where you have made changes to the staging area. 
(These will mainly be source code and/or documentation in plain text or markup formats.)

```
git add file1
git add file2
git add file3
```

3. Take a look at your staged commit to make sure that you have not forgotten any important files.

```
git status
```
All new or modified files containing code or documentation should be included in your commit.
(You may exclude temporary files which you are using for experimentation in your current work session only.)
Automatically generated output (compiled code, log files) should not be included in commits and can be excluded from the output of `git status` using the `.gitignore` file. 
(See the tutorial or ask a more experienced team member for more information on `.gitignore.`)
Large amounts of data should never be included in repositories, but it is sometimes appropriate to include small amounts of data as a way of tracking the evolution of program output.
This should be discussed with your collaborators, and any data files you do not wish to include in the repository can be similarly excluded with `.gitignore`.)

If your commit looks good, then continue to the next step.
If you need to make changes, use `git add` and `git rm` to add and remove files as needed.

4. Make a commit to record your work.
```
git commit
```

5. Git should open your text editor so that you can enter a commit message.
Write a message that describes what changes you have made and why.
(You do not need to record which files were changed, your own name, or any timestamp information, as git saves this automatically.)

6. Optionally, if you know that your collaborators are also currently writing code, go ahead and update both your local repository and the remote copy on Github.
```
git pull
git push
```

## When you finish work for the day
1. Review the changes that you have made.
```
git status
```

2. Add files where you have made changes to the staging area. 

```
git add file1
git add file2
git add file3
```

3. Take a look at your staged commit to make sure that you have not forgotten any important files.

```
git status
```
If your commit looks good, then continue to the next step.
(See previous section for guidelines for what to include in commits.)
If you need to make changes, use `git add` and `git rm` to add and remove files as needed.

4. Make a commit to record your work.
```
git commit
```

5. Git should open your text editor so that you can enter a commit message.
Write a message that describes what changes you have made and why.

6. Push your changes to Github.
```
git push
```

If this command fails, the most likely cause is that one of your collaborators has pushed changes since your last pull.
To fix this, pull and then push again.
```
git pull
git push
```
When running `git pull`, there is a small chance that git will tell you that you need to manually merge changes.
(This can happen when you and a colleague both edit the same part of the same file.)
If you are not comfortable with the manual merge process, please seek assistance from a more experienced team member.

# Maintaining a log of weekly research progress updates
## When you begin working on your log for the week

1. Navigate to your repository

```
cd path/to/repository
```

2. Pull down changes from Github (not required if you work on only one computer)
```
git pull
```

3. Make a new directory for this week's updates
```
mkdir yyyy-mm-dd
```

4. Make a new text file for this week's report
```
cd yyyy-mm-dd
nano report_yyyy-mm-dd.txt
```
You can use any text editor of your choosing. 
Nano is just an example.
(You do not necessarily need to use a command line text editor.
Any GUI-based text editor is fine as long as you save your file in the appropriate location.)

5. Edit the plain text file and begin writing your report.

6. Copy any relevant supporting files into this week's directory.

For example, this might include a PDF of a paper in progress, data plots in PDF format, raw data tables as plain text, PDF of more complex data or information prepared in LaTeX.
It is generally not necessary to duplicate information that is already included in another repository; you can just provide a link in your report.

7. (Optional step that allows you to work on your report on multiple computers.
Also has the advantage of creating a remote backup of your work.)
Make a commit and push to Github.

Add your report to the staging area.
```
git add report_yyyy-mm-dd.txt
```
Then add your supporting files (if any) to the staging area.
```
git add file1
git add file2
```
If you are adding more than a couple files, you can run `git status` to check that you have added all of them.

Make a commit.
```
git commit
```
Use your text editor to write a commit message.
Since you are not yet finished with work for the week, it is good practice to include a phrase like "work in progress" or "rough draft" so that others seeing the automatically generated notification for your commit will know that you are not yet finished.

Push to Github.
```
git push
```

## As you are working on your report throughout the week
1. If you are working on multiple computers, pull down your latest updates.
```
git pull
```

2. Edit report_yyyy-mm-dd.txt using the text editor of your choice.

3. Add any new or updated supporting files (e.g. data plots, PDFs of papers) to this week's directory.
If you are updating a supporting file, be sure that you overwrite the original file.

4. (Optional step that allows you to work on your report on multiple computers.)
Make a commit and push to Github.

Add your report to the staging area.
```
git add report_yyyy-mm-dd.txt
```
Then add your supporting files (if any) to the staging area.
```
git add file1
git add file2
```
If you are adding more than a couple files, you can run `git status` to check that you have added all of them.

Make a commit.
```
git commit
```
Use your text editor to write a commit message.

Push to Github.
```
git push
```

## When you have finished your report for the week
1. Add your report to the staging area.
```
git add report_yyyy-mm-dd.txt
```

2. Add any supporting files to the staging area.
```
git add file1
git add file2
```

3. Verify that all of the relevant files have been added to the staging area.
```
git status
```
Look at this output and verify that all of the relevant files are listed as changes added to commit. 
Make sure that you do not have any untracked files.
(These will be listed as untracked in that the output of `git status` if you have any.)

4. Make a commit.
```
git commit
```

5. Git will open your text editor.
Write a message to accompany this commit.
In this context, a brief message is generally appropriate.
For example, "final report for [date]" should be fine.
Exit your text editor, saving the file.

6. Push to Github.
```
git push
```
