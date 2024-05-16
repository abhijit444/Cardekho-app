from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.car_list_view, name= 'car-list'),
    path('detail/<int:pk>/', views.car_detail_view, name= 'car-detail'),
    path('showroom/', views.showroom_view.as_view(), name= 'showroom-list'),
    path('showroom/<int:pk>/cars', views.get_cars_in_showroom_view, name= 'showroom-cars'),
    path('review/', views.review_view, name= 'review-list'),
    path('car/<int:pk>/reviews/', views.CarReviewAPIView.as_view(), name='car_reviews'),
    path('showroom/<int:showroom_id>/reviews/', views.ShowroomReviewAPIView.as_view(), name='showroom_reviews'),
]
