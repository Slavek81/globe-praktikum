/**
 * Modern JavaScript for Praktické aplikace fyziky a chemie
 * Gymnázium Globe
 */

// DOM Content Loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeNavigation();
    initializeScrollEffects();
    initializeMobileMenu();
    initializeStatsAnimation();
    initializeCardAnimations();
});

/**
 * Navigation functionality
 */
function initializeNavigation() {
    // Smooth scrolling for navigation links (both main nav and quick nav)
    const navLinks = document.querySelectorAll('.nav-link, .quick-nav-item');

    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Only handle internal anchor links
            if (href && href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    const offsetTop = targetElement.offsetTop - 80; // Account for fixed header
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            }
        });
    });

    // Active navigation highlighting
    window.addEventListener('scroll', updateActiveNavigation);
}

/**
 * Update active navigation item based on scroll position
 */
function updateActiveNavigation() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link, .quick-nav-item');
    const scrollPosition = window.scrollY + 100;

    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.offsetHeight;
        const sectionId = section.getAttribute('id');

        if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === `#${sectionId}`) {
                    link.classList.add('active');
                }
            });
        }
    });
}/**
 * Mobile menu functionality
 */
function initializeMobileMenu() {
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const nav = document.querySelector('.nav');
    
    if (mobileToggle && nav) {
        console.log('Mobile menu initialized');
        mobileToggle.addEventListener('click', function() {
            console.log('Mobile toggle clicked');
            nav.classList.toggle('mobile-active');
            this.classList.toggle('active');
            console.log('Nav classes after toggle:', nav.classList.toString());

            // Toggle icon
            const icon = this.querySelector('i');
            if (icon.classList.contains('fa-bars')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
        
        // Close mobile menu on nav link click
        document.querySelectorAll('.nav-link, .quick-nav-item').forEach(link => {
            link.addEventListener('click', function() {
                nav.classList.remove('mobile-active');
                mobileToggle.classList.remove('active');
                const icon = mobileToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            });
        });
    }
}

/**
 * Scroll effects and animations
 */
function initializeScrollEffects() {
    // Parallax effect for hero section
    const hero = document.querySelector('.hero');
    if (hero) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const parallax = scrolled * 0.5;
            hero.style.transform = `translateY(${parallax}px)`;
        });
    }
}/**
 * Animated stats counter
 */
function initializeStatsAnimation() {
    const stats = document.querySelectorAll('.stat-number');
    
    const animateStats = () => {
        stats.forEach(stat => {
            const target = parseInt(stat.innerText);
            const increment = target / 60; // Animation over ~1 second at 60fps
            let current = 0;
            
            const updateCounter = () => {
                if (current < target) {
                    current += increment;
                    stat.innerText = Math.floor(current);
                    requestAnimationFrame(updateCounter);
                } else {
                    stat.innerText = target + (target === 100 ? '+' : '');
                }
            };
            
            updateCounter();
        });
    };
    
    // Trigger animation when hero section is visible
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                setTimeout(animateStats, 500); // Small delay for better effect
                observer.unobserve(entry.target);
            }
        });
    });
    
    const heroSection = document.querySelector('.hero');
    if (heroSection) {
        observer.observe(heroSection);
    }
}

/**
 * Card hover animations and interactions
 */
function initializeCardAnimations() {
    const cards = document.querySelectorAll('.lecture-card, .project-card, .about-card, .exercise-card');
    
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transition = 'all 0.3s cubic-bezier(0.4, 0, 0.2, 1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transition = 'all 0.2s ease';
        });
    });
}/**
 * Scroll to top functionality
 */
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

/**
 * Loading animations for sections
 */
function initializeLoadingAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
            }
        });
    }, observerOptions);
    
    // Observe sections for loading animations
    document.querySelectorAll('section').forEach(section => {
        observer.observe(section);
    });
}

/**
 * Performance optimizations
 */
function initializePerformanceOptimizations() {
    // Lazy loading for images
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
    
    // Debounced scroll handler
    let scrollTimeout;
    window.addEventListener('scroll', function() {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }
        scrollTimeout = setTimeout(updateActiveNavigation, 10);
    });
}

// Initialize performance optimizations
document.addEventListener('DOMContentLoaded', function() {
    initializeLoadingAnimations();
    initializePerformanceOptimizations();
});