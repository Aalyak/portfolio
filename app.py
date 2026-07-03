from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/download_resume')
def download_resume():
    return send_from_directory(
        'static',
        'Aalya_Krishnan_Resume_.pdf',
        as_attachment=True
    )

@app.route('/test')
def test():
    return "WORKING"

if __name__ == '__main__':
    app.run(debug=True)
