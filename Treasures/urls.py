from django.urls import path
from . import views

urlpatterns = [
    path('new_treasure', views.new_treasure),
    path('create_treasure', views.create_treasure),
    path('<int:treasure_id>/delete_treasure', views.delete_treasure),
    path('<int:treasure_id>', views.treasure_info),
    path('<int:treasure_id>/edit_treasure', views.edit_treasure),
    path('<int:treasure_id>/update_treasure', views.update_treasure),
    path('create_post/<int:treasure_id>', views.create_post),
    path('create_comment/<int:treasure_id>/<int:post_id>', views.create_comment),
    path('delete_post/<int:treasure_id>/<int:post_id>', views.delete_post),
    path('delete_comment/<int:treasure_id>/<int:post_id>/<int:comment_id>', views.delete_comment),
    path('create_hint/<int:treasure_id>', views.create_hint),
    path('delete_hint/<int:treasure_id>/<int:hint_id>', views.delete_hint),
]