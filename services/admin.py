from django.contrib import admin
from .models import Specialservice
from .models import Team
from .models import Skills




class SpecialserviceAdmn(admin.ModelAdmin):
    list_display = ['title' , 'status']
    list_filter = ['status']
    search_fields = ['title']
    # fields = ['title' , 'content']


admin.site.register(Specialservice , SpecialserviceAdmn)
admin.site.register(Team)
admin.site.register(Skills)

# Register your models here.
