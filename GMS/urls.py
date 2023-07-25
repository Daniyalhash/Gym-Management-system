from django.contrib import admin
from django.urls import path
from GMS import views

from .views import *
urlpatterns = [
   path('',dashboard,name='home'),

   #  dashboard
   path('dashboard/',dashboard,name='dashboard'),
   # member
   path('member/',member,name='member'),
   path('save_member',save_member,name='save_member'),
   path('delete_member/<str:m_id>',delete_member,name='delete_member'),
   path('update_member/<str:m_id>/',update_member,name='update_member'),
   path('getmember',getmember,name='getmember'),
   path('editmember',editmember,name='editmember'),



   # trainer
   path('trainer/',trainer,name='trainer'),
   path('save_trainer',save_trainer,name='save_trainer'),
   path('delete_trainer/<str:t_id>',delete_trainer,name='delete_trainer'),
   path('update_trainer/<str:t_id>/',update_trainer,name='update_trainer'),
   path('gettrainer',gettrainer,name='gettrainer'),
   path('edittrainer',edittrainer,name='edittrainer'),




   # plan
   path('plan/',plan,name='plan'),
   path('create_plan/<str:m_id>/',create_plan,name='create_plan'),
   path('save_plan',save_plan,name='save_plan'),
   path('delete_plan/<str:mm_id>',delete_plan,name='delete_plan'),

   path('count/',your_view_function,name='your_view_function')
   
]
