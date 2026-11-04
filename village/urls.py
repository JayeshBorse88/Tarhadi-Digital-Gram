from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("gramseva/", views.gramseva, name="gramseva"),
    path("about/", views.about, name="about"),
    path("gallery/", views.gallery, name="gallery"),
    path("contacts/", views.contacts, name="contacts"),
    path("schemes/", views.schemes, name="schemes"),
    path("shetkari-yojana/", views.shetkari_yojana, name="shetkari_yojana"),

    # Online complaint: old and new URLs
    path("complaints/", views.complaint, name="complaints"),
    path("online-takrar/", views.complaint, name="complaint"),

    # Complaint status tracking
    path("takrar-status/", views.complaint_track, name="complaint_track"),
]