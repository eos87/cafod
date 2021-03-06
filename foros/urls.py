from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from models import Foros

urlpatterns = patterns('foros.views',
    #url(r'^$', 'index', name='index'),
    url(r'^$', ListView.as_view(model=Foros, 
    	                        template_name="foros/foro_list.html"),
    	                        name='foro-list'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Foros, 
    	                                        template_name='foros/foro_detail.html'),
                                                name='foro-detail'),
    url(r'^crear/$', 'crear_foro', name='crear-foro'),
    url(r'^editar/(?P<id>\d+)/$', 'editar_foro', name='editar-foro'),
    url(r'^borrar/(?P<id>\d+)/$', 'borrar_foro', name='borrar-foro'),
    url(r'^ver/(?P<foro_id>\d+)/$', 'ver_foro', name='ver-foro'),
    url(r'^ver_comentario/(?P<aporte_id>\d+)/$', 'comentario_foro', name='cometario-foro'),
    url(r'^perfil/$', 'perfil', name='ver-perfil'),

)
