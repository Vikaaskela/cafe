from django.contrib import admin
from .models import DishCategory, Dish, Event, Gallery, Booking

admin.site.register(DishCategory)
admin.site.register(Dish)
admin.site.register(Event)
admin.site.register(Gallery)
admin.site.register(Booking)

