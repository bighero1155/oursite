from django.urls import path
from . import views

urlpatterns = [
    path('genders', views.index_gender),
    path('gender/create', views.create_gender),
    path('gender/store', views.store_gender),
    path('gender/show/<int:gender_id>', views.show_gender),
    path('gender/edit/<int:gender_id>', views.edit_gender),
    path('gender/update/<int:gender_id>', views.update_gender),
    path('gender/delete/<int:gender_id>', views.delete_gender),
    path('gender/destroy/<int:gender_id>', views.destroy_gender),
    path('users', views.index_user),
    path('users/create', views.create_user),
    path('users/store', views.store_user),
    path('users/show/<int:user_id>', views.show_user),
    path('users/edit/<int:user_id>', views.edit_user),
    path('users/update/<int:user_id>', views.update_user),
    path('users/delete/<int:user_id>', views.delete_user),
    path('users/destroy/<int:user_id>', views.destroy_user),
]
