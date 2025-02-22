from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "An example GET TEST 1234"}

@app.post("/")
async def root():
    return {"message": "An example POST"}

@app.put("/")
async def root():
    return {"message": "An example PUT"}

@app.delete("/")
async def root():
    return {"message": "An example DELETE"}
