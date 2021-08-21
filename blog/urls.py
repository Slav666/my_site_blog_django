from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting_page"),
    path("post", views.AllPostsView.as_view(), name="post-page"),
    path("post/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page")
]
