import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = "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"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(question),
            temperature=0.6,
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(question):
    return """
    {}
    """.format(
        question.capitalize()
    )
if __name__ == '__main__':
    app.run()
