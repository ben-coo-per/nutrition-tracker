from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from lib.openAI import generate_estimate

app = FastAPI()


class Request(BaseModel):
    food_description: str

@app.post("/")
def estimate_food_macros(req: Request):
    try:
        return generate_estimate(req.food_description)
    except Exception as e:
        try:
            return generate_estimate(req.food_description)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Trouble estimating the food macros: {e}")
