
# PRA-CLI

PRA-CLI is a command-line interface (CLI) tool that allows users to upload a document and generate AI-driven content based on the document using the Google GenAI API.

## Features

- Upload a document for analysis.
- Generate AI content based on the uploaded document.
- Configurable API key, model, and base URL via environment variables.

## Prerequisites

- Python 3.7 or higher
- A Google GenAI API key
- The `dotenv` Python package for environment variable management

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd PRA-CLI
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   - Copy the `.env.template` file to `.env`:
     ```bash
     cp .env.template .env
     ```
   - Replace the placeholder values in `.env` with your API key and model details.

## Usage

1. Run the program:
   ```bash
   python main.py
   ```

2. Enter the path to your document when prompted.

3. The program will upload the document and generate AI-driven content based on it.

## Configuration

The following environment variables are used:

- `API_KEY`: Your Google GenAI API key.
- `MODEL`: The AI model to use (e.g., `gemini-2.5-flash`).
- `BASE_URL`: (Optional) The base URL for the API.

## Example

```bash
$ python main.py
Enter the path to your document. 
/path/to/document.txt
Uploaded document name is document.txt
Generated content: "This document discusses..."
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
