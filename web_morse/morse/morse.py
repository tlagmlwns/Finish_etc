class MorseCodeTranslator:
    def __init__(self):
        self.english_dict = {
            "A": ".-", "B": "-...", "C": "-.-.",
            "D": "-..", "E": ".", "F": "..-.",
            "G": "--.", "H": "....", "I": "..",
            "J": ".---", "K": "-.-", "L": ".-..",
            "M": "--", "N": "-.", "O": "---",
            "P": ".--.", "Q": "--.-", "R": ".-.",
            "S": "...", "T": "-", "U": "..-",
            "V": "...-", "W": ".--", "X": "-..-",
            "Y": "-.--", "Z": "--.."," ": ""
        }
        self.morse_dict = {value: key for key, value in self.english_dict.items()}
    def english_to_morse(self, english_text):

        #print(self.english_dict)
        morse_text = ""
        for char in english_text:
            if char.upper() in self.english_dict:
                morse_text += self.english_dict[char.upper()] + " "
            else:
                # ignore characters that are not in the dictionary
                pass
        return morse_text
    
    def morse_to_english(self, morse_text):
        english_text = ""
        morse_words = morse_text.strip().split(" ")
        #print("morse[] >>",morse_words)
        for morse_word in morse_words:
            morse_chars = morse_word.split(" ")

            for morse_char in morse_chars:
                if morse_char in self.morse_dict:
                    english_text += self.morse_dict[morse_char]
                else: #ignore characters that are not in the dictionary
                    pass
        english_text += " "
        return english_text