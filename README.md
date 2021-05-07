# Scheduling Simulator

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

## Algorithms
Algorithms implemented can be found - [here](./Documentation/Algorithms/README.md)

## Literature
The research paper can be found - [here](./Documentation/Research-Paper/Scheduling_Simulator.pdf)

## References
1. A. S. Pillai and T. B. Isha, "A new real time simulator for task scheduling," 2012 IEEE International Conference on Computational Intelligence and Computing Research, Coimbatore, 2012, pp. 1-4, doi: 10.1109/ICCIC.2012.6510232.
2. Chart.js https://www.chartjs.org/ Accessed: 22.08.2020
3. Black Dashboard https://www.creative-tim.com/product/black-dashboard Accessed: 22.08.2020
4. Dragos-Paul Pop, Adam Altar, "Designing an MVC Model for Rapid Web Application Development" Procedia Engineering, Volume 69, 2014, Pages 1172-1179, ISSN 1877-7058.
5. E. Okuyan and B. Kayayurt, "Earliest deadline first scheduling algorithm and its use in ANKA UAV," 2012 IEEE/AIAA 31st Digital Avionics Systems Conference (DASC), Williamsburg, VA, 2012, pp. 8B1-1-8B1-8, doi: 10.1109/DASC.2012.6382435.
6. M. Saleh and L. Dong, "Comparing FCFS \& EDF scheduling algorithms for real-time packet switching networks," 2010 International Conference on Networking, Sensing and Control (ICNSC), Chicago, IL, 2010, pp. 698-703, doi: 10.1109/ICNSC.2010.5461572.
7. Lui Sha, R. Rajkumar and S. S. Sathaye, "Generalized rate-monotonic scheduling theory: a framework for developing real-time systems," in Proceedings of the IEEE, vol. 82, no. 1, pp. 68-82, Jan. 1994, doi: 10.1109/5.259427.
8. https://www.geeksforgeeks.org/program-for-shortest-job-first-or-sjf-cpu-scheduling-set-1-non-preemptive/
9. Module 6 Embedded System Software, https://nptel.ac.in/content/storage2/courses/108105057/Pdf/Lesson-30.pdf Accessed: 25.08.2020
