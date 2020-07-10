from django.contrib import admin

from .models import Contact, Client


class ContactInLine(admin.StackedInline):
    model = Contact
    extra = 1


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    inlines = [
        ContactInLine,
    ]


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'mobile', 'client')


admin.site.register(Client, ClientAdmin)
admin.site.register(Contact, ContactAdmin)
