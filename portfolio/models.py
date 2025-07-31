from django.db import models


class Profile(models.Model):
    """Model for personal profile information"""
    full_name = models.CharField(max_length=100)
    full_name_en = models.CharField(max_length=100, blank=True, help_text="English name")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    address_en = models.CharField(max_length=200, blank=True, help_text="English address")
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    website = models.URLField(blank=True)
    professional_summary = models.TextField()
    professional_summary_en = models.TextField(blank=True, help_text="English professional summary")
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    
    def __str__(self):
        return self.full_name


class Experience(models.Model):
    """Model for work experience"""
    job_title = models.CharField(max_length=100)
    job_title_en = models.CharField(max_length=100, blank=True, help_text="English job title")
    company = models.CharField(max_length=100)
    company_en = models.CharField(max_length=100, blank=True, help_text="English company name")
    location = models.CharField(max_length=100)
    location_en = models.CharField(max_length=100, blank=True, help_text="English location")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    description_en = models.TextField(blank=True, help_text="English description")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Education(models.Model):
    """Model for educational background"""
    degree = models.CharField(max_length=100)
    degree_en = models.CharField(max_length=100, blank=True, help_text="English degree")
    institution = models.CharField(max_length=100)
    institution_en = models.CharField(max_length=100, blank=True, help_text="English institution")
    location = models.CharField(max_length=100)
    location_en = models.CharField(max_length=100, blank=True, help_text="English location")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    gpa = models.CharField(max_length=10, blank=True)
    description = models.TextField(blank=True)
    description_en = models.TextField(blank=True, help_text="English description")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Skill(models.Model):
    """Model for skills"""
    SKILL_CATEGORIES = [
        ('technical', 'Technical Skills'),
        ('programming', 'Programming Languages'),
        ('tools', 'Tools & Technologies'),
        ('soft', 'Soft Skills'),
        ('languages', 'Languages'),
    ]
    
    name = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50, blank=True, help_text="English skill name")
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    proficiency_level = models.IntegerField(default=5, help_text="Scale of 1-10")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(max_length=200, verbose_name="Project Title")
    title_en = models.CharField(max_length=200, blank=True, help_text="English project title")
    
    description = models.TextField(verbose_name="Project Description")
    description_en = models.TextField(blank=True, help_text="English project description")
    
    # Video field for project demonstration
    video = models.FileField(upload_to='project_videos/', blank=True, null=True, 
                           help_text="Upload MP4 video file of the project")
    
    # Technologies and libraries used
    technologies = models.TextField(help_text="List technologies, frameworks, and libraries used (comma separated)")
    technologies_en = models.TextField(blank=True, help_text="English technologies list")
    
    # Project links
    github_url = models.URLField(blank=True, verbose_name="GitHub Repository")
    live_demo_url = models.URLField(blank=True, verbose_name="Live Demo URL")
    
    # Project thumbnail/image
    thumbnail = models.ImageField(upload_to='project_thumbnails/', blank=True, null=True,
                                help_text="Project thumbnail image")
    
    # Project dates
    start_date = models.DateField(verbose_name="Project Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="Project End Date")
    is_ongoing = models.BooleanField(default=False, verbose_name="Is this project ongoing?")
    
    # Project status and display order
    is_featured = models.BooleanField(default=False, help_text="Show this project prominently")
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_featured', 'order', '-start_date']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.title
    
    @property
    def technology_list(self):
        """Return technologies as a list"""
        return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
    
    @property
    def technology_list_en(self):
        """Return English technologies as a list"""
        if self.technologies_en:
            return [tech.strip() for tech in self.technologies_en.split(',') if tech.strip()]
        return self.technology_list
