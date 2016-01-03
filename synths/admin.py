from django.contrib import admin
from synths.models import Synth

class SynthAdmin(admin.ModelAdmin):
    model = Synth
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Synth, SynthAdmin)
