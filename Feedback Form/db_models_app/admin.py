from django.contrib import admin
from .models import ContactQuery,FeedbackForm

# Register your models here.
#
# admin.site.register(FeedbackForm)
# admin.site.register(ContactQuery)
#
class ContactAdmin(admin.ModelAdmin):
    list_display =  ['full_name','email','query']


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


admin.site.register(FeedbackForm,FeedBackAdmin)
admin.site.register(ContactQuery,ContactAdmin)