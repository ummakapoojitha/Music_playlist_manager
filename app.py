from flask import Flask, render_template, request

app = Flask(__name__)

songs = []

@app.route("/")
def home():
    return render_template("index.html", songs=songs)

@app.route("/add", methods=["POST"])
def add_song():
    title = request.form["title"]
    artist = request.form["artist"]

    songs.append({
        "title": title,
        "artist": artist
    })

    return render_template("index.html", songs=songs)

if __name__ == "__main__":
    app.run(debug=True)
