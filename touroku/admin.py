from django.contrib import admin
from .forms import TourokuForm
from .models import Kansuu


class KansuuAdmin(admin.ModelAdmin):
    pass
admin.site.register(Kansuu, KansuuAdmin)
