from django.contrib import admin
from interests.models import Interest, InterestCategory, UserInterests

admin.site.register(Interest)
admin.site.register(InterestCategory)
admin.site.register(UserInterests)
