from django.contrib import admin
from .models import Profile, Experience, Education, Skill, Project


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone']
    search_fields = ['full_name', 'email']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current', 'company']
    search_fields = ['job_title', 'company']
    ordering = ['order', '-start_date']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date', 'is_current', 'order']
    list_filter = ['is_current', 'institution']
    search_fields = ['degree', 'institution']
    ordering = ['order', '-start_date']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency_level', 'order']
    list_filter = ['category']
    search_fields = ['name']
    ordering = ['category', 'order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'is_ongoing', 'is_featured', 'order']
    list_filter = ['is_featured', 'is_ongoing', 'start_date']
    search_fields = ['title', 'description', 'technologies']
    ordering = ['-is_featured', 'order', '-start_date']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'title_en', 'description', 'description_en')
        }),
        ('Media', {
            'fields': ('video', 'thumbnail')
        }),
        ('Technologies', {
            'fields': ('technologies', 'technologies_en')
        }),
        ('Links', {
            'fields': ('github_url', 'live_demo_url')
        }),
        ('Timeline', {
            'fields': ('start_date', 'end_date', 'is_ongoing')
        }),
        ('Display Options', {
            'fields': ('is_featured', 'order')
        }),
    )
