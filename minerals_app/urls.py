from django.conf.urls import url

from . import views


app_name="minerals_app"  # needed for the include() function


urlpatterns = [
    url(r'minerals_app/(?P<pk>\d+)/$', views.mineral_detail, name='detail'),
    url(r'', views.mineral_list, name='list'),
]

