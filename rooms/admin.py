from django.contrib import admin
from django_countries.fields import Country
from django.utils.html import mark_safe
from . import models
# Register your models here.

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "used_by",
    )
    def used_by(self, obj):
        return obj.rooms.count()
    
class PhotoInline(admin.TabularInline):

    model = models.Photo

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)
    
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        (
            "Time",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "baths")},
        ),
        (
            "More About the Spaces",

            {   "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules")},
        ),
        (
            "Last Details",
            {"fields": ("host",)},
        ),
    )
    list_display = (
        "name",
        "country",
        "city",
        "price",
        "address",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating"
    )

    ordering = ("name", "price", "bedrooms")
    list_filter = (
        "instant_book", 
        "host__superhost", #외래키
        "host__gender", 
        "guests",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    raw_id_fields = ("host",)

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    search_fields = ("city", "^host__username",)

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()
    count_photos.short_description = "Photo Count"
        

    count_amenities.short_description = "Amenity Count"

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition"""

    list_display = ("__str__", "get_thumnail")

    def get_thumnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumnail.short_description = "Thumnail"
