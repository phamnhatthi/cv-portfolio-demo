from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Profile, Skill, Experience, Education, Project, Contact
from .forms import ContactForm

def home(request):
    """Trang chủ - CV chính"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    skills = Skill.objects.all()
    experiences = Experience.objects.all()[:3]  # Hiển thị 3 kinh nghiệm gần nhất
    education = Education.objects.all()[:3]  # Hiển thị 3 học vấn gần nhất
    featured_projects = Project.objects.filter(featured=True)[:4]  # 4 dự án nổi bật
    
    context = {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'education': education,
        'featured_projects': featured_projects,
    }
    return render(request, 'portfolio/home.html', context)

def projects(request):
    """Trang danh sách tất cả dự án"""
    project_list = Project.objects.all()
    project_type = request.GET.get('type')
    
    if project_type:
        project_list = project_list.filter(project_type=project_type)
    
    # Phân trang
    paginator = Paginator(project_list, 6)  # 6 dự án mỗi trang
    page_number = request.GET.get('page')
    projects_page = paginator.get_page(page_number)
    
    # Lấy danh sách loại dự án để filter
    project_types = Project.PROJECT_TYPES
    
    context = {
        'projects': projects_page,
        'project_types': project_types,
        'current_type': project_type,
    }
    return render(request, 'portfolio/projects.html', context)

def project_detail(request, pk):
    """Trang chi tiết dự án"""
    project = get_object_or_404(Project, pk=pk)
    
    # Lấy các dự án liên quan (cùng loại, trừ dự án hiện tại)
    related_projects = Project.objects.filter(
        project_type=project.project_type
    ).exclude(pk=pk)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'portfolio/project_detail.html', context)

def contact(request):
    """Trang liên hệ"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cảm ơn bạn đã liên hệ! Tôi sẽ phản hồi sớm nhất có thể.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'portfolio/contact.html', context)

def about(request):
    """Trang giới thiệu chi tiết"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    
    context = {
        'profile': profile,
        'skills': skills,
        'experiences': experiences,
        'education': education,
    }
    return render(request, 'portfolio/about.html', context)

def ajax_contact(request):
    """AJAX endpoint cho form liên hệ"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'success': True, 
                'message': 'Cảm ơn bạn đã liên hệ! Tôi sẽ phản hồi sớm nhất có thể.'
            })
        else:
            return JsonResponse({
                'success': False, 
                'errors': form.errors
            })
    return JsonResponse({'success': False, 'message': 'Invalid request'})
