from django.contrib import admin
from .models import CreatedModel, PublishedModel, TextModel, TitleModel, AuthorModel
# Register your models here.

admin.site.register(CreatedModel)
admin.site.register(PublishedModel)
admin.site.register(TextModel)
admin.site.register(TitleModel)
admin.site.register(AuthorModel)