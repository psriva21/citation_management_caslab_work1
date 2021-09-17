
var journal_list;
var selected_journal_for_edit;
function login(data)
{
    $.ajax({
        "url": 'login',
        "type": 'GET',
        "data": data,
        "success": function(data){
           if (data.login_success==1)
           {
            $.ajax({
                "url":'setCookies',
                "type":'GET',
                "data": {'user_id':data.user_id},
                "success": function(data)
                {
                    window.open('logNewEntry');
                },
                "failure": function(data)
                {
                    console.log(data)
                },
                "error":function(data)
                {
                    console.log(data)
                }
           });
               
           }
           else
           {
               $("#incorrect_login").show();
           }

           
        }, 
        "failure": function(data)
        {
            console.log(data)
        },
        "error": function(error, textStatus, errorText){
            log_error({"error_code":error.status.toString(),"error_body":error.statusText});
            
        }});
}

function get_dbase_journals()
{
    $.ajax({
        "url": 'get_dbase_journals',
        "type": 'GET',
        "data": JSON,
        "success": function(data){
            journal_list = data;
            i=2;
            var $dropdown = $("#journal_dbase_ddl");
            $.each(data, function() 
            {            
            $dropdown.append($("<option />").val(i).text(data[i]));
            i++;
            });
        }, 
        "failure": function(data)
        {
            console.log(data)
        },
        "error": function(error){
            log_error({"error_code":error.status.toString(),"error_body":error.statusText});
            
        }});
}
function getPaidSubscriptionsList()
{
    $.ajax({
        "url": 'get_paid_subscriptions',
        "type": 'GET',
        "data": JSON,
        "success": function(data){
            
            insRow(data);
        }, 
        "failure": function(data)
        {
            alert(data);
        },
        "error": function(error){
            log_error({"error_code":error.status.toString(),"error_body":error.statusText});
            
        }});
}
function getEditSubscriptionRecords()
{
    $.ajax({
        "url": 'get_paid_subscriptions',
        "type": 'GET',
        "data": JSON,
        "success": function(data){
            journal_list = data;
            i=0;
            var $dropdown = $("#select_journal");
            $.each(data, function() 
            {            
            $dropdown.append($("<option />").val(data[i][0]).text(data[i][1]));
            i++;
            });
            document.getElementById("edit_journal_modal").style.display = "block";
            
            $('#select_journal').on('change', function() {
                i = this.options.selectedIndex;
                j_id = journal_list[i][0];
                j_name = journal_list[i][1];
                j_web_addr = journal_list[i][2];
                j_login_id = journal_list[i][3];
                j_pw = journal_list[i][4];
                j_ac_no = journal_list[i][5];
                j_notes = journal_list[i][6];
                selected_journal_for_edit = i.toString();
                $("#edit_journal_name")[0].value = j_name;
                $("#edit_journal_web_addr")[0].value = j_web_addr;
                $("#edit_journal_login_id")[0].value = j_login_id;
                $("#edit_journal_pw")[0].value = j_pw;
                $("#edit_journal_ac_no")[0].value = j_ac_no;
                 $("#edit_journal_notes")[0].value = j_notes;
              });
        }, 
        "failure": function(data)
        {
            alert(data);
        },
        "error": function(error, textStatus, errorText){
            log_error({"error_code":error.status.toString(),"error_body":error.statusText});
            
        }});
}


function insRow(data)
{
    var tbl=document.getElementById('paid_journals');
    var rowCount = tbl.rows.length;
    var size = Object.keys(data).length;
    for (i=0;i<size;++i)
    {
        var row = tbl.insertRow(rowCount+i);

        var cell1 = row.insertCell(0);
        cell1.innerHTML = data[i][1];

        var cell2 = row.insertCell(1);
        cell2.innerHTML = data[i][2];

        var cell3 = row.insertCell(2);
        cell3.innerHTML = data[i][3];

        var cell4 = row.insertCell(3);
        cell4.innerHTML = data[i][4];

        var cell5 = row.insertCell(4);
        cell5.innerHTML = data[i][5];

        var cell6 = row.insertCell(5);
        cell6.innerHTML = data[i][6];
    }


}

function addNewPaidSubscription(subscription_data)
{
    //var data_to_post=JSON.stringify(subscription_data);
    $.ajax({
        "url": 'add_new_paid_subscription',
        "type": 'GET',
        "data": subscription_data,
        "success": function(data){
            
            document.getElementById("add_new_journal_modal").style.display='None';
        }, 
        "failure": function(data)
        {
            alert('failed to add new record');
        },
        "error": function(error, textStatus, errorText){
            log_error({"error_code":error.status.toString(),"error_body":error.statusText});
            
        }});
}

function save_journal_dbase()
{
    journal_name = journal_list[$("#journal_dbase_ddl")[0].value][0];  
    volume_no = $("#volume_no")[0].value;
    issue_no = $("#issue_no")[0].value;
    pg_no_start = $("#pg_no_start")[0].value;
    pg_no_end = $("#pg_no_end")[0].value;
    pub_date = $("#pub_date")[0].value;
    journal_posted_by = $("#journal_posted_by")[0].value;
    
    data = {"journal_name":journal_name,"volume_no":volume_no,"issue_no":issue_no,"page_no_start":pg_no_start,"page_no_end":pg_no_end,"published_dtm":pub_date,"user_id":journal_posted_by};
    save_journal(data);
    
}

function save_journal(data)
{
   
//var data_to_post=JSON.stringify(subscription_data);
$.ajax({
    "url": 'log_new_mail_journal_DBase',
    "type": 'GET',
    "data": data,
    "success": function(data){
        
       console.log(data)
    }, 
    "failure": function(data)
    {
        alert('failed to add new record');
    },
    "error": function(error, textStatus, errorText){
        log_error({"error_code":error.status.toString(),"error_body":error.statusText});
        
    }});
}

function editPaidSubscription(subscription_data)
{
    $.ajax({
        "url": 'edit_journal_data',
        "type": 'GET',
        "data": subscription_data,
        "success": function(data){
            
            document.getElementById("edit_journal_modal").style.display='None';
        }, 
        "failure": function(data)
        {
            alert('failed to add new record');
        },
        "error": function(error, textStatus, errorText){
            log_error({"error_code":error.status.toString(),"error_body":error.statusText});
            
        }});
}
function GetPubMedInfo()
{
    var id= document.getElementById('PubMedID').value;
    if (id.substring(0,3)=='PMC')
    {
        id = id.substring(3,id.length);
    }
    url= 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&id='+id+'&retmode=json'
 $.ajax({
         "url": url,
         "type": 'GET',
         "success": function(data){
            pmcid = data.result.uids[0];
            journal_title = data.result[pmcid].title;
            journal_volume = data.result[pmcid].volume;
            journal_issue = data.result[pmcid].issue;
            published_date = data.result[pmcid].pubdate;
            
            json_data = {"title":journal_title,"volume":journal_volume,"issue":journal_issue,"date":published_date}
            fillLogEntry(json_data);
         }, 
         "failure": function(data)
         {
             alert(data);
         },
         "error": function(error, textStatus, errorText){
             console.log(errorText);
             log_error({"error_code":error.status.toString(),"error_body":error.statusText});
         }});
}

function fillLogEntry(json_data)
{
    $("#journal_title")[0].value=json_data.title
    $("#journal_issue")[0].value=json_data.issue
    $("#journal_volume")[0].value = json_data.volume
    $("#journal_published_date")[0].value = convertDate(json_data.date)
}


function getRootDirectories()
{
    url= ''
    $.ajax({
         "url": 'get_directories',
         "type": 'GET',
         "data": JSON,
         "success": function(data){
            i=1;
            var $dropdown = $("#directory");
            $.each(data, function() 
            {            
            $dropdown.append($("<option />").val(i).text(data[i]));
            i++;
            });
         }, 
         "failure": function(data)
         {
             alert(data);
         },
         "error": function(error, textStatus, errorText){
            log_error({"error_code":error.status.toString(),"error_body":error.statusText});
             
         }});
}
function getUsers()
{
    $.ajax({
        "url": 'get_users',
        "type": 'GET',
        "data": JSON,
        "success": function(data){
           i=1;
           var $dropdown = $("#journal_posted_by");
           $.each(data, function() 
           {            
           $dropdown.append($("<option />").val(i).text(data[i]));
           i++;
           });
        }, 
        "failure": function(data)
        {
            alert(data);
        },
        "error": function(error, textStatus, errorText){
            log_error({"error_code":error.status.toString(),"error_body":error.statusText});
            
        }});
}
function getSubDirectories(directory_name)
{
   
    $.ajax({
         "url": 'get_sub_directories',
         "type": 'GET',
         "data": {dir:directory_name},
         "success": function(data){
            i=1;
            var $dropdown = $("#sub_directory");
            $.each(data, function() 
            {            
            $dropdown.append($("<option />").val(i).text(data[i]));
            i++;
            });
         }, 
         "failure": function(data)
         {
             alert(data);
         },
         "error": function(error, textStatus, errorText){
            log_error({"error_code":error.status.toString(),"error_body":error.statusText});
             
         }});
}


function getMetaDataFromDOI(doi)
{
    var doi= document.getElementById('doi').value;
    $.ajax({  
        "url": 'https://api.crossref.org/works/'+doi,
        "type": 'GET',
        
        "success": function(data){
            journal_title = data.message.title[0];
            journal_volume = data.message.volume[0];
            year = data.message.published["date-parts"][0][0];
            month = data.message.published["date-parts"][0][1];
            day = data.message.published["date-parts"][0][2];
            published_date = year+" "+month+" "+day;

            if (data.message.issue[0] != null)
            {
                journal_issue = data.message.issue[0]
            }
            else {journal_issue = ""}
            //keeping date null for now, will test this later and populate
            
            json_data = {"title":journal_title,"volume":journal_volume,"issue":journal_issue,"date":published_date}
            fillLogEntry(json_data);
        }, 
        "failure": function(data)
        {
            alert(data);
        },
        "error": function(error, textStatus, errorText){
            log_error({"error_code":error.status.toString(),"error_body":error.statusText});
            
        }});
    
}

function convertDate(published_date)
{
    year = published_date.split(" ")[0]
    month = published_date.split(" ")[1]
    date = published_date.split(" ")[2]

    if (month == "Jan") 
    {month = "01"}
    else if (month == "Feb")
    {
        month = "02"
    }
    else if (month == "Feb")
    {
        month = "02"
    }
    else if (month == "Feb")
    {
        month = "02"
    }
    else if (month == "Feb")
    {
        month = "02"
    }
    else if (month == "Feb")
    {
        month = "02"
    }
    else if (month == "Mar")
    {
        month = "03"
    }
    else if (month == "Apr")
    {
        month = "04"
    }
    else if (month == "May")
    {
        month = "05"
    }
    else if (month == "Jun")
    {
        month = "06"
    }
    else if (month == "Jul")
    {
        month = "07"
    }
    else if (month == "Aug")
    {
        month = "08"
    }
    else if (month == "Sep")
    {
        month = "09"
    }
    else if (month == "Oct")
    {
        month = "10"
    }
    else if (month == "Nov")
    {
        month = "11"
    }
    else if (month == "Dec")
    {
        month = "12"
    }
    
    if (date.length==1)
    {
        date='0'+date;
    }
    

    return year+"-"+month+"-"+date;
}

function log_error(data)
{
    $.ajax({
        "url": 'log_error',
        "type": 'GET',
        "data": data,
        "success": function(data){
            
            console.log('error occured, check tbl_error');
        }, 
        "failure": function(data)
        {
            alert('failed to log error');
        },
        "error": function(error, textStatus, errorText){
            console.log(errorText);      
        }});
}
