# Checking getting the other  branches 
Android :*git fetch && git checkout Android* - slack channel is (android)
DataAnalysis: git fetch && git checkout DataAnalysis slack channel is (data analysis)
Latex_Src: git fetch && git checkout Latex_src slack channel is (paper)

---

#Utilizing *requirements.txt*

Instead of pushing the virtual environment to the reapo we will just save our environments settings inside a requirements.txt file. Once you have your virtual envirnment set up outside of your local git repo
use : *pip install -r requirements.txt* inside your activated virtual environment. It will automatically update your dependincies. If you make any changes to your local environment use pip *freez>requirements.txt* it will overwrite the requirements.txt file with all the python libraries that you have installed in your virtual environment including the ones that you recently added. This will save space and time on your commits and pulls from the repo.

---



## Activating a virtualenv
 
Activating a virtualenv will put the virtualenv-specific python and pip executables into your shell’s PATH.

### On macOS and Linux:

*source env/bin/activate* to activate the environment

### On Windows:

*.\env\Scripts\activate*

---

## You can confirm you’re in the virtualenv by checking the location of your Python interpreter, it should point to the env directory.

### On macOS and Linux:

*which python*
.../env/bin/python

### On Windows:

*where python*
.../env/bin/python.exe

As long as your virtualenv is activated pip will install packages into that specific environment and you’ll be able to import and use packages in your Python application.

---

## Leaving the virtualenv
If you want to switch projects or otherwise leave your virtualenv, simply run:
*deactivate*
**Edit a file, create a new file, and clone from Bitbucket in under 2 minutes**

When you're done, you can delete the content in this README and update the file with details for others getting started with your repository.

*We recommend that you open this README in another tab as you perform the tasks below. You can [watch our video](https://youtu.be/0ocf7u76WSo) for a full demo of all the steps in this tutorial. Open the video in a new tab to avoid leaving Bitbucket.*

---

## Edit a file

You’ll start by editing this README file to learn how to edit a file in Bitbucket.

1. Click **Source** on the left side.
2. Click the README.md link from the list of files.
3. Click the **Edit** button.
4. Delete the following text: *Delete this line to make a change to the README from Bitbucket.*
5. After making your change, click **Commit** and then **Commit** again in the dialog. The commit page will open and you’ll see the change you just made.
6. Go back to the **Source** page.

---

## Create a file

Next, you’ll add a new file to this repository.

1. Click the **New file** button at the top of the **Source** page.
2. Give the file a filename of **contributors.txt**.
3. Enter your name in the empty file space.
4. Click **Commit** and then **Commit** again in the dialog.
5. Go back to the **Source** page.

Before you move on, go ahead and explore the repository. You've already seen the **Source** page, but check out the **Commits**, **Branches**, and **Settings** pages.

---

## Clone a repository

Use these steps to clone from SourceTree, our client for using the repository command-line free. Cloning allows you to work on your files locally. If you don't yet have SourceTree, [download and install first](https://www.sourcetreeapp.com/). If you prefer to clone from the command line, see [Clone a repository](https://confluence.atlassian.com/x/4whODQ).

1. You’ll see the clone button under the **Source** heading. Click that button.
2. Now click **Check out in SourceTree**. You may need to create a SourceTree account or log in.
3. When you see the **Clone New** dialog in SourceTree, update the destination path and name if you’d like to and then click **Clone**.
4. Open the directory you just created to see your repository’s files.

Now that you're more familiar with your Bitbucket repository, go ahead and add a new file locally. You can [push your change back to Bitbucket with SourceTree](https://confluence.atlassian.com/x/iqyBMg), or you can [add, commit,](https://confluence.atlassian.com/x/8QhODQ) and [push from the command line](https://confluence.atlassian.com/x/NQ0zDQ).