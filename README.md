
## Setup and Installation

1. Clone this repository to your local machine.

   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the API Server

Execute the following command to start the FastAPI server:

```bash
uvicorn app:app --reload
```

The server will start on http://127.0.0.1:8000. You can access the API directly through this URL or use the interactive documentation at http://127.0.0.1:8000/docs.

## Interacting with the API

To make predictions, send a POST request to /predict/ with a JSON payload containing the text. For example, using curl:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"text": "example text"}'
```

Replace "example text" with the text you want to classify.

## Interactive API Documentation

FastAPI generates interactive API documentation available at http://127.0.0.1:8000/docs. 
