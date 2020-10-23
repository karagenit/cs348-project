from django.urls import path
from rush import views

app_name = 'rush'
urlpatterns = [
    path('', views.rush, name='start_screen'),
    path("student/setup/<int:pk>/", views.setup, name="student_setup"),
    path("student/<int:pk>/", views.home, name="homepage"),
    path("fraternity/setup/", views.fraternitySetup, name="fraternity_setup"),
    path("fraternity/<int:pk>/", views.fraternityHome, name="fraternity_home"),
]