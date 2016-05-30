from django.contrib import admin
from models import BlogEntry,Testimonial

class BlogEntryAdmin(admin.ModelAdmin):
    change_form_template = 'master/change_form.html'

admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(Testimonial)

# Register your models here.
