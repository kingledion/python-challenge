import logging
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI

from lib.data import DB
from notify.basedata import populate
from notify.routes import notify

# get root logger
logger = logging.getLogger(__name__)

# determine up db connection
db = DB.new()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    logger.info("Performing database migration...")
    db.init_db()
    logger.info("...finished local database migration")

    logger.info("Adding base data...")
    populate(db)
    logger.info("...added base data")
    yield
    # any required cleanup will go here


# declare app; app is run by uvicorn
app = FastAPI(
    lifespan=lifespan,
    docs_url="/notify/docs",
)

#  configure app
app.include_router(notify(db))
