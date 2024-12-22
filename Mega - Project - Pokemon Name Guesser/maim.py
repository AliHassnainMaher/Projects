import random
import tkinter as tk
from PIL import Image, ImageTk

def load_pokemon_list(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def load_pokemon_hints(filename):
    hints = {}
    with open(filename, 'r') as file:
        for line in file:
            name, hint_str = line.strip().split(': ', 1)
            hints[name] = hint_str.split(', ')
    return hints

def get_random_pokemon(pokemon_list):
    return random.choice(pokemon_list)

def get_pokemon_hints(pokemon_name, pokemon_hints):
    return pokemon_hints.get(pokemon_name, [])

def check_guess(pokemon_name, guess_entry, result_label):
    guess = guess_entry.get()
    if guess.lower() == pokemon_name.lower():
        result_label.config(text="Correct! You guessed the Pokémon!")
    else:
        result_label.config(text=f"Sorry, the correct answer was {pokemon_name}.")

def next_pokemon(pokemon_list, pokemon_hints, guess_entry, result_label, hint_frame):
    pokemon_name = get_random_pokemon(pokemon_list)
    hints = get_pokemon_hints(pokemon_name, pokemon_hints)
    
    guess_entry.delete(0, tk.END)
    result_label.config(text="")
    
    for widget in hint_frame.winfo_children():
        widget.destroy()
    
    for hint in hints:
        hint_label = tk.Label(hint_frame, text=f"Hint: {hint}", font=("Arial", 14), bg='white', fg='darkblue')
        hint_label.pack(pady=5)
    
    return pokemon_name

def main():
    pokemon_list = load_pokemon_list('list.txt')
    pokemon_hints = load_pokemon_hints('hints.txt')
    
    root = tk.Tk()
    root.title("Who's That Pokémon")
    root.configure(bg='white')
    
    title_label = tk.Label(root, text="Guess the Pokémon!", font=("Arial", 24), bg='white')
    title_label.pack(pady=10)
    
    pokeball_image = Image.open("pokeball.png")
    pokeball_image = pokeball_image.resize((100, 100), Image.LANCZOS)
    pokeball_photo = ImageTk.PhotoImage(pokeball_image)
    
    pokeball_label = tk.Label(root, image=pokeball_photo, bg='white')
    pokeball_label.pack(pady=10)
    
    guess_entry = tk.Entry(root, font=("Arial", 14), bd=2, relief="solid")
    guess_entry.pack(pady=10)
    guess_entry.config(highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=0)
    
    result_label = tk.Label(root, text="", font=("Arial", 14), bg='white')
    result_label.pack(pady=10)
    
    hint_frame = tk.Frame(root, bg='white')
    hint_frame.pack(pady=10)
    
    pokemon_name = next_pokemon(pokemon_list, pokemon_hints, guess_entry, result_label, hint_frame)
    
    guess_button = tk.Button(root, text="Submit Guess", font=("Arial", 14), command=lambda: check_guess(pokemon_name, guess_entry, result_label))
    guess_button.pack(pady=10)
    
    next_button = tk.Button(root, text="Next Pokémon", font=("Arial", 14), command=lambda: next_pokemon(pokemon_list, pokemon_hints, guess_entry, result_label, hint_frame))
    next_button.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
