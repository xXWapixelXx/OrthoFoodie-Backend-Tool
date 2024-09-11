import os
import csv
import json
import time
import shutil
from colorama import Fore, Style, init
import pyfiglet
from tqdm import tqdm
from googletrans import Translator

# Initialize colorama
init(autoreset=True)

# Initialize the translator
translator = Translator()

# Function to center text based on terminal width
def center_text(text):
    terminal_size = shutil.get_terminal_size().columns
    return text.center(terminal_size)

# Function to clear the terminal
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Mac and Linux
        os.system('clear')

# Function to display the title in ASCII art
def display_title():
    title = pyfiglet.figlet_format("OrthoFoodie", font="slant")
    subtitle = pyfiglet.figlet_format("Backend Tool", font="small")
    for line in title.splitlines():
        print(Fore.CYAN + center_text(line))
    for line in subtitle.splitlines():
        print(Fore.YELLOW + center_text(line))
    description_lines = [
        "This tool helps you format backend text for translation and export.",
        "Drag and drop your CSV file or enter the path."
    ]
    for line in description_lines:
        print(Fore.GREEN + center_text(line))
    print("\n")

# Function to display a "Completed!" message
def display_completed_message():
    success_message = pyfiglet.figlet_format("Completed!", font="big")
    for i, line in enumerate(success_message.splitlines()):
        if i % 2 == 0:
            print(Fore.MAGENTA + center_text(line))
        else:
            print(Fore.CYAN + center_text(line))

# Retry mechanism for translation
def translate_with_retry(text, target_language, retries=3):
    for attempt in range(retries):
        try:
            return translator.translate(text, dest=target_language).text
        except Exception as e:
            print(Fore.YELLOW + f"Error translating {text}. Retrying {attempt + 1}/{retries}...")
            time.sleep(2)  # Wait before retrying
    return text  # Return the original text if all retries fail

# Logging function to log errors or success to a file
def log_translation(log_file, message):
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(message + "\n")

# Function to preview the first few rows of translation
def preview_translation(translated_rows):
    print(Fore.CYAN + center_text("Preview of the first 5 translations:"))
    for row in translated_rows[:5]:
        print(center_text(str(row)))
    return input(Fore.GREEN + center_text("Does this look good? (Y/N): ")).strip().lower() == 'y'

# Function to select language
def select_language():
    print(Fore.GREEN + center_text("Please choose a language to translate to:"))
    print(center_text(Fore.CYAN + "1. Dutch (nl)"))
    print(center_text(Fore.CYAN + "2. French (fr)"))
    print(center_text(Fore.CYAN + "3. German (de)"))
    print(center_text(Fore.CYAN + "4. Spanish (es)"))
    print(center_text(Fore.CYAN + "5. Italian (it)"))
    print(center_text(Fore.CYAN + "6. Custom (enter your own language code)"))

    language_choice = input(Fore.YELLOW + center_text("Enter the number of your choice: ")).strip()

    language_map = {
        '1': 'nl',
        '2': 'fr',
        '3': 'de',
        '4': 'es',
        '5': 'it',
    }

    if language_choice == '6':
        custom_language = input(Fore.YELLOW + center_text("Please enter a two-letter language code (e.g., 'kr' for Korean): ")).strip()
        return custom_language

    return language_map.get(language_choice, 'nl')

# Batch processing of multiple CSV files
def batch_translate(file_paths):
    for file_path in file_paths:
        translate_csv(file_path)

# Mode 1: Translate CSV (Keeps keys untouched, translates values)
def translate_csv(file_path):
    if os.path.exists(file_path):
        base_name = os.path.splitext(file_path)[0]  # Get the base name without extension
        output_file = f"{base_name}Translated.csv"
        log_file = f"{base_name}_translation.log"
        
        print(Fore.YELLOW + center_text(f"We found {file_path}."))
        user_input = input(Fore.GREEN + center_text("Would you like to continue with translation? (Y/N): ")).strip().lower()

        if user_input == 'y':
            target_language = select_language()
            clear_screen()  # Clear the screen after language selection
            display_title()  # Display the title again after clearing the screen
            print(Fore.YELLOW + center_text(f"Preparing to format and translate to {target_language}...\n"))
            time.sleep(1)

            translated_rows = []

            with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                total_rows = sum(1 for _ in reader)  # Get total number of rows for the progress bar
                csvfile.seek(0)  # Reset file pointer
                next(reader)  # Skip header

                with tqdm(total=total_rows, desc="Translating", unit="row", ncols=100) as pbar:
                    for row in reader:
                        row_id = row['id']   # ID remains untouched
                        name = row['name']   # Name will be translated
                        description = row['description']  # Description will be translated

                        # Translate only the values (right-hand side) with retries and error handling
                        translated_name = translate_with_retry(name, target_language)
                        translated_description = translate_with_retry(description, target_language)

                        # Log each translation
                        log_translation(log_file, f"Translated: {name} -> {translated_name}")
                        log_translation(log_file, f"Translated description for {name} -> {translated_description}")

                        # Store translated rows with the ID and translated values
                        translated_rows.append({
                            'id': row_id,
                            'name': translated_name,
                            'description': translated_description
                        })

                        pbar.update(1)

            # Preview the first 5 rows of translations before saving
            if not preview_translation(translated_rows):
                print(Fore.RED + center_text("Translation aborted by user."))
                return

            # Write the translated content back to CSV
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'name', 'description']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
                writer.writeheader()
                writer.writerows(translated_rows)

            display_completed_message()
            print(Fore.GREEN + center_text(f"Your translated file has been saved as {output_file}."))

            # Ask if the user wants to convert to JSON
            convert_to_json = input(Fore.GREEN + center_text("Would you like to format it to JSON? (Y/N): ")).strip().lower()
            if convert_to_json == 'y':
                generate_json_from_csv(output_file, f"{base_name}.json")
            else:
                print(Fore.CYAN + center_text("You can manually convert it later if needed."))

        else:
            print(Fore.RED + center_text("Translation aborted."))
    else:
        print(Fore.RED + center_text(f"{file_path} not found. Make sure the file exists and the path is correct."))


# Mode 2: Generate JSON from CSV (Both name and description are keys, their values are translated)
def generate_json_from_csv(csv_file, json_output):
    if os.path.exists(csv_file):
        print(Fore.YELLOW + center_text(f"Preparing to generate {json_output} from {csv_file}...\n"))
        translated_dict = {}

        # Read CSV and convert to dictionary
        with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                # Name and Description will be treated as keys, their translated values as values
                name_key = row['name']
                name_value = row['name']  # Keep the name translated

                description_key = row['description']
                description_value = row['description']  # Keep the translated description

                # Add both name and description as keys in the dictionary
                translated_dict[name_key] = name_value
                translated_dict[description_key] = description_value

        # Write to JSON file
        with open(json_output, 'w', encoding='utf-8') as jsonfile:
            json.dump(translated_dict, jsonfile, ensure_ascii=False, indent=4)

        display_completed_message()
        print(Fore.GREEN + center_text(f"Your translated JSON has been saved as {json_output}."))
    else:
        print(Fore.RED + center_text(f"{csv_file} not found. Make sure the file exists."))


# Main Menu
def main_menu():
    display_title()
    print(Fore.GREEN + center_text("Please choose a mode:"))
    print(center_text(Fore.CYAN + "1. Translate CSV"))
    print(center_text(Fore.CYAN + "2. Generate JSON from CSV"))
    user_choice = input(Fore.YELLOW + center_text("Enter the number of your choice: ")).strip()

    if user_choice == '1':
        file_path = input(Fore.YELLOW + center_text("Drag and drop the CSV file or enter the file path: ")).strip('"')
        translate_csv(file_path)
    elif user_choice == '2':
        file_path = input(Fore.YELLOW + center_text("Drag and drop the CSV file or enter the file path: ")).strip('"')
        generate_json_from_csv(file_path, file_path.replace(".csv", ".json"))
    else:
        print(Fore.RED + center_text("Invalid choice. Exiting..."))

# Run the main menu
if __name__ == "__main__":
    main_menu()
