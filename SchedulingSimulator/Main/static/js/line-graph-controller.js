var colors = ['#FF6633', '#6b339c', '#d6d43e', '#00B3E6',
    '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
    '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
    '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
    '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
    '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
    '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
    '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
    '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
    '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'
];

var lcm = 0;
	var startAxes = 0;
	var endAxes = 50;

function createLineGraph(canvasID, title, schedulingArray, inputArray, arrayIndex) {
    var labels = [];
    var data = generateLineGraph(schedulingArray , arrayIndex);
    var dataSet = [];
    var set = {};
    var i;
    var axisLabel = []
    for (i = startAxes[arrayIndex]; i < endAxes[arrayIndex] ; i++) {
        axisLabel.push(i.toString());
    }
    for (i = 0; i < noOfTasks; i++) {
        var inputTask = '[' + inputArray[i][1] + ', ' + inputArray[i][2] + ', ' + inputArray[i][3] + ', ' + inputArray[i][4] + ']';
        var temp = {};

        temp['steppedLine'] = 'steppedLine';
        temp['label'] = 'Task ' + (i + 1).toString() + inputTask;
        temp['borderColor'] = colors[i];
        temp['data'] = data[i];
        temp['fill'] = false;
        dataSet.push(temp);
    }
    var barChartData = {
        labels: axisLabel,
        datasets: dataSet
    };
    var ctx = document.getElementById(canvasID);
    var myChart = new Chart(ctx, {
        type: 'line',
        data: barChartData,
        options: {
            legend: {
                labels: {

                    fontColor: 'white'
                }
            },
            title: {
                display: true,
                text: title,
                fontColor: 'white'
            },

            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    ticks: {
                        fontColor: 'white'
                    }
                }],
                yAxes: [{

                    display: false,
                }]

            }
        }
    });
    var canvasHeight = 0;
    for (i = 0; i < noOfTasks; i++) {
        canvasHeight = canvasHeight + 125;
    }
    canvasHeight = canvasHeight + 'px';
    myChart.canvas.parentNode.style.height = canvasHeight;
};




function generateLineGraph(dataArray, arrayIndex) {
    var timeLineLength = dataArray[0].length;
    var startingPoints = dataArray[0];
    var tasks = dataArray[1];
    var i = 0;
    var j;
    var tasksDataset = new Array(noOfTasks);
    for (i = 0; i < noOfTasks; i++) {
        tasksDataset[i] = new Array(endAxes[arrayIndex] - startAxes[arrayIndex]).fill(0);
    }
    for (i = 0; i < startingPoints.length; i++) {
        var start = startingPoints[i]
        var end = startingPoints[i + 1]
        var taskNo = tasks[i]

        if (taskNo > 0) {
            taskNo = taskNo - 1
            for (j = start; j < end; j++) {
                tasksDataset[taskNo][j - startingPoints[0]] = 1;
            }
        }
    }
    var xaxisLength = 0;
    var points = new Array(noOfTasks);
    for (i = 0; i < tasksDataset.length; i++) {
        tasks = tasksDataset[i];
        points[i] = [];
        for (j = 0; j < tasks.length; j++) {
            var point = {};
            point['x'] = j;
            if (tasks[j] == 1) {
                point['y'] = xaxisLength + 0.5;
            } else {
                point['y'] = xaxisLength;
            }
            points[i].push(point);
        }
        xaxisLength = xaxisLength + 1;
    }
    return points;

}