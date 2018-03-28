from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
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


class RoyalShoesAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Royal Shoes Admin')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Royal Shoes administration')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Royal Shoes administration')


admin_site = RoyalShoesAdminSite()

admin_site.register(Registration, RegisterAdmin)
admin_site.register(ShoeList, ShoeAdmin)
admin_site.register(CompanyList, CompanyAdmin)
admin_site.register(AddToCart, AddToCartAdmin)
admin_site.register(CompanyBanner, CompanyBannerAdmin)