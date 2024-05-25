from fastapi import FastAPI
from lib.openAI import get_estimate
app = FastAPI()

@app.get("/")
def read_root():
    return get_estimate("banana with peanut butter and honey")