from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .enums import ActionType, ComplaintType, UserRole
from .models import (Company, Complaint, ComplaintDecision, ComplaintStatus,
                     Producer, User)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'surname',
                    'role', 'last_activity', 'is_active']
    list_filter = ['role', 'is_active', 'last_activity']
    search_fields = ['email', 'first_name', 'surname']
    ordering = ['email']
    exclude = ['signature', 'last_activity']

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
         'fields': ('first_name', 'surname', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {
         'fields': ('last_login', 'date_joined')}),
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


@admin.register(ComplaintDecision)
class ComplaintDecisionAdmin(admin.ModelAdmin):
    list_display = ['label']
    search_fields = ['label']
    ordering = ['label']


@admin.register(ComplaintStatus)
class ComplaintStatusAdmin(admin.ModelAdmin):
    list_display = ['label']
    search_fields = ['label']
    ordering = ['label']


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['number', 'type', 'status', 'barcode',
                    'quantity_of_good', 'registration_unit', 'submit_date']
    list_filter = ['type', 'status', 'submit_date']
    search_fields = ['number']
    ordering = ['-submit_date']
    date_hierarchy = 'submit_date'
    list_editable = ['status']  # Allow quick status changes from list view

    def get_fieldsets(self, request, obj=None):
        if obj is None:  # Creating a new complaint
            return (
                (None, {
                    'fields': ('number', 'date_of_purchase', 'type')
                }),
                ('Product Information', {
                    'fields': ('barcode', 'quantity_of_good', 'registration_unit')
                }),
                ('Details', {
                    'fields': ('description', 'demand')
                }),
            )
        else:  # Editing an existing complaint
            return (
                (None, {
                    'fields': ('number', 'type', 'status', 'submit_date', 'exit_date')
                }),
                ('Product Information', {
                    'fields': ('barcode', 'quantity_of_good', 'registration_unit')
                }),
                ('Details', {
                    'fields': ('description', 'demand')
                }),
            )
