from django.conf.urls import url
from basic_app import views

# Template Tagging. Always give app name as the original app name. This name will indicate in relative html file
app_name = 'basic_app'

# The name parameter will indicate to html file
urlpatterns=[
    url(r'^relative/$',views.relative,name='relative_page'),
    url(r'^other/$',views.other,name='other_page'),
]
