// Language toggle functionality for Home page
document.addEventListener('DOMContentLoaded', function() {
    const langToggle = document.getElementById('langToggle');
    const viLabel = document.getElementById('vi-label');
    const enLabel = document.getElementById('en-label');
    
    // Load saved language preference
    const savedLang = localStorage.getItem('cvLanguage') || 'vi';
    if (savedLang === 'en') {
        switchToEnglish();
    }
    
    // Language toggle event listener
    if (langToggle) {
        langToggle.addEventListener('click', function() {
            const isEnglish = document.body.classList.contains('english');
            if (isEnglish) {
                switchToVietnamese();
            } else {
                switchToEnglish();
            }
        });
    }
    
    function switchToEnglish() {
        document.body.classList.add('english');
        if (langToggle) langToggle.classList.add('active');
        if (viLabel) viLabel.classList.remove('active');
        if (enLabel) enLabel.classList.add('active');
        localStorage.setItem('cvLanguage', 'en');
        
        // Update page title
        const currentTitle = document.title;
        if (currentTitle.includes('Portfolio')) {
            document.title = currentTitle.replace('Portfolio', 'Resume');
        }
    }
    
    function switchToVietnamese() {
        document.body.classList.remove('english');
        if (langToggle) langToggle.classList.remove('active');
        if (viLabel) viLabel.classList.add('active');
        if (enLabel) enLabel.classList.remove('active');
        localStorage.setItem('cvLanguage', 'vi');
        
        // Update page title
        const currentTitle = document.title;
        if (currentTitle.includes('Resume')) {
            document.title = currentTitle.replace('Resume', 'Portfolio');
        }
    }
    
    // Smooth scrolling for internal links (if any)
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add hover effects to contact items
    const contactItems = document.querySelectorAll('.contact-item');
    contactItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});
