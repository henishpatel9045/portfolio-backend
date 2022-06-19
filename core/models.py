from django.db import models
from django.core.validators import MinValueValidator
from ckeditor.fields import RichTextField

# Create your models here.

class SiteInfo(models.Model):
    name = models.CharField(max_length=50)
    profile_1 = models.ImageField(upload_to="site")
    profile_2 = models.ImageField(upload_to="site")
    resume = models.FileField(upload_to="site")
    experience = models.IntegerField(validators=[MinValueValidator(0, "Value can't be negative")])
    clients = models.IntegerField(validators=[MinValueValidator(0, "Value can't be negative")])
    projects = models.IntegerField(validators=[MinValueValidator(0, "Value can't be negative")])
    about_us = RichTextField()
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    gmail = models.EmailField()
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Site Info"
              
    

class Designation(models.Model):
    post = models.CharField(max_length=150)
    site = models.ForeignKey(SiteInfo , on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post
    
class SkillSection(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date_created']
        verbose_name_plural = "Skill Section"
        
    
class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        ("B", 'Beginner'),
        ("I", 'Intermediate'),
        ("A", 'Advanced'),
    ]
    skill_name = models.CharField(max_length=150)
    proficiency = models.CharField(
        max_length=2,
        choices=PROFICIENCY_CHOICES,
        default="B"
    )
    skill_section = models.ForeignKey(SkillSection, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.skill_section) + " - " + self.skill_name
    
class ServiceSection(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date_created'] 
        verbose_name_plural = "Services Section"   
        
class Service(models.Model):
    title = models.CharField(max_length=400)
    service_section = models.ForeignKey(ServiceSection, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.service_section)
     
class Project(models.Model):
    title = models.CharField(max_length=150)
    photo = models.ImageField(upload_to="projects")
    github_repo = models.URLField()    
    live_link = models.URLField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date_created']
        verbose_name_plural = "Projects"    
    
    
class ContactMe(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["date_created"]
        verbose_name_plural = "Messages"