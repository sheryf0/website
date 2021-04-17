from django.contrib import admin
from dashboard.models import lecture_update, upcoming_test, pending_assignment, important_information

# Register your models here


class Lecture_updateAdmin (admin.ModelAdmin):
    list_display = ('course_name', 'author', 'group_id')
    search_fields = ( 'group_id',)
    filter_horizontal = ()
    list_filter = ('course_name', 'group_id')
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("course_name", "group_id"),
        }),
    )

    ordering = ('group_id',)

class Upcoming_testAdmin (admin.ModelAdmin):
    list_display = ('course_name', 'author', 'group_id')
    search_fields = ( 'group_id',)
    filter_horizontal = ()
    list_filter = ('course_name', 'group_id')
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("course_name", "group_id"),
        }),
    )

    ordering = ('group_id',)

class Pending_assignmentAdmin (admin.ModelAdmin):
    list_display = ('course_name', 'author', 'group_id')
    search_fields = ( 'group_id',)
    filter_horizontal = ()
    list_filter = ('course_name', 'group_id')
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("course_name", "group_id"),
        }),
    )

    ordering = ('group_id',)


class important_informationAdmin (admin.ModelAdmin):
    list_display = ('title', 'author', 'group_id')
    search_fields = ( 'group_id',)
    filter_horizontal = ()
    list_filter = ('title', 'group_id')
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("title", "group_id"),
        }),
    )

    ordering = ('group_id',)
admin.site.register(lecture_update, Lecture_updateAdmin)
admin.site.register(upcoming_test, Upcoming_testAdmin)
admin.site.register(pending_assignment, Pending_assignmentAdmin)
admin.site.register(important_information, important_informationAdmin)
