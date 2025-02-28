from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scanner import scan_url

app = FastAPI()  # ✅ Define the app first!

# Fix CORS errors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scan/")
def scan_endpoint(url: str):
    return scan_url(url)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
