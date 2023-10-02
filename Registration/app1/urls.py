from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import UserDataView

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('signup/login/', views.LoginPage, name='login'),
    path('signup/', views.SignupPage, name='signup'),
    path('signup/login/welcome/', views.WelcomePage, name='welcome'),
    path('signup/login/welcome/dashboard', views.dashboard, name='dashboard'),
    path("mark_completed/", views.mark_video_completed, name="mark_video_completed"),
    path('logout/', views.logout_view, name='logout'),
    path('upload/', views.upload_image, name='upload'),
    path('change-password/', views.change_password, name='change_password'),
    path('mark_video_as_done/', views.mark_video_as_done, name='mark_video_as_done'),
    path('check_username/', views.check_username, name='check_username'),
    path('check_email/', views.check_email, name='check_email'),
    path('signup/login/user-data/', UserDataView.as_view(), name='user_data'),
    path('signup/login/Taekwondo/', views.Taekwondo, name='Taekwondo'),
    path('signup/login/swimming/', views.swimming, name='swimming'),
    path('signup/login/basketball/', views.basketball, name='basketball'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)