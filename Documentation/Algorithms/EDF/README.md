# Earliest Deadline First

The Earliest Deadline First Scheduling algorithm is one of the fundamental and efficient scheduling algorithms, the priorities of a task are assigned dynamically based on the task's deadline. The EDF algorithm assigns the task with the earliest deadline the highest priority and is executed first. Meaning that the priority of a task is directly proportional to the task's deadline. This is a preemptive algorithm, therefore a currently executing task is preempted whenever another task with the earliest deadline is active. The EDF algorithm works on continuous-time, that is, it assumes that any task can get active at any iteration, so the algorithm selects the task with the earliest deadline at each iteration.[1]

## Algorithm
1. The parameters arrival time, execution time, period are considered as inputs to the algorithm.
2. Utilization is calculated to verify if the tasks are schedulable or not. The utilization for a task set with **n** number of tasks can be calculated using

    <img src="https://render.githubusercontent.com/render/math?math=U=\sum_{i=1}^n \frac{executionTime[i]}{period[i]}">

3. If the Utilization of a task set *>* 1 (100%), the tasks cannot be scheduled. 
4. A  counter is maintained for each task which is initialized to the execution time of the task that is being executed, which is decremented as the time progress.
5. For each time interval starting from 0
6. Retrieve the task number which has the earliest deadline (Minimum deadline) from a list of all the deadlines of all the task
7. If there is already an active task, the current task is paused, and the new task is made active. The current task can resume its executions, only after the new task completes its execution.
8. The above steps are carried out until LCM.

## Advantages
- One of the most optimal scheduling algorithms.
- The algorithm can make the CPU utilization to about 100\% while still guaranteeing the deadlines of all the tasks.
- The algorithm produces fewer preemptions in practice, and hence less overhead for context switching.

## Disadvantages
- The EDF algorithm does not avoid deadline-misses, it can execute a job even though there is not enough time to complete before the deadline.

## References
1. M. Saleh and L. Dong, "Comparing FCFS \& EDF scheduling algorithms for real-time packet switching networks," 2010 International Conference on Networking, Sensing and Control (ICNSC), Chicago, IL, 2010, pp. 698-703, doi: 10.1109/ICNSC.2010.5461572.