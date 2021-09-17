from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logEntry',views.logEntry,name='logEntry'),
    path('logNewEntry',views.logNewEntry,name='logNewEntry'),
    path('subscriptions',views.subscriptions,name='subscriptions'),
    path('eventHistory',views.eventHistory,name='eventHistory'),
    path('findEntry',views.findEntry,name='findEntry'),
    path('preferences',views.preferences,name='preferences'),
    path('get_directories',views.get_directories,name='get_directories'),
    path('<str:dir>/',views.get_sub_directories,name='get_sub_directories'),
    path('get_users',views.get_users,name='get_users'),
    path('get_paid_subscriptions',views.get_paid_subscriptions,name='get_paid_subscriptions'),
    path('add_new_paid_subscription',views.add_new_paid_subscription,name='add_new_paid_subscription'),
    path('edit_journal_data',views.edit_journal_data,name='edit_journal_data'),
    path('create_event_history_journal_upload',views.create_event_history_journal_upload,name='create_event_history_journal_upload'),
    path('get_event_history_journal_upload',views.get_event_history_journal_upload,name='get_event_history_journal_upload'),
    path('get_event_history_journal_mail_log',views.get_event_history_journal_mail_log,name='get_event_history_journal_mail_log'),
    path('get_event_history_subscriptions',views.get_event_history_subscriptions,name='get_event_history_subscriptions'),
    path('JournalDBase',views.JournalDBase,name='JournalDBase'),
    path('log_new_mail_journal_DBase',views.log_new_mail_journal_DBase,name='log_new_mail_journal_DBase'),
    path('login',views.login,name='login'),
    path('get_dbase_journals',views.get_dbase_journals,name='get_dbase_journals'),
    path('setCookies',views.setCookies,name='setCookies'),
    path('links',views.links,name='links'),
    path('upload_file_temp',views.upload_file_temp,name='upload_file_temp'),
    path('log_error',views.log_error,name='log_error')
    
    

]