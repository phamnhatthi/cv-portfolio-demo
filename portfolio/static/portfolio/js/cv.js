// Language toggle functionality for CV page
document.addEventListener('DOMContentLoaded', function() {
    const langToggle = document.getElementById('langToggle');
    const viLabel = document.getElementById('vi-label');
    const enLabel = document.getElementById('en-label');
    const printButton = document.getElementById('printButton');
    
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
    
    // Print button event listener
    if (printButton) {
        printButton.addEventListener('click', function() {
            window.print();
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
        if (currentTitle.includes('CV')) {
            document.title = currentTitle.replace('CV', 'Resume');
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
            document.title = currentTitle.replace('Resume', 'CV');
        }
    }
    
    // Print preparation
    window.addEventListener('beforeprint', function() {
        // Any specific print preparation can go here
        console.log('Preparing for print...');
    });
    
    window.addEventListener('afterprint', function() {
        // Any cleanup after print can go here
        console.log('Print completed or cancelled');
    });
});
