from fastapi import FastAPI, Request

app = FastAPI()

# To store the last POST request's URL and body
last_post = {}

@app.post("/{path:path}")
async def post_data(path: str, request: Request):
    body = await request.json()
    last_post["url"] = f"/{path}"
    last_post["body"] = body
    return {"message": "Data received"}

@app.get("/callback")
async def post_data(request: Request):
    body = await request.json()
    last_post["url"] = f"/{request.path_params}"
    last_post["body"] = body
    return {"message": "Data received"}

@app.get("/data")
def get_data():
    return last_post
