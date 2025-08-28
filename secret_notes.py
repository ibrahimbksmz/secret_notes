from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import base64
import csv


# ============            FUNCTIONS            ============

def encrypt(input_text : str) -> str:
    # encryption steps
    input_text_bytes = input_text.encode('utf-8')
    input_text_b64_bytes = base64.b64encode(input_text_bytes)
    input_text_b64_str = input_text_b64_bytes.decode('utf-8')
    return input_text_b64_str

def decrypt(input_base64_text: str):
    # decryption steps
    input_text_b64_bytes = input_base64_text.encode('utf-8')
    input_text_bytes = base64.b64decode(input_text_b64_bytes)
    input_text_str = input_text_bytes.decode('utf-8')
    return input_text_str

def key_control(secret_notes_text_input: str, input_master_key_entry: str):
    # take control master key and base64 text info
    control_master_key = input_master_key_entry.get()
    input_text = secret_notes_text_input.get("1.0", END).strip()

    if control_master_key == "" or input_text == "":
        messagebox.showinfo('INFO', 'Empty input!')
    else:
        if find_base64_text(input_text)[1] != None:
            master_key = decrypt(find_base64_text(input_text)[1])
            input_text_str = decrypt(input_text)

            if master_key == control_master_key:
                secret_notes_text_input.delete("1.0", END)
                input_master_key_entry.delete(0, END)
                secret_notes_text_input.insert("1.0", input_text_str)
            else:
                messagebox.showerror("INFO", "Your note does not match your master key")
        else:
            messagebox.showerror("INFO", "Your note not found.")

def save_encrypt(note_title_input : "widget entry", secret_notes_text_input : "widget text",master_key_input : "widget entry"):
    # get widget info
    notes_title = note_title_input.get()
    note_text = secret_notes_text_input.get("1.0", END)
    master_key = master_key_input.get()

    if note_text == "" or master_key == "" or notes_title == "":
        messagebox.showinfo('INFO', 'Empty input')
    else:

       # encrypt note and master key
       encrypted_notes = encrypt(note_text)
       encrypted_master_key = encrypt(master_key)

       # "encrypted master key : base64_text" file
       global note_file
       file = open(note_file, "a")
       file.write(f"{notes_title},{encrypted_notes},{encrypted_master_key}\n")
       file.flush()
       file.close()

       # widget input delete
       note_title_input.delete(0, END)
       secret_notes_text_input.delete("1.0", END)
       master_key_input.delete(0, END)

def find_base64_text(base64_text_note):
    global note_file
    with open(note_file, "r") as file:
        file_csv = csv.reader(file)
        # continue header
        next(file_csv, None)

        for line in file_csv:
            if len(line) != 3:
                continue

            a, b, c = line
            if b == base64_text_note:
                return [b,c]

    return [None,None]


#============            WIDGET AND FILE            ============

# create file
note_file ="secret_notes.txt"
create_file = open(note_file,"a+")
create_file.write("note title,encrypted text,encrypted master key\n")
create_file.close()

# create screen
screen = Tk()
screen.geometry("400x700")
screen.title("Secret Notes")

# add image
resize_image = Image.open("logo.png").resize((100, 100))
image = ImageTk.PhotoImage(resize_image, master=screen)
label = Label(screen,image=image)
label.pack(pady=50)

# add note title lable and entry
note_title_label = Label(screen,text="Enter your title",font=("Courier",15))
note_title_label.pack()

note_title_entry = Entry(screen, relief="solid")
note_title_entry.pack()

# add secret label and entry
secret_notes_label = Label(screen,text="Enter your secret note or encrypted note", font=("Courier",15))
secret_notes_label.pack()

secret_notes_text = Text(screen,width=40,height=20, relief="solid")
secret_notes_text.pack()

# add masterkey title
master_key_title = Label(screen,text="Enter master Key",font=("Courier",15))
master_key_title.pack()

master_key_entry = Entry(screen, relief="solid",show="*")
master_key_entry.pack()

# save&encrypt button
save_encrypt_button = Button(screen,text="Save & Encrypt",font = "Courier",activeforeground="red",cursor="hand2",command= lambda : save_encrypt(note_title_entry,secret_notes_text,master_key_entry))
save_encrypt_button.pack()

# decrypt button
decrypt_button = Button(screen,text="Decrypt",font = "Courier" ,activeforeground="blue",cursor="hand2", command= lambda : key_control(secret_notes_text,master_key_entry))
decrypt_button.pack()

screen.mainloop()
