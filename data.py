"""
All editable content for the portfolio lives here.
Update these values with your own info — no HTML editing required.
"""

PROFILE = {
    "name": "Mariam Elsoufy",
    "title": "Software Engineer / AI Backend Developer",
    "grad_year": "2026",
    "university": "Cairo University - STEP",
    "major": "Communication and Computer Engineering - Computer Track",
    "intro": (
        "I'm a software engineer focused on AI-powered backend systems — "
        "designing APIs, data pipelines, and infrastructure that let machine "
        "learning models actually ship. I like clean architecture, well-tested "
        "code, and turning research into production-ready systems."
    ),
    # Add your quote later, e.g. "Code is poetry that compiles."
    "quote": "Powered by Coding and Iced Coffee ",
    "quote_author": "",
    "photo": "/static/images/mariam.jpg",  # e.g. "/static/images/profile.jpg"
    "resume": "/static/resume/MariamElsoufy_Resume.pdf",
    "email": "mariammelsoufy@gmail.com",
    "socials": {
        "github": "https://github.com/mariamelsoufy",
        "linkedin": "https://www.linkedin.com/in/mariamelsoufy/",
    },
}

# Each entry is a past role: "role", "company", "duration" (shown as a
# badge), a "description", and optional "tags".
EXPERIENCE = [
    {
        "role": "Core Banking Development Intern",
        "company": "SAIB Bank",
        "duration": "Aug 2025 – Sep 2025",
        "description": (
"Developed a device inventory management system for tracking bank-issued assets, Designed and implemented database schemas, Enums, and relationships for devices, users, and actions, and explored Temenos T24 core banking system"
        ),
        "tags": ["Temenos T24", "C#", "SQL Server", "Database Design"],
    },
        {
        "role": "IT & Security Intern",
        "company": "Enppi",
        "duration": "Aug 2024 – Sep 2024",
        "description": (
"Configured Cisco switches, developed low-code web applications, and worked on Python-based data analysis and visualization"
        ),
        "tags": ["Cisco", "Python", "Data Analysis", "Low-Code Development"],
    },
]

# Each project supports an optional "video" (local file in static/videos/
# or a YouTube/Vimeo URL) shown beside its description, a "github" link to
# the repo, and a "logo" image (local file in static/images/). If "logo" is
# left blank, the project's initial is shown instead.
PROJECTS = [
    {
        "name": "IMMERSA",
        "description": (
            "An AI backend for an interactive AR historical experience, enabling users to have real-time voice conversations with AI-powered historical characters. Developed an asynchronous 5-stage pipeline for audio preprocessing, Speech-to-Text, FAQ/LLM processing, Text-to-Speech, and WebSocket streaming. Integrated multiple AI services through APIs and optimized the system for low-latency real-time communication, achieving under 1.5 seconds from end of speech to response."
        ),
        "role": "Backend AI Engineer",
        "tags": ["Python", "FastAPI", "WebSocket", "OpenAI API", "ElevenLabs API"],
        "video": "/static/videos/immersa.mp4",  # e.g. "/static/videos/project-one.mp4" or a YouTube URL
        "github": "https://github.com/MariamElsoufy/IMMERSA-Voice-Chat-API",  # e.g. 
        "logo": "/static/images/immersa.png",  # e.g. "/static/images/immersa-logo.png"
    },
    {
        "name": "E7gezly",
        "description": (
        "A complete booking platform for football and padel courts using C# and Microsoft SQL Server. Implemented user features for court booking, reviews, and complaints, along with trainer and manager modules for court reviews, tournament management, and maintenance requests. Built admin functionality for managing complaints and platform operations, with a structured database supporting the different user roles and workflows."
        ),
        "role": "Backend Developer",
        "tags": ["C#", "Microsoft SQL Server", ".NET", "Database Design"],
        "video": "/static/videos/e7gezly.mp4",
        "github": "https://github.com/youssefsaher26/Ehgezly",
        "logo": "/static/images/e7gezly.png",
    },
    {
            "name": "TawasolApp – LinkedIn-Style Social Networking App",
            "description": (
                "A LinkedIn-style Android application using Flutter and Dart with social networking, search, privacy, and premium subscription features. Implemented connection and follow workflows, user blocking and reporting, and search across users, posts, jobs, and companies. Integrated Stripe for secure premium subscription payments and built a structured mobile experience around multiple user interactions."
            ),
            "role": "Flutter Developer",
            "tags": ["Flutter", "Dart", "Android Development", "Stripe", "Mobile Development"],
            "video": "/static/videos/tawasol.mp4",
            "github": "",
            "logo": "",
        },
        {
        "name": "Python Malware Detection Tool Using YARA",
        "description": (
            "A Python-based malware detection tool that analyzes files using custom YARA rules to identify suspicious patterns and potential malicious behavior. Designed detection rules for different malware indicators and integrated YARA scanning into a Python application. The project focused on automated file analysis, rule-based detection, and presenting clear results to help identify potentially malicious files."
        ),
        "role": "Python Developer",
        "tags": ["Python", "YARA", "Malware Analysis", "Automation", "Malware Analysis"],
        "video": "",
        "github": "https://github.com/MariamElsoufy/Malware-Detector-using-python-and-yara-rules",
        "logo": "",
    },
    
]
