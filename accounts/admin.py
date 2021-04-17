from django.contrib import admin
from accounts.models import student, group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.


class studentAdmin (BaseUserAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_courseRep',
                    'phone', 'group_id', 'date_joined', 'last_login')
    search_fields = ('first_name', 'group_id', 'email', 'phone')
    filter_horizontal = ()
    # read_only
    list_filter = ('last_login', 'group_id',)
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ('first_name', 'last_name', 'email', 'phone', 'is_courseRep', 'group_id', 'password1', 'password2'),
        }),
    )

    ordering = ('first_name',)


class groupAdmin (admin.ModelAdmin):
    list_display = ('department', 'level', 'group_id')
    search_fields = ('department', 'level', 'group_id')
    filter_horizontal = ()
    list_filter = ('department', 'group_id')
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("department", "level", "group_id"),
        }),
    )

    ordering = ('group_id',)


admin.site.register(student, studentAdmin)
admin.site.register(group, groupAdmin )
#admin.site.unregister(Group)

# Register your models here.
