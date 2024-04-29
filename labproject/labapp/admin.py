from django.contrib import admin

from .models import Homes,Branch,Gallery,Blog,Package,Enquery,Appointment,Contact,Testimo
# Register your models here.
class HomesAdmin(admin.ModelAdmin):
    list_display=['name','image']
admin.site.register(Homes,HomesAdmin)


class TestimoAdmin(admin.ModelAdmin):
    list_display=['name','detail','place']
admin.site.register(Testimo,TestimoAdmin)


class EnqueryAdmin(admin.ModelAdmin):
    list_display=['names','email','number','message']
admin.site.register(Enquery,EnqueryAdmin)   



class AppointmentAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','date','time','age','gender','address','message']
admin.site.register(Appointment,AppointmentAdmin) 



class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','subject','message']
admin.site.register(Contact,ContactAdmin) 


class BranchAdmin(admin.ModelAdmin):
    list_display=['image','name']
admin.site.register(Branch,BranchAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display=['image']
admin.site.register(Gallery,GalleryAdmin)



class BlogAdmin(admin.ModelAdmin):
    list_display=['image','name']
admin.site.register(Blog,BlogAdmin)



class PackageAdmin(admin.ModelAdmin):
    list_display=['image','price','name','ln1','ln2','ln3','ln4','ln5','ln6','ln7','ln8','ln9','ln10','ln11','ln12','ln13']
admin.site.register(Package,PackageAdmin)





