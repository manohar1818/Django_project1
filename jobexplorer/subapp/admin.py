from django.contrib import admin
# Register your models here.
from .models import Article

class ArticleDetail(admin.ModelAdmin):
    list_display = ('id', 'Title', 'created', )
    search_fields = ('Title', 'created', )

admin.site.register(Article, ArticleDetail)
