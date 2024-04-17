from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.config import config
from src.routes.users import router as users_router

app = FastAPI(
    title=config.APP_NAME,
    version=config.VERSION
)

app.include_router(users_router.router)


@app.get("/")
async def main():
    """
    Main function
    Redirects to /docs
    """
    return RedirectResponse(url="/docs/")
