from django.contrib import admin
from .models import Visitors, Orders, Bank, Employees, Intermediary


admin.site.register(Visitors)
admin.site.register(Orders)
admin.site.register(Bank)
admin.site.register(Employees)
admin.site.register(Intermediary)
