from django.contrib import admin

from .models import *


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'title', 'date']

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', 'title', 'date']
