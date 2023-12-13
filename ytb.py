from flask import Flask, request, send_file, render_template
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    url = request.form.get('text_input')
    if not url:
        return "Aucune URL fournie", 400

    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    filename = video.title + ".mp4"
    video.download(output_path='C:\\Users\\louis\\OneDrive\\Bureau\\web-dev\\YTB_downloader', filename=filename)

    filepath = 'C:\\Users\\louis\\OneDrive\\Bureau\\web-dev\\YTB_downloader\\' + filename
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
