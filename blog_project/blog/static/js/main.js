document.addEventListener('DOMContentLoaded', function() {
    // Like button animation
    const likeButtons = document.querySelectorAll('.btn-outline-danger');
    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const icon = this.querySelector('i');
            icon.classList.add('heart-beat');
            setTimeout(() => {
                icon.classList.remove('heart-beat');
            }, 1000);
        });
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Flash message auto dismiss
    setTimeout(() => {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(alert => {
            alert.style.transition = 'opacity 0.5s ease';
            alert.style.opacity = '0';
            setTimeout(() => {
                alert.remove();
            }, 500);
        });
    }, 3000);
});