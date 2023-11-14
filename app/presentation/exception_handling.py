from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

class CustomError(Exception):
    def __init__(self):
        if type(self) == CustomError:
            raise Exception("CustomError type cannot be instantiated. Use it as a super class only.")

    def to_response(self) -> dict:
        pass

class CustomNotFoundError(CustomError):
    def __init__(self, message: str) -> None:
        self.message = message
        self.status_code: int = status.HTTP_404_NOT_FOUND

    def to_response(self) -> dict:
        return {
            "message": self.message
        }

class CustomValidationError(CustomError):
    def __init__(self, errors_dict: dict) -> None:
        self.message = ""
        self.status_code: int = status.HTTP_400_BAD_REQUEST
        self.errors_dict = errors_dict

    def to_response(self) -> dict:
        return {
            "message": "Check the validation errors.",
            "errors": self.errors_dict
        }


async def custom_exception_handling(request: Request, exc: Exception):
    match exc:
        case CustomError():
            return JSONResponse(exc.to_response(), exc.status_code)
        case RequestValidationError():
            errs : RequestValidationError = exc
            return JSONResponse({
                "message": "Oppps! Check the payload.",
                "errors": errs.errors()
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)
        case _:
            return JSONResponse({
                "message": "Sorry! Something went wrong."
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)
