from django.urls import path
from . import views

app_name = 'user_api'

urlpatterns = [
    path('defaultsubscriptions/', views.DefaultSubView.as_view()),
    path('defaultsubscriptions/<int:uid>', views.DefaultSubViewWithId.as_view()),
    path('plans/', views.PlanView.as_view()),
]