from django.contrib import admin
from django.urls import path
from blog import views

from django.conf import settings
from django.conf.urls.static import static   


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('create/', views.create_post, name='create_post'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)