#!/usr/bin/env python
# -*- coding: utf-8 -*-

html_content = '''{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About - LUCIFER</title>
    <link rel="stylesheet" href="{% static 'about.css' %}">
</head>
<body>
    <div class="stars"></div>
    <div class="nebula"></div>

    <header class="futuristic-header">
        <div class="header-inner">
            <div class="glitch-logo" data-text="LUCIFER">LUCIFER</div>
            <nav class="space-nav">
                <a href="#hero" class="nav-link">Home</a>
                <a href="#mission" class="nav-link">Mission</a>
                <a href="#stats" class="nav-link">Stats</a>
                <a href="#journey" class="nav-link">Journey</a>
                <a href="#team" class="nav-link">Team</a>
            </nav>
        </div>
    </header>

    <section id="hero" class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">Born in Code, Forged in Light</h1>
            <p class="hero-subtitle">Hyper-futuristic systems for the next digital frontier</p>
            <div class="pulse-bar"></div>
        </div>
    </section>

    <section id="mission" class="section mission-section">
        <div class="section-wrap">
            <h2 class="section-title">Our Mission</h2>
            <div class="glowing-cards">
                <article class="mission-card">
                    <span>01</span>
                    <h3>Quantum Edge</h3>
                    <p>Transmit intelligence across the next generational stack with zero latency.</p>
                </article>
                <article class="mission-card">
                    <span>02</span>
                    <h3>Cyber Integration</h3>
                    <p>Merge human and machine vision in secure, transparent neural fabrics.</p>
                </article>
                <article class="mission-card">
                    <span>03</span>
                    <h3>Infinite Scale</h3>
                    <p>Construct composable ecosystems that span planets and virtual spheres.</p>
                </article>
            </div>
        </div>
    </section>

    <section id="stats" class="section stats-section">
        <div class="section-wrap">
            <h2 class="section-title">By the Numbers</h2>
            <div class="stats-grid">
                <div class="stat-card"><h3>582</h3><p>Systems Deployed</p></div>
                <div class="stat-card"><h3>207</h3><p>Innovation Nodes</p></div>
                <div class="stat-card"><h3>99.7%</h3><p>Uptime Stability</p></div>
                <div class="stat-card"><h3>42</h3><p>Live Regions</p></div>
            </div>
        </div>
    </section>

    <section id="journey" class="section timeline-section">
        <div class="section-wrap">
            <h2 class="section-title">Journey to Singularity</h2>
            <div class="timeline">
                <div class="timeline-event"><span>2020</span><h4>Genesis</h4><p>From a single node in a lab to a planetary mesh.</p></div>
                <div class="timeline-event"><span>2021</span><h4>Expansion</h4><p>Integrated across 3 continents with adaptive AI.</p></div>
                <div class="timeline-event"><span>2022</span><h4>Hybridization</h4><p>Blended edge and cloud into unified neural fabrics.</p></div>
                <div class="timeline-event"><span>2023</span><h4>Acceleration</h4><p>Deployed quantum-safe protocols with hyper-rotation throughput.</p></div>
                <div class="timeline-event"><span>2024</span><h4>Symbiosis</h4><p>Co-created with community ecosystems and autonomous agents.</p></div>
                <div class="timeline-event"><span>2025</span><h4>Singularity</h4><p>Built the first metaverse-level decision stack for global resilience.</p></div>
            </div>
        </div>
    </section>

    <section id="team" class="section team-section">
        <div class="section-wrap">
            <h2 class="section-title">The Core Architects</h2>
            <div class="team-grid">
                <div class="team-card"><div>👨‍💻</div><h3>Nova Systems</h3><p>Synthetic Intelligence & Automation</p></div>
                <div class="team-card"><div>👩‍🔬</div><h3>Aria Quantum</h3><p>Quantum Orchestration & Safety</p></div>
                <div class="team-card"><div>👨‍🚀</div><h3>Rin Forge</h3><p>UX Holos, XR, Spatial Collaboration</p></div>
                <div class="team-card"><div>🧬</div><h3>Zari Net</h3><p>Neural Data Fabric & Predictive Ethics</p></div>
            </div>
        </div>
    </section>

    <section id="contact" class="section cta-section">
        <div class="section-wrap">
            <h2 class="section-title">Join the Transcendence</h2>
            <p>Launch with us into the next era of digital civilization.</p>
            <div class="cta-actions"><button class="btn btn-primary">Ignite Spectrum</button><button class="btn btn-outline">Contact Nexus</button></div>
        </div>
    </section>

    <footer class="futuristic-footer">
        <p>&copy; 2026 LUCIFER Nexus • All systems integrated • Hyper secure</p>
    </footer>
</body>
</html>'''

css_content = '''/* ===== HYPER FUTURISTIC ABOUT PAGE ===== */
:root { --bg-dark: #040712; --bg-mid: #090f2e; --neon-green: #00ffd8; --neon-magenta: #ff00d0; --neon-blue: #09b4ff; --neon-orange: #ffa400; --card-bg: rgba(12, 17, 42, 0.72); --text-light: #ecf6ff; --text-fade: rgba(218, 227, 255, 0.75); --border: rgba(0, 255, 216, 0.22); }
* {box-sizing: border-box; margin: 0; padding: 0;}
body { font-family: 'Segoe UI', 'Roboto', sans-serif; background: radial-gradient(circle at 15% 10%, #19242c 0%, var(--bg-dark) 35%, var(--bg-mid) 100%); color: var(--text-light); overflow-x: hidden; }
.stars, .nebula { position: fixed; width: 100%; height: 100%; top: 0; left: 0; pointer-events: none; z-index: -2; }
.stars::after, .nebula::before { content: ''; position: absolute; width: 100%; height: 100%; }
.stars::after { background: radial-gradient(circle at 30% 10%, rgba(255,255,255,0.08), transparent 15%), radial-gradient(circle at 80% 20%, rgba(255,255,255,0.06), transparent 12%), radial-gradient(circle at 50% 80%, rgba(255,255,255,0.05), transparent 10%); animation: twinkle 9s linear infinite; }
.nebula::before { background: linear-gradient(140deg, rgba(255, 0, 208, 0.16), rgba(0, 255, 216, 0.12), rgba(9, 180, 255, 0.06)); filter: blur(16px); animation: drift 12s ease-in-out infinite; }
@keyframes twinkle { 0%,100% {opacity:0.7;} 50% {opacity:1;} }
@keyframes drift { 0% {transform: translate(0,0);} 50% {transform: translate(10px,-10px);} 100% {transform: translate(0,0);} }
.futuristic-header { position: sticky; top: 0; z-index: 20; width: 100%; backdrop-filter: blur(12px); background: rgba(2, 7, 19, 0.58); border-bottom: 1px solid var(--border); }
.header-inner { max-width: 1260px; margin: 0 auto; padding: 18px 24px; display: flex; justify-content: space-between; align-items: center; }
.glitch-logo { font-size: 1.85rem; font-weight: 900; letter-spacing: 0.15em; color: var(--neon-green); position: relative; text-transform: uppercase; }
.glitch-logo::before, .glitch-logo::after { content: attr(data-text); position: absolute; left: 0; top: 0; }
.glitch-logo::before { animation: glitch-top 2.4s infinite; color: var(--neon-magenta); clip-path: inset(0 0 66% 0); }
.glitch-logo::after { animation: glitch-bottom 2.2s infinite; color: var(--neon-blue); clip-path: inset(66% 0 0 0); }
@keyframes glitch-top { 0% {transform: translate(0,0);} 20% {transform: translate(-2px,-1px);} 40% {transform: translate(2px,2px);} 60% {transform: translate(-1px,1px);} 100% {transform: translate(0,0);} }
@keyframes glitch-bottom { 0% {transform: translate(0,0);} 20% {transform: translate(2px,1px);} 40% {transform: translate(-2px,-2px);} 60% {transform: translate(1px,-1px);} 100% {transform: translate(0,0);} }
.space-nav { display: flex; gap: 1rem; }
.nav-link { color: var(--text-fade); text-decoration: none; font-size: 0.94rem; letter-spacing: 0.09em; border-bottom: 1px solid transparent; transition: .25s; }
.nav-link:hover { color: var(--neon-blue); border-bottom-color: var(--neon-blue); }
.hero-section { padding: 8rem 2rem 6rem; text-align: center; position: relative; }
.hero-content { max-width: 920px; margin: 0 auto; backdrop-filter: blur(10px); }
.hero-title { font-size: clamp(2.2rem, 6vw, 4.5rem); font-weight: 900; letter-spacing: 0.14em; line-height: 1.1; text-transform: uppercase; margin-bottom: 1rem; color: #fff; background-image: linear-gradient(120deg, var(--neon-green), var(--neon-magenta), var(--neon-blue)); background-clip: text; -webkit-background-clip: text; color: transparent; }
.hero-subtitle { font-size: 1.25rem; color: var(--text-fade); margin-bottom: 2rem; }
.pulse-bar { width: 220px; height: 3px; margin: 0 auto; border-radius: 999px; background: linear-gradient(90deg, var(--neon-green), var(--neon-blue), var(--neon-magenta)); animation: pulse 1.5s infinite; }
@keyframes pulse { 0%,100% {transform: scaleX(0.7); opacity: 0.7;} 50% {transform: scaleX(1); opacity: 1;} }
.section { position: relative; padding: 4.5rem 2rem; }
.section-wrap { max-width: 1080px; margin: 0 auto; position: relative; }
.section-title { font-size: 2.45rem; letter-spacing: 0.12em; margin-bottom: 2rem; background: linear-gradient(90deg, var(--neon-magenta), var(--neon-green), var(--neon-blue)); -webkit-background-clip: text; color: transparent; }
.mission-section { background: rgba(6,11,28,0.42); border: 1px solid var(--border); border-radius: 14px; backdrop-filter: blur(8px); box-shadow: 0 0 36px rgba(0,255,216,0.12); }
.glowing-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap: 1rem; }
.mission-card { background: rgba(5, 9, 27, 0.65); border: 1px solid var(--border); border-radius: 16px; padding: 1.35rem; min-height: 175px; display: flex; flex-direction: column; gap: 0.75rem; overflow: hidden; box-shadow: inset 0 0 12px rgba(8, 252, 226, 0.15); transition: transform .3s ease, box-shadow .3s ease; }
.mission-card:hover { transform: translateY(-6px); box-shadow: 0 0 30px rgba(0,255,216,0.45), inset 0 0 14px rgba(255,10,166,0.26); }
.mission-card span { font-weight: 700; color: var(--neon-orange); font-size: 1.75rem; }
.mission-card h3 { font-size: 1.22rem; color: #d7f8ff; }
.mission-card p { color: rgba(235,240,255,0.9); font-size: 0.95rem; line-height: 1.45; }
.stats-section { margin-top: 2rem; }
.stats-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(200px,1fr)); gap: 1rem; }
.stat-card { padding:1.25rem; border-radius: 14px; border: 1px solid var(--border); background: linear-gradient(135deg, rgba(7,14,38,0.72), rgba(7,13,52,0.56)); box-shadow: 0 0 18px rgba(0, 255, 216, 0.14); transition: transform .25s ease; }
.stat-card:hover { transform: translateY(-4px); }
.stat-card h3 { font-size:2.5rem; letter-spacing:0.05em; color: var(--neon-green); }
.stat-card p { color: var(--text-fade); text-transform: uppercase; margin-top:.35rem; letter-spacing:.1em; font-size:.84rem; }
.timeline-section { background: rgba(4, 8, 22, 0.45); border-radius:16px; border:1px solid var(--border); box-shadow:0 0 25px rgba(9,180,255,0.18); }
.timeline { border-left:2px solid rgba(0,255,216,0.4); margin-left: 20px; padding-left: 18px; display:grid; gap:1rem; }
.timeline-event { padding: 0.95rem 1.05rem; background:rgba(11, 17, 46, 0.6); border:1px solid rgba(0,255,216,0.25); border-radius: 12px; position:relative; }
.timeline-event::before { content:''; position:absolute; left:-12px; top:9px; width: 12px; height: 12px; background: linear-gradient(135deg, var(--neon-blue), var(--neon-magenta)); border-radius:50%; box-shadow:0 0 15px rgba(0,255,216,0.7); }
.timeline-event span { display:inline-block; font-weight:700; font-size:.92rem; color: var(--neon-orange); margin-bottom:.4rem; }
.timeline-event h4 { font-size:1.05rem; color:#fff; margin-bottom:.2rem; }
.timeline-event p { color:var(--text-fade); font-size:.9rem; line-height:1.4; }
.team-section { padding-bottom: 2rem; }
.team-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:1rem; }
.team-card { background: rgba(7, 12, 32, 0.68); border: 1px solid rgba(0,255,216,0.24); border-radius: 16px; padding: 1rem; display:flex; flex-direction:column; align-items:center; gap:.6rem; text-align:center; transition: transform .3s ease, box-shadow .3s ease; }
.team-card:hover { transform: translateY(-5px); box-shadow: 0 0 22px rgba(0,255,216,0.24); }
.team-card > div { background: #0d1838; border-radius: 50%; width: 66px; height:66px; display:flex; align-items:center; justify-content:center; font-size:1.9rem; }
.team-card h3 { font-size:1.06rem; color:#e6ffff; }
.team-card p { color: var(--text-fade); font-size:.88rem; }
.cta-section { background:linear-gradient(140deg, rgba(0,255,216,0.15), rgba(196,0,255,0.17)); border:1px solid var(--border); border-radius:16px; margin: 1rem 0; text-align:center; padding:2.35rem 1rem; }
.cta-section p { color: var(--text-fade); margin: .8rem 0 1.4rem; font-size:1rem; }
.cta-actions { display:flex; flex-wrap:wrap; justify-content:center; gap:.8rem; }
.btn { border:0; padding:.88rem 1.4rem; border-radius:10px; letter-spacing:.09em; font-weight:700; cursor:pointer; transition:.2s; }
.btn-primary { background: linear-gradient(90deg, var(--neon-green), var(--neon-blue)); color: #081029; box-shadow:0 0 20px rgba(0,255,216,0.3); }
.btn-outline { background: transparent; color: var(--neon-magenta); border:1px solid var(--neon-magenta); }
.btn:hover { transform: translateY(-2px); }
.futuristic-footer { border-top: 1px solid rgba(0,255,216,0.22); text-align:center; padding:1.1rem; color:var(--text-fade); font-size:.86rem; }
@media (max-width: 900px) { .space-nav { gap:.65rem; } .hero-title { font-size:clamp(1.8rem,8vw,3.2rem); } }
@media (max-width: 680px) { .header-inner { flex-direction:column; gap:.8rem; } .timeline { margin-left: 13px; } }
'''

with open('templates/about.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

with open('static/about.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print('✓ about.html written successfully in UTF-8')
print('✓ about.css written successfully in UTF-8')

html_bytes = open('templates/about.html', 'rb').read(4)
css_bytes = open('static/about.css', 'rb').read(4)
print(f'HTML first 4 bytes: {" ".join(hex(b) for b in html_bytes)}')
print(f'CSS first 4 bytes: {" ".join(hex(b) for b in css_bytes)}')
