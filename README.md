# OrthoFoodie Backend Text Translator

OrthoFoodie Backend Text Translator is a Python command-line tool designed to format and translate backend text files into Dutch (NL) for easy integration into backend systems. It wraps each word or phrase in JSON-style key-value pairs, helping streamline the process of setting up translations and data formatting.

This script features a visually enhanced interface with ASCII art, progress bars, and color-coded messages for a more engaging user experience.

## Features

- **Easy-to-Use**: Simply drop a text file named `Translate.txt` in the same folder as the script, and it will handle the rest.
- **Interactive Prompts**: The script guides you through the process, asking for confirmation before proceeding.
- **Visual Enhancements**: ASCII art, colorful progress messages, and a loading bar to track progress.
- **Smart Formatting**: Automatically wraps each line from `Translate.txt` in a JSON-style key-value format.
- **Dutch Translation**: Translates the backend text into Dutch (NL).
- **Error Handling**: Informs the user if `Translate.txt` is missing, prompting them to create the file and rerun the script.

## How It Works

1. The script starts by displaying a welcome message with the **OrthoFoodie** ASCII logo.
2. It checks for the existence of `Translate.txt` and prompts the user to confirm if they'd like to continue.
3. The script processes each line, formatting it into a JSON-like structure.
4. A progress bar tracks the processing of each line.
5. Once complete, it displays a **"Completed!"** message and saves the results to `Translated.txt`.

## Example Input (`Translate.txt`)

```txt
Microgram
Milligram
Gram
Kilogram
Ounce
Pound
Metric ton
Teaspoon
Tablespoon
