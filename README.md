# Scheduling Simulator
RTS Project - Simulation of scheduling algorithms

## Abstract
Understanding the working of scheduling algorithms provides us with a knowledge of how to analyse the scheduling of processes, resource utilization, and performance in real-time applications. Various algorithms perform differently and have their unique set characteristics which are advantageous depending on the scenario and application. A simulator enables us to visualize these characteristics, working, and behaviour of scheduling algorithms. By automating the process of scheduling these tasks provided as input and displaying the output intuitively, which reduces the work on creating the schedule and focuses on analysing the behaviour of the scheduling algorithms. This literature focuses on the development of a web application that is machine and platform-independent, with the scope of illustrating multiple scheduling algorithms graphically to help one to draw comparisons and conclusions based on the results.

## Requirements
1. [Python 3](https://www.python.org/downloads/)
2. [pip3](https://pip.pypa.io/en/stable/)

## Deployment

1. Download the source code using the following command.
```bash
$ git clone https://github.com/bhatvineeth/SchedulingSimulation.git
```
2. Install virtual environment.
```bash
$ pip3 install virtualenv
```
3. Change the directory to SchedulingSimulator app.
```bash
$ cd SchedulingSimulation\SchedulingSimulator\
```
4. Create virtual environment and activate it.
```bash
$ virtualenv env
$ .env/bin/activate
```
5. Install django.
```bash
$ pip3 install django
```
6. Execute manage.py to start the server.
```bash
$ python manage.py runserver
```
7. Application will be available on localhost:8000.

## Literature
https://github.com/bhatvineeth/SchedulingSimulation/blob/master/Documentation/Paper/Scheduling_Simulator.pdf
