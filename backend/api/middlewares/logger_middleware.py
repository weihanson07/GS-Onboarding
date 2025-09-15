from collections.abc import Callable
from typing import Any
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from loguru import logger
from backend.utils.logging import logger_close, logger_setup, logger_setup_file
from datetime import datetime


class LoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(
        self, request: Request, call_next: Callable[[Request], Any]
    ) -> Response:
        """
        Logs all incoming and outgoing request, response pairs. This method logs the request params,
        datetime of request, duration of execution. Logs should be printed using the custom logging module provided.
        Logs should be printed so that they are easily readable and understandable.

        :param request: Request received to this middleware from client (it is supplied by FastAPI)
        :param call_next: Endpoint or next middleware to be called (if any, this is the next middleware in the chain of middlewares, it is supplied by FastAPI)
        :return: Response from endpoint
        """
        # TODO:(Member) Finish implementing this method
        logger_setup()
        logger_setup_file()
        params = request.query_params
        request_time = datetime.now()
        response = await call_next(request)
        duration = datetime.now() - request_time
        logger.info(f"Request params: {params}, Datetime of request: {request_time}, Duration of execution: {duration}")
        await logger_close()
        return response
