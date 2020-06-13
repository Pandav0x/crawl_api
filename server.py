import uvicorn
import json
from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
def index():
    return {
        'message': 'server is up'
    }

def run_server(host, port):
    uvicorn.run('server:app', host=host, port=port, log_level="info")

if __name__ == "__main__":
    run_server("127.0.0.1", 5000)