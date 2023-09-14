from django.urls import include, path
from rest_framework import routers

from api.views.booking import SettingBookingView
from api.views.playground import (
    GetOrCancelBookingUserViewSet,
    GetOwnerCreateUserBookingPlaygroundViewSet,
    CoveringViewSet,
    SportViewSet,
    PlaygroundViewSet,
)
from api.views.users import CustomUserViewSet

v1_router = routers.DefaultRouter()

v1_router.register("sports", SportViewSet, basename="sport")
v1_router.register("coverings", CoveringViewSet, basename="covering")
v1_router.register("playgrounds", PlaygroundViewSet, basename="playground")
v1_router.register(
    r"bookings", GetOrCancelBookingUserViewSet, basename="bookings"
)
# v1_router.register(
#     r'bookings/(?P<playground_slug>\d+)',
#     BookingViewSet, basename='booking',
# )
v1_router.register("users", CustomUserViewSet, basename="users")
v1_router.register(
    r"playgrounds/(?P<playground_id>\d+)/bookings",
    GetOwnerCreateUserBookingPlaygroundViewSet,
    basename="playgrounds",
)

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path(
        "v1/playgrounds/<int:playground_id>/settings/",
        SettingBookingView.as_view(),
    ),
    path("v1/auth/", include("djoser.urls.authtoken")),
]
