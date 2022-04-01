from django.contrib import admin
# from .models import add_account
# from .models import dep_amount
from .models import Contact


# Register your models here.
# @admin.register(add_account)
# @admin.register(dep_amount)
admin.register(Contact)



# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id_no','name','fathers_name','address']

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id_no','name','amount'
