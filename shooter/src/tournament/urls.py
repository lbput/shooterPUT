from django.conf.urls import patterns, url

urlpatterns = patterns('tournament.views',
    url(r'^$', 'tournament_option', name='tournament_option'),

    url(r'^signup/$', 'tournament_signup', name='tournament_signup'),
    url(r'^results/$', 'tournament_results', name='tournament_results'),
)

#ajax
urlpatterns += patterns('tournament.ajax',

    url(r'^get_comp_for_tour/$', 'get_comp_for_tour'),
    url(r'^tournament_signup_ajax/$', 'tournament_signup_ajax'),

    url(r'^get_tournaments/$', 'get_tournaments'),
    url(r'^get_competitions/$', 'get_competitions'),
    url(r'^get_result_current_user/$', 'get_result_current_user'),

)
