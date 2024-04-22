from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('uploaded_profile_picture.jpg')  
        return 'Profile picture uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True)
