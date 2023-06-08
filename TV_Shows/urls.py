from django.urls import path
from . import views


urlpatterns = [
    path('', views.root),
    path('shows', views.shows, name="shows"),
    path('shows/new', views.new_show, name="new_show"),
    path('shows/edit/<int:id>', views.edit_show, name="edit_show"),
    path('shows/show/<int:id>', views.show_show, name="show_show"),
    path('shows/delete/<int:id>', views.delete_show, name="delete_show"),
    path('shows/new/create', views.create_show, name="create_show"),
    path('shows/update', views.update_show, name="update_show"),
]