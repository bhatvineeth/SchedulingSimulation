# Rate Monotonic Scheduling

Rate Monotonic Scheduling (RMS) is a preemptive based algorithm. It is a priority-based algorithm where a static priority is assigned based on the period. The task with the least period time will have the highest priority. The task with the highest priority will preempt any other process with lower priority. In RMS it is assumed that the deadlines are equal to periods. Resources are not shared between the processes. RMS is one of the most commonly used scheduling algorithms.

## Algorithm

1. RMS algorithm takes execution time, period, and arrival time as input.
2. The process is sorted based on period in an increasing sequence. This will set the task with the least period with the highest priority.
3. Utilization is calculated to verify the schedulability of the tasks. The utilization for a task set with n number of tasks is calculated using

    <img src="https://render.githubusercontent.com/render/math?math=U=\sum_{i=1}^n \frac{executionTime[i]}{period[i]}">  

4. If the utilisation <img src="https://render.githubusercontent.com/render/math?math=U \leq 1">, which is the necessary condition for the algorithm to meet the CPU utilization, then then tasks set can be schedulable. 
5. The sufficient condition for RMS schedulability is, <img src="https://render.githubusercontent.com/render/math?math=U\leq n(2^{1/n}-1)">. If this condition is not met then the tasks are not schedulable in the current simulator.
6. A list of all the tasks that need to be executed based on the priority is maintained and this list will contain the execution time of the task, with task number being the index and the value is the execution time and it is updated as the timeline progresses from 0 to LCM.
7. Once the execution list is updated and if it is not empty, the tasks are executed. The execution time of that task is decremented every time it is executed until it is zero or preempted by another task if that task has higher priority than the current task that is being executed.
8. This process is repeated until the time reaches the LCM calculated.

## Advantages
- Simple and easy to implement algorithm.
- It is optimal compared to other static priority algorithms.
- It contains calculated time periods in contrast to other algorithms that neglect the scheduling needs of the tasks.

## Disadvantages
- It is not optimal in-case of different deadline and periods.
- Difficult to support support a periodic and sporadic tasks.