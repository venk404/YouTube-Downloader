from flask import Flask,request,render_template,session,jsonify,send_file
from io import BytesIO
from pytube import YouTube

import sys

app = Flask(__name__)


@app.route("/")
def Index():
    return render_template("Index.html")


@app.route("/api/download", methods = ["GET","POST"])
def download_video():
    username = request.args.get('entry1_id')
    formate = request.args.get('entry_id')
    if request.method == "GET":
            buffer = BytesIO()
            #pag.alert(text=username, title="The Hello World Box")
            yt = YouTube(username)
            yttitle = yt.title
            stream = yt.streams.get_by_itag(int(formate))
            stream.stream_to_buffer(buffer)
            buffer.seek(0)
            title = yttitle +'.mp4'
            return send_file(buffer,as_attachment=True, download_name=title, mimetype='video/mp4')          
    else:
            return "failer"
 
@app.route("/api/fillformat", methods = ["GET","POST"])
def fillformat():
        # video_resolutions = []
        # videos = []
       
        username = request.args.get('entry1_id')
        yt = YouTube(username)  # Download YouTube Rewind 2019   
        #kaam = yt.streams.filter(adaptive=True,type="video").all()
        # for i in range(0,len(kaam)):
        #     itag_res[kaam[i].itag] = kaam[i].resolution
        #     print(kaam[i].resolution)
        #     print(kaam[i].itag,end="\n")
        # print(itag_res)
        dicto = {}
        kaam = yt.streams.filter(progressive=True,type="video")
        for stream in kaam:
            dicto[stream.resolution] = stream.itag          #dictoty for resolution(key) + itag(value)
        return dicto
      

@app.route("/api/thumbnail", methods = ["GET","POST"])
def thumbnail():
    username = request.args.get('entry1_id')
    A = YouTube(username)
    Ak = []
    Ak.append(A.thumbnail_url)
    Ak.append(A.title)
    return Ak


        

if __name__ == '__main__':
    app.run(debug=True)