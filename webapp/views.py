from django.shortcuts import render
from django.http import JsonResponse
from . import dropbox_utils as D
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import dropbox
from . import db_utils
from django.shortcuts import HttpResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
FILE_UPLOAD_DIR = '/temp_files'
dropboxurl='xyz123'
dbx = dropbox.Dropbox(dropboxurl)
    
import dropbox
def index(request):
    response = render(request,'webapp/index.html')  
    return response
    # if 'user_id' in request.COOKIES:
    #     user_id = request.COOKIES['user_id']
    
    # print(user_id)
    # return render(request, 'webapp/index.html')
def setCookies(request):
    response = render(request,'webapp/setcookies.html')
    response.set_cookie(key='user_id', value=request.GET['user_id'])
    return response
def links(request):
    return render(request,'webapp/links.html')
def logNewEntry(request):
    return render(request, 'webapp/logNewEntry.html')
def logEntry(request):
    return render(request,'webapp/logNewEntry.html')
def subscriptions(request):
    return render(request,'webapp/subscriptions.html')
def JournalDBase (request):
    return render(request,'webapp/JournalDBase.html')
def eventHistory(request):
    return render(request,'webapp/eventHistory.html')
def findEntry(request):
    return render(request,'webapp/findEntry.html')
def preferences(request):
    return render(request,'webapp/preferences.html')

def get_directories(request):
    
    return JsonResponse(D.getAllDirectories(dbx))

def get_users(request):
    return JsonResponse(db_utils.get_users())

def get_sub_directories(request,dir):
    dir_name = request.GET['dir']
    return JsonResponse(D.getSubDirectories(dbx,dir_name))

def get_paid_subscriptions(request):
    return JsonResponse(db_utils.get_paid_subscription_list())

def get_event_history_journal_upload(request):
    return JsonResponse(db_utils.get_event_history_journal_upload())

def get_event_history_journal_mail_log(request):
    return JsonResponse(db_utils.get_event_history_journal_mail_log())

def get_event_history_subscriptions(request):
    return JsonResponse(db_utils.get_event_history_subscriptions())



def create_event_history_journal_upload(request):
    data={}
    data['created_dtm']= request.GET['created_dtm']
    data['event_type_id'] = request.GET['event_type_id']
    data['journal_or_website_name'] = request.GET['journal_or_website_name']
    data['volume_no'] = request.GET['volume_no']
    data['issue_no'] = request.GET['issue_no']
    data['published_dtm'] = request.GET['published_dtm']
    data['user_id'] = request.GET['user_id']

    return JsonResponse(db_utils.create_event_history_journal_upload(data))

def add_new_paid_subscription(request):
    data = {}
    data['journal_name'] = request.GET['journal_name']
    data['journal_web_addr'] = request.GET['journal_web_addr']
    data['journal_subscription_id'] = request.GET['journal_subscription_id']
    data['journal_subscription_pw'] = request.GET['journal_subscription_pw']
    data['journal_subscription_ac'] = request.GET['journal_subscription_ac']
    data['journal_notes'] = request.GET['journal_notes']
    
    return JsonResponse(db_utils.add_new_paid_subscription(data))    

def edit_journal_data(request):
    data = {}
    data['journal_id'] = request.GET['journal_id']
    data['journal_name'] = request.GET['journal_name']
    data['journal_web_addr'] = request.GET['journal_web_addr']
    data['journal_subscription_id'] = request.GET['journal_subscription_id']
    data['journal_subscription_pw'] = request.GET['journal_subscription_pw']
    data['journal_subscription_ac'] = request.GET['journal_subscription_ac']
    data['journal_notes'] = request.GET['journal_notes']    

    return JsonResponse(db_utils.edit_paid_subscription(data))    

def login(request):
    data={}
    data['email']=request.GET['email']
    data['password']=request.GET['password']
    return JsonResponse(db_utils.user_login(data))   

def get_dbase_journals(request):
    return JsonResponse(db_utils.get_dbase_journals())

def log_new_mail_journal_DBase(request):
    data={}
    data['journal_name']=request.GET['journal_name']
    data['volume_no']=request.GET['volume_no']
    data['issue_no'] = request.GET['issue_no']
    data['published_dtm'] = request.GET['published_dtm']
    data['page_no_start'] = request.GET['page_no_start']
    data['page_no_end'] = request.GET['page_no_end']
    data['user_id'] = request.GET['user_id']

    return JsonResponse(db_utils.log_new_mail_journal_DBase(data))

def upload_file_temp(request):
    if request.method == 'POST' and request.FILES['file']:
        dir = request._post['dir']
        sub_dir = request._post['subdir']
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        if uploaded_file_url!=None:
            D.save_temp_file_to_dropbox(myfile.name,uploaded_file_url,dir,sub_dir,dbx,myfile)
            return JsonResponse({"success":True})
        else:
            return JsonResponse({"success":False})
    else:
        return JsonResponse({"success":False})

def log_error(request):
    data = {}
    data['error_code'] = request.GET['error_code']
    data['error_body'] = request.GET['error_body']
    return JsonResponse(db_utils.log_error(data))