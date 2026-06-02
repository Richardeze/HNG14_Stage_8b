from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI(title="Eze Richard - Backend Engineer")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Eze Richard | Backend Engineer</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: 'Segoe UI', sans-serif; line-height: 1.6; background: #f8f9fa; color: #333; }
            .container { max-width: 1000px; margin: 2rem auto; padding: 0 1rem; }
            nav { background: white; padding: 1rem; border-bottom: 1px solid #ddd; }
            .nav-container { max-width: 1000px; margin: 0 auto; display: flex; justify-content: space-between; }
            h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
            .profile { text-align: center; margin-bottom: 3rem; }
            .btn { background: #0066cc; color: white; padding: 12px 24px; border-radius: 6px; text-decoration: none; display: inline-block; margin-top: 1rem; }
            .projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; }
            .project-card { background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #eee; }
            .skills { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; list-style: none; }
            .skills li { background: white; padding: 1rem; border-radius: 6px; border-left: 4px solid #0066cc; }
            footer { text-align: center; margin-top: 4rem; color: #666; }
        </style>
    </head>
    <body>
        <nav>
            <div class="nav-container">
                <h2>Eze Richard</h2>
            </div>
        </nav>
        
        <div class="container">
            <header class="profile">
                <h1>Eze Richard</h1>
                <h3>Backend Engineer</h3>
                <p>Lagos, Nigeria • WAT (UTC+1)</p>
                <p>FastAPI specialist with hands-on experience building production APIs during HNG Internship.</p>
                <a href="mailto:ezerichard100@gmail.com" class="btn">Contact Me</a>
            </header>

            <h2>HNG Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <h3>Stage 1: User Profile API</h3>
                    <p>Integrated 3 external APIs (Genderize, Agify, Nationalize), data classification, idempotency, SQLAlchemy.</p>
                    <p><strong>Stack:</strong> FastAPI, SQLAlchemy, SQLite, HTTPX</p>
                </div>
                <div class="project-card">
                    <h3>Stage 2/3: Insighta Labs</h3>
                    <p>Demographic Intelligence API with advanced filtering, natural language search, GitHub OAuth, JWT, roles, and Redis caching.</p>
                    <p><strong>Stack:</strong> FastAPI, PostgreSQL, JWT, Redis</p>
                </div>
                <div class="project-card">
                    <h3>Stage 5: Auth Features</h3>
                    <p>Logout with token blacklisting, guest session management & migration.</p>
                </div>
                <div class="project-card">
                    <h3>Stage 6: Real-time Chat</h3>
                    <p>WebSocket with AI streaming + rate limiting + mobile OAuth fix.</p>
                    <p><strong>Stack:</strong> FastAPI, WebSockets</p>
                </div>
                <div class="project-card">
                    <h3>Stage 7: Append-Only Event Store</h3>
                    <p>Crash-safe file-based event store for resilience challenge.</p>
                </div>
            </div>

            <h2>Backend Skills</h2>
            <ul class="skills">
                <li>FastAPI & REST API Design</li>
                <li>Authentication (JWT, OAuth2, Role-based)</li>
                <li>Databases (PostgreSQL, SQLAlchemy, Redis)</li>
                <li>WebSockets & Real-time Features</li>
                <li>External API Integration</li>
                <li>Natural Language Query Parsing</li>
                <li>Token Blacklisting & Security</li>
                <li>Caching with Redis</li>
            </ul>

            <footer>
                <p>Built with FastAPI • HNG Internship 2026</p>
            </footer>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)