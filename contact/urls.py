from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('admin-contact/', views.admin_contact_page, name='admin-contact'),
    path('reply-email/<int:email_id>/', views.reply_email, name='reply-email'),
]
