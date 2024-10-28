from fastapi import FastAPI
app = FastAPI()

@app.api_route("/homedata",methods=['GET','POST','PUT','DELETE'])
def handle_hamedata(username:str):
    print(username)
    return{
        "username":username
    }
