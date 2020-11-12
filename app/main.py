import logging
import sys
from typing import List

from fastapi import FastAPI, HTTPException, Path, status

# from fastapi.logger import logger as log
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Extra, Field, validator

app = FastAPI()

# configure logging with filename, function name and line numbers
logging.basicConfig(
    datefmt="%I:%M:%S %p %Z",
    format="%(levelname)s [%(asctime)s - %(filename)s:%(lineno)s::%(funcName)s]\t%(message)s",
    stream=sys.stdout,
    level=logging.INFO,
)
log = logging.getLogger(__name__)


@app.on_event("startup")
async def app_bootstrap():
    log.info("startup event")


@app.on_event("shutdown")
def shutdown_event():
    log.warning("shutting down.")


@app.post("", description="Home page")
async def root(
):
    raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Server not implemented.")
