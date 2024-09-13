from django.contrib import admin
from app_news.models import News
from jalali_date.admin import ModelAdminJalaliMixin	
 

@admin.register(News)
class NewsAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    pass

# admin.site.register(News)