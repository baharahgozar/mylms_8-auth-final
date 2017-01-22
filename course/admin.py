from django.contrib import admin
from course.models import Department, Course, UserEnrollment


class DeparmentAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CourseAdmin(admin.ModelAdmin):
    list_display=('code', 'title', )
    search_fields = ('code',)
    list_filter = ('code',)


class UserEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', )

admin.site .register(Department, DeparmentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(UserEnrollment, UserEnrollmentAdmin)