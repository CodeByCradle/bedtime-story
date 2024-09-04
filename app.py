from flask import Flask, render_template
from model import BedTimeStory


app = Flask(__name__) 

@app.route("/")
def index():
    titles = BedTimeStory().get_story_titles()
    return render_template("index.html", titles = titles)


@app.route("/<title>")
def handle_story(title):
    content = BedTimeStory().get_story(title)
    return render_template("story.html", title=title, story_content=content)


if __name__ == "__main__": 
    app.run(debug=True)