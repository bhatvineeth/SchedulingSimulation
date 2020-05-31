    var colors= ['#FF6633', '#FFB399', '#FF33FF', '#FFFF99', '#00B3E6',
		  '#E6B333', '#3366E6', '#999966', '#99FF99', '#B34D4D',
		  '#80B300', '#809900', '#E6B3B3', '#6680B3', '#66991A',
		  '#FF99E6', '#CCFF1A', '#FF1A66', '#E6331A', '#33FFCC',
		  '#66994D', '#B366CC', '#4D8000', '#B33300', '#CC80CC',
		  '#66664D', '#991AFF', '#E666FF', '#4DB3FF', '#1AB399',
		  '#E666B3', '#33991A', '#CC9999', '#B3B31A', '#00E680',
		  '#4D8066', '#809980', '#E6FF80', '#1AFF33', '#999933',
		  '#FF3380', '#CCCC00', '#66E64D', '#4D80CC', '#9900B3',
		  '#E64D66', '#4DB380', '#FF4D4D', '#99E6E6', '#6666FF'];

    var lcm = 0;
    function generateGraph(dataArray) {
        var timeLineLength = dataArray[0].length;
        var startingPoints = dataArray[0];
        var tasks = dataArray[1];
        if (interval == 0) {
            lcm = dataArray[0][timeLineLength - 1];
        } else {
            lcm = interval;
            tasks = tasks.slice(0, lcm+2);
            startingPoints = startingPoints.slice(0, lcm+2);
        }
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

    function generateLineGraph(dataArray) {
        var timeLineLength = dataArray[0].length;
        var startingPoints = dataArray[0];
        var tasks = dataArray[1];
        if (interval == 0) {
            lcm = dataArray[0][timeLineLength - 1];
        } else {
            lcm = interval;
            tasks = tasks.slice(0, lcm+2);
            startingPoints = startingPoints.slice(0, lcm+2);
        }
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
        var xaxisLength = 0;
        var points = new Array(noOfTasks);
        for (i =0; i < tasksDataset.length; i++) {
            tasks = tasksDataset[i];
            points[i] = [];
            for (j = 0; j < tasks.length ; j++) {
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

    function createGraph(canvasID, title, schedulingArray, inputArray) {
        var labels = [];
        var data = generateGraph(schedulingArray);
        var dataSet = [];
        var set = {};
        var i;
        var axisLabel = []
        for (i = 0; i < lcm ; i++) {
            axisLabel.push(i.toString());
        }
        for (i = 0; i < noOfTasks ; i++) {
            var inputTask = '['+inputArray[i][0] +', '+inputArray[i][1]+', '+ inputArray[i][2]+', '+inputArray[i][3]+']';
            var temp = {};
            temp['catergoryPercentage'] = 1;
            temp['barPercentage'] = 1.2;
            temp['barThickness'] = 'flex';
            temp['label'] = 'Task ' + (i+1).toString() + inputTask;
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

     function createTable(inputArray) {
        var table = document.getElementById("data_table");
        var row = 0;
        var cell = 0;
        for (row = 0; row < inputArray.length ; row++) {
            addRowRefresh(inputArray[row]);
            ri = ri+1;
        }
        var lastRow = table.rows.length;
        var x = table.rows[table.rows.length-1].cells;
        x[0].innerHTML = (table.rows.length-1).toString();
     };

     function addRowRefresh(row) {
         var new_name = row[0];
         var arrival_time=row[4];
         var exec_time=row[1];
         var period=row[2];
         var deadline=row[3];

         var table=document.getElementById("data_table");
         var table_len=(table.rows.length)-1;
         var row = table.insertRow(table_len).outerHTML="<tr id='row"+table_len+"'><td id='name_row"+table_len+"'>"+new_name+"</td><td id='exec_row"+table_len+"'>"+exec_time+"</td><td id='period_row"+table_len+"'>"+period+"</td><td id='deadline_row"+table_len+"'>"+deadline+"</td><td id='arrival_row"+table_len+"'>"+arrival_time+"</td><td><input type='button' id='edit_button"+table_len+"' value='Edit' class='edit' onclick='edit_row("+table_len+")'><input type='button' id='save_button"+table_len+"' value='Save' class='save' onclick='save_row("+table_len+")'><input type='button' value='Delete' class='delete' onclick='delete_row("+table_len+")'></td></tr>";


     }

     function createLineGraph(canvasID, title, schedulingArray, inputArray) {
        var labels = [];
        var data = generateLineGraph(schedulingArray);
        var dataSet = [];
        var set = {};
        var i;
        var axisLabel = []
        for (i = 0; i < lcm ; i++) {
            axisLabel.push(i.toString());
        }
        for (i = 0; i < noOfTasks ; i++) {
            var inputTask = '['+inputArray[i][0] +', '+inputArray[i][1]+', '+ inputArray[i][2]+', '+inputArray[i][3]+']';
            var temp = {};

            temp['steppedLine'] = 'steppedLine';
            temp['label'] = 'Task ' + (i+1).toString() + inputTask;
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
                scales: {
                    xAxes: [{

                    }],
                    yAxes: [{

                        display: false,
                    }]

                }
            }
        });
     };

     function createTable(inputArray) {
        var table = document.getElementById("data_table");
        var row = 0;
        var cell = 0;
        for (row = 0; row < inputArray.length ; row++) {
            addRowRefresh(inputArray[row]);
            ri = ri+1;
        }
        var lastRow = table.rows.length;
        var x = table.rows[table.rows.length-1].cells;
        x[0].innerHTML = (table.rows.length-1).toString();
     };

     function addRowRefresh(row) {
         var new_name = row[0];
         var arrival_time=row[4];
         var exec_time=row[1];
         var period=row[2];
         var deadline=row[3];

         var table=document.getElementById("data_table");
         var table_len=(table.rows.length)-1;
         var row = table.insertRow(table_len).outerHTML="<tr id='row"+table_len+"'><td id='name_row"+table_len+"'>"+new_name+"</td><td id='exec_row"+table_len+"'>"+exec_time+"</td><td id='period_row"+table_len+"'>"+period+"</td><td id='deadline_row"+table_len+"'>"+deadline+"</td><td id='arrival_row"+table_len+"'>"+arrival_time+"</td><td><input type='button' id='edit_button"+table_len+"' value='Edit' class='edit' onclick='edit_row("+table_len+")'><input type='button' id='save_button"+table_len+"' value='Save' class='save' onclick='save_row("+table_len+")'><input type='button' value='Delete' class='delete' onclick='delete_row("+table_len+")'></td></tr>";


     }


        function edit_row(no)
        {
         document.getElementById("edit_button"+no).style.display="none";
         document.getElementById("save_button"+no).style.display="block";

         //var name=document.getElementById("name_row"+no);
         var arrival=document.getElementById("arrival_row"+no);
         var exec=document.getElementById("exec_row"+no);
          var perioD=document.getElementById("period_row"+no);
         var deadLine=document.getElementById("deadline_row"+no);

         var name_data=name.innerHTML;
         var arrival_data=arrival.innerHTML;
         var exec_data=exec.innerHTML;
         var period_data=perioD.innerHTML;
         var deadline_data=deadLine.innerHTML;

         //name.innerHTML="<input type='text' id='name_text"+no+"' value='"+name_data+"'>";
         arrival.innerHTML="<input type='text' id='arrival_text"+no+"' value='"+arrival_data+"'>";
         exec.innerHTML="<input type='text' id='exec_text"+no+"' value='"+exec_data+"'>";
         perioD.innerHTML="<input type='text' id='period_text"+no+"' value='"+period_data+"'>";
         deadLine.innerHTML="<input type='text' id='deadline_text"+no+"' value='"+deadline_data+"'>";
        }


        function save_row(no)
        {
         //var name_val=document.getElementById("name_text"+no).value;
         var arrival_val=document.getElementById("arrival_text"+no).value;
         var exec_val=document.getElementById("exec_text"+no).value;
         var period_val=document.getElementById("period_text"+no).value;
         var deadline_val=document.getElementById("deadline_text"+no).value;

         //document.getElementById("name_row"+no).innerHTML=name_val;
         document.getElementById("arrival_row"+no).innerHTML=arrival_val;
         document.getElementById("exec_row"+no).innerHTML=exec_val;
          document.getElementById("period_row"+no).innerHTML=period_val;
         document.getElementById("deadline_row"+no).innerHTML=deadline_val;

         document.getElementById("edit_button"+no).style.display="block";
         document.getElementById("save_button"+no).style.display="none";
        }


        function delete_row(no)
        {
         document.getElementById("row"+no+"").outerHTML="";
         var len = document.getElementById("data_table").rows.length;
         for (i = 1; i < len ; i++) {
            document.getElementById("data_table").rows[i].cells[0].innerHTML = i;
         }
         ri = len-1;
        }


        function add_row()
        {
            var new_name = ri;

         var arrival_time=document.getElementById("arrival_time").value;
         var exec_time=document.getElementById("exec_time").value;
         var period=document.getElementById("period").value;
         var deadline=document.getElementById("deadline").value;
        if (arrival_time == '' || exec_time == '' || period == '' || deadline == '') {
            alert("Invaid Input")
            return false;
        }

         var table=document.getElementById("data_table");
         var table_len=(table.rows.length)-1;
         var row = table.insertRow(table_len).outerHTML="<tr id='row"+table_len+"'><td id='name_row"+table_len+"'>"+new_name+"</td><td id='exec_row"+table_len+"'>"+exec_time+"</td><td id='period_row"+table_len+"'>"+period+"</td><td id='deadline_row"+table_len+"'>"+deadline+"</td><td id='arrival_row"+table_len+"'>"+arrival_time+"</td><td><input type='button' id='edit_button"+table_len+"' value='Edit' class='edit' onclick='edit_row("+table_len+")'><input type='button' id='save_button"+table_len+"' value='Save' class='save' onclick='save_row("+table_len+")'><input type='button' value='Delete' class='delete' onclick='delete_row("+table_len+")'></td></tr>";

        ri = ri+1;

        document.getElementById("task").innerHTML=ri;
         document.getElementById("arrival_time").value="";
         document.getElementById("exec_time").value="";
         document.getElementById("period").value="";
         document.getElementById("deadline").value="";
        }

        function submitData() {
			add_row()
            var table=document.getElementById("data_table");
            var row = 0;
            var col = 0;
            var final_array = '';
            for (row = 1; row < document.getElementById("data_table").rows.length - 1; row++) {
                var rowData = document.getElementById("data_table").rows[row];
                for (col = 0; col < rowData.cells.length - 1 ; col++) {
                    var cellsData = rowData.cells[col].innerHTML;
                    final_array = final_array + cellsData + ",";

                }
                final_array = final_array + "|";

            }
            document.getElementById("id_final_array").innerHTML = final_array;
            document.getElementById("id_final_array").value=final_array;
            document.getElementById("id_noOfTasks").innerHTML = document.getElementById("data_table").rows.length - 2
            document.getElementById("id_noOfTasks").value = document.getElementById("data_table").rows.length - 2
        }





