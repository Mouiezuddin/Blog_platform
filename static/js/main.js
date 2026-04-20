// =====================
// Developers Tale - Main JS
// =====================

// Theme Management
const THEME_KEY = 'dt-theme';

function getTheme() {
    return localStorage.getItem(THEME_KEY) || 'dark';
}

function applyTheme(theme) {
    const html = document.getElementById('html-root');
    if (theme === 'light') {
        html.classList.remove('dark');
        html.classList.add('light');
    } else {
        html.classList.remove('light');
        html.classList.add('dark');
    }
    // Update icon
    const icons = document.querySelectorAll('#theme-icon, #theme-icon-mobile');
    icons.forEach(icon => {
        icon.textContent = theme === 'light' ? 'dark_mode' : 'light_mode';
    });
}

function toggleTheme() {
    const current = getTheme();
    const next = current === 'dark' ? 'light' : 'dark';
    localStorage.setItem(THEME_KEY, next);
    applyTheme(next);
}

// Mobile Menu
function toggleMobileMenu() {
    const menu = document.getElementById('mobile-menu');
    const icon = document.getElementById('mobile-menu-icon');
    const isHidden = menu.classList.contains('hidden');
    menu.classList.toggle('hidden');
    icon.textContent = isHidden ? 'close' : 'menu';
}

// Navbar scroll effect
function handleNavbarScroll() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;
    if (window.scrollY > 10) {
        navbar.style.boxShadow = '0 4px 30px rgba(0,0,0,0.5)';
    } else {
        navbar.style.boxShadow = 'none';
    }
}

// Scroll to top button
function createScrollToTop() {
    const btn = document.createElement('button');
    btn.innerHTML = '<span class="material-icons-round">keyboard_arrow_up</span>';
    btn.id = 'scroll-top-btn';
    btn.className = 'fixed bottom-6 right-6 w-12 h-12 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white flex items-center justify-center shadow-lg shadow-indigo-600/30 transition-all duration-300 z-40 opacity-0 pointer-events-none';
    btn.onclick = () => window.scrollTo({ top: 0, behavior: 'smooth' });
    document.body.appendChild(btn);
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
        } else {
            btn.style.opacity = '0';
            btn.style.pointerEvents = 'none';
        }
    });
}

// CSRF Token helper
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Copy to clipboard utility
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).catch(() => {
        const el = document.createElement('textarea');
        el.value = text;
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
    });
}

// Add copy button to code blocks
function addCodeCopyButtons() {
    document.querySelectorAll('.post-content pre').forEach(pre => {
        if (pre.querySelector('.copy-btn')) return;
        const btn = document.createElement('button');
        btn.className = 'copy-btn absolute top-3 right-3 px-2.5 py-1 rounded-lg bg-gray-700 hover:bg-gray-600 text-gray-300 text-xs font-mono flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-all';
        btn.innerHTML = '<span class="material-icons-round" style="font-size:14px">content_copy</span> Copy';
        btn.onclick = () => {
            const code = pre.querySelector('code');
            if (code) {
                copyToClipboard(code.textContent);
                btn.innerHTML = '<span class="material-icons-round" style="font-size:14px">check</span> Copied!';
                btn.classList.add('bg-green-700');
                setTimeout(() => {
                    btn.innerHTML = '<span class="material-icons-round" style="font-size:14px">content_copy</span> Copy';
                    btn.classList.remove('bg-green-700');
                }, 2000);
            }
        };
        pre.style.position = 'relative';
        pre.classList.add('group');
        pre.appendChild(btn);
    });
}

// Animate elements on scroll
function initScrollAnimations() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                entry.target.style.opacity = '1';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });
    
    document.querySelectorAll('article, .post-card').forEach(el => {
        el.style.opacity = '0';
        observer.observe(el);
    });
}

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    // Apply saved theme
    applyTheme(getTheme());
    
    // Scroll effects
    window.addEventListener('scroll', handleNavbarScroll, { passive: true });
    
    // Scroll to top
    createScrollToTop();
    
    // Code copy buttons
    addCodeCopyButtons();
    
    // Close mobile menu on outside click
    document.addEventListener('click', (e) => {
        const menu = document.getElementById('mobile-menu');
        const btn = e.target.closest('[onclick="toggleMobileMenu()"]');
        if (!menu || menu.classList.contains('hidden') || btn) return;
        if (!menu.contains(e.target)) {
            menu.classList.add('hidden');
            const icon = document.getElementById('mobile-menu-icon');
            if (icon) icon.textContent = 'menu';
        }
    });
    
    // Reading progress bar
    const progressBar = document.createElement('div');
    progressBar.id = 'reading-progress';
    progressBar.style.cssText = 'position:fixed;top:0;left:0;width:0%;height:3px;background:linear-gradient(90deg,#6366f1,#22d3ee);z-index:9999;transition:width 0.1s;';
    document.body.appendChild(progressBar);
    
    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset;
        const docHeight = document.body.offsetHeight - window.innerHeight;
        const progress = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
        progressBar.style.width = `${Math.min(100, progress)}%`;
    }, { passive: true });
});
