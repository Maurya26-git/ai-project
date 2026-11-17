/**
 * Sentix Advanced Motion Graphics Engine - Emerald Obsidian & Deep Black Edition
 * - Emerald AI Neural Constellation & Twinkling Stardust
 * - Reactive Mouse Nebula Wave
 * - 3D Card Spatial Perspective Tilt
 * - Emerald Confetti & Sparkle Bursts
 * - Animated Number Counters & Sentiment Energy Bars
 */

document.addEventListener('DOMContentLoaded', () => {
    initEmeraldParticleCanvas();
    init3DTiltCards();
    initSentimentAudioBars();
});

/* ==========================================================================
   1. Emerald AI Neural Constellation & Shimmering Stardust
   ========================================================================== */
function initEmeraldParticleCanvas() {
    const canvas = document.getElementById('motion-canvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
    });

    const particles = [];
    const particleCount = Math.min(85, Math.floor((width * height) / 18000));
    const mouse = { x: null, y: null, radius: 160 };

    window.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
    });

    window.addEventListener('mouseleave', () => {
        mouse.x = null;
        mouse.y = null;
    });

    class EmeraldParticle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.vx = (Math.random() - 0.5) * 0.7;
            this.vy = (Math.random() - 0.5) * 0.7;
            this.baseRadius = Math.random() * 2.0 + 0.8;
            this.radius = this.baseRadius;
            this.twinkleSpeed = Math.random() * 0.03 + 0.01;
            this.twinkleAngle = Math.random() * Math.PI * 2;
        }

        update() {
            this.x += this.vx;
            this.y += this.vy;

            if (this.x < 0 || this.x > width) this.vx = -this.vx;
            if (this.y < 0 || this.y > height) this.vy = -this.vy;

            // Twinkle oscillation
            this.twinkleAngle += this.twinkleSpeed;
            this.radius = this.baseRadius + Math.sin(this.twinkleAngle) * 0.5;

            // Mouse gravitational repulsion
            if (mouse.x !== null && mouse.y !== null) {
                const dx = mouse.x - this.x;
                const dy = mouse.y - this.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < mouse.radius) {
                    const force = (mouse.radius - dist) / mouse.radius;
                    this.x -= (dx / dist) * force * 2.5;
                    this.y -= (dy / dist) * force * 2.5;
                }
            }
        }

        draw(isDark) {
            ctx.beginPath();
            ctx.arc(this.x, this.y, Math.max(0.2, this.radius), 0, Math.PI * 2);
            
            // Tasteful emerald particles (not overly bright)
            const alpha = 0.45 + Math.sin(this.twinkleAngle) * 0.25;
            if (isDark) {
                ctx.fillStyle = `rgba(52, 211, 153, ${alpha * 0.7})`;
                ctx.shadowBlur = 8;
                ctx.shadowColor = 'rgba(16, 185, 129, 0.4)';
            } else {
                ctx.fillStyle = `rgba(5, 150, 105, ${alpha * 0.55})`;
                ctx.shadowBlur = 5;
                ctx.shadowColor = 'rgba(5, 150, 105, 0.3)';
            }
            ctx.fill();
            ctx.shadowBlur = 0;
        }
    }

    for (let i = 0; i < particleCount; i++) {
        particles.push(new EmeraldParticle());
    }

    function animate() {
        ctx.clearRect(0, 0, width, height);
        const isDark = document.documentElement.classList.contains('dark');

        // Draw subtle connecting threads
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 120) {
                    const alpha = (1 - dist / 120) * (isDark ? 0.2 : 0.15);
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = isDark ? `rgba(52, 211, 153, ${alpha})` : `rgba(5, 150, 105, ${alpha})`;
                    ctx.lineWidth = 1;
                    ctx.stroke();
                }
            }
        }

        particles.forEach((p) => {
            p.update();
            p.draw(isDark);
        });

        requestAnimationFrame(animate);
    }

    animate();
}

/* ==========================================================================
   2. 3D Spatial Perspective Tilt on Cards
   ========================================================================== */
function init3DTiltCards() {
    apply3DTiltListeners();
}

window.apply3DTiltListeners = function() {
    const tiltCards = document.querySelectorAll('.tilt-card:not([data-tilt-active])');

    tiltCards.forEach((card) => {
        card.setAttribute('data-tilt-active', 'true');

        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = ((y - centerY) / centerY) * -7;
            const rotateY = ((x - centerX) / centerX) * 7;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px) scale3d(1.015, 1.015, 1.015)`;
            card.style.transition = 'transform 0.08s ease-out';
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px) scale3d(1, 1, 1)';
            card.style.transition = 'transform 0.45s cubic-bezier(0.16, 1, 0.3, 1)';
        });
    });
};

/* ==========================================================================
   3. Emerald Confetti & Sparkles Celebration
   ========================================================================== */
window.triggerGoldConfetti = window.triggerConfetti = function() {
    if (!window.confetti) return;
    
    // Sophisticated emerald green, mint, deep forest & silver sparkle palette
    const emeraldColors = ['#10b981', '#34d399', '#059669', '#6ee7b7', '#a7f3d0', '#ffffff', '#064e3b'];

    // Left cannon
    window.confetti({
        particleCount: 35,
        angle: 60,
        spread: 55,
        origin: { x: 0, y: 0.7 },
        colors: emeraldColors
    });

    // Right cannon
    window.confetti({
        particleCount: 35,
        angle: 120,
        spread: 55,
        origin: { x: 1, y: 0.7 },
        colors: emeraldColors
    });
};

/* ==========================================================================
   4. Animated Sentiment Energy Waveform Bars
   ========================================================================== */
function initSentimentAudioBars() {
    const barsContainer = document.getElementById('sentiment-wave-bars');
    if (!barsContainer) return;

    barsContainer.innerHTML = '';
    const barCount = 18;
    for (let i = 0; i < barCount; i++) {
        const bar = document.createElement('div');
        bar.className = 'w-1 rounded-full bg-emerald-500/70 dark:bg-emerald-400/80 transition-all duration-300';
        bar.style.height = `${Math.floor(Math.random() * 20) + 6}px`;
        barsContainer.appendChild(bar);
    }

    // Animate bars on interval
    setInterval(() => {
        const bars = barsContainer.children;
        for (let i = 0; i < bars.length; i++) {
            const h = Math.floor(Math.random() * 24) + 4;
            bars[i].style.height = `${h}px`;
        }
    }, 280);
}

/* ==========================================================================
   5. Smooth Number Counter Animation
   ========================================================================== */
window.animateCountUp = function(elem, targetVal, duration = 800, prefix = '', suffix = '') {
    if (!elem) return;
    const startVal = parseFloat(elem.innerText.replace(/[^0-9.-]/g, '')) || 0;
    const startTime = performance.now();

    function update(now) {
        const elapsed = now - startTime;
        const progress = Math.min(1, elapsed / duration);
        const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
        const current = startVal + (targetVal - startVal) * ease;

        elem.innerText = `${prefix}${current.toFixed(current % 1 === 0 ? 0 : 2)}${suffix}`;

        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            elem.innerText = `${prefix}${targetVal}${suffix}`;
        }
    }

    requestAnimationFrame(update);
};
