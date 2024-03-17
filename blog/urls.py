from django.urls import path
from .views import BlogListView, BlogDetailView,BlogCreateView,BlogUpdateView,ListAndCreate,\
    function_based_list_and_create,BlogDeleteView,BlogListDeleteView

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/", BlogDetailView.as_view(),name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(),name="post_edit"), # new
    path("", BlogListView.as_view(), name="home"),
    path("list_and_create/", ListAndCreate.as_view(), name="list_and_create"),
    path("function_based_list_and_create/", function_based_list_and_create, name="function_based_list_and_create"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(),name="post_delete"),
    path("delete_multiple/", BlogListDeleteView, name="home_delete"),
]