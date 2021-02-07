# First-party
from .views import UserViewSet, UserProfileViewSet

# Django
from django.urls import include, path

# Third-party
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"profiles", UserProfileViewSet)
# router.register(r"profiles", TopicViewSet)


urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "api/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    # path('api-auth/', include('rest_framework.urls')),
]