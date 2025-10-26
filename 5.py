import tkinter as tk
from tkinter import messagebox

def AddContact():
    name = NameEntry.get()
    phone = PhoneEntry.get()
    if name and phone:
        if phone.isdigit():
            if any(contact_phone == phone for contact_phone in contacts.values()):
                messagebox.showerror("ERROR", "The phone number you entered already exists.")
            else:
                contacts[name] = phone
                UpdateDisplay()
        else:
            messagebox.showerror("ERROR", "Phone number must contain only digits.")
    else:
        messagebox.showerror("ERROR", "Please enter both name and phone number.")

def SearchContact():
    search_term = SearchEntry.get()
    if search_term in contacts:
        ResultLabel.config(text=f"Name: {search_term}, Phone Number: {contacts[search_term]}")
    else:
        ResultLabel.config(text="Contact cannot be found")

def DeleteContact():
    name = NameEntry.get()
    phone = PhoneEntry.get()
    if name and phone:
        if (name, phone) in contacts.items():
            confirm = messagebox.askyesno("Confirm for Deletion", f"Are you sure you want to delete {name}?")
            if confirm:
                del contacts[name]
                UpdateDisplay()
        else:
            messagebox.showerror("ERROR", "Contact cannot be found")
    else:
        messagebox.showerror("ERROR", "Please enter both name and phone number.")

def UpdateContact():
    name = NameEntry.get()
    new_name = new_NameEntry.get()
    new_phone = new_PhoneEntry.get()

    if name not in contacts or contacts[name] != PhoneEntry.get():  # Check if current name and phone are correct
        messagebox.showerror("ERROR", "Current name or phone number is incorrect.")
        return

    while True:
        if not new_name and not new_phone:
            messagebox.showerror("ERROR", "Please enter new name or new phone number.")
            break

        if new_phone and not new_phone.isdigit():
            messagebox.showerror("ERROR", "New phone number must contain only digits.")
            break

        if any(new_phone == phone for phone in contacts.values() if phone != contacts[name]):
            messagebox.showerror("ERROR", "The phone number you inserted already exists in the phonebook.")
            break

        if new_name:
            contacts[new_name] = contacts.pop(name)
        if new_phone:
            contacts[new_name] = new_phone

        UpdateDisplay()
        messagebox.showinfo("SUCCESS", "Contact updated successfully.")
        break

def UpdateDisplay():
    contactListBox.delete(0, tk.END)
    for name, phone in contacts.items():
        contactListBox.insert(tk.END, f"{name}: {phone}")

contacts = {}

root = tk.Tk()
root.title("Phonebook")

cool_font = ("Verdana", 10, "bold")
header_font = ("Fixedsys", 20, "bold")
result_font = ("Verdana", 10)

root.config(bg="skyblue")

HeaderLabel = tk.Label(root, text="GROUP 3'S PHONEBOOK", font=header_font, bg="skyblue", fg="black")
HeaderLabel.grid(row=0, column=0, columnspan=4, pady=10)

SearchEntry = tk.Entry(root, width=29, font=cool_font)
SearchEntry.grid(row=1, column=1, pady=5, sticky="w")
SearchButton = tk.Button(root, text="Search", command=SearchContact, font=cool_font)
SearchButton.grid(row=1, column=2)
tk.Label(root, text="Name:", font=cool_font, bg="skyblue", fg="black").grid(row=3, column=0, sticky="e")
tk.Label(root, text="Phone Number:", font=cool_font, bg="skyblue", fg="black").grid(row=4, column=0, sticky="e")
tk.Label(root, text="Search:", font=cool_font, bg="skyblue", fg="black").grid(row=1, column=0, sticky="e")
ResultLabel = tk.Label(root, text="", font=result_font, bg="skyblue", fg="black")
ResultLabel.grid(row=2, columnspan=4)

NameEntry = tk.Entry(root, width=30, font=cool_font)
NameEntry.grid(row=3, column=1)
PhoneEntry = tk.Entry(root, width=30, font=cool_font)
PhoneEntry.grid(row=4, column=1)
PhoneEntry.config(validate="key")
PhoneEntry.config(validatecommand=(root.register(lambda char: char.isdigit() or char == ''), '%S'))

AddButton = tk.Button(root, text="Add Contact", command=AddContact, font=cool_font)
AddButton.grid(row=5, column=1, pady=5, sticky="w", padx=5)
DeleteButton = tk.Button(root, text="Delete Contact", command=DeleteContact, font=cool_font)
DeleteButton.grid(row=5, column=1, pady=5, padx=5, sticky="e")

tk.Label(root, text="New Name:", font=cool_font, bg="skyblue", fg="black").grid(row=6, column=0, sticky="e")
tk.Label(root, text="New Phone Number:", font=cool_font, bg="skyblue", fg="black").grid(row=7, column=0, sticky="e")
new_NameEntry = tk.Entry(root, width=30, font=cool_font)
new_NameEntry.grid(row=6, column=1, sticky="w")
new_PhoneEntry = tk.Entry(root, width=30, font=cool_font)
new_PhoneEntry.grid(row=7, column=1, sticky="w")

UpdateButton = tk.Button(root, text="Update Contact", command=UpdateContact, font=cool_font)
UpdateButton.grid(row=8, column=1, columnspan=1, pady=5)

contactListBox = tk.Listbox(root, width=40, height=8, font=cool_font)
contactListBox.grid(row=9, columnspan=5, pady=5)

root.mainloop()
