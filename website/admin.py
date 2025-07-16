from django.contrib import admin
from .models import Course, Consultancy, Events, Services, User,  SliderImage
# Register your models here.


admin.site.register(User),

admin.site.register(Course),

admin.site.register(Consultancy),

admin.site.register(Services),

admin.site.register(Events),

admin.site.register(SliderImage),



