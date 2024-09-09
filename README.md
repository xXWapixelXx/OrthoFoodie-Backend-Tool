# OrthoFoodie Backend Text Translator

OrthoFoodie Backend Text Translator is a Python command-line tool designed to format and translate backend text files into Dutch (NL) for easy integration into backend systems. It wraps each word or phrase in JSON-style key-value pairs, helping streamline the process of setting up translations and data formatting.

This script features a visually enhanced interface with ASCII art, progress bars, and color-coded messages for a more engaging user experience.

## Features

- **Easy-to-Use**: Handles both already formatted key-value pairs and single words in the input.
- **Interactive Prompts**: The script guides you through the process, asking for confirmation before proceeding.
- **Visual Enhancements**: ASCII art, colorful progress messages, and a loading bar to track progress.
- **Smart Formatting**: Automatically wraps each line from `Translate.txt` in a JSON-style key-value format.
- **Dutch Translation**: Translates the backend text into Dutch (NL).
- **Error Handling**: Informs the user if `Translate.txt` is missing, prompting them to rerun the script.

## How It Works

1. The script starts by displaying a welcome message with the **OrthoFoodie** ASCII logo.
2. It checks for the existence of `Translate.txt` and prompts the user to confirm if they'd like to continue.
3. The script processes each line, determining if it's a key-value pair or a standalone word.
4. If the right-hand side of the key-value pair is blank, the script offers to translate the values into Dutch.
5. A progress bar tracks the processing of each line.
6. Once complete, it displays a **"Completed!"** message and saves the results to `Translated.txt`.

## Example Input (`Translate.txt`)

```txt
"Food": "",
 Water
"Drink": ""
```

**2. User Workflow:**
1. The script will format and detect the input.
2. It will ask the user: "I see some blank "" values. Would you like me to translate them?"
3. If the user says "Y", it will translate the empty values.

## Example Output (`Translate.txt`)
```json
{
  "Food": "Eten",
  "Water": "Water",
  "Drink": "Drank"
}
```

## Installation
**1. Clone the Repository**
To use the OrthoFoodie Backend Text Translator, you'll need Python and the required dependencies.

```txt
git clone https://github.com/yourusername/OrthoFoodie-Backend-Text-Translator.git
cd OrthoFoodie-Backend-Text-Translator
```

**Install Dependencies**
```txt
pip install -r requirements.txt
```
## Running the Script
Make sure you have a file called **Translate.txt** in the same folder as the script. This file should contain the words or phrases you want to format, each on a new line.
**Run the script:**
```txt
python translate.py
```
## Contributing
Contributions are welcome! If you have any suggestions, improvements, or issues, feel free to open a pull request or issue.








