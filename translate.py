import os
import time
import shutil
from colorama import Fore, Style, init
import pyfiglet
from tqdm import tqdm
from googletrans import Translator  # Assuming you are using googletrans for translation
import re  # Add this import to use regular expressions

# Initialize colorama
init(autoreset=True)

# Initialize the translator
translator = Translator()

# Function to center text based on terminal width
def center_text(text):
    terminal_size = shutil.get_terminal_size().columns
    return text.center(terminal_size)

# Function to display the title in ASCII art
def display_title():
    # Generate the ASCII art for OrthoFoodie
    title = pyfiglet.figlet_format("OrthoFoodie", font="slant")
    # Generate a smaller ASCII text for Backend Tool
    subtitle = pyfiglet.figlet_format("Backend Tool", font="small")  # Smaller than OrthoFoodie

    # Split the ASCII art by lines and center each line
    for line in title.splitlines():
        print(Fore.CYAN + center_text(line))

    # Center the smaller subtitle as well
    for line in subtitle.splitlines():
        print(Fore.YELLOW + center_text(line))

    # Add the description of what the tool does
    description_lines = [
        "This tool helps you format backend text by wrapping every word in the format:",
        '"<word>": ""',
        "It then translates the text into Dutch (NL) if the right side is empty."
    ]
    for line in description_lines:
        print(Fore.GREEN + center_text(line))
    
    print("\n")  # Extra space after the titles

# Function to display a more beautiful "Completed!" message
def display_completed_message():
    # Use a different, more artistic font for the completed message
    success_message = pyfiglet.figlet_format("Completed!", font="big")

    # Colorize the success message with a gradient effect using colorama
    for i, line in enumerate(success_message.splitlines()):
        if i % 2 == 0:
            print(Fore.MAGENTA + center_text(line))  # Magenta for alternating lines
        else:
            print(Fore.CYAN + center_text(line))  # Cyan for alternating lines

# Function to process the text
def process_text(lines):
    translated_lines = []

    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace

        # Check if line is a key-value pair (formatted like "key": "value")
        match = re.match(r'^"(.+?)":\s*"(.*?)"$', line)
        if match:
            key, value = match.groups()
            # If value is empty, prepare it for translation
            if value == "":
                translated_lines.append((key, ""))
            else:
                translated_lines.append((key, value))  # If value exists, keep it
        else:
            # Line is not a key-value pair, assume it's a standalone word
            translated_lines.append((line, ""))  # Treat word as key with empty value

    return translated_lines

# Path to the text file to translate
file_to_translate = 'Translate.txt'
output_file = 'Translated.txt'

# Display title and program's purpose
display_title()

# Check if Translate.txt exists
if os.path.exists(file_to_translate):
    # Inform the user that the file has been found
    print(Fore.YELLOW + center_text(f"We found {file_to_translate}."))
    
    # Ask if the user wants to continue
    user_input = input(Fore.GREEN + center_text("Would you like to continue? (Y/N): ")).strip().lower()

    if user_input == 'y':
        print(Fore.YELLOW + center_text("Preparing to format and translate...\n"))
        time.sleep(1)  # Just for a nice effect

        # Read the content from Translate.txt
        with open(file_to_translate, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Process the text (detect key-value pairs or words)
        processed_lines = process_text(lines)

        # Ask if the user wants to translate empty values
        translate_choice = input(Fore.GREEN + center_text("I see some blank \"\" values. Would you like me to translate them? (Y/N): ")).strip().lower()

        if translate_choice == 'y':
            for i, (key, value) in enumerate(processed_lines):
                if value == "":
                    # Translate the key (if value is empty)
                    translation = translator.translate(key, dest='nl').text
                    processed_lines[i] = (key, translation)
                    print(Fore.CYAN + f'Translated: {key} -> {translation}')
        
        # Format the processed lines as key-value pairs
        translated_lines = [f'"{key}": "{value}"' for key, value in processed_lines]

        # Write the translated content to Translated.txt
        with open(output_file, 'w', encoding='utf-8') as output:
            output.write(',\n'.join(translated_lines))

        # Display the completed message
        display_completed_message()
        print(Fore.GREEN + center_text(f"Your translated file has been saved as {output_file}."))
    else:
        print(Fore.RED + center_text("Translation aborted."))
else:
    # If Translate.txt doesn't exist, create it
    with open(file_to_translate, 'w', encoding='utf-8') as file:
        file.write('')  # Create an empty file

    # Inform the user that the file has been created
    print(Fore.RED + center_text(f"{file_to_translate} not found, so we created one for you."))
    print(Fore.YELLOW + center_text("Please add your words or key-value pairs to 'Translate.txt' and rerun the script."))
