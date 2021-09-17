# loading in modules
import sqlite3
from datetime import date
# creating file path
pathtodb='xyz123'
dbfile = pathtodb
# Create a SQL connection to our SQLite database

def get_users():
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    sql = "select * from tbl_user;"
    cur.execute(sql)
    result = cur.fetchall()
    i =1
    dct = {}
    for i in result:
        id = i[0]
        name = i[1]
        dct[id]=name
    
    return dct

def get_paid_subscription_list():
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    sql = "select * from tbl_paid_subscriptions_creds;"
    cur.execute(sql)
    result = cur.fetchall()
    dct={}
    iterator_val=0
    for i in result:
        id = i[0]
        name = i[1]
        web_addr = i[2]
        login_id = i[3]
        pw = i[4]
        ac_no = i[5]
        notes = i[6]
        lst=[]
        lst.append(id)
        lst.append(name)
        lst.append(web_addr)
        lst.append(login_id)
        lst.append(pw)
        lst.append(ac_no)
        lst.append(notes)
        dct[iterator_val]= lst
        iterator_val+=1
    return dct

def add_new_paid_subscription(data):
    print(data)
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    j_name = data['journal_name']
    j_web_addr = data['journal_web_addr']
    j_subscription_id = data['journal_subscription_id']
    j_subscription_pw = data['journal_subscription_pw']
    j_subscription_ac = data['journal_subscription_ac']
    j_notes = data['journal_notes']

    
    str = "'"+j_name+"'"+','+"'"+j_web_addr+"'"+','+"'"+j_subscription_id+"'"+','+"'"+j_subscription_pw+"'"+','+"'"+j_subscription_ac+"'"+','+"'"+j_notes+"'"
    sql = 'insert into tbl_paid_subscriptions_creds(name,website_addr,login_id,password,ac_no,notes) values '
    sql+="( "+str+" );"
    try:   
         
        cur.execute(sql)
        con.commit()
        return {'val':1}
    except:
        return {'error':sql}    

def edit_paid_subscription(data):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    
    j_id = data['journal_id']
    j_name = data['journal_name']
    j_web_addr = data['journal_web_addr']
    login_id = data['journal_subscription_id']
    j_subscription_pw = data['journal_subscription_pw']
    j_subscription_ac = data['journal_subscription_ac']
    j_notes = data['journal_notes']


    sql = "update tbl_paid_subscriptions_creds "
    sql+="set name='"+j_name+"',"
    sql+="set website_addr='"+j_web_addr+"',"
    sql+="set login_id='"+login_id+"',"
    sql+="set password='"+j_subscription_pw+"',"
    sql+="set ac_no='"+j_subscription_ac+"',"
    sql+="set notes='"+j_notes+"'"
    sql+=" where id="+j_id+";"
    try:   
         
        cur.execute(sql)
        con.commit()
        return {'val':1}
    except:
        return {'error':sql}    

def log_new_mail_journal_DBase(data):
    
    j_name = data['journal_name']
    j_vol = data['volume_no']
    j_issue = data['issue_no']
    j_pub_dtm = data['published_dtm']
    j_page_start = data['page_no_start']
    j_page_end = data['page_no_end']
    worker_id = data['user_id']

    con = sqlite3.connect(dbfile)

    cur = con.cursor()
    str = "'"+ j_name+"','"+j_vol+"','"+j_issue+"','"+j_pub_dtm+"',"+j_page_start+','+j_page_end+','+worker_id
    sql = " insert into tbl_journal_log_DBase "
    sql+=" (journal_name,volume_no,issue_no,published_dtm,page_no_start,page_no_end,user_id) "
    sql+=" values "+"("   +str+  ");"
    try:    
        cur.execute(sql)
        con.commit()
        create_event_history_journal_mail_log(data)
        return 1
    except:
        return 0

def create_new_journal(data):

    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    j_name = data['journal_name']
    j_publication = data['publication']
    j_missing = data['missing']
    j_duplicates = data['duplicates']
    j_initials = data['initials']

    str = j_name+','+j_publication+','+j_missing+','+j_duplicates+','+j_initials
    sql = " insert into tbl_journals (name,Publication,Missing,Duplicates,Initials) values"
    sql+="( "+str+" );"

    try:   
         
        cur.execute(sql)
        con.commit()
        return 1
    except:
        return 0    
def get_dbase_journals():
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    sql = "select * from tbl_journals;"
    cur.execute(sql)
    res = cur.fetchall()
    dct={}
    
    for i in res:
        id = i[0]
        name = i[1]
        lst=[]
        
        lst.append(name)
        dct[id]= lst
        
    return dct

def get_event_history_journal_upload():
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    sql  = "select * from tbl_event_history_journal_upload;"
    cur.execute(sql)
    result = cur.fetchall()
    dct={}
    iterator_val=0
    
    for i in result:
        id = i[0]
        created_dtm = i[1]
        journal_or_website_name = i[2]
        volume_no = i[3]
        issue_no = i[4]
        published_dtm = i[5]
        user_id = i[6]
        title = i[7]

        lst = []
        lst.append(id)
        lst.append(created_dtm)
        lst.append(journal_or_website_name)
        lst.append(volume_no)
        lst.append(issue_no)
        lst.append(published_dtm)
        lst.append(user_id)
        lst.append(title)
        dct[id] = lst
    
    return dct

def create_event_history_journal_upload(data):
    created_dtm = data[created_dtm]
    event_type_id = data[event_type_id]
    journal_or_website_name = data[journal_or_website_name]
    volume_no = data[volume_no]
    issue_no = data[issue_no]
    published_dtm = data[published_dtm]
    user_id = data[user_id]
    title = data[title]

    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    str = created_dtm+','+journal_or_website_name+','+volume_no+','+issue_no+','+published_dtm+','+user_id+','+title
    sql = "insert into tbl_event_history_journal_upload (created_dtm,journal_or_website_name,volume_no,issue_no,published_dtm,user_id,title) values "
    sql+= str
    sql+= "("+str+");"

    try:   
         
        cur.execute(sql)
        con.commit()
        return 1
    except:
        return 0    

def get_event_history_subscriptions():
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    sql  = "select * from tbl_event_history_subscriptions;"
    cur.execute(sql)
    result = cur.fetchall()
    dct={}
    
    for i in result:
        id = i[0]
        journal_name = i[1]
        field_updated = i[2]
        previous_value = i[3]
        new_value = i[4]
        user_id = i[5]
        event_date = i[6]
        lst = []
        lst.append(id)
        lst.append(journal_name)
        lst.append(field_updated)
        lst.append(previous_value)
        lst.append(new_value)
        lst.append(user_id)
        lst.append(event_date) #later to be changed to user name
        dct[id] = lst
    return dct
def create_event_history_subscriptions():
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
def get_event_history_journal_mail_log():
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    sql  = "select * from tbl_event_history_journal_mail_log;"
    cur.execute(sql)
    result = cur.fetchall()
    dct={}

    for i in result:
        id = i[0]
        journal_name = i[1]
        journal_volume = i[2]
        journal_issue = i[3]
        user_id = i[4] #later to be user name
        date_uploaded = i[5]
        lst=[]
        lst.append(id)
        lst.append(journal_name)
        lst.append(journal_volume)
        lst.append(journal_issue)
        lst.append(user_id)
        lst.append(date_uploaded)
        dct[id] = lst
    return dct

def create_event_history_journal_mail_log(data):
    j_name = data['journal_name']
    j_vol = data['volume_no']
    j_issue = data['issue_no']
    j_pub_dtm = data['published_dtm']
    j_page_start = data['page_no_start']
    j_page_end = data['page_no_end']
    worker_id = data['user_id']
    today_dtm = str(date.today())
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    sql = "insert into tbl_event_history_journal_mail_log (journal_name,journal_volume,journal_issue,user_id,date_uploaded) values "
    sql+= "('"+ j_name+"','"+j_vol+"','"+j_issue+"',"+worker_id+",'"+today_dtm+"');"
    try:    
        cur.execute(sql)
        con.commit()
       
        return 1
    except:
        return 0


def user_login(data):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    sql = "select firstname,lastname,user_id from tbl_login where email='"+data['email']+"' and password = '"+data['password']+"';"
    cur.execute(sql)
    result=cur.fetchall()
    dct={}
    
    dct['user_id']=-1
    dct['login_success']=0
    if result[0][2]>0:
        dct['firstname'] = result[0][0]
        dct['lastname'] = result[0][1]
        dct['user_id'] = result[0][2]
        dct['login_success']=1
    return dct

def log_error(data):
    con = sqlite3.connect(dbfile)
    cur = con.cursor()
    error_code = data['error_code']
    error_body = data['error_body']
    sql = "insert into tbl_error (error_code,error_body) values "+"('"+error_code+"','"+error_body+"');"
    try:    
        cur.execute(sql)
        con.commit()
       
        return {"success":True}
    except:
        return {"success":False}
#main function to debug

   
