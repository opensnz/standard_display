import tkinter as tk

def key_press(key):
    
    text_entry.insert(tk.END, key)

def clear_text():
    
    text_entry.delete(0, tk.END)

def create_keyboard(root):
    buttons = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
        ['@','-','.','_'],
    ]

    special_buttons = [
        ['Effacer'],
    ]

    for row in buttons + special_buttons:
        button_frame = tk.Frame(root)
        button_frame.pack(side=tk.TOP, pady=5)

        for key in row:
            if key == 'Effacer':
                button = tk.Button(button_frame, text=key, width=5, command=clear_text)
            else:
                button = tk.Button(button_frame, text=key, width=5, command=lambda key=key: key_press(key))
            button.pack(side=tk.LEFT, padx=5)

window = tk.Tk()
window.title("Clavier virtuel")

text_entry = tk.Entry(window, width=50)
text_entry.pack(pady=10)

create_keyboard(window)

window.mainloop()
