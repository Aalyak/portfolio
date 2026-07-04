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

@app.route('/projects/adhd')
def project_adhd():
    return render_template('project_adhd.html')

@app.route('/projects/iot')
def project_iot():
    return render_template('project_iot.html')

@app.route('/projects/studentapi')
def project_studentapi():
    return render_template('project_studentapi.html')

@app.route('/projects/jacc')
def project_jacc():
    return render_template('project_jacc.html')

@app.route('/projects/emotion')
def project_emotion():
    return render_template('project_emotion.html')

if __name__ == '__main__':
    app.run(debug=True)

