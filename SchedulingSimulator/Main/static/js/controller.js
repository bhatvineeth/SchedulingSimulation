controller {

    function generateGraph() {
        var startingPoints = [0,2,10,15,23,25,28,30,38,45,50,53,56,60,68];
        var tasks = [0,2,0,2,0,1,0,2,0,2,1,2,0,2,0,];
        var lcm = 75;
        var noOfTasks = 2
        var i =0;
        var j;
        var tasksDataset = new Array(noOfTasks);
        for (i =0 ; i < noOfTasks; i++) {
            tasksDataset[i] = new Array(lcm).fill(0);
        }
        for (i = 0; i < startingPoints.length ; i++){
            var start = startingPoints[i]
            var end = startingPoints[i+1]
            var taskNo = tasks[i]

            if (taskNo > 0) {
                taskNo = taskNo - 1
                for (j = start; j < end ; j++) {
                    tasksDataset[taskNo][j] = 1;
                }
            }
        }
        return tasksDataset;
    }

    function createGraph() {
        var noOfTasks = 2;
        var lcm = 75;
        var labels = [];
        var data = generateGraph();
        var dataSet = [];
        var set = {};
        var i;
        var axisLabel = []
        for (i = 0; i < lcm ; i++) {
            axisLabel.push(i.toString());
        }
        for (i = 0; i < noOfTasks ; i++) {
            var temp = {};
            temp['catergoryPercentage'] = 1;
            temp['barPercentage'] = 1.2;
            temp['barThickness'] = 'flex';
            temp['label'] = 'Task No ' + (i+1).toString() ' : ';
            temp['backgroundColor'] = '#ff6384';
            temp['data'] = data[i];
            dataSet.push(temp);
        }
        var barChartData = {
             labels: axisLabel,
             datasets: dataSet
         };
        var ctx = document.getElementById('myChart');
        var myChart = new Chart(ctx, {
            type: 'bar',
            data: barChartData,
            options: {
                title: {
                    display: true,
                    text: 'Scheduling'
                },

                responsive: true,
                scales: {
                    xAxes: [{
                        stacked: true,
                    }],
                    yAxes: [{
                        stacked: true,
                        display: false,
                    }]
                }
            }
        });
    };

};