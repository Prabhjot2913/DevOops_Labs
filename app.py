# app.py
import django
from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.management import execute_from_command_line

# Step 1: Configure Django
settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    SECRET_KEY="abc123",
    ALLOWED_HOSTS=["*"],
)

# Step 2: Create a simple view
def home(request):
     return HttpResponse("""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Academic Demo</title>
  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --accent:#7dd3fc;
      --muted:#94a3b8;
    }
    html,body{height:100%;margin:0;font-family:Inter,Segoe UI,Roboto,Arial,sans-serif;background:var(--bg);color:#e6eef8}
    .wrap{
      min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px;
    }
    .card{
      width:min(880px,96%);background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border:1px solid rgba(255,255,255,0.03);backdrop-filter: blur(6px);
      padding:36px;border-radius:12px;box-shadow: 0 10px 30px rgba(2,6,23,0.6);
    }

    /* Typing heading */
    .title {
      font-size: clamp(20px, 3.8vw, 36px);
      font-weight:700;
      color:var(--accent);
      white-space:nowrap;
      overflow:hidden;
      border-right: 3px solid var(--accent);
      width:0;
      animation: typing 3.2s steps(36,end) forwards, blink 1s step-end infinite;
      margin:0 0 12px 0;
    }
    @keyframes typing{
      from { width:0 }
      to   { width: 100% }
    }
    @keyframes blink{
      50% { border-color: transparent }
    }

    /* Subheading fade-in */
    .sub{
      color:var(--muted);margin:6px 0 18px 0;font-size:16px;opacity:0;transform:translateY(8px);
      animation: fadeup 1s 3.6s ease forwards;
    }
    @keyframes fadeup{
      to { opacity:1; transform:translateY(0) }
    }

    /* Animated academic keywords */
    .keywords{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}
    .chip{
      padding:8px 12px;border-radius:999px;background:rgba(125,211,252,0.07);
      color:var(--accent);border:1px solid rgba(125,211,252,0.08);font-weight:600;font-size:14px;
      transform-origin:center;
      animation: pop 1s ease forwards;
    }
    .chip:nth-child(1){animation-delay:4.0s}
    .chip:nth-child(2){animation-delay:4.15s}
    .chip:nth-child(3){animation-delay:4.30s}
    .chip:nth-child(4){animation-delay:4.45s}
    .chip:nth-child(5){animation-delay:4.60s}

    @keyframes pop{
      from{opacity:0; transform:scale(.6) translateY(6px)}
      to{opacity:1; transform:scale(1) translateY(0)}
    }

    .footer { margin-top:20px;color:#9fb0c9;font-size:13px;opacity:.9 }
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <h1 class="title">Academic DevOps — Demo Application</h1>
      <p class="sub">A tiny demo page showing animated text for your MSc DevOps portfolio. Use this as an example homepage for CI/CD and deployment labs.</p>

      <div class="keywords" aria-hidden="true">
        <div class="chip">Version Control</div>
        <div class="chip">CI/CD</div>
        <div class="chip">Containerisation</div>
        <div class="chip">Automation Deploy</div>
      
      </div>

      <p class="footer">Tip: this page can be Dockerised and deployed to Render / PythonAnywhere, then connected to your CI pipelines.</p>
    </div>
  </div>
</body>
</html>
""", content_type="text/html")

# Step 3: Define URL pattern
urlpatterns = [
    path("", home),
]

# Step 4: Run server if executed directly
if __name__ == "__main__":
    execute_from_command_line(["manage.py", "runserver", "0.0.0.0:8000"])
