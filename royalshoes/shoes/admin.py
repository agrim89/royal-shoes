from django.contrib import admin
from .models import Registration, ShoeList, CompanyList, AddToCart, CompanyBanner


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email')


class CompanyBannerAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ShoeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'company')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name',)


class AddToCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'shoe', 'items')


admin.site.register(Registration, RegisterAdmin)
admin.site.register(ShoeList, ShoeAdmin)
admin.site.register(CompanyList, CompanyAdmin)
admin.site.register(AddToCart, AddToCartAdmin)
admin.site.register(CompanyBanner, CompanyBannerAdmin)