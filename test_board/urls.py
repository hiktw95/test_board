from django.conf.urls import include, url
from django.contrib import admin
from kkk import *
urlpatterns = [
    # Examples:
    # url(r'^$', 'test_board.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^board', 'kkk.main_views.board_page'),
    url(r'^login', 'kkk.main_views.login'),
    url(r'^$', 'kkk.main_views.main_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve',{'document_root': 'D:\\kkk\\test_board\\images'}),
    url(r'^writeBoard', 'kkk.main_views.write_board'),
    url(r'^write', 'kkk.main_views.write_page'),
    url(r'^regist_user', 'kkk.main_views.regist_user'),
    url(r'^regist', 'kkk.main_views.regist_page'),
    url(r'^view', 'kkk.main_views.view_page'),
                                                               
]
