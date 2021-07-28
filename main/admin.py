from django.contrib import admin

from .models import CommonInfo, Rubric


# Register your models here.
# admin.site.register(CommonInfo)

class CommonInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content',)


admin.site.register(CommonInfo, CommonInfoAdmin)
admin.site.register(Rubric)
