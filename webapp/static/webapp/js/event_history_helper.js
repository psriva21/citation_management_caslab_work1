function getFileUploadEventHistory()
{
    $.ajax({
        "url": 'get_event_history_journal_upload',
        "type": 'GET',
        "data": JSON,
        "success": function(data){
            
            insRow_File_Uploads(data);
        }, 
        "failure": function(data)
        {
            alert(data);
        },
        "error": function(error, textStatus, errorText){
            console.log(errorText);
            
        }});

}

function getSubscriptionChangesEventHistory()
{
    $.ajax({
        "url": 'get_event_history_subscriptions',
        "type": 'GET',
        "data": JSON,
        "success": function(data){
            
            insRow_Subscription_Updates(data)
        }, 
        "failure": function(data)
        {
            alert(data);
        },
        "error": function(error, textStatus, errorText){
            console.log(errorText);
            
        }});

}
function getJournalMailLogEventHistory()
{
    $.ajax({
        "url": 'get_event_history_journal_mail_log',
        "type": 'GET',
        "data": JSON,
        "success": function(data){
            
            insRow_Mail_Log(data);
        }, 
        "failure": function(data)
        {
            alert(data);
        },
        "error": function(error, textStatus, errorText){
            console.log(errorText);
            
        }});

}

function insRow_File_Uploads(data)
{
    var tbl=document.getElementById('tbl_file_upload_events');
    var rowCount = tbl.rows.length;
    var size = Object.keys(data).length;
    i=0;
    for (const [key, value] of Object.entries(data)) {
        
        var row = tbl.insertRow(rowCount+i);
        i+=1;
        var cell1 = row.insertCell(0);
        cell1.innerHTML = value[1];
        var cell1 = row.insertCell(1);
        cell1.innerHTML = value[7];
        var cell1 = row.insertCell(2);
        cell1.innerHTML = value[3];
        var cell1 = row.insertCell(3);
        cell1.innerHTML = value[4];
        var cell1 = row.insertCell(4);
        cell1.innerHTML = value[5];
        var cell1 = row.insertCell(5);
        cell1.innerHTML = value[6];
        var cell1 = row.insertCell(6);
        cell1.innerHTML = value[6];
        

      }
      
    
    // for (i=0;i<size;++i)
    // {
    //     var row = tbl.insertRow(rowCount+i);

    //     var cell1 = row.insertCell(0);
    //     cell1.innerHTML = data[i][1];

    // }
}

function insRow_Subscription_Updates(data)
{
    var tbl=document.getElementById('tbl_subscription_events');
    console.log(data);
    var rowCount = tbl.rows.length;
    var size = Object.keys(data).length;
    i=0;
    for (const [key, value] of Object.entries(data)) {
        
        var row = tbl.insertRow(rowCount+i);
        i+=1;
        var cell1 = row.insertCell(0);
        cell1.innerHTML = value[6];
        var cell1 = row.insertCell(1);
        cell1.innerHTML = value[1];
        var cell1 = row.insertCell(2);
        cell1.innerHTML = value[2];
        var cell1 = row.insertCell(3);
        cell1.innerHTML = value[3];
        var cell1 = row.insertCell(4);
        cell1.innerHTML = value[4];
        var cell1 = row.insertCell(5);
        cell1.innerHTML = value[5];

      }
}

function insRow_Mail_Log(data)
{
    var tbl=document.getElementById('tbl_journal_mail_log_events');
    var rowCount = tbl.rows.length;
    var size = Object.keys(data).length;
    i=0;
    for (const [key, value] of Object.entries(data)) {
        var row = tbl.insertRow(rowCount+i);
        i+=1;
        var cell1 = row.insertCell(0);
        cell1.innerHTML = data[i][5];
        var cell1 = row.insertCell(1);
        cell1.innerHTML = data[i][1];
        var cell1 = row.insertCell(2);
        cell1.innerHTML = data[i][2];
        var cell1 = row.insertCell(3);
        cell1.innerHTML = data[i][3];
        var cell1 = row.insertCell(4);
        cell1.innerHTML = data[i][4];
    }
}