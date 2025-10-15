from fastapi import FastAPI, status, Response

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/health")
async def health_check() -> Response:
    return Response(status_code=status.HTTP_200_OK)