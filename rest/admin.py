from django.contrib import admin
from .models import School, Coach

class CoachAdmin(admin.ModelAdmin):

	list_display = ('short_name', 'name', 'position', 'imageUrl')
	#list_display_links = ('short_name', 'name', 'position', 'imageUrl')
	search_fields = ('short_name', 'name')

class SchoolAdmin(admin.ModelAdmin): 

	list_display = ('name', 'description', 'place', 'startTime', 'endTime', 'weekDay', 'teacher_v2', 'color')
	#list_display_links = ('name', 'description', 'place', 'startTime', 'endTime', 'weekDay', 'teacher', 'color')
	search_fields = ('name',)
	prepopulated_fields = {'teacher': ('teacher_v2',)}



admin.site.register(School, SchoolAdmin)
admin.site.register(Coach, CoachAdmin)

