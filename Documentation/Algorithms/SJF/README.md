# Shortest Job First

The shortest job first can be preemptive and non-preemptive. Preemptive is where the execution of a task can be interrupted by another task that has the least execution time than the one that is being executed. Whereas in a non-preemptive algorithm the task with shortest execution time is executed till its completion. The application implements the non-preemptive version of the algorithm. Following steps explains the steps involved in scheduling the tasks based on the shortest job first,

## Algorithm
1. Tasks are sorted based on the execution time with the least execution time at the beginning of the order.
2. For each time point starting from 0, if a task or multiple tasks has arrived execution time of those tasks is added to an execution list.
3. Task with minimum execution time is considered for execution and the period is updated based on the arrival time. Also, the execution time of that task in the execution list is updated, so that it is not considered for further execution.
4. A counter is maintained which is initialized to the execution time of the task that is being executed, which is decremented as the time progress, and once the execution is completed the next task with least execution time is picked up for execution.
5. The process is repeated till the LCM of execution time which is calculated earlier.

## Advantages
1. Shortest jobs are executed early, there by maximizing the throughput. It is possible to complete more tasks in the given time.
2. Algorithm provides optimal average waiting time for the tasks scheduled.

## Disadvantages
1. Possibility of starvation if shortest jobs keep occurring. That cases the tasks with larger execution to wait indefinitely.
2. Not possible to implement this at short term CPU scheduling level.