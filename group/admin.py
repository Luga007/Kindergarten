from django.contrib import admin
from .models import Group
# Register your models here.


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ('total_quantity',)
    list_display = ('id', 'group_name', 'total_quantity')


