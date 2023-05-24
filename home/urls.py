from django.urls import  path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('detail/<int:post_id>/<slug:post_slug>/',views.post_detail_view.as_view(), name='post_detail'),
    path('post/delete/<int:post_id>',views.PostDeleteView.as_view(), name='post_delete'),
    path('post/upgrade/<int:post_id>',views.PostUpdateView.as_view(), name='post_update'),
]