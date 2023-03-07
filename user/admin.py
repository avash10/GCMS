from django.contrib import admin

from user.models import Designation, UserProfile


# Register your models here.

class DesignationAdmin(admin.ModelAdmin):
    list_display = ["id", "designation", "designation_short", "grade", "order", "created_on"]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "office_id", "mobile", "email", "created_on"]


admin.site.register(Designation, DesignationAdmin)
admin.site.register(UserProfile, UserProfileAdmin)