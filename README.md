# jenkins-flask-project

A website built with Flask and Jenkins as CI/CD pipeline

## Installing Jenkins on my Virtual Machine
-   For this task, I will be making use of the Azure cloud service.
-   [This article](https://docs.microsoft.com/en-us/azure/developer/jenkins/configure-on-linux-vm) served as a guide in setting my VM
-   I also installed Docker on my VM

## To integrate my repo with Jenkins
-   [This article](https://www.blazemeter.com/blog/how-to-integrate-your-github-repository-to-your-jenkins-project) served as a guide in integrating my repo with Jenkins and creating my first job.   
-   [This article](https://cloudaffaire.com/how-to-install-git-on-azure-virtual-machine/) was used to install git on my VM, to enable me access my code via my VM.

## Building the Jenkins Pipeline
Place the Jenkins file, in root of your folder.
-   I created a Jenkins file, specifying the actions to be taken at each stage:
    -   At stage 'build and test', I deploy a docker image.
    -   At stage 'build', I install my code's dependencies in my requirements.txt file
    -   At stage 'test', I run my test and display the results in a graphical way with the Junit
    -   At stage 'build docker image and deploy', I build my docker image and deploy it
![image](https://user-images.githubusercontent.com/49791498/126075384-5f568387-27e6-4026-8faa-b6a16c4cc0b0.png)

*result of Jenkins pipeline*