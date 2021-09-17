function create_form()
{
    file = document.getElementById("file_upload").files[0];
    formdata = new FormData();
    fname = create_file_name();
    fextention = file.name.split('.')[file.name.split('.').length-1];
    fname = [fname,fextention].join('.');
    if (fname=='')
    {
        fname=file.name;
    }
    selected_directory_value = $("#directory")[0].value;
    dir_name = $("#directory option:selected").text();
    sub_dir_name = $("#sub_directory option:selected").text();
    formdata.append("file",file,fname);
    formdata.append("dir",dir_name);
    formdata.append("subdir",sub_dir_name);
    if (formdata.get("file") == null)
    {
        console.log("file upload failed");
    }
    else
    {
        console.log("uploading file to temp");
        save_file(formdata);
    }
}

function save_file(formdata)
{
    $.ajax({
        "url":'upload_file_temp',
        "type":'POST',
        "data": formdata,
        processData: false,
        contentType: false,
        
        credentials: 'include',
        "success": function(data)
        {
            console.log(data)
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

function create_file_name()
{
    try
    {
    selected_directory_value = $("#directory")[0].value;
    directory_name = $("#directory option:selected").text();
    sub_dir = $("#sub_directory option:selected").text();
    title = $("#journal_title")[0].value;
    volume = $("#journal_volume")[0].value;
    issue = $("#journal_issue")[0].value;
    date = $("#journal_published_date")[0].value;
    date = date.replaceAll("-",".");
    doc_type=   $("#journal_document_type")[0].value;
    user="PS"; //later to be fetched from cookies
    file_name = [directory_name,sub_dir,title,volume,issue,date,doc_type,user].join("_");
    return file_name;
    }
    catch{
        return '';
    }
    console.log(file_name);

}