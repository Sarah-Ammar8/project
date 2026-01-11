class AppError(Exception):
    """Base class for expected application errors."""
    def __init__(self, message: str, *, error: str = "APP_ERROR", details: dict | None = None):
        super().__init__(message)
        self.error = error
        self.message = message
        self.details = details or {}

class NotFoundError(AppError):
    def __init__(self, message: str = "Resource not found", *, details: dict | None = None):
        super().__init__(message, error="NOT_FOUND", details=details)

class ValidationError(AppError):
    def __init__(self, message: str = "Invalid input", *, details: dict | None = None):
        super().__init__(message, error="VALIDATION_ERROR", details=details)
