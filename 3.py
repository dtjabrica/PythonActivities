import tkinter as tk


def encryption():
    plaintext = input_entry.get()
    ciphertext = ""
    for char in plaintext:
        if char.isdigit():
            ciphertext += str((int(char) + 1) % 99)
        elif char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            ciphertext += chr((ord(char) - ascii_offset + 1) % 26 + ascii_offset)
        else:
            ciphertext += char
    output.config(state=tk.NORMAL)
    output.delete(1.0, tk.END)
    output.insert(tk.END, ciphertext)


root = tk.Tk()
root.configure(bg='gold')
root.title("Group 3's Encryption Tool")

# Create header
header = tk.Label(root, text="Encryption Tool", fg='#212121', bg='gold', font=('Fixedsys', 40))
header.pack()

# Create separator line
separator = tk.Frame(root, height=2, bg='#212121')
separator.pack(fill=tk.X, pady=5)

# Create labels and entry widget
label1 = tk.Label(root, text="Input text:", fg='#212121', bg='#F2F2F2', font=('FixedSys', 20))
label1.pack()

input_entry = tk.Entry(root, width=50, borderwidth=3, fg='#212121', bg='#F2F2F2', font=('FixedSys', 20))
input_entry.pack(padx=10, pady=10)

# Create button and output widget
button = tk.Button(root, text="Encrypt", borderwidth=5, command=encryption, fg='#212121', bg='#F2F2F2',
                   font=['FixedSys', 25])
button.pack(padx=10, pady=10)

label2 = tk.Label(root, text="Ciphered input:", fg='#212121', bg='#F2F2F2', font=('FixedSys', 20))
label2.pack()

output = tk.Text(root, height=10, width=50, borderwidth=5, fg='#212121', bg='#F2F2F2',
                 font=['FixedSys', 20])
output.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()