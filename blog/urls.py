from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blogcontent/<int:pk>', views.blogcontent, name='blogcontent'),
    path('comment', views.comment, name='comment'),
    path('reply', views.replies, name='reply'),
    path('contctmessage', views.contctmessage, name='contctmessage' )
]
