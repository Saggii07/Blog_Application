
from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('detail/<int:pk>',views.DetailView.as_view(),name='detail'),
    path('delete/<int:pk>',views.DeleteView.as_view(),name='delete'),
    path('addblog/',views.AddPostView.as_view(),name='addblog'),
    path('update/<int:pk>/',views.UpdateView.as_view(),name='update'),
    
    # API URL
    path('api/v1/',views.ListPost.as_view(),name='api_post'),
    path('api/v1/<int:pk>/',views.ListDetailPost.as_view(),name='api_post_detail'),



 
    
]
