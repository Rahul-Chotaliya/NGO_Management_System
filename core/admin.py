from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    pass


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass


@admin.register(Otp)
class OtpAdmin(admin.ModelAdmin):
    list_display = ['otp',]


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title',]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title',]
