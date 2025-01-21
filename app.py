from flask import Flask, render_template, url_for
import os
import glob

app = Flask(__name__)

# Define the path to your static folder
app.static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

@app.route('/')
@app.route('/use-case-1')
def use_case_1():
    return render_template('index.html', active_page='use-case-1')

@app.route('/use-case-2')
def use_case_2():
    return render_template('use-case-2.html', active_page='use-case-2')

# Ensure video can be served
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    # Verify the video file exists
    video_path = os.path.join(app.static_folder, 'liquidVideo.mp4')
    if not os.path.exists(video_path):
        print(f"Warning: Video file not found at {video_path}")
    app.run(debug=True) 