# How to use git for version control

Github is a website for version control, code sharing and code storing. This is the perfect interface for a group project as well as a more massive personal project as it allows you to come back to previous versions of the code as well as keep track of what other people have to say about your contibutions.

This text will quickly remind what are the important features of github and the git commands that go with it.

### Initial downloads and settings

Using github only through the web interface is very inefficiant and clumsy. It is much better to have a version of the repository on your own computer and make all the changes directly there. The first step is of course to [downoald Git](https://git-scm.com/downloads). If you are using mac or linux you might have it pre-installed, so check in the terminal by entering `git --version`. If you have it it should just outpus something like `git version 2.25.1`. Of course for the next steps you will need a Github account. 

Hopefully the installation has gone nicely and you have a fresh version on your computer. It is now time to link your Github account to your installation. For this, just follow the information on this [page](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/about-ssh). It will teach you how to create a secure connection between your computer to the Github mainframe. If on windows, you might also need to download ssh through [PuTTY](https://www.putty.org/).

We now have all the tools to start participating to the project! The first step now, is to clone the repo. This is done on the main page and clicking the **Code** button and copying the SSH link. In your terminal, you go to the folder you want the download to be done using the change directory `cd` command, e.g. `cd firstDir/secondDir/` and then using the cloning git command `git clone copiedGithubLink` 

From there on you have your personal version of the repository (!! be sure that you are a collaborator to the project, otherwise you won't be able to make modifications !!). 

### Steps to manage personal branches and code

The master branch is reserved to mature and ready code, this is not the place you want to upload your unfinished or partially working code. This means you will create your own branch of the project to work on which is separate and as such doesn't impact the master branch.

##### Creating your branch

The command is `git checkout -b BranchName`. The same command without the `-b` is used to switch from branch to branch in the repository. The command puts you directly in the new branch and you can start working on your code. An extra step is to just verify the branch you are on with `git status`. This command gived you general information about the status of your branch and your branch name.

Once you are satisfied with your work and think is is the time to create a lasting step in the progress, it is time to commit your work to your branch.

##### Uploading your code to Github 

While working on your files locally on the computer, nothing is sent to github to be stored, meaning that you have to do this manually everytime you think your code is worthy of upload (generally everytime you manage to complete a specific task in your program). The steps can be summarized as: `add`, `commit` and `push`.

The first step is to decide which files are ready to be sent to github (commited to the site in the git language). By typing `git status`, you will see all of the modified files you have been working on. They appear in red because they have not been selected to be commited to the Github repository. To change that, you will have to use the `add` command. Choosing a specific file to commit is done with `git add FileName`. Generally there are many files and as said above, you are probably happy with a big part of your code at this point, so you can also add all the files in one go using `git add -A`.

Once you are satisfied with the files to commit, you can simply create the commit by entering `git commit -m "Commit message"`. The message is important, as the commit will not be accepted without one. If you forget the `-m "message"`, you will be put into Vim, which is a command line text editor that can be intimidating to the non initiated. If that happens, just type `:qa` and enter and this should leave the prompt and cancel the commit. After that you just have to redo the commit command.

Now that you have created the commit, the last step is to just `push` the changes to github with the command `git push origin YourBranchName`. This will upload your changes to the site. The `origin` means that the commit comes from your local computer and `YourBranchName` is the name of the branch you are working on. It is good practice to always have those two words to make sure that you are pushing your files to the right place.

You can now go and check on the github website that all of your new files have correctly been uploaded :)

##### Pulling from Github

It is sometimes possible that changes chave been made to your branch by someone else than yoursel, meaning that your local version is not synchronized with the online version of the reepository. To fix that, before you can push your commit you will have to pull down the extra code that you don't have. This is done simply with the `git pull` command. If you wannt to synchromize your branch with the master branch then you can call `git pull origin master`, but this is not something that I have ever used in practice.

## Summary

If you follow the steps above you will theoretically always succeed in uploading you files! This is a quick summary of all the steps necessary, assuming you are already on your personnal branch:

1. `git add -A` 
2. `git commit -m "Short explanation of the changes"`
3. `git push origin YourBranchName`
4. Possibly `git pull` in case your branch has been modified

If you want to check what files are included in the commit or which branch you are in, type `git status`. If you want to change to another branch use `git checkout BranchName`, including `master`.
