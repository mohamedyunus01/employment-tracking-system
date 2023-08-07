from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('login/',login),
    path('loginqr/',loginQR, name = 'loginqr'),
    path('<str:code>/home/',home,name='home'),
    path('<str:code>/register/',register, name='register'),
    path('<str:code>/add_course/',add_course,name='add_course'),
    path('<str:code>/add_courseqr/',add_course_qr,name='add_course_qr'),


    path('<str:code>/add_work/',add_work,name='add_work'),
    path('<str:code>/add_workqr/',add_work_qr,name='add_work_qr'),


    path('<str:code>/add_resign/',add_resign,name='add_resign'),
    path('<str:code>/add_resignqr/',add_resign_qr,name='add_resign_qr'),

    path('<str:code>/activity/',activity,name='activity'),
    path("<str:uid>/view_details/",view_details,name='view_details'),
    path("<str:code>/add_course/confirm", confirmAddCourse, name='confirmAddCourse'),
    path("<str:code>/add_work/confirm", confirmAddWork, name='confirmAddWork'),
    path("<str:code>/add_resign/confirm", confirmAddResign, name='confirmAddResign'),
    path("trace/", trace,name='trace'),
    path('SEV1234/home3/',home3, name='home3'),
    path('search/',search,name='search' ),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('media/Files/<int:pk>',PostDeleteView.as_view(),name='post-delete' ),
    path('search/',search,name='search' ),
    path('about/', about, name='blog-about'),
    path('login2/',login2),


    path('<str:uid>/api/', API.as_view())

]

