var colors = ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
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

function createGraph(canvasID, title, schedulingArray, inputArray) {
    if(schedulingArray.length == 0 ){
        return;
    }
    var labels = [];
    var data = generateGraph(schedulingArray);
    var dataSet = [];
    var set = {};
    var i;
    var axisLabel = []
    for (i = 0; i < lcm; i++) {
        axisLabel.push(i.toString());
    }
    for (i = 0; i < noOfTasks; i++) {
        var inputTask = '[' + inputArray[i][1] + ', ' + inputArray[i][2] + ', ' + inputArray[i][3] + ', ' + inputArray[i][4] + ']';
        var temp = {};
        temp['catergoryPercentage'] = 1;
        temp['barPercentage'] = 1.2;
        temp['barThickness'] = 'flex';
        temp['label'] = 'Task ' + (i + 1).toString() + inputTask;
        temp['backgroundColor'] = colors[i];
        temp['data'] = data[i];
        dataSet.push(temp);
    }
    var barChartData = {
        labels: axisLabel,
        datasets: dataSet
    };

    var ctx = document.getElementById(canvasID);
    var myChart = new Chart(ctx, {
        type: 'bar',
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
                    stacked: true,
                }],
                yAxes: [{
                    stacked: true,
                    display: false,
                }]

            }
        }
    });
    myChart.canvas.parentNode.style.height = '125px';

};




var lcm = 0;

function generateGraph(dataArray) {
    var timeLineLength = dataArray[0].length;
    var startingPoints = dataArray[0];
    var tasks = dataArray[1];
    if (interval == 0) {
        lcm = dataArray[0][timeLineLength - 1];
    } else {
        lcm = interval;
        tasks = tasks.slice(0, lcm + 2);
        startingPoints = startingPoints.slice(0, lcm + 2);
    }
    var i = 0;
    var j;
    var tasksDataset = new Array(noOfTasks);
    for (i = 0; i < noOfTasks; i++) {
        tasksDataset[i] = new Array(lcm).fill(0);
    }
    for (i = 0; i < startingPoints.length; i++) {
        var start = startingPoints[i]
        var end = startingPoints[i + 1]
        var taskNo = tasks[i]

        if (taskNo > 0) {
            taskNo = taskNo - 1
            for (j = start; j < end; j++) {
                tasksDataset[taskNo][j] = 1;
            }
        }
    }
    return tasksDataset;

}