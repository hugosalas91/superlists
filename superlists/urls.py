from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'lists.views.home_page', name='home'), 
    # url(r'^blog/', include('blog.urls')), 
    
    # url(r'^admin/', admin.site.urls),
]