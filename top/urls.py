from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('players/',player),
    path('latest/',latest),
    path('clubs/',clubs),
    path('c_p/<str:name>/',country_club),
    path('tryouts/',tryouts),
    path('about/',about),
    path('header/',header),
    path('t_archive/',t_archive),
    path('mavsum/<str:num>/',season_t),
    path('countries/<str:name>/',country_c),
    path('u-20/',u_20),

    path('t_records/',transfer_r),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
