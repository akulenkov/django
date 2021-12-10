from django.contrib import admin

from .models import Emp

admin.site.register(Emp)

from .models import Projects

from .models import JoinProj

admin.site.register(JoinProj)



# Register your models here.


# admin.site.register(Bb)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'volume')
    list_display_links = ('name', 'start_date')
    search_fields = ('name', 'start_date', 'end_date', 'volume')

admin.site.register(Projects, ProjectsAdmin)

# Register your models here.
