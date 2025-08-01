class MyCustomError(Exception):
    """기본 커스텀 예외 클래스."""
    pass

class DataNotFoundError(MyCustomError):
    """특정 데이터가 없을 때 발생하는 예외."""
    def __init__(self, message="데이터를 찾을 수 없습니다."):
        super().__init__(message)