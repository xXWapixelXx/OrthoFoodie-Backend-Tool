import os
import time
import shutil
import re
from colorama import Fore, Style, init
import pyfiglet
from tqdm import tqdm
from googletrans import Translator

# Initialize colorama
init(autoreset=True)

# Initialize the translator
translator = Translator()

# List of valid language codes (ISO 639-1)
valid_languages = {
    'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb',
    'zh', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'fi', 'fr', 'fy', 'gl',
    'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig',
    'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo',
    'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my',
    'ne', 'no', 'ny', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd',
    'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tl',
    'ta', 'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'uz', 'vi', 'cy', 'xh', 'yi',
    'yo', 'zu'
}

# Function to center text based on terminal width
def center_text(text):
    terminal_size = shutil.get_terminal_size().columns
    return text.center(terminal_size)

# Function to display the title in ASCII art
def display_title():
    title = pyfiglet.figlet_format("OrthoFoodie", font="slant")
    subtitle = pyfiglet.figlet_format("Backend Tool", font="small")
    for line in title.splitlines():
        print(Fore.CYAN + center_text(line))
    for line in subtitle.splitlines():
        print(Fore.YELLOW + center_text(line))
    description_lines = [
        "This tool helps you format backend text by wrapping every word in the format:",
        '"<word>": ""',
        "It then translates the text into a language of your choice."
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

# Function to process the text
def process_text(lines):
    translated_lines = []
    for line in lines:
        line = line.strip()
        match = re.match(r'^"(.+?)":\s*"(.*?)"$', line)
        if match:
            key, value = match.groups()
            if value == "":
                translated_lines.append((key, ""))
            else:
                translated_lines.append((key, value))
        else:
            translated_lines.append((line, ""))
    return translated_lines

# Function to select language
def select_language():
    print(Fore.GREEN + center_text("Please choose a language to translate to:"))
    print(Fore.CYAN + "1. Dutch (nl)")
    print(Fore.CYAN + "2. French (fr)")
    print(Fore.CYAN + "3. German (de)")
    print(Fore.CYAN + "4. Spanish (es)")
    print(Fore.CYAN + "5. Italian (it)")
    print(Fore.CYAN + "6. Custom (enter your own language code)")

    language_choice = input(Fore.YELLOW + "Enter the number of your choice: ").strip()

    language_map = {
        '1': 'nl',
        '2': 'fr',
        '3': 'de',
        '4': 'es',
        '5': 'it',
    }

    if language_choice == '6':
        custom_language = input(Fore.YELLOW + "Please enter a two-letter language code (e.g., 'kr' for Korean): ").strip()
        if custom_language.lower() in valid_languages:
            return custom_language.lower()
        else:
            print(Fore.RED + f"Invalid language code '{custom_language}'. Defaulting to Dutch (nl).")
            return 'nl'
    
    return language_map.get(language_choice, 'nl')

# Path to the text file to translate
file_to_translate = 'Translate.txt'
output_file = 'Translated.txt'

# Display title and program's purpose
display_title()

# Check if Translate.txt exists
if os.path.exists(file_to_translate):
    print(Fore.YELLOW + center_text(f"We found {file_to_translate}."))
    
    user_input = input(Fore.GREEN + center_text("Would you like to continue? (Y/N): ")).strip().lower()

    if user_input == 'y':
        target_language = select_language()
        print(Fore.YELLOW + center_text(f"Preparing to format and translate to {target_language}...\n"))
        time.sleep(1)

        with open(file_to_translate, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        processed_lines = process_text(lines)

        translate_choice = input(Fore.GREEN + center_text("I see some blank \"\" values. Would you like me to translate them? (Y/N): ")).strip().lower()

        if translate_choice == 'y':
            for i, (key, value) in enumerate(processed_lines):
                if value == "":
                    translation = translator.translate(key, dest=target_language).text
                    processed_lines[i] = (key, translation)
                    print(Fore.CYAN + f'Translated: {key} -> {translation}')
        
        translated_lines = [f'"{key}": "{value}"' for key, value in processed_lines]

        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(',\n'.join(translated_lines))

        display_completed_message()
        print(Fore.GREEN + center_text(f"Your translated file has been saved as {output_file}."))
    else:
        print(Fore.RED + center_text("Translation aborted."))
else:
    with open(file_to_translate, 'w', encoding='utf-8') as file:
        file.write('')
    print(Fore.RED + center_text(f"{file_to_translate} not found, so we created one for you."))
    print(Fore.YELLOW + center_text("Please add your words or key-value pairs to 'Translate.txt' and rerun the script."))
