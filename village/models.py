from django.db import models
import uuid


class Notice(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'सूचना'
        verbose_name_plural = 'सूचना'

    def __str__(self):
        return self.title


class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('water', 'पाणी समस्या'),
        ('road', 'रस्ता समस्या'),
        ('electricity', 'वीज समस्या'),
        ('cleanliness', 'स्वच्छता'),
        ('other', 'इतर'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    complaint_id = models.CharField(
        max_length=12,
        unique=True,
        blank=True
    )
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.complaint_id:
            self.complaint_id = uuid.uuid4().hex[:12].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.complaint_id} - {self.name}"


class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=300, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']
        verbose_name = 'गॅलरी फोटो'
        verbose_name_plural = 'गॅलरी फोटो'

    def __str__(self):
        return self.title


class ImportantContact(models.Model):
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    is_emergency = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'संपर्क माहिती'
        verbose_name_plural = 'संपर्क माहिती'

    def __str__(self):
        return f"{self.name} - {self.designation}"


class VillageInfo(models.Model):
    key = models.CharField(max_length=100, unique=True)
    label = models.CharField(max_length=200)
    value = models.TextField()

    class Meta:
        verbose_name = 'गाव माहिती'
        verbose_name_plural = 'गाव माहिती'

    def __str__(self):
        return self.label