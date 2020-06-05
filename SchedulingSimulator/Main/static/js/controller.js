function createTable(inputArray) {
    var table = document.getElementById("data_table");
    var row = 0;
    var cell = 0;
    for (row = 0; row < inputArray.length; row++) {
        addRowRefresh(inputArray[row]);
        ri = ri + 1;
    }
    var lastRow = table.rows.length;
    var x = table.rows[table.rows.length - 1].cells;
    x[0].innerHTML = (table.rows.length - 1).toString();
};

function addRowRefresh(row) {
    var new_name = row[0];
    var arrival_time = row[4];
    var exec_time = row[1];
    var period = row[2];
    var deadline = row[3];
    var table = document.getElementById("data_table");
    var table_len = (table.rows.length) - 1;
    var row = table.insertRow(table_len).outerHTML = "<tr id='row" + table_len + "'><td id='name_row" + table_len + "'>" + new_name + "</td><td id='exec_row" + table_len + "'>" + exec_time + "</td><td id='period_row" + table_len + "'>" + period + "</td><td id='deadline_row" + table_len + "'>" + deadline + "</td><td id='arrival_row" + table_len + "'>" + arrival_time + "</td><td><input type='button' id='edit_button" + table_len + "' value='Edit' class='edit' onclick='edit_row(" + table_len + ")'><input type='button' id='save_button" + table_len + "' value='Save' class='save' onclick='save_row(" + table_len + ")'><input type='button' value='Delete' class='delete' onclick='delete_row(" + table_len + ")'></td></tr>";
}

function createTable(inputArray) {
    var table = document.getElementById("data_table");
    var row = 0;
    var cell = 0;
    for (row = 0; row < inputArray.length; row++) {
        addRowRefresh(inputArray[row]);
        ri = ri + 1;
    }
    var lastRow = table.rows.length;
    var x = table.rows[table.rows.length - 1].cells;
    x[0].innerHTML = (table.rows.length - 1).toString();
};

function chooseGraph(chartID, canvasID) {
    document.getElementById(canvasID).innerHTML = "<canvas id=\"" + chartID + "\" height=\"100\"> </canvas>";
};

function addRowRefresh(row) {
    var new_name = row[0];
    var arrival_time = row[4];
    var exec_time = row[1];
    var period = row[2];
    var deadline = row[3];
    var table = document.getElementById("data_table");
    var table_len = (table.rows.length) - 1;
    var row = table.insertRow(table_len).outerHTML = "<tr id='row" + table_len + "'><td id='name_row" + table_len + "'>" + new_name + "</td><td id='exec_row" + table_len + "'>" + exec_time + "</td><td id='period_row" + table_len + "'>" + period + "</td><td id='deadline_row" + table_len + "'>" + deadline + "</td><td id='arrival_row" + table_len + "'>" + arrival_time + "</td><td><input type='button' id='edit_button" + table_len + "' value='Edit' class='edit' onclick='edit_row(" + table_len + ")'><input type='button' id='save_button" + table_len + "' value='Save' class='save' onclick='save_row(" + table_len + ")'><input type='button' value='Delete' class='delete' onclick='delete_row(" + table_len + ")'></td></tr>";
}

function edit_row(no) {
    document.getElementById("edit_button" + no).style.display = "none";
    document.getElementById("save_button" + no).style.display = "block";

    //var name=document.getElementById("name_row"+no);
    var arrival = document.getElementById("arrival_row" + no);
    var exec = document.getElementById("exec_row" + no);
    var perioD = document.getElementById("period_row" + no);
    var deadLine = document.getElementById("deadline_row" + no);

    var name_data = name.innerHTML;
    var arrival_data = arrival.innerHTML;
    var exec_data = exec.innerHTML;
    var period_data = perioD.innerHTML;
    var deadline_data = deadLine.innerHTML;

    //name.innerHTML="<input type='text' id='name_text"+no+"' value='"+name_data+"'>";
    arrival.innerHTML = "<input type='text' id='arrival_text" + no + "' value='" + arrival_data + "'>";
    exec.innerHTML = "<input type='text' id='exec_text" + no + "' value='" + exec_data + "'>";
    perioD.innerHTML = "<input type='text' id='period_text" + no + "' value='" + period_data + "'>";
    deadLine.innerHTML = "<input type='text' id='deadline_text" + no + "' value='" + deadline_data + "'>";
}


function save_row(no) {
    //var name_val=document.getElementById("name_text"+no).value;
    var arrival_val = document.getElementById("arrival_text" + no).value;
    var exec_val = document.getElementById("exec_text" + no).value;
    var period_val = document.getElementById("period_text" + no).value;
    var deadline_val = document.getElementById("deadline_text" + no).value;

    //document.getElementById("name_row"+no).innerHTML=name_val;
    document.getElementById("arrival_row" + no).innerHTML = arrival_val;
    document.getElementById("exec_row" + no).innerHTML = exec_val;
    document.getElementById("period_row" + no).innerHTML = period_val;
    document.getElementById("deadline_row" + no).innerHTML = deadline_val;

    document.getElementById("edit_button" + no).style.display = "block";
    document.getElementById("save_button" + no).style.display = "none";
}


function delete_row(no) {
    document.getElementById("row" + no + "").outerHTML = "";
    var len = document.getElementById("data_table").rows.length;
    for (i = 1; i < len; i++) {
        document.getElementById("data_table").rows[i].cells[0].innerHTML = i;
    }
    ri = len - 1;
}


function add_row() {
    var new_name = ri;
    var arrival_time = document.getElementById("arrival_time").value;
    var exec_time = document.getElementById("exec_time").value;
    var period = document.getElementById("period").value;
    var deadline = document.getElementById("deadline").value;
    if (arrival_time == '' || exec_time == '' || period == '' || deadline == '') {
        alert("Empty row is not considered for scheduling")
        return false;
    }

    var table = document.getElementById("data_table");
    var table_len = (table.rows.length) - 1;
    var row = table.insertRow(table_len).outerHTML = "<tr id='row" + table_len + "'><td id='name_row" + table_len + "'>" + new_name + "</td><td id='exec_row" + table_len + "'>" + exec_time + "</td><td id='period_row" + table_len + "'>" + period + "</td><td id='deadline_row" + table_len + "'>" + deadline + "</td><td id='arrival_row" + table_len + "'>" + arrival_time + "</td><td><input type='button' id='edit_button" + table_len + "' value='Edit' class='edit' onclick='edit_row(" + table_len + ")'><input type='button' id='save_button" + table_len + "' value='Save' class='save' onclick='save_row(" + table_len + ")'><input type='button' value='Delete' class='delete' onclick='delete_row(" + table_len + ")'></td></tr>";

    ri = ri + 1;

    document.getElementById("task").innerHTML = ri;
    document.getElementById("arrival_time").value = "";
    document.getElementById("exec_time").value = "";
    document.getElementById("period").value = "";
    document.getElementById("deadline").value = "";
}

function submitData() {
    add_row()
    var table = document.getElementById("data_table");
    var row = 0;
    var col = 0;
    var final_array = '';
    for (row = 1; row < document.getElementById("data_table").rows.length - 1; row++) {
        var rowData = document.getElementById("data_table").rows[row];
        for (col = 0; col < rowData.cells.length - 1; col++) {
            var cellsData = rowData.cells[col].innerHTML;
            final_array = final_array + cellsData + ",";
        }
        final_array = final_array + "|";
    }
    document.getElementById("id_final_array").innerHTML = final_array;
    document.getElementById("id_final_array").value = final_array;
    document.getElementById("id_noOfTasks").innerHTML = document.getElementById("data_table").rows.length - 2
    document.getElementById("id_noOfTasks").value = document.getElementById("data_table").rows.length - 2
}