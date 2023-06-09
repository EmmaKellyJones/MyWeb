from typing import Any

class ContainerIO:
    fh: Any
    pos: int
    offset: Any
    length: Any
    def __init__(self, file, offset, length) -> None: ...
    def isatty(self): ...
    def seek(self, offset, mode=0) -> None: ...
    def tell(self): ...
    def read(self, n: int = 0): ...
    def readline(self): ...
    def readlines(self): ...
