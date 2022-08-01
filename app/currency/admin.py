from django.contrib import admin
from currency.models import Rate, ContactUs, Source
from rangefilter.filters import DateTimeRangeFilter

from import_export.admin import ImportExportModelAdmin
from import_export import resources


class RateResource(resources.ModelResource):

    class Meta:
        model = Rate
        fields = (
            'id',
            'base_currency_type',
            'currency_type',
            'sale',
            'buy',
            'source',
        )
        export_order = (
            'id',
            'base_currency_type',
            'currency_type',
            'sale',
            'buy',
            'source',
        )


class ContactUsResource(resources.ModelResource):

    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'email_to',
            'subject',
            'message',
        )
        export_order = (
            'id',
            'email_from',
            'email_to',
            'subject',
            'message',
        )


class SourceResource(resources.ModelResource):

    class Meta:
        model = Source
        fields = (
            'id',
            'source',
            'name',
            'theme',
        )
        export_order = (
            'id',
            'source',
            'name',
            'theme',
        )


class RateAdmin(ImportExportModelAdmin):
    resource_class = RateResource
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


class ContactUsAdmin(ImportExportModelAdmin):
    resource_class = ContactUsResource
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


class SourceAdmin(ImportExportModelAdmin):
    resource_class = SourceResource
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
