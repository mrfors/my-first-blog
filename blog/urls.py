from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),#path(r'^post/new/$', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),#path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    path('pogar/', views.pogar_list, name='pogar_list'),
    path('pogar/<int:pk>', views.pogar_detail, name='pogar_detail'),
    path('sevsk/', views.sevsk_list, name='sevsk_list'),
    path('sevsk/<int:pk>', views.sevsk_detail, name='sevsk_detail'),
    path('summernote/', include('django_summernote.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
