from django.contrib import admin
from .models import Specialservice
from .models import Team
from .models import Skill
from .models import Category
from .models import Option
from .models import Service




class SpecialserviceAdmn(admin.ModelAdmin):
    list_display = ['title' , 'status']
    list_filter = ['status']
    search_fields = ['title']
    # fields = ['title' , 'content']


admin.site.register(Specialservice , SpecialserviceAdmn)
admin.site.register(Team)
admin.site.register(Skill)
admin.site.register(Category)
admin.site.register(Option)
admin.site.register(Service)

# Register your models here.
