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
            nav { background: white; border-bottom: 1px solid #ddd; position: sticky; top: 0; z-index: 100; }
            .nav-container { max-width: 1000px; margin: 0 auto; padding: 1rem; display: flex; justify-content: space-between; align-items: center; }
            nav a { margin-left: 1.5rem; text-decoration: none; color: #0066cc; font-weight: 500; }
            .container { max-width: 1000px; margin: 2rem auto; padding: 0 1rem; }
            section { margin-bottom: 3rem; }
            h2 { font-size: 1.6rem; margin-bottom: 1.2rem; border-bottom: 2px solid #0066cc; padding-bottom: 0.4rem; }
            h3 { margin-bottom: 0.5rem; }
            .profile { text-align: center; padding: 2rem 0; }
            .profile h1 { font-size: 2.5rem; }
            .profile p { color: #555; margin-top: 0.3rem; }
            .btn { display: inline-block; background: #0066cc; color: white; padding: 0.8rem 1.5rem; border-radius: 6px; text-decoration: none; margin-top: 1rem; }
            .projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
            .project-card { background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #eee; }
            .project-card p { color: #555; font-size: 0.95rem; margin-top: 0.3rem; }
            .tag { display: inline-block; background: #e8f0fe; color: #0066cc; font-size: 0.8rem; padding: 2px 8px; border-radius: 4px; margin: 4px 2px 0 0; }
            .skills { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 0.8rem; list-style: none; }
            .skills li { background: white; padding: 1rem; border-radius: 6px; border-left: 4px solid #0066cc; font-size: 0.95rem; }
            .skills li span { display: block; color: #777; font-size: 0.85rem; margin-top: 0.2rem; }
            .featured { background: white; padding: 2rem; border-radius: 8px; border: 1px solid #eee; }
            .featured h3 { margin-top: 1.2rem; color: #0066cc; }
            .featured p { color: #444; margin-top: 0.4rem; }
            .featured code { background: #f1f3f5; padding: 2px 6px; border-radius: 4px; font-size: 0.9rem; }
            .reflection { background: white; padding: 1.5rem; border-radius: 8px; border: 1px solid #eee; color: #444; }
            .contact-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }
            .contact-card { background: white; padding: 1.2rem; border-radius: 8px; border: 1px solid #eee; text-align: center; }
            .contact-card a { color: #0066cc; text-decoration: none; font-weight: 500; }
            footer { text-align: center; padding: 2rem; color: #888; border-top: 1px solid #ddd; margin-top: 2rem; }
        </style>
    </head>
    <body>
        <nav>
            <div class="nav-container">
                <strong>Eze Richard</strong>
                <div>
                    <a href="#projects">Projects</a>
                    <a href="#skills">Skills</a>
                    <a href="#featured">Deep Dive</a>
                    <a href="#reflection">Reflection</a>
                    <a href="#contact">Contact</a>
                </div>
            </div>
        </nav>

        <div class="container">

            <!-- PROFILE -->
            <section class="profile">
                <h1>Eze Richard</h1>
                <h3>Backend Engineer</h3>
                <p>Lagos, Nigeria &bull; WAT (UTC+1)</p>
                <p style="max-width:600px; margin: 0.8rem auto;">FastAPI specialist with hands-on experience building production-grade APIs, real-time systems, and resilient infrastructure during the HNG Internship.</p>
                <a href="#contact" class="btn">Get In Touch</a>
            </section>

            <!-- PROJECTS -->
            <section id="projects">
                <h2>HNG Projects</h2>
                <div class="projects-grid">
                    <div class="project-card">
                        <h3>Stage 1 — User Profile API</h3>
                        <p>Integrated 3 external APIs (Genderize, Agify, Nationalize) with data classification, idempotency, and persistent storage.</p>
                        <p><strong>Built:</strong> API orchestration, idempotency logic, SQLAlchemy models</p>
                        <div><span class="tag">FastAPI</span><span class="tag">SQLAlchemy</span><span class="tag">SQLite</span><span class="tag">HTTPX</span></div>
                    </div>
                    <div class="project-card">
                        <h3>Stage 2/3 — Insighta Labs</h3>
                        <p>Demographic Intelligence API with advanced filtering, natural language search, GitHub OAuth, JWT auth, role-based access, and Redis caching.</p>
                        <p><strong>Built:</strong> Auth system, NLP query parser, Redis caching layer</p>
                        <div><span class="tag">FastAPI</span><span class="tag">PostgreSQL</span><span class="tag">JWT</span><span class="tag">Redis</span></div>
                    </div>
                    <div class="project-card">
                        <h3>Stage 5 — Auth Features</h3>
                        <p>Logout with token blacklisting and guest session management with account migration flow.</p>
                        <p><strong>Built:</strong> Token blacklist middleware, guest-to-user migration endpoint</p>
                        <div><span class="tag">FastAPI</span><span class="tag">JWT</span><span class="tag">PostgreSQL</span></div>
                    </div>
                    <div class="project-card">
                        <h3>Stage 6 — Real-time Chat</h3>
                        <p>WebSocket endpoint with AI token streaming, rate limiting, message queuing, reconnection history, and context window management.</p>
                        <p><strong>Built:</strong> Full WebSocket handler, streaming AI integration, rate limiter</p>
                        <div><span class="tag">FastAPI</span><span class="tag">WebSockets</span><span class="tag">PostgreSQL</span></div>
                    </div>
                    <div class="project-card">
                        <h3>Stage 8a — Append-Only Event Store</h3>
                        <p>Crash-safe file-based event store where events.log is the database. No SQLite, no JSON rewrites — pure append-only with in-memory index for O(1) reads.</p>
                        <p><strong>Built:</strong> Entire service — append logic, byte-seek reads, crash recovery</p>
                        <div><span class="tag">FastAPI</span><span class="tag">File I/O</span><span class="tag">In-memory Index</span></div>
                    </div>
                </div>
            </section>

            <!-- SKILLS -->
            <section id="skills">
                <h2>Backend Skills</h2>
                <ul class="skills">
                    <li>API Design with FastAPI <span>Used across all HNG stages</span></li>
                    <li>Authentication — JWT, OAuth2, Role-based Access <span>Stages 2/3 and 5</span></li>
                    <li>Databases — PostgreSQL, SQLAlchemy, SQLite <span>Stages 1, 2, 5, 6</span></li>
                    <li>Caching with Redis <span>Stage 2/3 — reduced repeated DB queries</span></li>
                    <li>WebSockets & Real-time Systems <span>Stage 6 — live AI chat streaming</span></li>
                    <li>File I/O & Append-only Storage <span>Stage 8a — crash-safe event store</span></li>
                    <li>External API Integration <span>Stage 1 — 3 third-party APIs orchestrated</span></li>
                    <li>Token Blacklisting & Session Security <span>Stage 5</span></li>
                </ul>
            </section>

            <!-- FEATURED PROJECT -->
            <section id="featured">
                <h2>Featured Project — Append-Only Event Store</h2>
                <div class="featured">
                    <h3>The Problem</h3>
                    <p>On a platform with 2M MAUs, traditional databases rewrite data in place under heavy load — causing slowdowns and data loss during crashes. The challenge was to prototype a crash-safe storage layer using only a flat file.</p>

                    <h3>Architecture</h3>
                    <p>The log file <code>events.log</code> is the database. Every write appends a JSON line to the end of the file. An in-memory index (<code>Map&lt;id, &#123;offset, length&#125;&gt;</code>) tracks where each event lives in the file so reads never scan from the top.</p>
                    <p style="margin-top:0.5rem;">On startup, the server replays the log once to rebuild the index. After that, every read is a direct byte seek.</p>

                    <h3>Key Endpoints</h3>
                    <p><code>POST /events</code> — appends a new event, records byte offset and length in index, returns 201</p>
                    <p><code>GET /events/:id</code> — looks up index, seeks directly to offset, reads exactly length bytes — no file scan</p>
                    <p><code>GET /stats</code> — returns total event count and log file size in bytes</p>

                    <h3>Technical Challenge — Crash Recovery</h3>
                    <p>The hardest part was ensuring the index was always recoverable after a crash. The solution was to treat the log as the single source of truth — on every restart, the server streams the log line by line, rebuilds the index from byte offsets, and logs the recovered count. If a line is corrupted (e.g. server crashed mid-write), a try/except safely skips it without bringing down the whole recovery.</p>
                </div>
            </section>

            <!-- REFLECTION -->
            <section id="reflection">
                <h2>Learning Reflection</h2>
                <div class="reflection">
                    <p>Before HNG, I knew how to build APIs but I treated databases as black boxes. After Stage 8a, I understand what actually happens underneath — data is written sequentially to a file, a position is recorded, and reads jump directly to that byte. That mental model changed how I think about performance and crash safety.</p>
                    <p style="margin-top:1rem;">The WebSocket stage (Stage 6) taught me that not every FastAPI pattern works for persistent connections — JWT auth via <code>Depends()</code> doesn't work on WebSocket handshakes the same way it does on HTTP, which forced me to implement token verification through an init message instead. That kind of constraint teaches you more than any tutorial.</p>
                    <p style="margin-top:1rem;">Across all stages, the biggest shift was learning to read error messages carefully instead of guessing. Most bugs — including a Redis connection error in CI, a missed character in a UUID, and a broken environment variable — were solved by reading exactly what the terminal said.</p>
                </div>
            </section>

            <!-- CONTACT -->
            <section id="contact">
                <h2>Contact</h2>
                <div class="contact-grid">
                    <div class="contact-card">
                        <p>Email</p>
                        <a href="mailto:ezerichard100@gmail.com">ezerichard100@gmail.com</a>
                    </div>
                    <div class="contact-card">
                        <p>GitHub</p>
                        <a href="https://github.com/Richardeze" target="_blank">github.com/Richardeze</a>
                    </div>
                    <div class="contact-card">
                        <p>Location</p>
                        <p>Lagos, Nigeria — WAT (UTC+1)</p>
                    </div>
                </div>
            </section>

        </div>

        <footer>
            <p>Eze Richard &bull; Backend Engineer &bull; HNG Internship 2026 &bull; Built with FastAPI</p>
        </footer>

    </body>
    </html>
    """
    return HTMLResponse(content=html_content)