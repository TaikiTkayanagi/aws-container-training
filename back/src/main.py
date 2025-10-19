from fastapi import FastAPI, status, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello")
async def hello():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
async def health_check() -> Response:
    return Response(status_code=status.HTTP_200_OK)