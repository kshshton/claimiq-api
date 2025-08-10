from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import ActionHistory, Company, Complaint, Producer, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'surname',
                    'role', 'last_activity', 'is_active']
    list_filter = ['role', 'is_active', 'last_activity']
    search_fields = ['email', 'first_name', 'surname']
    ordering = ['email']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
         'fields': ('first_name', 'surname', 'signature', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {
         'fields': ('last_login', 'date_joined', 'last_activity')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'surname', 'password1', 'password2', 'role'),
        }),
    )


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'nip', 'town', 'email', 'phone_number']
    list_filter = ['town']
    search_fields = ['company_name', 'nip', 'email']
    ordering = ['company_name']


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['number', 'type', 'status', 'submit_date', 'exit_date']
    list_filter = ['type', 'status', 'submit_date']
    search_fields = ['number']
    ordering = ['-submit_date']
    date_hierarchy = 'submit_date'


@admin.register(ActionHistory)
class ActionHistoryAdmin(admin.ModelAdmin):
    list_display = ['action', 'email', 'date', 'details']
    list_filter = ['action', 'date', 'email']
    search_fields = ['email__email', 'details']
    ordering = ['-date']
    date_hierarchy = 'date'
