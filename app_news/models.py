from django.db import models
from django.utils.timezone import now
from django.urls import reverse

STATUS_CHOICES = (
    ('dr', 'Draft'),
    ('pb', 'Published'),
    ('ar', 'Archived'),
)

class News(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True)
    status = models.CharField(default='dr', choices=STATUS_CHOICES, max_length=2)
    publish_datetime = models.DateTimeField(default=now)
    top_image = models.ImageField(upload_to='news/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("app_news:news-detail", kwargs={"id": self.id})
    