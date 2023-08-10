from django.urls import path
from . import views

app_name='site_admin'
urlpatterns = [
        path('', views.login, name="login"),
        path('login', views.login, name="login"),
        path('dashboard', views.dashboard, name="dashboard"),
        path('list-screens', views.list_screens, name="list_screens"),
        path('add-screens', views.add_screens, name="add_screens"),
        path('view-screens', views.view_screens, name="view_screens"),
        path('list-movie', views.list_movie, name='list_movie'),
        path('view-movie/<int:id>', views.view_movie, name='view_movie'),
        path('list-people', views.list_people, name='list_people'),
        path('view-people/<int:id>', views.view_people, name='view_people'),
        path('list-user', views.list_user, name='list_user'),
        path('list-pro', views.list_pro, name='list_pro'),
        path('change-pro-status/<int:id>/<str:status>', views.change_pro_status, name='change_pro_status'),
        path('logout', views.logout, name='logout'),
]
