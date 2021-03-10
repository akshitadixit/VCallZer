# VCallZer <img align="right" src="https://github.com/DSC-IIIT-Kalyani/winter-of-code/blob/main/images/logos/logo3.png">

* The project was initiated during Winter of Code 1.0 by [DSC IIIT Kalyani](https://github.com/DSC-IIIT-Kalyani) and is currently under development.
* The idea behind this is to facilitate a video calling service built with python sockets(IPv4) and Open-CV, which replaces the users voice by a robotic/AI voice and the video by a neon projection of the users face on a black screen for anonimity purposes. 

A screenshot of the connected system is shown below:
<br/>![ss](https://github.com/akshitadixit/VCallZer/blob/main/temp/ss.jpeg)

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

##### Note: The voice modulation and GUI part is still being worked upon.
