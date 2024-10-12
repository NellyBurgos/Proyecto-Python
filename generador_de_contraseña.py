import tkinter as tk  
import random  
import string  

def generate_password():  
    length = int(length_entry.get())  
    use_uppercase = uppercase_var.get()  
    use_lowercase = lowercase_var.get()  
    use_numbers = numbers_var.get()  
    use_special = special_var.get()  

    characters = ''  
    if use_uppercase:  
        characters += string.ascii_uppercase  
    if use_lowercase:  
        characters += string.ascii_lowercase  
    if use_numbers:  
        characters += string.digits  
    if use_special:  
        characters += string.punctuation  

    if not characters:  
        password_label.config(text="No se seleccionaron tipos de caracteres.")  
        return  

    password = ''.join(random.choice(characters) for _ in range(length))  
    password_label.config(text=f"Contraseña generada: {password}")  
 
app = tk.Tk()  
app.title("Generador de Contraseñas")  
app.geometry("400x300")  
app.configure(bg="#D9FFE6")   

length_label = tk.Label(app, text="Longitud de la contraseña:", bg="#D9FFE6", fg="#333")  
length_label.pack(pady=10)  

length_entry = tk.Entry(app)  
length_entry.pack(pady=5)  
 
uppercase_var = tk.BooleanVar()  
lowercase_var = tk.BooleanVar()  
numbers_var = tk.BooleanVar()  
special_var = tk.BooleanVar()  

uppercase_check = tk.Checkbutton(app, text="Incluir mayúsculas", variable=uppercase_var, bg="#f2f2f2", fg="#333")  
uppercase_check.pack(anchor=tk.W)  

lowercase_check = tk.Checkbutton(app, text="Incluir minúsculas", variable=lowercase_var, bg="#f2f2f2", fg="#333")  
lowercase_check.pack(anchor=tk.W)  

numbers_check = tk.Checkbutton(app, text="Incluir números", variable=numbers_var, bg="#f2f2f2", fg="#333")  
numbers_check.pack(anchor=tk.W)  

special_check = tk.Checkbutton(app, text="Incluir caracteres especiales", variable=special_var, bg="#f2f2f2", fg="#333")  
special_check.pack(anchor=tk.W)  

generate_button = tk.Button(app, text="Generar Contraseña", command=generate_password, bg="#4CAF50", fg="black")  
generate_button.pack(pady=20)  
  
password_label = tk.Label(app, text="", bg="#f2f2f2", fg="#333")  
password_label.pack(pady=10)  

app.mainloop()