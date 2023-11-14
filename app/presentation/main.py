from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError

from app.presentation.exception_handling import custom_exception_handling
from .config import configs
from .container import Container
from .routes.v1.routes import routers as v1_routers
from .routes.v2.routes import routers as v2_routers
from .utils.class_object import singleton

@singleton
class Bootstrap:
    def __init__(self):
        # set app default
        self.app = FastAPI(
            title=configs.SERVICE_NAME,
            openapi_url=f"{configs.API}/openapi.json",
            version="0.0.1",
        )

        # set db and container
        self.container = Container()

        #custom exception handler
        @self.app.exception_handler(Exception)
        @self.app.exception_handler(RequestValidationError)
        async def exception_handler(request: Request, exc: Exception):
            return await custom_exception_handling(request, exc)

        # set routes
        @self.app.get("/")
        def root():
            return "service is working"
        
        self.app.include_router(v1_routers, prefix=configs.API_V1_PREFIX)
        self.app.include_router(v2_routers, prefix=configs.API_V2_PREFIX)

bootstrap = Bootstrap()
app = bootstrap.app
#container = bootstrap.container

# HOW TO RUN
# ~/projects/fastapi$ uvicorn app.presentation.main:app --reload