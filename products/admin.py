from django.contrib import admin
from .models import featuredproducts,ringsdatabase,necklessdatabase,braceletsdatabase,jewellarydatabase,earingsdatabase,message,reviewdatabase
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html

# Register your models here.


class featuredproductAdmin(admin.ModelAdmin):
    model=featuredproducts
    list_display=['name','price','image','summary','image_display']
    def image_display(self, obj):
        return format_html('<img src="/media/{0}" style="width: 200px; \
                           height: 250px"/>'.format(obj.image))
    image_display.short_descripition = "image_display"
admin.site.register(featuredproducts,featuredproductAdmin)

# class ringsAdmin(admin.ModelAdmin):
#     model=ringsdatabase
#     list_display=['name','price','image','summary','image_display']
#     def image_display(self, obj):
#         return format_html('<img src="/media/{0}" style="width: 130px; \
#                           height: 100px"/>'.format(obj.image))
#     image_display.short_descripition = "image_display"
# admin.site.register(ringsdatabase,ringsAdmin)

class necklessAdmin(admin.ModelAdmin):
    model=necklessdatabase
    list_display=['name','price','image','summary','image_display']
    def image_display(self, obj):
        return format_html('<img src="/media/{0}" style="width: 200px; \
                           height: 250px"/>'.format(obj.image))
    image_display.short_descripition = "image_display"
admin.site.register(necklessdatabase,necklessAdmin)

class braceletsAdmin(admin.ModelAdmin):
    model=braceletsdatabase
    list_display=['name','price','image','summary','image_display']
    def image_display(self, obj):
        return format_html('<img src="/media/{0}" style="width: 200px; \
                           height: 250px"/>'.format(obj.image))
    image_display.short_descripition = "image_display"
admin.site.register(braceletsdatabase,braceletsAdmin)

# class jewellaryAdmin(admin.ModelAdmin):
#     model=jewellarydatabase
#     list_display=['name','price','image','summary','image_display']
#     def image_display(self, obj):
#         return format_html('<img src="/media/{0}" style="width: 130px; \
#                           height: 100px"/>'.format(obj.image))
#     image_display.short_descripition = "image_display"
# admin.site.register(jewellarydatabase,jewellaryAdmin)

class earingAdmin(admin.ModelAdmin):
    model=earingsdatabase
    list_display=['name','price','image','summary','image_display']
    def image_display(self, obj):
        return format_html('<img src="/media/{0}" style="width: 200px; \
                           height: 250px"/>'.format(obj.image))
    image_display.short_descripition = "image_display"
admin.site.register(earingsdatabase,earingAdmin)


class messageAdmin(admin.ModelAdmin):
    model=message
    list_display=['name','email','phone','message']
admin.site.register(message,messageAdmin)

class reviewAdmin(admin.ModelAdmin):
    model=reviewdatabase
    list_display=['name','review','star' ,'code','time']
admin.site.register(reviewdatabase,reviewAdmin)
