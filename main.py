import tkinter as tk
Fgame = tk.Tk()
height = 500
width = 500
def sum_guesses(previous_guesses:list = None) -> str:
    aggregate_word = ""
    if previous_guesses:
        for chars in zip(*previous_guesses):
            aggregate_word += sorted(set(chars))[-1]
    return aggregate_word
words = ['aggro', 'flank', 'flick', 'tiles', 'baths', 'cubby', 'swing', 'entry', 'round', 'match', 'force', 'haven', 'molly', 'creds', 'angle', 'split', 'sewer', 'plant', 'smoke', ]

def guess(entry):
    print("Thisd")






mainframe = tk.Canvas(Fgame, height=height, width=width, bg='yellow')
mainframe.pack()
label = tk.Label(mainframe, text='5 LETTER GUESS THE WORD', bg='red')
label.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.1)
label1 = tk.Label(mainframe, text='1', bg='green', font='80')
label1.place(relx=0.25, rely=0.22, relwidth=0.5, relheight=0.38)

entry = tk.Entry(mainframe, bg='white', )
entry.place(relx=0.3, rely=0.62,relwidth=0.4, relheight=0.07)

fbutton = tk.Button(mainframe,text="yeah boi", pady=-10, bg="blue", command=lambda: guess(entry.get()))
fbutton.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.06)




for word in words:
    hiddenl = []
    while True:
        print(sum_guesses(hiddenl))
        guess = input("Guess the Word! : ")
        guessl = [letter for letter in guess]
        wordl = [letter for letter in word]
        if guessl == wordl:
            label1['text']= (f"Well Done! The Word is {guessl}")
            break
        else:
            label1['text']=("Try Again!")
            guessed = [x for x in guessl if x in wordl]
            hidden = ''
            for letter in word:
                if letter in guessed:
                    hidden = hidden + letter
                else:
                    hidden = hidden + '*'
            hiddenl.append(hidden)

Fgame.mainloop()

