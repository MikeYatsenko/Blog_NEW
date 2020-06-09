from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import BlogUser


class BlogUserAdmin(UserAdmin):
    model = BlogUser
    list_display = ["username","email"]



admin.site.register(BlogUser,BlogUserAdmin)