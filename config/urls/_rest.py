from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token

from <app>.serializers import ProfileSerializer


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'profiles', views.ProfileViewSet)

schema_view = get_schema_view(title='Pastebin API')


rest_patterns = [

  url(r'^api/', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls')),
  url(r'^api/schema/$', schema_view),
  url(r'^api/obtain-auth-token/$', obtain_auth_token),

]
