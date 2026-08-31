"""
All editable content for the portfolio lives here.
Update these values with your own info — no HTML editing required.
"""

PROFILE = {
    "name": "Your Name",
    "title": "Software Engineer / AI Backend Developer",
    "grad_year": "2026",
    "university": "Your University",
    "major": "Computer Science",
    "intro": (
        "I'm a software engineer focused on AI-powered backend systems — "
        "designing APIs, data pipelines, and infrastructure that let machine "
        "learning models actually ship. I like clean architecture, well-tested "
        "code, and turning research into production-ready systems."
    ),
    # Add your quote later, e.g. "Code is poetry that compiles."
    "quote": "",
    "quote_author": "",
    # Add your photo to static/images/ and point to it here, e.g.
    # "photo": "/static/images/profile.jpg"
    "photo": "",
    "email": "you@example.com",
    "socials": {
        "github": "https://github.com/yourusername",
        "linkedin": "https://linkedin.com/in/yourusername",
    },
}

# Each project supports an optional "video" (local file in static/videos/
# or a YouTube/Vimeo URL) shown in the horizontal video-demo scroller.
PROJECTS = [
    {
        "name": "Project One",
        "description": (
            "A short, clear description of what this project does and the "
            "problem it solves."
        ),
        "role": "Backend Engineer — designed the API and data layer",
        "tags": ["Python", "FastAPI", "PostgreSQL"],
        "video": "",  # e.g. "/static/videos/project-one.mp4" or a YouTube URL
        "link": "",   # optional live link or repo URL
    },
    {
        "name": "Project Two",
        "description": (
            "A short, clear description of what this project does and the "
            "problem it solves."
        ),
        "role": "AI Engineer — built and served the inference pipeline",
        "tags": ["PyTorch", "Docker", "AWS"],
        "video": "",
        "link": "",
    },
    {
        "name": "Project Three",
        "description": (
            "A short, clear description of what this project does and the "
            "problem it solves."
        ),
        "role": "Full-Stack — end-to-end ownership from backend to UI",
        "tags": ["Flask", "React", "Redis"],
        "video": "",
        "link": "",
    },
]
