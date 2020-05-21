from django.conf.urls import url
from . import views as my_views
from django.contrib.auth import views

urlpatterns = [
	# url(r'^login/$',views.user_login,name='login'),
	url(r'^$', my_views.home, name='home'),

	url(r'^register/$', my_views.register, name='register'),
    url(r'^edit/$', my_views.edit, name='edit'),

    # login / logout urls
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^logout-then-login/$', views.logout_then_login, name='logout_then_login'),

    # change password urls
    url(r'^password-change/$', views.PasswordChangeView.as_view(), name='password_change'),
    url(r'^password-change/done/$', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$', views.PasswordResetView.as_view(), name='password_reset'),
    url(r'^password-reset/done/$', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^password-reset/complete/$', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	
]