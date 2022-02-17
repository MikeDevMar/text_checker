from tkinter import *

import time
start_time = time.time()

text ="We and our partners are using technologies like cookies and process personal data like the IP-address or browser" \
      " information in order to personalize the advertising that you see. This helps us to show you more relevant ads and" \
      " improves your internet experience. We also use it in order to measure results or align our website content. Because" \
      " we value your privacy, we are herewith asking for your permission to use these technologies. You can always change/withdraw" \
      " your consent later by clicking on the settings button on the left lower corner of the page."
letter =[]
def say_something():
    input_text.config(state='disabled')
    required_text = input_text.get()
    for letters in required_text:
        letter.append(letters)
    no_letter = len(letter)
    the_result = Label(fg='black', text=f'your results says you can type {no_letter / num} letters per second', font=('arial.ttf', 15))
    the_result.pack()
    letter.clear()
    time.sleep(3)
    input_text.config(state='normal')
    input_text.delete(0,'end')



def start_playing_easy():
    global num
    num = 120
    window.after(120000, say_something)

def start_playing_medium():
    global num
    num = 60
    window.after(60000, say_something)

def start_playing_hard():
    global num
    num = 30
    window.after(30000, say_something)


window = Tk()
window.title('Typing Speed Tester')
window.minsize(width=700,height=700)
welcome_label = Label(fg='black', text='Welcome to the typing speed tester', font=('arial.ttf', 28))
welcome_label.pack(padx=10, pady=10)
task_label = Label(fg='black', text='type the text below in the box as fast as you can:', font=('arial.ttf',18))
task_label.pack(padx=10, pady=10)
test_text =Text(width=60, height=8)
test_text.insert(1.0, text)
test_text.config(state='disabled',fg='red', font=('arial.ttf', 12))
test_text.pack(padx=10, pady=10)
input_text = Entry(width=40,font=('arial.ttf', 12))
input_text.pack(padx=10, pady=10)
start_easy_button = Button(text='2 minute', font=('arial.ttf', 10), command=start_playing_easy)
start_easy_button.pack(padx=10, pady=10)
start_medium_button = Button(text='1 minutes', font=('arial.ttf', 10), command=start_playing_medium)
start_medium_button.pack(padx=10, pady=10)
start_hard_button = Button(text='30 seconds', font=('arial.ttf', 10), command=start_playing_hard)
start_hard_button.pack(padx=10, pady=10)


window.mainloop()

