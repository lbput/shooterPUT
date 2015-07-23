from django.conf.urls import patterns, include, url
#from django.contrib.auth import views as auth_views


urlpatterns = patterns('',
	url(r'^register/$', 'userprofile.views.ShooterRegistration', name='register'),
	url(r'^register-success/$', 'userprofile.views.RegisterSuccess', name='registersuccess'),
	url(r'^login/$', 'userprofile.views.LoginRequest', name='login'),
	url(r'^logout/$', 'userprofile.views.LogoutRequest', name='logout'),
	url(r'^profile/', 'userprofile.views.Profile', name ='profile'),
	url(r'^change-password/', 'userprofile.views.ChangePasswordRequest', name ='changepassword'),
	url(r'^change-email/', 'userprofile.views.ChangeEmailRequest', name ='changeemail'),
	url(r'^reset-password/', 'userprofile.views.ResetPasswordRequest', name ='resetpassword'),
	url(r'^reset-success/', 'userprofile.views.ResetPasswordSuccessRequest', name ='resetpasswordsuccess'),
)

#urlpatterns += patterns('',
#	url(r'^resetpasword/passwordsent/$', auth_views.password_reset_done),
#	url(r'^resetpassword/$', auth_views.password_reset, {}, name='password_reset'),
#	url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm),
#	url(r'^reset/done/$',auth_views.password_reset_complete),
#)
