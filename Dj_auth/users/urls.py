
from django.urls import path,include
from users.views import signup,home,profile


urlpatterns = [
    path('', home, name='home'),
    path('profile/',profile, name='profile'),
    path('signup/',signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
