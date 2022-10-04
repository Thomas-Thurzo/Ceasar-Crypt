import tkinter as tk
from tkinter import ttk


# Funktionen
def perform_action():
    if selected_action.get() == "verschlüsseln":
        encrypted_input = encrypt(input_entry.get(), int(key_entry.get()))
        output_entry.delete(0, tk.END)
        output_entry.insert(0, encrypted_input)
    elif selected_action.get() == "entschlüsseln":
        decrypted_input = decrypt(input_entry.get(), int(key_entry.get()))
        output_entry.delete(0, tk.END)
        output_entry.insert(0, decrypted_input)
    else:
        print("Fehler")


def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + key - 65) % 26 + 65)
        else:
            result += chr((ord(char) + key - 97) % 26 + 97)
    return result


def decrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) - key - 65) % 26 + 65)
        else:
            result += chr((ord(char) - key - 97) % 26 + 97)
    return result


# Hauptfenster
fenster = tk.Tk()
fenster.title("Verschlüsselungs-Software")
foto = tk.PhotoImage(file="img/logo.png")
fenster.iconphoto(False, foto)

# Variablen
selected_action = tk.StringVar()

# Frames Responsive
fenster.columnconfigure(0, weight=1)
fenster.rowconfigure(2, weight=1)

# Input Frame
input_frame = ttk.Frame(fenster, padding=10)
input_frame.grid(column=0, row=0)

input_label = ttk.Label(input_frame, text="Nachricht:", font=("Arial", 16))
input_label.grid(column=0, row=0)

input_entry = ttk.Entry(input_frame, width=30, font=("Arial", 16))
input_entry.grid(column=1, row=0)

input_text_scroll = ttk.Scrollbar(input_frame, orient="horizontal", command=input_entry.xview)
input_text_scroll.grid(column=1, row=1, pady=1, sticky="ew")
input_entry.configure(xscrollcommand=input_text_scroll.set)

key_label = ttk.Label(input_frame, text="Key:", font=("Arial", 16))
key_label.grid(column=0, row=2)

key_entry = ttk.Entry(input_frame, width=3, font=("Arial", 16))
key_entry.grid(column=1, row=2, pady=5, sticky="w")

action_label = ttk.Label(input_frame, text="Operation:", font=("Arial", 16))
action_label.grid(column=0, row=3)

action_rb1 = ttk.Radiobutton(input_frame, text="Verschlüsseln", variable=selected_action, value="verschlüsseln")
action_rb1.grid(column=1, row=3, sticky="w")
action_rb2 = ttk.Radiobutton(input_frame, text="Entschlüsseln", variable=selected_action, value="entschlüsseln")
action_rb2.grid(column=1, row=4, sticky="w")

action_button = ttk.Button(input_frame, text="Operation ausführen", command=perform_action)
action_button.grid(column=0, row=5, columnspan=2, sticky="ew")

# Seperator
seperator = ttk.Separator(fenster)
seperator.grid(column=0, row=1, sticky="ew")

# Output Frame
output_frame = ttk.Frame(fenster, padding=10)
output_frame.grid(column=0, row=2)

output_label = ttk.Label(output_frame, text="Ergebnis:", font=("Arial", 16))
output_label.grid(column=0, row=0)

output_entry = ttk.Entry(output_frame, width=30, font=("Arial", 16))
output_entry.grid(column=1, row=0)

# Mainloop
fenster.mainloop()
