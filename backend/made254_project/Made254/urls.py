from django.urls import path


from .views import ListMade254, DetailMade254

urlpatterns = [
    path('<int:pk>/', DetailMade254.as_view()),
    path('', ListMade254.as_view()),
]