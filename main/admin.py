from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# admin.site.register(Post)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
admin.site.register(Post, PostAdmin)


admin.site.register(Appointment)
admin.site.register(contactus)
admin.site.register(UserMail)