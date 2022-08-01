from django.contrib import admin
from currency.models import Rate, ContactUs, Source
from rangefilter.filters import DateTimeRangeFilter


class RateAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'base_currency_type',
        'currency_type',
        'sale',
        'buy',
    )

    readonly_fields = (
        'base_currency_type',
        'currency_type',
        'sale',
        'buy',
        'source',
    )
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_create_permission(self, request, obj=None):
        return False
    search_fields = (
        'id',
        'base_currency_type',
        'currency_type',
        'sale',
        'buy',
    )
    list_filter = (
        'base_currency_type',
        ('created', DateTimeRangeFilter),
    )

class ContactUsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'email_to',
        'subject',
    )

    readonly_fields = (
        'email_from',
        'email_to',
        'subject',
        'message',
    )
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_create_permission(self, request, obj=None):
        return False
    search_fields = (
        'id',
        'email_from',
        'email_to',
        'subject',
        'message',
    )
    list_filter = (
        ('sent', DateTimeRangeFilter),
    )

class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source',
        'name',
        'theme',
        'price',
    )
    readonly_fields = (
        'source',
        'name',
        'theme',
        'price',
    )

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_create_permission(self, request, obj=None):
        return False

    search_fields = (
        'id',
        'source',
        'name',
        'theme',
        'price',
    )


admin.site.register(Rate, RateAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Source, SourceAdmin)