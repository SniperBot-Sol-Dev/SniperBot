import webbrowser

from flask import Flask, render_template, send_from_directory

# Initialize Flask application
app = Flask(__name__)

# Define the home route to serve the index.html file
@app.route('/')
def home():
    return render_template('index.html')  # Looks for index.html in the templates folder
@app.route('/settings.js')
def serve_settings():
    # Serve the file from the 'static/js/' directory
    return send_from_directory('static/js', 'settings.js')
# Run the app
if __name__ == '__main__':
    webbrowser.open("http:/127.0.0.1:5000")
    app.run(debug=True)  # Enables debugging mode for easier development
