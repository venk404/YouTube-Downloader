from flask import Flask, request, render_template, session, jsonify, send_file
from io import BytesIO
from pytube import YouTube

app = Flask(__name__)


@app.route("/")
def Index():
    return render_template("Index.html")


@app.route("/api/download", methods=["GET", "POST"])
def download_video():
    username = request.args.get('entry1_id')
    formate = request.args.get('entry_id')
    if request.method == "GET":
        buffer = BytesIO()
        yt = YouTube(username)
        titleofvideo = yt.title
        stream = yt.streams.get_by_itag(int(formate))
        stream.stream_to_buffer(buffer)
        buffer.seek(0)
        title = titleofvideo + '.mp4'
        return send_file(buffer, as_attachment=True, download_name=title, mimetype='video/mp4')
    else:
        return "Fail"


@app.route("/api/fillformat", methods=["GET", "POST"])
def fillformat():
    username = request.args.get('entry1_id')
    yt = YouTube(username)  # Download YouTube Rewind 2019
    dicto = {}
    streamfil = yt.streams.filter(progressive=True, type="video")
    for stream in streamfil:
        dicto[stream.resolution] = stream.itag
    return dicto


@app.route("/api/thumbnail", methods=["GET", "POST"])
def thumbnail():
    username = request.args.get('entry1_id')
    yt = YouTube(username)
    send_thumbnails = []
    send_thumbnails.append(yt.thumbnail_url)
    send_thumbnails.append(yt.title)
    return send_thumbnails


if __name__ == '__main__':
    app.run(debug=True)
