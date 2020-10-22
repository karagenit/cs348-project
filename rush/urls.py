from django.urls import path
from rush import views

app_name = 'rush'
urlpatterns = [
    path('', views.rush, name='start_screen'),
    path("setup/<int:pk>/", views.setup, name="student_setup"),
    path("<int:pk>/", views.home, name="homepage"),
]