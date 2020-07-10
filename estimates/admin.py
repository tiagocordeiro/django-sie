from django.contrib import admin

from .forms import EstimateFormAdmin
from .models import Estimate, EstimateItem


class EstimateItemInLine(admin.StackedInline):
    model = EstimateItem
    extra = 1


class EstimateAdmin(admin.ModelAdmin):
    list_display = ('client', 'status', 'validate', 'total')
    inlines = [
        EstimateItemInLine,
    ]
    form = EstimateFormAdmin


admin.site.register(Estimate, EstimateAdmin)
