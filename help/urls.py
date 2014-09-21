from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'help.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^$', 'fix_it.views.front', name='front'),
    url(r'^new_post/', 'fix_it.views.new_post', name='new_post'),
    url(r'^profile/$', 'fix_it.views.profile', name='profile'),
    url(r'^register/$', 'fix_it.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^view_posts/$', 'fix_it.views.view_posts', name='view_posts'),
    url(r'^(?P<comment_id>\w+)/$', 'fix_it.views.up_vote', name='up_vote'),
    #  # Generic view to vote on Link objects
    # (r'^links/(?P<object_id>\d+)/(?P<direction>up|down|clear)vote/?$',
    #     vote_on_object, dict(model=Link,
    #     template_object_name='link',
    #     template_name='kb/link_confirm_vote.html',
    #     allow_xmlhttprequest=True)),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
