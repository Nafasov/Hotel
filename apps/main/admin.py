from django.contrib import admin

from .models import (
                        AboutUs,
                        MeContact,
                        Service,
                        Partners,
                        HomeBanner,
                                    )


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')


@admin.register(MeContact)
class MeContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'created_date')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_date')


@admin.register(HomeBanner)
class HomeBannersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date')