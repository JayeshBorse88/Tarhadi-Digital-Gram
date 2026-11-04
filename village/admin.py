from django.contrib import admin
from .models import Notice, Complaint, GalleryImage, ImportantContact, VillageInfo


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "message")
    ordering = ("-created_at",)


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        "complaint_id",
        "name",
        "mobile",
        "category",
        "status",
        "created_at",
    )

    list_filter = ("status", "category", "created_at")

    search_fields = (
        "complaint_id",
        "name",
        "mobile",
        "description",
    )

    list_editable = ("status",)

    readonly_fields = ("complaint_id", "created_at")

    ordering = ("-created_at",)

    list_per_page = 20


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "uploaded_at")
    search_fields = ("title", "description")
    ordering = ("-uploaded_at",)
    list_per_page = 20


@admin.register(ImportantContact)
class ImportantContactAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "phone", "is_emergency", "order")
    list_filter = ("is_emergency",)
    search_fields = ("name", "designation", "phone")
    list_editable = ("phone", "is_emergency", "order")
    ordering = ("order",)


@admin.register(VillageInfo)
class VillageInfoAdmin(admin.ModelAdmin):
    list_display = ("label", "key", "value")
    search_fields = ("label", "key")