from django.conf.urls import patterns, url

urlpatterns = patterns('quintette.contrib.password_auth.views',

    url(r'^login/$', 
        'login',
        name='login'),

    url(r'^logout/$', 
        'logout', 
        name='logout'),

)
