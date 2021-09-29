from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    ordering = ['date_joined']
    editable_list = ['is_staff']
    search_fields = ['username', 'email']
    list_filter = ['is_superuser' ,'is_staff']
    list_display=['username','full_name', 'email', 'is_staff']
    fieldsets =(
                ('User Details',{
                    'description' : 'Basic informations section',
                    'fields':[
                        'first_name', 'last_name', 'username','email','phone_number'
                        ]
                }),
                ('Dates',{
                    'fields':[
                        'date_joined', 'last_login'
                    ]
                }),
                ('Others',{
                    'fields':[
                        'is_active','is_staff','is_superuser'
                    ]
                }),
                ('Permissions & Password',{
                    'classes' : ('collapse',),
                    'fields': [
                        'password', 'groups', 'user_permissions'
                    ]
                })
        )

admin.site.register(CustomUser, CustomUserAdmin)
