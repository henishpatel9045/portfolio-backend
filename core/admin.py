from django.contrib import admin
from . import models

admin.site.site_header = "Portfolio Administrator"
admin.site.index_title = "Dashboard"

class DesignationInline(admin.TabularInline):
    model = models.Designation
    fields = ["post"]
    min_num = 1
    max_num = 10
    extra = 0   

# Register your models here.
@admin.register(models.SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "date_created", "last_update"]
    inlines = [DesignationInline]
    
    
class SkillInline(admin.TabularInline):
    model = models.Skill
    fields = ["skill_name", "proficiency"]
    min_num = 1
    extra = 0
    
@admin.register(models.SkillSection)
class SkillSectionAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "date_created", "total_skill"]
    inlines = [SkillInline]
    search_fields = ["title"]
    
    def total_skill(self, obj):
        return models.Skill.objects.filter(skill_section=obj.id).count()

    
class ServiceInline(admin.TabularInline):
    model =models.Service
    fields = ["title"]
    min_num = 1
    extra = 0

@admin.register(models.ServiceSection)
class ServiceSectionAdmin(admin.ModelAdmin):
    list_display = ["title", "date_created", "total_services"]
    inlines = [ServiceInline]
    search_fields = ["title"]

    def total_services(self, obj):
        return models.Service.objects.filter(service_section=obj.id).count()

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "date_created", "last_updated"]
    search_fields = ["title"]
    

@admin.register(models.ContactMe)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "date_created"]
    search_fields = ["name", "message", "email"]
    readonly_fields = ["name", "message", "email"]
    