from fastapi import FastAPI
import classroom
app = FastAPI()


@app.get("/")
async def root():
    return {"message": classroom.main()}
