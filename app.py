from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.config["SECRET_KEY"] = "12345"
debug = DebugToolbarExtension(app)


@app.route("/")
def get_prompt():
    prompts = story.prompts

    return render_template("prompts.html", prompts=prompts)


@app.route("/story")
def display_story():
    text = story.generate(request.args)

    return render_template("story.html", text=text)
