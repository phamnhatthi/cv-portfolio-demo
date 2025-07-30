from django.contrib import admin
from .models import Profile, Skill, Experience, Education, Project, ProjectImage, Contact

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'title', 'email']
    search_fields = ['full_name', 'email']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'percentage']
    list_filter = ['level']
    search_fields = ['name']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'start_date']
    search_fields = ['position', 'company']
    date_hierarchy = 'start_date'

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'field_of_study', 'start_date', 'end_date']
    list_filter = ['degree', 'start_date']
    search_fields = ['institution', 'degree', 'field_of_study']
    date_hierarchy = 'start_date'

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'created_date', 'featured']
    list_filter = ['project_type', 'featured', 'created_date']
    search_fields = ['title', 'description', 'technologies']
    date_hierarchy = 'created_date'
    inlines = [ProjectImageInline]
    
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('title', 'description', 'project_type', 'technologies')
        }),
        ('Media', {
            'fields': ('image', 'video')
        }),
        ('Liên kết', {
            'fields': ('github_url', 'demo_url')
        }),
        ('Khác', {
            'fields': ('created_date', 'featured')
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
