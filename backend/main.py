import logging
import signal
import sys

import uvicorn
from fastapi import FastAPI

import api
from api import probes
from config import settings
from logger import get_log_config

TITLE = "Quotes"


class ExitOnSignal(Exception):
    pass


app = FastAPI(title=TITLE)
app.include_router(api.router, prefix="/api")
app.include_router(probes.router, prefix="/_")


def main():
    log_level = logging.DEBUG if settings.debug else logging.INFO
    log_format = "plain"
    exit_code = 0
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, signal_handler)
    try:
        print(f"Starting {TITLE} with configuration {settings}")
        uvicorn.run(
            "main:app",
            host=settings.bind_address,
            port=settings.port,
            proxy_headers=True,
            root_path=settings.root_path,
            log_config=get_log_config(log_format, log_level),
            log_level=log_level,
            reload=settings.debug,
            access_log=settings.debug,
        )
    except ExitOnSignal:
        pass
    except Exception as e:
        print(f"unwanted exception: {e}")
        exit_code = 113
    return exit_code


def signal_handler(signum, frame):
    raise ExitOnSignal()


if __name__ == "__main__":
    sys.exit(main())
