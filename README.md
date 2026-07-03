# Aalya Krishnan U — Portfolio

Dark-themed Flask portfolio with animations, skill logos, and separate pages.

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

## Deploy Free on Render

1. Push this folder to a GitHub repo
2. Go to render.com → New → Web Service
3. Connect your GitHub repo
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`
6. Deploy!

## Deploy Free on Railway

1. Push to GitHub
2. Go to railway.app → New Project → Deploy from GitHub
3. It auto-detects Flask and deploys!

## Pages

- `/` — Hero landing page
- `/about` — About, education, tags
- `/skills` — Skill logos by category
- `/projects` — All 9 projects
- `/experience` — Internships + certifications
- `/contact` — Contact info + form
