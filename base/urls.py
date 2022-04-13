"""URL routing for base app"""

from django.urls import path
from .views import (
    IndexView,
    InteriorsView,
    InteriorView,
    AboutUsView,
    MediaView,
    ContactsView,
    ReferncesViev,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("interiors/", InteriorsView.as_view(), name="interiors"),
    path("interior/<int:pk>/", InteriorView.as_view(), name="interior"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("references/", ReferncesViev.as_view(), name="references"),
    path("about/", AboutUsView.as_view(), name="about"),
    path("media/", MediaView.as_view(), name="media"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
