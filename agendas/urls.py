from django.conf.urls.defaults import *
from django.views.generic import ListView, DetailView
from models import Agendas

urlpatterns = patterns('agendas.views',
    url(r'^$', ListView.as_view(model=Agendas, 
    	                        template_name="agendas/agenda_list.html"),
                                name="agenda-list"),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Agendas, 
    	                                        template_name='agendas/agenda_detail.html'),
                                                name='agenda-detail'),
    url(r'^crear/$', 'crear_agenda', name="crear-agenda"),
    url(r'^editar/(?P<id>\d+)/$', 'editar_agenda', name='editar-agenda'),
    url(r'^borrar/(?P<id>\d+)/$', 'borrar_agenda', name='borrar-agenda'),
    )