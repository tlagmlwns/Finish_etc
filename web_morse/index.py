from flask import Flask, request
from flask import render_template
from morse import MorseCodeTranslator

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/morse_decoding", methods=["POST", "GET"])
def morse_decoding():
    if request.method == "POST":
        inputMorse = request.form.get("inputMorse")
        # 코드를 넣어주세요.
        morse_translator = MorseCodeTranslator() 
        
        inputMorset_M = set(inputMorse) # 부호 확인용
        if inputMorset_M.issubset(['-','.',' ']): 
            english_text = morse_translator.morse_to_english(inputMorse)
            print("Morse -> English",english_text)
            program_result = english_text
        elif inputMorse.isalpha():
            morse_text = morse_translator.english_to_morse(inputMorse)
            print("Englist -> Morse",morse_text)
            program_result = morse_text
        else:
            program_result='ERROR'
        #english_text = morse_translator.morse_to_english(inputMorse)
        #english_text = inputMorse

        return render_template("index.html", result=program_result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100)
