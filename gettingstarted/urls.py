from django.conf.urls import include, url
from django.contrib import admin
import hello.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^project', hello.views.createProject, name='project'),
    url(r'^register', hello.views.registerManager, name='registerManager'),
    url(r'^login', hello.views.loginUser, name='login'),
    url(r'^islogged', hello.views.isLoggedUser, name='isLoggedUser'),
    url(r'^logout', hello.views.logoutUser, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^design', hello.views.createDesign, name='design'),
]
