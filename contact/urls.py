from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('admin-contact/', views.admin_contact_page, name='admin-contact'),
    path('admin-contact-reply/<int:email_id>/',
         views.admin_contact_reply, name='admin-contact-reply'),
    path('reply-email/<int:email_id>/', views.reply_email, name='reply-email'),
    path('delete-email/<int:email_id>/',
         views.delete_email, name='delete-email'),
]
