from flask import Flask, render_template, request, redirect, url_for
# import tempfile
# import os
# import speech_recognition as sr


app = Flask(__name__)

# recognizer = sr.Recognizer()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit_text', methods=['POST'])
def submit_text():
   
    text = request.form.get('text')
    return render_template('result.html', text = text + "submit_text")


# @app.route('/submit_audio', methods=['POST'])
# def submit_audio():
#     if request.method == "POST":
#         audio_file = request.files['audio_data']
    

#     if audio_file:
#         print("hellooo")
#         with tempfile.NamedTemporaryFile(delete=False) as temp_audio_file:
#             audio_file.save(temp_audio_file.name)

#             # Recognize the captured audio
#             with sr.AudioFile(temp_audio_file.name) as source:
#                 try:
#                     audio = recognizer.record(source)  # Record the audio
#                     text = recognizer.recognize_google(audio)
#                     os.remove(temp_audio_file.name)  # Remove the temporary audio file
#                     return render_template('result.html', text=text)
#                 except sr.UnknownValueError:
#                     return render_template('result.html', text="Unable to transcribe audio.")
#                 except sr.RequestError as e:
#                     return render_template('result.html', text=f"An error occurred: {str(e)}")
#     return render_template('result.html', text="No audio received.")


if __name__ == '__main__':
    app.run(debug=True)
