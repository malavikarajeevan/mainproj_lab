from django.urls import path
from . import views
app_name='lab' 
urlpatterns = [
    path('',views.Home,name='home'),
    path('about/',views.about,name='about'),
    path('test/',views.test,name='test'),
    path('package/',views.package,name='package'),
    path('blog/',views.blog,name='blog'),
    path('gallery/',views.gallery,name='gallery'),
    path('branches/',views.branches,name='branches'),
    path('contacts/',views.contacts,name='contacts'),
    path('branchplace/<int:id>',views.branchplace,name='branchplace'),
    path('blogpage/',views.blogpage,name='blogpage'),
    path('blogpage1/',views.blogpage1,name='blogpage1'),
    path('packages/<int:id>',views.packages,name='packages'),
    path('appointment/',views.appointment,name='appointment'),
    path('privacy/',views.privacy,name='privacy'),
    path('term/',views.term,name='term'),
    path('depart/',views.depart,name='depart'),
    path('enquiry/', views.enquiry_view, name='enquiry'),
 

]