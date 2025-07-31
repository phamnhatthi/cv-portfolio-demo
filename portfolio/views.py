from django.shortcuts import render, get_object_or_404
from .models import Profile, Experience, Education, Skill, Project


def home_view(request):
    """Home page view - Introduction for recruiters"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    # Get latest experience for quick intro
    latest_experience = Experience.objects.first() if Experience.objects.exists() else None
    
    context = {
        'profile': profile,
        'latest_experience': latest_experience,
    }
    return render(request, 'portfolio/home.html', context)


def cv_view(request):
    """CV page view"""
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    experiences = Experience.objects.all()
    education = Education.objects.all()
    
    # Group skills by category with Vietnamese/English labels
    skills_by_category = {}
    skills = Skill.objects.all()
    
    # Category translations
    category_translations = {
        'technical': {'vi': 'Kỹ năng Kỹ thuật', 'en': 'Technical Skills'},
        'programming': {'vi': 'Ngôn ngữ Lập trình', 'en': 'Programming Languages'},
        'tools': {'vi': 'Công cụ & Công nghệ', 'en': 'Tools & Technologies'},
        'soft': {'vi': 'Kỹ năng Mềm', 'en': 'Soft Skills'},
        'languages': {'vi': 'Ngôn ngữ', 'en': 'Languages'},
    }
    
    for skill in skills:
        category_key = skill.category
        if category_key not in skills_by_category:
            skills_by_category[category_key] = {
                'vi': category_translations.get(category_key, {}).get('vi', skill.get_category_display()),
                'en': category_translations.get(category_key, {}).get('en', skill.get_category_display()),
                'skills': []
            }
        skills_by_category[category_key]['skills'].append(skill)
    
    context = {
        'profile': profile,
        'experiences': experiences,
        'education': education,
        'skills_by_category': skills_by_category,
    }
    return render(request, 'portfolio/cv.html', context)


def projects_view(request):
    """Projects page view - Display all projects with videos and details"""
    projects = Project.objects.all()
    featured_projects = projects.filter(is_featured=True)
    regular_projects = projects.filter(is_featured=False)
    
    context = {
        'projects': projects,
        'featured_projects': featured_projects,
        'regular_projects': regular_projects,
        'page_title': 'Dự án đã thực hiện',
        'page_title_en': 'Completed Projects',
    }
    return render(request, 'portfolio/projects.html', context)


def project_detail_view(request, project_id):
    """Individual project detail view"""
    project = get_object_or_404(Project, id=project_id)
    
    context = {
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', context)
