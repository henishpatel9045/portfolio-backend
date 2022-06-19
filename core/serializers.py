from dataclasses import fields
from multiprocessing import context
from rest_framework import serializers
from . import models

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = ["post"]

class SiteInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SiteInfo
        fields = "__all__"
    des = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    projects_detail = serializers.SerializerMethodField()
    
    def get_des(self, obj):
        return DesignationSerializer(models.Designation.objects.all(), many=True).data
    
    def get_skills(self, obj):
        return SkillSectionSerializer(models.SkillSection.objects.all(), many=True).data
    
    def get_services(self, obj):
        return ServiceSectionSerializer(models.ServiceSection.objects.all(), many=True).data
    
    def get_projects_detail(self, obj):
        return ProjectSerializer(models.Project.objects.all(), many=True, context={'request': self.context.get('request')}).data


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ["skill_name", "proficiency"]

class SkillSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SkillSection
        fields = "__all__"
    skills = serializers.SerializerMethodField()
    def get_skills(self, obj):
        return SkillSerializer(models.Skill.objects.filter(skill_section=obj.id), many=True).data

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Service
        fields = ["title"]

class ServiceSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceSection
        fields = "__all__"
    services = serializers.SerializerMethodField()
    def get_services(self, obj):
        return ServiceSerializer(models.Service.objects.filter(service_section=obj.id), many=True).data
        
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = "__all__"
        
    photo = serializers.SerializerMethodField()
    
    def get_photo(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.photo.url)
    
        
class ContactMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactMe
        fields = "__all__"
        
                