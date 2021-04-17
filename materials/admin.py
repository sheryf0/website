from django.contrib import admin
from .models import course, handout , book, past_question, syllabus

# Register your models here.


class course_Admin (admin.ModelAdmin):
    list_display = ('course_name',)
    search_fields = ( 'group_id','course_name', 'course_code')
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


class handout_Admin (admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ( 'course', 'name',)
    filter_horizontal = ()
    list_filter = ('name', 'course')
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("name", "course"),
        }),
    )

    ordering = ('course',)


class book_Admin (admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ( 'course', 'name',)
    filter_horizontal = ()
    list_filter = ('name', 'course')
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("name", "course"),
        }),
    )

    ordering = ('course',)


class pastQuestion_Admin (admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ( 'course', 'name',)
    filter_horizontal = ()
    list_filter = ('name', 'course')
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("name", "course"),
        }),
    )

    ordering = ('course',)

class syllabus_Admin (admin.ModelAdmin):
    list_display = ('name', 'course')
    search_fields = ( 'course', 'name',)
    filter_horizontal = ()
    list_filter = ('name', 'course')
    fieldsets = ()

    add_fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': ("name", "course"),
        }),
    )

    ordering = ('course',)
admin.site.register(course, course_Admin)
admin.site.register(handout, handout_Admin)
admin.site.register(book, book_Admin)
admin.site.register(past_question, pastQuestion_Admin)
admin.site.register(syllabus, syllabus_Admin)

