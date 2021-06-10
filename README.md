# VCallZer <img align="right" src="https://github.com/DSC-IIIT-Kalyani/winter-of-code/blob/main/images/logos/logo3.png">

* The project was initiated during Winter of Code 1.0 by [DSC IIIT Kalyani](https://github.com/DSC-IIIT-Kalyani) and is currently under development.
* The idea behind this is to facilitate a video calling service built with python sockets(IPv4) and Open-CV, which replaces the users voice by a robotic/AI voice and the video by a neon projection of the users face on a black screen for anonimity purposes. 

A screenshot of the connected system is shown below:
<br/>![ss](https://github.com/akshitadixit/VCallZer/blob/main/temp/ss.jpeg)

## To-Do List/ In Progress
* Add documentation #2
* Transfer audio over the connection #3
* Improve facial landmark detection #8
 
## Setting up

* Create a [Conda](https://docs.conda.io/en/latest/miniconda.html) environment 
> conda create -name myenv python=3.6 
* Cd into your newly created environment (from command line)
> cd C:\...\path-to-your-conda-environment\

> conda activate myenv
* Installing modules we will need
> conda install -c conda-forge dlib

> conda install -c conda-forge opencv

## Running the code

* Fork and clone this repo
* Make sure your clone resides into the conda environment you created
* Run server.py and client.py in two different cmd windows/terminals

## Our valuable Contributors👩‍💻👨‍💻 :
| | | | | |
|:--:|:--:|:--:|:--:|:--:|
|<a href="https://github.com/akshitadixit"><img src="https://avatars.githubusercontent.com/u/56997545?v=4" height="150px" width="150px"></a>| <a href="https://github.com/akshitadixit"><img src="https://avatars.githubusercontent.com/u/56997545?v=4" height="150px" width="150px"></a>| <a href="https://github.com/akshitadixit"><img src="https://avatars.githubusercontent.com/u/56997545?v=4" height="150px" width="150px"></a>| <a href="https://github.com/akshitadixit"><img src="https://avatars.githubusercontent.com/u/56997545?v=4" height="150px" width="150px"></a>| <a href="https://github.com/akshitadixit"><img src="https://avatars.githubusercontent.com/u/56997545?v=4" height="150px" width="150px"></a>|


# Contribute to VCallZer

Are You a newbie in the world of open source and want to Contribute to our Open Source Project ?
Don't worry we got your back 

Below are the steps to follow to contribute to this project 

1. #### If you don't have git on your machine, [install it](https://help.github.com/articles/set-up-git/).

2. ## Fork this repository
<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/fork.png" alt="fork this repository" />
Fork this repository by clicking on the fork button on the top of this page.
This will create a copy of this repository in your account.

3. ## Clone the repository

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project). See the previous steps to obtain the url.

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

For example:

```
git clone https://github.com/this-is-you/VCallZer.git
```

where `this-is-you` is your GitHub username. Here you're copying the contents of the first-contributions repository on GitHub to your computer.

4. ## Navigate to the project directory :file_folder: .

```
cd VCallZer
```
5. ## Add a reference(remote) to the original repository.

```
git remote add upstream https://github.com/akshitadixit/VCallZer.git 
```
6. ## Check the remotes for this repository.

```
git remote -v
```
7. ## Always take a pull from the upstream repository to your master branch to keep it at par with the main project(updated repository) this will avoid the merge conflicts.

```
git pull upstream master
```
8. ## Create a branch
Now create a branch using the `git checkout` command:

```
git checkout -b your-new-branch-name
```

For example:

```
git checkout -b add-issueno.x
```
(The name of the branch does not need to have the word _add_ in it, but it's a reasonable thing to include because the purpose of this branch is to add your solved issue to the project.)

9. ## Make necessary changes and commit those changes

Perform your desired changes to the code base.

<p align="center"><img width=35% src="https://media2.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif?cid=ecf05e47pzi2rpig0vc8pjusra8hiai1b91zgiywvbubu9vu&rid=giphy.gif"></p>


If you go to the project directory and execute the command `git status`, you'll see there are changes.

Add those changes to the branch you just created using the `git add` command:

```
git add <file name>
```

Now commit those changes using the `git commit` command:

```
git commit -m "Add new feature <issue-no> to the main repo "
```

replacing `<issue-no>` with the issue number you are assigned.

10. ## Push changes to GitHub

Push your changes using the command `git push`:

```
git push origin <add-your-branch-name>
```

replacing `<add-your-branch-name>` with the name of the branch you created earlier.

11. ## Submit your changes for review

If you go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

Now submit the pull request.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

12. Hurray :exclamation: You have created a PR to the VCallZer :boom: . Sit back patiently and relax till then the project maintainers will review your PR. Please understand,  there will be some time taken to review a PR and can vary from a few hours to a few days too so be Patient and keep contributing.

## Till Then 
<p align="center"><img src="https://thumbs.dreamstime.com/b/keep-learning-word-written-wood-block-text-table-concept-175173431.jpg" width=50%></p>


##### Note: The voice modulation and GUI part is still being worked upon.

## Overall winner
![Cert](https://github.com/akshitadixit/VCallZer/blob/main/temp/WoC.png) 


