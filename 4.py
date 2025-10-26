import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class InventoryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management")
        self.root.geometry("400x300")  # Set initial window size

        self.style = ttk.Style()
        self.style.configure("Custom.TButton", font=("Helvetica", 12), background="#007bff", foreground="black", bordercolor="#007bff", highlightthickness=0)
        self.style.map("Custom.TButton", background=[("active", "#0056b3"), ("disabled", "#bfbfbf")])  # Hover color, Disabled color
        self.style.map("Custom.TButton", foreground=[("disabled", "#595959")])  # Disabled text color
        self.style.configure("Custom.TFrame", background="#cdf2ff")  # Custom background color

        self.inventory = {
            "motherboard": 0,
            "hard_disk": 0,
            "diskette": 0,
            "compact_disk": 0,
            "memory_card": 0
        }

        self.create_widgets()

    def create_widgets(self):
        # Main frame with custom background
        main_frame = ttk.Frame(self.root, style="Custom.TFrame")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        self.title_label = tk.Label(main_frame, text="Inventory Management", font=("Helvetica", 16, "bold"),bg="#cdf2ff")
        self.title_label.pack(pady=10)

        # Display Inventory button
        self.display_button = ttk.Button(main_frame, text="Display Inventory", command=self.display_inventory, style="Custom.TButton")
        self.display_button.pack(pady=5)

        # Add Items button
        self.add_button = ttk.Button(main_frame, text="Add Items", command=self.add_items, style="Custom.TButton")
        self.add_button.pack(pady=5)

        # Remove Items button
        self.remove_button = ttk.Button(main_frame, text="Remove Items", command=self.remove_items, style="Custom.TButton")
        self.remove_button.pack(pady=5)

        # Quit button
        self.quit_button = ttk.Button(main_frame, text="Quit", command=self.root.destroy, style="Custom.TButton")
        self.quit_button.pack(pady=5)

    def display_inventory(self):
        inventory_text = "Current Inventory:\n"
        for item, quantity in self.inventory.items():
            inventory_text += f"{item.capitalize()}: {quantity}\n"

        # Create a custom-styled messagebox
        inventory_window = tk.Toplevel(self.root)
        inventory_window.title("Current Inventory")
        inventory_window.geometry("300x200")
        inventory_window.configure(bg="#cdf2ff")  # Set background color

        # Create a label to display inventory text
        inventory_label = tk.Label(inventory_window, text=inventory_text, font=("Helvetica", 12), bg="#cdf2ff")
        inventory_label.pack(padx=20, pady=20)

    def add_items(self):
        item = simpledialog.askstring("Add Items", "Enter item to add:")
        if item:
            item = item.lower()
            if item in self.inventory:
                quantity = simpledialog.askinteger("Add Items", "Enter quantity to add:")
                if quantity is not None and quantity > 0:
                    self.inventory[item] += quantity
                    self.root.lift()  # Bring the main window to the front
                    messagebox.showinfo("Success", f"Added {quantity} {item.capitalize()}(s) to inventory.")
                else:
                    self.root.lift()  # Bring the main window to the front
                    messagebox.showerror("Error", "Invalid quantity.")
            else:
                self.root.lift()  # Bring the main window to the front
                messagebox.showerror("Error", "Invalid item.")

    def remove_items(self):
        item = simpledialog.askstring("Remove Items", "Enter item to remove:")
        if item:
            item = item.lower()
            if item in self.inventory:
                quantity = simpledialog.askinteger("Remove Items", "Enter quantity to remove:")
                if quantity is not None and quantity > 0:
                    if self.inventory[item] >= quantity:
                        self.inventory[item] -= quantity
                        self.root.lift()  # Bring the main window to the front
                        messagebox.showinfo("Success", f"Removed {quantity} {item.capitalize()}(s) from inventory.")
                    else:
                        self.root.lift()  # Bring the main window to the front
                        messagebox.showerror("Error", "Insufficient quantity in inventory.")
                else:
                    self.root.lift()  # Bring the main window to the front
                    messagebox.showerror("Error", "Invalid quantity.")
            else:
                self.root.lift()  # Bring the main window to the front
                messagebox.showerror("Error", "Invalid item.")

def main():
    root = tk.Tk()
    app = InventoryGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()