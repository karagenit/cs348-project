from django.urls import path
from rush import views

app_name = 'rush'
urlpatterns = [
    path('', views.rush, name='start_screen'),
    path("student/setup/<int:pk>/", views.setup, name="student_setup"),
    path("student/<int:pk>/", views.home, name="homepage"),
    path("<int:pk>/fraternity/brief/<int:id>/",views.fraternityBrief, name="fraternity_brief"),
    path("<int:pk>/fraternity/<int:fid>/event/<int:event>/", views.eventBrief, name="event_brief"),
    path("fraternity/setup/", views.fraternitySetup, name="fraternity_setup"),
    path("fraternity/<int:pk>/", views.fraternityHome, name="fraternity_home"),
    path("<int:student>/fraternity/<int:pk>/",views.fraternity, name="fraternity"),
    path("fraternity/<int:pk>/eventSetup/", views.eventSetup, name="event_setup"),
    path("fraternity/<int:pk>/<int:puid>/",views.studentBrief, name="student_brief"),
    path("<int:pk>/event/<int:id>/", views.event, name="event")
]