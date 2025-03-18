# My Flask API

This repository contains a Flask API that interacts with the OpenAI API for summarization, answering questions, and performing web searches.

## Setup and Installation

1. ### Clone the Repository
   ```bash
   git clone https://github.com/gevahaviv1/my-flask-api.git
   cd my-flask-api
   ```

2. ### Create a Virtual Environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. ### Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. ### Set Up Environment Variables
   - Create a .env file in the root directory.
   
   - Add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   
4. ### Run the API
   ```bash
   python app.py
   ```
   The server will start running at http://127.0.0.1:5000.

## API Endpoints and Sample Requests

### 1. Upload & Summarize

    - Endpoint: /upload
    - Method: POST
    - Description: Upload a text file to get a summary.

**Sample Request using cURL:**
```bash
curl -X POST -F "file=@sample.txt" http://127.0.0.1:5000/upload
```

**Sample Response:**
```json
{
  "summary": "This is the AI-generated summary of the provided text."
}
```

### 2. Chat (Ask a Question)

    - Endpoint: /chat
    - Method: POST
    - Description: Send a message to ask a question.

**Sample Request using cURL:**
```bash
curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "How much is it 5 times 5?"}'
```

**Sample Response:**
```json
{
  "response": "The capital of France is Paris."
}
```

### 3. Web Search

    - Endpoint: /search
    - Method: GET
    - Description: Perform a web search based on a query parameter.

**Sample Request using cURL:**
```bash
curl -X GET "http://127.0.0.1:5000/search?q=latest%20tech%20news"
```

**Sample Response:**
```json
{
  "results": "This is the AI-generated response with the most relevant web search results."
}
```
