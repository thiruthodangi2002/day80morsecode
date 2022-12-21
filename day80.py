from tkinter import *

MORSE_CODE_DICT = { 'A':'.-',
                    'B':'-...',
                    'C':'-.-.',
                    'D':'-..',
                    'E':'.',
                    'F':'..-.',
                    'G':'--.',
                    'H':'....',
                    'I':'..',
                    'J':'.---',
                    'K':'-.-',
                    'L':'.-..',
                    'M':'--',
                    'N':'-.',
                    'O':'---',
                    'P':'.--.',
                    'Q':'--.-',
                    'R':'.-.',
                    'S':'...',
                    'T':'-',
                    'U':'..-',
                    'V':'...-',
                    'W':'.--',
                    'X':'-..-',
                    'Y':'-.--',
                    'Z':'--..',
                    '1':'.----',
                    '2':'..---',
                    '3':'...--',
                    '4':'....-',
                    '5':'.....',
                    '6':'-....',
                    '7':'--...',
                    '8':'---..',
                    '9':'----.',
                    '0':'-----',
                    ', ':'--..--',
                    '.':'.-.-.-',
                    '?':'..--..',
                    '/':'-..-.',
                    '-':'-....-',
                    '(':'-.--.',
                    ')':'-.--.-'}


def convert():
    message = text_input.get().upper()

    encrypt=""
    for letter in message :
        if letter != " ":
            encrypt += MORSE_CODE_DICT[letter] + ' '
        else:
            encrypt += "  "

    translated_text.config(text=encrypt)




window = Tk()
window.title("Morse Code Translator")
window.geometry("500x200")
window.eval("tk::PlaceWindow . center")

app_name = Label(text="Text to Morse Code", font="Arial 24 bold")
app_name.grid(row=0, column=0, columnspan=2)
text_input = Entry(width=30)
text_input.grid(row=1, column=1)

convert_button = Button(text="Encrypt", command=convert)
convert_button.grid(row=2, column=1)

translated_text = Label(text="", font="Arial 20 bold")
translated_text.grid(row=3, column=1)

window.mainloop()