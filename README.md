# VCallZer <img align="right" src="https://github.com/DSC-IIIT-Kalyani/winter-of-code/blob/main/images/logos/logo3.png">

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat&logo=github)](https://github.com/akshitadixit/VCallZer) [![Open Source Love](https://img.shields.io/badge/Open%20Source-%F0%9F%A4%8D-Green)](https://github.com/akshitadixit/VCallZer) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/akshitadixit/VCallZer/graphs/commit-activity)

![GitHub contributors](https://img.shields.io/github/contributors-anon/akshitadixit/VCallZer) ![](https://badgen.net/github/stars/akshitadixit/VCallZer)
![](https://badgen.net/github/forks/akshitadixit/VCallZer)
![](https://badgen.net/github/open-issues/akshitadixit/VCallZer)
![](https://badgen.net/github/closed-issues/akshitadixit/VCallZer)
![](https://badgen.net/github/prs/akshitadixit/VCallZer)
![](https://badgen.net/github/open-prs/akshitadixit/VCallZer)
![](https://badgen.net/github/closed-prs/akshitadixit/VCallZer)

[![GitHub forks](https://img.shields.io/github/forks/akshitadixit/VCallZer.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/akshitadixit/VCallZer/network)  [![GitHub stars](https://img.shields.io/github/stars/akshitadixit/VCallZer.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/akshitadixit/VCallZer/stargazers/)  [![GitHub watchers](https://img.shields.io/github/watchers/Naereen/StrapDown.js.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/Naereen/StrapDown.js/watchers/)




* The project was initiated during Winter of Code 1.0 by [DSC IIIT Kalyani](https://github.com/DSC-IIIT-Kalyani) and is currently under development.
* The idea behind this is to facilitate a video calling service built with python sockets(IPv4) and Open-CV, which replaces the users voice by a robotic/AI voice and the video by a neon projection of the users face on a black screen for anonimity purposes.

### A screenshot of the connected system is shown below:
![ss](https://github.com/akshitadixit/VCallZer/blob/main/temp/ss.jpeg)

## 📌 To-Do List/ In Progress⏳
* Add documentation [#2](https://github.com/akshitadixit/VCallZer/issues/2)
* Transfer audio over the connection [#3](https://github.com/akshitadixit/VCallZer/issues/3)
* Improve facial landmark detection [#8](https://github.com/akshitadixit/VCallZer/issues/8)
 
## 🛠 Setting up

**1.** Create a [Conda](https://docs.conda.io/en/latest/miniconda.html) environment.
```
conda create -name myenv python=3.6
```
**2.** Navigate into your newly created environment (from command line).
```
cd C:\...\path-to-your-conda-environment\
```
```
conda activate myenv
```
**3.** Installing modules we will need.
```
conda install -c conda-forge dlib
```
```
conda install -c conda-forge opencv
```

## ✔ Running the code

* Fork and clone this repo
* Make sure your clone resides into the conda environment you created
* Run server.py and client.py in two different cmd windows/terminals

## 📌 How to get started❓

You can refer to the following articles on the basics of Git and Github, in case you are stuck:

- If you don't have git on your machine, [install](https://help.github.com/articles/set-up-git/) it.
- [Watch this video to get started, if you have no clue about open source](https://youtu.be/SL5KKdmvJ1U)
- [Forking a Repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
- [Cloning a Repo](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository)
- [How to create an Issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-issues/creating-an-issue)
- [How to create a Pull Request](https://opensource.com/article/19/7/create-pull-request-github)
- [Getting started with Git and GitHub](https://towardsdatascience.com/getting-started-with-git-and-github-6fcd0f2d4ac6)

## 🙌 Contribute to VCallZer

Are you a newbie in the world of open source and want to Contribute to our Open Source Project ?
Don't worry we got your back 

Below are the steps to follow to contribute to this project:

**1.**  Fork [this](https://github.com/akshitadixit/VCallZer) repository.

**2.**  Clone your forked copy of the project.
```
git clone --depth 1 https://github.com/<your_user_name>/VCallZer.git
```
where `your_user_name` is your GitHub username. Here you're copying the contents of the first-contributions repository on GitHub to your computer.

**3.** Navigate to the project directory :file_folder: .
```
cd VCallZer
```
**4.** Add a reference(remote) to the original repository.
```
git remote add upstream https://github.com/akshitadixit/VCallZer.git 
```
**5.** Check the remotes for this repository.
```
git remote -v
```
**6.** Always take a pull from the upstream repository to your master branch to keep it at par with the main project(updated repository).
```
git pull upstream master
```
**7.** Create a new branch.
```
git checkout -b <your_branch_name>
```

**8.** Make necessary changes and commit those changes
<p align="center"><img width=35% src="https://media2.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif?cid=ecf05e47pzi2rpig0vc8pjusra8hiai1b91zgiywvbubu9vu&rid=giphy.gif"></p>

**9.** Track your changes:heavy_check_mark: .
```
git add . 
```
**10.** Commit your changes .
```
git commit -m "Relevant message"
```
**11.** Push the committed changes in your feature branch to your remote repo.
```
git push -u origin <your_branch_name>
```
**12.** To create a pull request, click on `compare and pull requests`. Please ensure you compare your feature branch to the desired branch of the repo you are suppose to make a PR to.

**13.** Add appropriate title and description to your pull request explaining your changes and efforts done.

**14.** Click on `Create Pull Request`.

**15.** Hurray :exclamation: You have created a PR to the VCallZer :boom: . Sit back patiently and relax till then the project maintainers will review your PR. Please understand,  there will be some time taken to review a PR and can vary from a few hours to a few days too so be Patient and keep contributing.

## Till Then 
<p align="center"><img src="https://thumbs.dreamstime.com/b/keep-learning-word-written-wood-block-text-table-concept-175173431.jpg" width=30%></p>

##### Note: The voice modulation and GUI part is still being worked upon.

## ✨ Our valuable Contributors👩‍💻👨‍💻 :
| | | | | |
|:--:|:--:|:--:|:--:|:--:|
|<a href="https://github.com/akshitadixit"><img src="https://avatars.githubusercontent.com/u/56997545?v=4" height="150px" width="150px"></a>| <a href="https://github.com/ShivaSankeerth"><img src="https://avatars.githubusercontent.com/u/29270279?v=4" height="150px" width="150px"></a>| <a href="https://github.com/supzi-del"><img src="https://avatars.githubusercontent.com/u/78655439?v=4" height="150px" width="150px"></a>| <a href="https://github.com/Vedant-Jayesh-Oza"><img src="https://avatars.githubusercontent.com/u/75005433?v=4" height="150px" width="150px"></a>| <a href="https://github.com/akshitadixit"><img src="https://avatars.githubusercontent.com/u/56997545?v=4" height="150px" width="150px"></a>|

## Overall winner
![Cert](https://github.com/akshitadixit/VCallZer/blob/main/temp/WoC.png) 
