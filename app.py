from flask import Flask, render_template

from data import PROFILE, PROJECTS, EXPERIENCE

app = Flask(__name__)


def video_kind(url: str) -> str:
    """Classify a video source so the template knows how to embed it."""
    if not url:
        return "none"
    lowered = url.lower()
    if "youtube.com" in lowered or "youtu.be" in lowered:
        return "youtube"
    if "vimeo.com" in lowered:
        return "vimeo"
    return "local"


def youtube_embed_url(url: str) -> str:
    if "youtu.be/" in url:
        video_id = url.split("youtu.be/")[-1].split("?")[0]
    else:
        video_id = url.split("v=")[-1].split("&")[0]
    return f"https://www.youtube.com/embed/{video_id}"


def vimeo_embed_url(url: str) -> str:
    video_id = url.rstrip("/").split("/")[-1].split("?")[0]
    return f"https://player.vimeo.com/video/{video_id}"


@app.context_processor
def inject_helpers():
    return {
        "video_kind": video_kind,
        "youtube_embed_url": youtube_embed_url,
        "vimeo_embed_url": vimeo_embed_url,
    }


@app.route("/")
def index():
    return render_template(
        "index.html", profile=PROFILE, projects=PROJECTS, experience=EXPERIENCE
    )


if __name__ == "__main__":
    app.run(debug=True)
