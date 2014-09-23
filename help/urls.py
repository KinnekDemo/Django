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
    url(r'^up_vote/(?P<comment_id>\w+)/$', 'fix_it.views.up_vote', name='up_vote'),
    url(r'^down_vote/(?P<comment_id>\w+)/$', 'fix_it.views.down_vote', name='down_vote'),
    url(r'^new_comment/(?P<post_id>\w+)$', 'fix_it.views.new_comment', name='new_comment'),
    url(r'^leaderboard/$', 'fix_it.views.leaderboard', name='leaderboard'),
    url('^view_posts/(?P<post_id>\w+)$', 'fix_it.views.view_specific_post', name='view_specific_post')



    #  # Generic view to vote on Link objects
    # (r'^links/(?P<object_id>\d+)/(?P<direction>up|down|clear)vote/?$',
    #     vote_on_object, dict(model=Link,
    #     template_object_name='link',
    #     template_name='kb/link_confirm_vote.html',
    #     allow_xmlhttprequest=True)),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
