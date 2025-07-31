// Language toggle functionality for Projects page
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
        if (currentTitle.includes('Projects')) {
            document.title = currentTitle.replace('Projects', 'Projects');
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
        if (currentTitle.includes('Projects')) {
            document.title = currentTitle.replace('Projects', 'Dự Án');
        }
    }
    
    // Add hover animations to navigation buttons
    const navButtons = document.querySelectorAll('.nav-btn');
    navButtons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-3px) scale(1.02)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
    
    // Add click animation to coming soon card
    const comingSoonCard = document.querySelector('.coming-soon-card');
    if (comingSoonCard) {
        comingSoonCard.addEventListener('click', function() {
            this.style.transform = 'scale(0.98)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    }
});
