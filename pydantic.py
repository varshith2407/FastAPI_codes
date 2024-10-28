from fastapi import FastAPI , Body
from pydantic import BaseModel
from typing import Union

app = FastAPI()
 
class PersanalValues(BaseModel):
    name       : str
    country    : str
    age        : int
    PhoneNumber: int
    Gmail      : Union[str, int]

@app.get("/persal/{user_name}")
def write_persal(user_name: str, age_num:int,query):
    return {
        "Name": user_name,
        "Age": age_num,
        "query": str
        

    }

@app.post("/postData")
def post_data(persanal_values: PersanalValues, spousal_status:str = Body(...) ):
    print(persanal_values)
    return{
        "name":persanal_values.name,
        "Spousal_status":spousal_status
    }
