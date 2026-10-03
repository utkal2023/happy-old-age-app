from flask import Flask, render_template, request
import random

from countries import COUNTRIES

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    country = None
    name = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if name:
            country = random.choice(COUNTRIES)

    return render_template(
        "index.html",
        name=name,
        country=country
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
