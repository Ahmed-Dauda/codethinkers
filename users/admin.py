from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import Profile
from users.models import NewUser
from quiz.models import Course, Question, Result
from student.models import Student
# from django.contrib.auth import get_user_model
# User = get_user_model()

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email','username', 'password','countries', 'phone_number','last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            'groups', 
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username','first_name','last_name','email','countries','phone_number' ,'password1', 'password2')
            }
        ),
    )

    list_display = ('username','first_name','last_name', 'email','countries', 'phone_number', 'last_login')
    list_filter = ( 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(NewUser, UserAdmin)
admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Result)
# admin.site.register(Student)
