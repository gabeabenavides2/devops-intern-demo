from fastapi import FastAPI

app = FastAPI(title="DevOps Intern Demo")

@app.get("/")
def root():
    return {"message": "Hello from CI/CD!"}

@app.get("/health")
def health():
    return {"status": "ok"}
