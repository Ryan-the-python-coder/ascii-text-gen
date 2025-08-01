import os
import pyfiglet
import random

# Get the user's profile directory (Windows)
USER = os.environ.get("USERPROFILE") or os.path.expanduser("~")

# Folder inside the user profile to save files
OUTPUT_DIR = os.path.join(USER, "pyfiglet-output")

def get_yes_no(prompt):
    """Ask a yes/no question until the user gives a valid answer."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ("y", "n"):
            return choice
        print("Please type y or n.")

def get_filename():
    """Ask for a filename and ensure it ends with .txt inside OUTPUT_DIR."""
    while True:
        filename = input("Filename (without folder path): ").strip()
        if not filename:
            print("Filename cannot be empty.")
            continue
        if not filename.endswith(".txt"):
            filename += ".txt"

        confirm = get_yes_no(f"Are you sure you want '{filename}' as your filename? (y/n?): ")
        if confirm == "y":
            return os.path.join(OUTPUT_DIR, filename)

def main():
    # Always create the output folder before anything else
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    fonts_list = pyfiglet.FigletFont.getFonts()

    while True:
        # Get text to render
        while True:
            text = input("Text to create: ").strip()
            confirm = get_yes_no("Are you sure you want to input this text? (y/n?): ")
            if confirm == "y":
                break

        # Create ASCII art
        art = pyfiglet.figlet_format(text, font=random.choice(fonts_list))
        print(art)

        # Optionally save to file
        if get_yes_no("Would you like to save this to a text file? (y/n?): ") == "y":
            filepath = get_filename()
            with open(filepath, "w", encoding="utf-8") as file:
                file.write(art)
            print(f"Written to {filepath}")
        else:
            print("Not saved.")

        # Exit or restart
        if get_yes_no("Would you like to exit? (y/n?): ") == "y":
            print("Exiting...")
            break
        else:
            print("Restarting...\n")

if __name__ == "__main__":
    main()
