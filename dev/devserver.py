import uvicorn

SERVER_PORT = 5678

if __name__ == "__main__":
    uvicorn.run(
        "notify.main:app",
        app_dir="./",
        port=SERVER_PORT,
        log_level="info",
        host="0.0.0.0",
        reload=True,
    )
