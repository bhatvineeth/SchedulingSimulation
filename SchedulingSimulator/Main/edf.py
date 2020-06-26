def earliestDeadlineFirstAlgorithm(tasks):
    logFile = open("log/EDF.log", "w+")
    print("EARLIEST DEADLINE FIRST: START\n", file=logFile)
    print("Earliest Deadline First:")
    n = len(tasks)
    tasks.sort(key=lambda x: x[1])
    i = 0
    for task in tasks:
        i = i + 1
        task[0] = i


    print(tasks)

    u = 0

    for i in range(n):
        u += float(tasks[i][1] / tasks[i][2])

    print("Utilization: ", u, file=logFile)
    print("Utilization: ", u)

    if u > 1:
        print("The tasks are not feasible", file=logFile)
        print("Processes are not schedulable")
        print("\n-------------------------------------------------\n")
        return [];

    else:

        lcm = 1
        temp_p = []
        for i in range(n):
            temp_p.append(tasks[i][2])

        print(temp_p, file=logFile)
        i = 2
        while i <= max(temp_p):
            counter = 0
            for j in range(n):
                if temp_p[j] % i == 0:
                    counter = 1
                    temp_p[j] /= i

            if counter == 1:
                lcm = lcm * i
            else:
                i += 1

        print("LCM: ", lcm, file=logFile)
        print("Processes are schedulable")
        print("Timeline length: ", lcm)


        i = 0
        instances = []
        for i in range(n):
            j = 1
            while 1:
                if j == 1:
                    instances.append([tasks[i], tasks[i][4] + (j * tasks[i][2])])
                    j += 1
                elif j * tasks[i][2] <= lcm:
                    instances.append([tasks[i], instances[len(instances) - 1][1] + tasks[i][2]])
                    j += 1
                else:
                    break

        for i in range(len(instances)):
            print(instances[i], file=logFile)

        for i in range(len(instances)):
            tmp = instances[i].copy()
            k = i
            while k > 0 and tmp[1] < instances[k - 1][1]:
                instances[k] = instances[k - 1].copy()
                k -= 1
            instances[k] = tmp.copy()

        print('', file=logFile)
        print('', file=logFile)

        for i in range(len(instances)):
            print(instances[i], file=logFile)

        timeLeft = []

        for i in range(n):
            if tasks[i][4] == 0:
                timeLeft.append(tasks[i][1])
            else:
                timeLeft.append(int(0))

        timeLine = []
        time = 0

        while time < lcm:
            for i in range(n):
                if time >= 1 and ((time % (tasks[i][4] + tasks[i][2]) == 0 and time > tasks[i][4]) or time == tasks[i][4]):
                    # print("true ", end='')
                    timeLeft[i] = tasks[i][1]
            anyrun = 0
            for j in range(len(instances)):
                if j == 0 and timeLeft[instances[j][0][0] - 1] > 0:
                    timeLine.append(instances[j][0][0])
                    timeLeft[instances[j][0][0] - 1] -= 1
                    anyrun = 1
                    if timeLeft[instances[j][0][0] - 1] == 0:
                        instances.pop(j)
                    # print("[",time,"]",instances[j][0][0],timeLeft[instances[j][0][0]-1], time )
                    break

                elif j > 0 and instances[j][1] == instances[0][1]:
                    if timeLeft[instances[j][0][0] - 1] > 0:
                        tmp = instances[j].copy()
                        instances[j] = instances[0].copy()
                        instances[0] = tmp.copy()
                        time -= 1
                        anyrun = 1
                        break
                elif j > 0 and timeLeft[instances[j][0][0] - 1] > 0:
                    timeLine.append(instances[j][0][0])
                    timeLeft[instances[j][0][0] - 1] -= 1
                    anyrun = 1
                    if timeLeft[instances[j][0][0] - 1] == 0:
                        instances.pop(j)
                    # print("[",time,"]",instances[j][0][0],timeLeft[instances[j][0][0]-1], time )
                    break

            if anyrun == 0:
                timeLine.append(0)

            time += 1

        print('', file=logFile)
        print('', file=logFile)

        mn = 0
        mx = 0

        startingPoints = []
        tasksArray = []
        resultArray = []
        for i in range(lcm):
            if i > 0 and timeLine[i] != timeLine[i - 1]:
                startingPoints.append(mn)
                tasksArray.append(timeLine[i - 1])
                mx = i
                #print(mn, "", mx, "", "[" + str(timeLine[i - 1]) + "]", file=logFile)
                mn = i
            if i == lcm - 1:
                mx = lcm
                #print(mn, "", mx, "", "[" + str(timeLine[i]) + "]", file=logFile)
                tasksArray.append(timeLine[i])
                startingPoints.append(mn)
                startingPoints.append(mx)

        #print()
        #print()

        #for i in range(len(instances)):
        #    print(instances[i])
        resultArray.append(list(range(lcm + 1)))
        resultArray.append(timeLine)
        print(resultArray, file=logFile)
        print("EARLIEST DEADLINE FIRST: END\n\n\n", file=logFile)
        print("\n-------------------------------------------------\n")
        return(resultArray)