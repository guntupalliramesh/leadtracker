from  django.urls import path
from . import views
urlpatterns = [
    path('registration_html/', views.registration_html,name="registration_html"),
    path('mainpage/',views.mainpage,name='mainpage'),
    path('data_page/',views.data_page,name='data_page'),
    path('calling/',views.calling,name='calling'),
    path('calling1/',views.calling1,name='calling1'),
    path('counselling/',views.counselling,name='counselling'),
    path('counselling1/',views.counselling1,name='counselling1'),
    path('join/',views.join,name='join'),
    path('update/<int:id>', views.update,name='update'),
    path('edit/<int:id>', views.edit,name='edit'),     
    path('delete/<int:id>', views.destroy,name='delete'),
    path('student/',views.student,name='student'),
    path('current/',views.current,name='current'),
    path('rejoin/',views.rejoin,name='rejoin'), 
    path('complete/<id>',views.complete,name='complete'),
    path('delay/<id>',views.delay,name='delay'),
    path('stop/<id>',views.stop,name='stop'),

 ]
