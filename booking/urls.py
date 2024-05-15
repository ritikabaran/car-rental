from django.urls import path
from booking import views
app_name='user'
urlpatterns = [
    path("welcome",views.welcome,name='welcome'),
    path("signup",views.signup,name='signup'),
    path("store_user",views.store_user,name='store_user'),
    path("login",views.login,name='login'),
    path("homepage",views.homepage,name='homepage'),
    path("profile",views.profile,name='profile'),
    path("profile_save",views.profile_save,name='profile_save'),
    path("logout",views.logout,name='logout'),
    path("book",views.book,name='book'),
    path("result",views.result,name='result'),
    path("result2",views.result2,name='result2'),
    path("history",views.history,name='history'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    
]