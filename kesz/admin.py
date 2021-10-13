from django.contrib import admin

from . models import (
    Person,
    Country,
    Phone,
    Email,
    Address,
    Organization,
    Position)


admin.site.register(Person)
admin.site.register(Country)
admin.site.register(Phone)
admin.site.register(Email)
admin.site.register(Address)
admin.site.register(Organization)
admin.site.register(Position)

