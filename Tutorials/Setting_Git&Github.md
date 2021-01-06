# How to use git for version control

Github is a website for version control, code sharing and code storing. This is the perfect interface for a group project as well as a more massive personal project as it allows you to come back to previous versions of the code as well as keep track of what other people have to say about your contibutions.

This text will quickly remind what are the important features of github and the git commands that go with it.

### Initial downloads and settings

Using github only through the web interface is very inefficiant and clumsy. It is much better to have a version of the repository on your own computer and make all the changes directly there. The first step is of course to [downoald Git](https://git-scm.com/downloads). If you are using mac or linux you might have it pre-installed, so check in the terminal by entering `git --version`. If you have it it should just outpus something like `git version 2.25.1`. Of course for the next steps you will need a Github account. 

Hopefully the installation has gone nicely and you have a fresh version on your computer. It is now time to link your Github account to your installation. For this, just follow the information on this [page](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/about-ssh). It will teach you how to create a secure connection between your computer to the Github mainframe. If on windows, you might also need to download ssh through [PuTTY](https://www.putty.org/).

We now have all the tools to start participating to the project! The first step now, is to clone the repo. This is done on the main page and clicking the **Code** button and copying the SSH link. In your terminal, you go to the folder you want the download to be done using the change directory `cd` command, e.g. `cd firstDir/secondDir/` and then using the cloning git command `git clone copiedGithubLink` 

From there on you have your personal version of the repository (!! be sure that you are a collaborator to the project, otherwise you won't be able to make modifications !!). 

### Steps to manage personal branches and code

The master branch is reserved to mature and ready code, this is not the place you want to upload your unfinished or partially working code. This means you will create your branch
