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


admin.site.register(Client, ClientAdmin)
