from django.contrib import admin
from voir.models import *
# Register your models here.


class TaskAdmin(admin.ModelAdmin):

    list_display = ("name", "description", "created_date" )


admin.site.register(Task, TaskAdmin)