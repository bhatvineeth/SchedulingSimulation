# First Come First Serve

The first come first serve algorithm is one of the most simple scheduling algorithms, as the implementation of this algorithm is not complicated, since the only parameter used for scheduling is the arrival time of the process. The algorithm assigns the priority to the process based on the arrival times, the process with the least arrival time is executed first. The algorithm is Non-Preemptive, that is there are no interruptions by other processes, a next process can be started only after the completion of the previous process. Similar to the implementation of the queue data structure. The First Come First Serve algorithm never fails to schedule, it always completed the scheduling successfully.

## Algorithm
1. The parameters arrival time, execution time, period are considered as inputs to the algorithm.
2. Based on the period of the process LCM is calculated or the LCM entered on the UI is considered.
3. The process with the least arrival time is executed first for its execution time.
4. Once this process completes its execution, the next process with the least arrival time is chosen.
5. Step 3 and 4 is repeated until the algorithm completes the execution till the LCM.
6. Waiting time for a process k is calculated using

    waitingTime[k] = executionTime[k-1] + waitingTime[k-1]
    
    waitingTime[0] = 0, as the first process never waits, its executed as soon as it arrives.
7. Average Waiting Time can be calculated using,

    averageWaitingTime = totalWaitingTimeForAllProcesses / numberOfProcesses
    
8. The turn around time for a process k is calculated using,

    turnAroundTime[k] = executionTime[k] + waitingTime[k]
    
9. Total Turn Around Time is calculated using,

   averageTurnAroundTime = totalTurnAroundTimeForAllProcesses / numberOfProcess

## Advantages
- Simplest Scheduling Algorithm.
- Implementation not complicated.
- First come First Served and allows the task to complete its execution, there is no need for any preemptions.

## Disadvantages
- As the algorithm is Non Preemptive, the average waiting time is very high.
- Short processes that are at the back of the queue have to wait for the long process at the front to finish.
- No Concurrent process execution.
- FCFS is not very efficient.
