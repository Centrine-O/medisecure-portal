import { useState } from "react";

const featureCards = [
  {
    title: "Secure Patient Vitals",
    text: "Monitor real-time health data with enterprise-level encryption and secure cloud storage."
  },
  {
    title: "Smart Staff Scheduling",
    text: "Optimize clinic workflow with automated scheduling tools and resource management."
  },
  {
    title: "Global Interoperability",
    text: "Seamlessly connect and exchange data with global health systems and standards."
  }
];

const ecosystemBullets = [
  "Localized data residency compliance",
  "Offline-first capabilities for remote areas",
  "Integrated mobile payment systems (M-Pesa)"
];

const roadmap = [
  {
    phase: "Phase 1 - MVP",
    outcomes: [
      "Patient auth + staff auth",
      "Appointments booking and status updates",
      "Medical forms submission and review queues",
      "Role-based dashboard foundation",
      "Core audit and encryption controls"
    ]
  },
  {
    phase: "Phase 2 - Multi-Facility Pilot",
    outcomes: [
      "Tenant onboarding for multiple clinics",
      "Facility-level settings, templates, and workflows",
      "Unified reporting for appointments and forms",
      "Pilot integration with selected EMR/claims pathways"
    ]
  },
  {
    phase: "Phase 3 - County Rollout",
    outcomes: [
      "County deployment toolkit and implementation playbook",
      "Offline-friendly workflow support for low-connectivity locations",
      "Inter-facility referral and handoff flows",
      "Stronger compliance and operations analytics"
    ]
  },
  {
    phase: "Phase 4 - National Scale",
    outcomes: [
      "Interoperability adapters for broad ecosystem integration",
      "National-grade tenant provisioning and governance controls",
      "Advanced fraud/risk checks for claims-facing workflows",
      "Performance and reliability hardening for large-scale usage"
    ]
  }
];

const marketDisconnects = [
  "Fragmented systems across hospitals, clinics, claims channels, and standalone portals.",
  "Different patient intake processes at each facility causing delays and confusion.",
  "Limited shared visibility for staff across appointments, forms, and review queues.",
  "Manual reconciliation between internal records and insurance/claims workflows.",
  "Inconsistent data governance practices across facilities."
];

const universalDesign = [
  "Multi-tenant model where each facility has isolated users, data, and settings.",
  "API-first architecture so modules can integrate with external health systems over time.",
  "Role-based access for patients, clinicians, admins, and operations teams.",
  "Configurable forms and workflows per facility without rebuilding core product logic.",
  "Audit-ready activity tracking and protected data handling by default."
];

const roadmapKpis = [
  "Reduce average patient check-in time by 30%+",
  "Increase digital form completion rate above 90%",
  "Reduce appointment no-show rate by 20%+",
  "Lower staff time spent on manual coordination and data entry",
  "Maintain complete, verifiable activity history across workflows"
];

function PublicLandingPage() {
  const [activeTab, setActiveTab] = useState("solutions");

  return (
    <div className="page-wrap">
      <div className="app-shell">
        <header className="topbar">
          <div className="brand">
            <span className="brand-shield">🛡️</span>
            <strong>MediSecure</strong>
          </div>

          <nav className="main-nav" aria-label="Main navigation">
            <a href="#features">Solutions</a>
            <a href="#interoperability">Interoperability</a>
            <a href="#about">About</a>
          </nav>

          <button type="button" className="login-btn">Login</button>
        </header>

        <main>
          <section className="hero" id="about">
            <div className="hero-copy">
              <h1>
                The <em>Operating System</em> for
                <br />
                Modern Healthcare
              </h1>
              <p>
                Refined healthcare infrastructure for patients, providers, and health systems in Kenya.
                Secure, interoperable, and built for scale.
              </p>
              <div className="hero-actions">
                <button type="button" className="btn-primary">Get Started</button>
                <button type="button" className="btn-ghost">Watch Demo</button>
              </div>
            </div>

            <div className="hero-visual" aria-label="Platform dashboard preview">
              <div className="visual-card">
                <div className="visual-nav" />
                <div className="visual-stats">
                  <span>03%</span>
                  <span>20%</span>
                  <span>33%</span>
                  <span>20%</span>
                </div>
                <div className="visual-bars">
                  <span />
                  <span />
                  <span />
                  <span />
                  <span />
                </div>
              </div>

              <div className="floating-vitals">
                <div className="dot" />
                <div>
                  <p>Live Vitals</p>
                  <div className="pulse-bar" />
                </div>
              </div>

              <div className="floating-security">
                <p>Security Status</p>
                <strong>AES-256 Encrypted</strong>
              </div>
            </div>
          </section>

          <section className="sub-tabs" aria-label="Solutions tabs">
            <button type="button" className={activeTab === "solutions" ? "tab active" : "tab"} onClick={() => setActiveTab("solutions")}>Solutions Overview</button>
            <button type="button" className={activeTab === "interoperability" ? "tab active" : "tab"} onClick={() => setActiveTab("interoperability")}>Interoperability</button>
            <button type="button" className={activeTab === "systems" ? "tab active" : "tab"} onClick={() => setActiveTab("systems")}>Health Systems</button>
          </section>

          <section className="features" id="features">
            <header className="section-head center">
              <h2>Enterprise-Grade Features</h2>
              <p>Experience a high-trust healthcare platform designed for Kenya's ecosystem.</p>
            </header>

            <div className="feature-grid">
              {featureCards.map((card) => (
                <article key={card.title} className="feature-card">
                  <span className="icon-dot">⌁</span>
                  <h3>{card.title}</h3>
                  <p>{card.text}</p>
                  <a href="#">Learn More →</a>
                </article>
              ))}
            </div>
          </section>

          <section className="ecosystem" id="interoperability">
            <div className="eco-image" role="img" aria-label="Healthcare facility environment" />

            <div className="eco-copy">
              <h2>Built for Kenya's Health Ecosystem</h2>
              <p>
                We understand the unique challenges of healthcare in East Africa. Our platform is designed
                to work in diverse environments, from urban hospitals to rural clinics.
              </p>
              <ul>
                {ecosystemBullets.map((item) => <li key={item}>{item}</li>)}
              </ul>
              <button type="button" className="btn-dark">Explore Ecosystem</button>
            </div>
          </section>
        </main>

        <footer className="footer">
          <div className="footer-brand">
            <strong>MediSecure</strong>
          </div>
          <p>© 2024 MediSecure Healthcare Solutions. All rights reserved.</p>
          <div className="footer-icons">🌐 ✉️ 📄</div>
        </footer>
      </div>
    </div>
  );
}

function RoadmapPage() {
  return (
    <div className="roadmap-page">
      <header className="roadmap-header-card">
        <div>
          <p className="roadmap-eyebrow">Project Presentation View</p>
          <h1>MediSecure Product Roadmap and Scale Strategy</h1>
          <p className="roadmap-subtitle">
            A complete overview of what problem MediSecure solves, how it is designed for universal use,
            and the phased path from MVP to national-scale platform operations.
          </p>
        </div>
        <a className="btn-primary" href="/">Back to Landing</a>
      </header>

      <section className="roadmap-section roadmap-panel">
        <h2>Purpose</h2>
        <p>
          MediSecure is a secure healthcare workflow platform that unifies patient onboarding,
          appointments, forms, staff operations, and facility management in one digital system.
        </p>
      </section>

      <section className="roadmap-section roadmap-panel">
        <h2>Current Market Disconnects</h2>
        <div className="roadmap-notes">
          {marketDisconnects.map((item) => (
            <article key={item} className="roadmap-note-card">
              <p>{item}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="roadmap-section roadmap-panel">
        <h2>Universal Platform Design</h2>
        <div className="roadmap-notes">
          {universalDesign.map((item) => (
            <article key={item} className="roadmap-note-card">
              <p>{item}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="roadmap-section roadmap-panel">
        <h2>Execution Plan</h2>
        <div className="roadmap-grid">
          {roadmap.map((phase, idx) => (
            <article key={phase.phase} className="roadmap-card">
              <span className="roadmap-step">{idx + 1}</span>
              <h3>{phase.phase}</h3>
              <ul>
                {phase.outcomes.map((item) => <li key={item}>{item}</li>)}
              </ul>
            </article>
          ))}
        </div>
      </section>

      <section className="roadmap-section roadmap-panel">
        <h2>Success Metrics</h2>
        <div className="roadmap-notes">
          {roadmapKpis.map((item) => (
            <article key={item} className="roadmap-note-card">
              <p>{item}</p>
            </article>
          ))}
        </div>
      </section>
    </div>
  );
}

function isRoadmapView() {
  if (typeof window === "undefined") return false;
  const params = new URLSearchParams(window.location.search);
  const byQuery = params.get("view") === "roadmap";
  const byPath = window.location.pathname === "/roadmap";
  return byQuery || byPath;
}

export default function App() {
  if (isRoadmapView()) return <RoadmapPage />;
  return <PublicLandingPage />;
}
