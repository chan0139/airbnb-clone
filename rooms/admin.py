from django.contrib import admin
from django_countries.fields import Country
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
    

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Time",
            {"fields": ("check_in", "check_out", "instant_book")},
        ),
        (
            "Spaces",
            {"fields": ("guests", "beds", "bedrooms", "bathrooms")},
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
        "bathrooms",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos"
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
        

    count_amenities.short_desctription = "count_amenity"

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

