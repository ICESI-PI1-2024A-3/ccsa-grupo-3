from django.contrib import admin
from .models import Materia, Curso, Clase, Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'telephone', 'user_group')
    search_fields = ('user__username', 'user__groups__name')
    list_filter = ('user__groups',)

    def user_group(self, obj):
        return ", ".join([group.name for group in obj.user.groups.all().order_by('name')])

    user_group.short_description = 'Grupo'

admin.site.register(Materia)
admin.site.register(Curso)
admin.site.register(Clase)
admin.site.register(Profile, ProfileAdmin)
