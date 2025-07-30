from django.db import models
from django.urls import reverse

class Profile(models.Model):
    """Model cho thông tin cá nhân"""
    full_name = models.CharField(max_length=100, verbose_name="Họ và tên")
    title = models.CharField(max_length=100, verbose_name="Chức danh")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Số điện thoại")
    address = models.TextField(verbose_name="Địa chỉ")
    about = models.TextField(verbose_name="Giới thiệu")
    profile_image = models.ImageField(upload_to='profile/', verbose_name="Ảnh đại diện", blank=True)
    linkedin = models.URLField(blank=True, verbose_name="LinkedIn")
    github = models.URLField(blank=True, verbose_name="GitHub")
    website = models.URLField(blank=True, verbose_name="Website")
    
    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = "Hồ sơ"
        verbose_name_plural = "Hồ sơ"

class Skill(models.Model):
    """Model cho kỹ năng"""
    SKILL_LEVELS = [
        ('beginner', 'Mới bắt đầu'),
        ('intermediate', 'Trung cấp'),
        ('advanced', 'Nâng cao'),
        ('expert', 'Chuyên gia'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Tên kỹ năng")
    level = models.CharField(max_length=20, choices=SKILL_LEVELS, verbose_name="Trình độ")
    percentage = models.IntegerField(default=0, verbose_name="Phần trăm thành thạo")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Kỹ năng"
        verbose_name_plural = "Kỹ năng"

class Experience(models.Model):
    """Model cho kinh nghiệm làm việc"""
    company = models.CharField(max_length=100, verbose_name="Công ty")
    position = models.CharField(max_length=100, verbose_name="Vị trí")
    start_date = models.DateField(verbose_name="Ngày bắt đầu")
    end_date = models.DateField(null=True, blank=True, verbose_name="Ngày kết thúc")
    description = models.TextField(verbose_name="Mô tả công việc")
    is_current = models.BooleanField(default=False, verbose_name="Hiện tại")
    
    def __str__(self):
        return f"{self.position} tại {self.company}"
    
    class Meta:
        verbose_name = "Kinh nghiệm"
        verbose_name_plural = "Kinh nghiệm"
        ordering = ['-start_date']

class Education(models.Model):
    """Model cho học vấn"""
    institution = models.CharField(max_length=100, verbose_name="Trường")
    degree = models.CharField(max_length=100, verbose_name="Bằng cấp")
    field_of_study = models.CharField(max_length=100, verbose_name="Chuyên ngành")
    start_date = models.DateField(verbose_name="Ngày bắt đầu")
    end_date = models.DateField(null=True, blank=True, verbose_name="Ngày kết thúc")
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, verbose_name="GPA")
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"
    
    class Meta:
        verbose_name = "Học vấn"
        verbose_name_plural = "Học vấn"
        ordering = ['-start_date']

class Project(models.Model):
    """Model cho dự án"""
    PROJECT_TYPES = [
        ('web', 'Web Application'),
        ('mobile', 'Mobile App'),
        ('desktop', 'Desktop App'),
        ('ai', 'AI/Machine Learning'),
        ('game', 'Game'),
        ('other', 'Khác'),
    ]
    
    title = models.CharField(max_length=100, verbose_name="Tên dự án")
    description = models.TextField(verbose_name="Mô tả dự án")
    technologies = models.TextField(verbose_name="Công nghệ sử dụng")
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, verbose_name="Loại dự án")
    image = models.ImageField(upload_to='projects/', verbose_name="Hình ảnh", blank=True)
    video = models.FileField(upload_to='projects/videos/', verbose_name="Video demo", blank=True)
    github_url = models.URLField(blank=True, verbose_name="GitHub URL")
    demo_url = models.URLField(blank=True, verbose_name="Demo URL")
    created_date = models.DateField(verbose_name="Ngày tạo")
    featured = models.BooleanField(default=False, verbose_name="Dự án nổi bật")
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = "Dự án"
        verbose_name_plural = "Dự án"
        ordering = ['-created_date']

class ProjectImage(models.Model):
    """Model cho ảnh bổ sung của dự án"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='projects/gallery/')
    caption = models.CharField(max_length=200, blank=True, verbose_name="Chú thích")
    
    def __str__(self):
        return f"Ảnh cho {self.project.title}"
    
    class Meta:
        verbose_name = "Ảnh dự án"
        verbose_name_plural = "Ảnh dự án"

class Contact(models.Model):
    """Model cho tin nhắn liên hệ"""
    name = models.CharField(max_length=100, verbose_name="Tên")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Chủ đề")
    message = models.TextField(verbose_name="Tin nhắn")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Thời gian gửi")
    
    def __str__(self):
        return f"Tin nhắn từ {self.name}"
    
    class Meta:
        verbose_name = "Liên hệ"
        verbose_name_plural = "Liên hệ"
        ordering = ['-created_at']
