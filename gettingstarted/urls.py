from django.conf.urls import include, url
import hello.views
urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
        url(r'project^$', hello.views.createProject, name='project'),


]
