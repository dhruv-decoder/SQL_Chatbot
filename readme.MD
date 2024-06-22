# SQL-Chatbot

This is a Streamlit-based application that leverages Vanna to convert natural language questions into SQL queries and visualizes the results. The project uses the Chinook database as a demonstration.

Live demo: [Hugging Face Space - SQL-Chatbot](https://huggingface.co/spaces/DhruvDecoder/SQL-Chatbot)

## Features

- Convert natural language questions into SQL queries.
- Execute SQL queries against the Chinook SQLite database.
- Display query results in a table.
- Generate and display visualizations based on the query results.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Streamlit
- Vanna
- An API key for Vanna

### Installation

1. Clone the repository:
    ```bash
    git clone https://huggingface.co/spaces/DhruvDecoder/SQL-Chatbot
    cd SQL-Chatbot
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set your Vanna API key as an environment variable:
    ```bash
    $env:VANNA_API_KEY="your_api_key_here"  # For Windows PowerShell
    ```

### Running the Application

To run the Streamlit application, execute the following command:
```bash
streamlit run app.py


### Using the Application
Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).
You will see the Chinook logo initially.
Ask a question in natural language in the input box (e.g., "What are the top 10 albums by sales?").
The application will convert your question into an SQL query and display it.
The results of the query will be shown in a table.
A visualization based on the query results will be displayed.
To ask another question, click the "Ask another question" button.


###Files
app.py: The main application file.
chinook.png: The image displayed initially.
requirements.txt: A list of required packages.
