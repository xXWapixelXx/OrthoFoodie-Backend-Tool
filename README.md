# OrthoFoodie Backend Text Translator

OrthoFoodie Backend Text Translator is a Python command-line tool designed to format and translate backend text files into a language of your choice for easy integration into backend systems. It wraps each word or phrase in JSON-style key-value pairs, helping streamline the process of setting up translations and data formatting.

This script features a visually enhanced interface with ASCII art, progress bars, and color-coded messages for a more engaging user experience.

## Features

- **Multi-Language Translation**: Select from predefined languages or enter a custom language code for translation.
- **Error Handling**: Detects invalid language codes and defaults to Dutch (`nl`) if an invalid code is entered.
- **Smart Formatting**: Automatically wraps each line from `Translate.txt` in a JSON-style key-value format.
- **Visual Enhancements**: ASCII art, colorful progress messages, and a loading bar to track progress.
- **User-Friendly**: If `Translate.txt` is missing, the script automatically creates it and informs the user.

## How to Use the Executable

For users who don't want to set up Python or dependencies, simply download the `.exe` file from the [Releases](https://github.com/OrthoFoodie-Backend-Text-Translator/releases) section:

1. **Download** the `.exe` file from the latest release.
2. **Place your `Translate.txt`** file in the same directory as the `.exe`.
3. **Double-click** the `.exe` to run the tool.
4. Follow the prompts to translate your file.

## How It Works

1. The script starts by displaying a welcome message with the **OrthoFoodie** ASCII logo.
2. It checks for the existence of `Translate.txt` and prompts the user to confirm if they'd like to continue.
3. The script processes each line, determining if it's a key-value pair or a standalone word.
4. You will be prompted to choose a language for translation, or enter your own custom two-letter language code.
5. If the right-hand side of the key-value pair is blank, the script offers to translate the values into the selected language.
6. A progress bar tracks the processing of each line.
7. Once complete, it displays a **"Completed!"** message and saves the results to `Translated.txt`.

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

## OR With different languages: Example Output (`Translate.txt`)
```json
{
  "Food": "Eten",
  "Water": "Vand",
  "Drink": "Drikke"
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
Make sure you have a file called **Translate.txt** in the same folder as the script. This file should contain the words or phrases you want to format, each on a new line. for example:
- **Key-value pairs** (e.g., "Food": "") that you want to translate.
- **Single words** (e.g., Food, Water) that will be wrapped in key-value pairs automatically.

**Run the script:**
```txt
python translate.py
```

## Option 2: Use the .EXE File
For users who don't want to bother with running the Python script, we've included a .exe file in the repository.

**How to Use the .exe File:**
-  **Download** the .exe: Go to the **Releases** section of this repository and download the latest executable file.
-  Prepare **Translate.txt**: Make sure you have a Translate.txt file in the same folder as the .exe. Otherwise it makes one for you.
-  **Run** the .exe: Double-click the .exe file, and follow the instructions. You will be prompted to select the language and proceed with the translation.
## Contributing
Contributions are welcome! If you have any suggestions, improvements, or issues, feel free to open a pull request or issue.








