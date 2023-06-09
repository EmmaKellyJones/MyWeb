import datetime
from _typeshed import ReadableBuffer, Unused
from collections import OrderedDict
from collections.abc import Iterator
from re import Match, Pattern
from typing import Any, overload
from typing_extensions import Literal, Self, TypeAlias

_RetType: TypeAlias = type[float | datetime.datetime]

step_search_re: Pattern[str]
only_int_re: Pattern[str]
star_or_int_re: Pattern[str]
special_weekday_re: Pattern[str]
hash_expression_re: Pattern[str]
VALID_LEN_EXPRESSION: list[int]

def timedelta_to_seconds(td: datetime.timedelta) -> float: ...

class CroniterError(ValueError): ...
class CroniterBadTypeRangeError(TypeError): ...
class CroniterBadCronError(CroniterError): ...
class CroniterUnsupportedSyntaxError(CroniterBadCronError): ...
class CroniterBadDateError(CroniterError): ...
class CroniterNotAlphaError(CroniterError): ...

def datetime_to_timestamp(d: datetime.datetime) -> float: ...

class croniter(Iterator[Any]):
    MONTHS_IN_YEAR: Literal[12]
    RANGES: tuple[tuple[int, int], ...]
    DAYS: tuple[
        Literal[31],
        Literal[28],
        Literal[31],
        Literal[30],
        Literal[31],
        Literal[30],
        Literal[31],
        Literal[31],
        Literal[30],
        Literal[31],
        Literal[30],
        Literal[31],
    ]
    ALPHACONV: tuple[dict[str, Any], ...]
    LOWMAP: tuple[dict[int, Any], ...]
    LEN_MEANS_ALL: tuple[int, ...]
    bad_length: str
    tzinfo: datetime.tzinfo | None
    cur: float
    expanded: list[list[str]]
    start_time: float
    dst_start_time: float
    nth_weekday_of_month: dict[str, Any]
    def __init__(
        self,
        expr_format: str,
        start_time: float | datetime.datetime | None = None,
        ret_type: _RetType | None = ...,
        day_or: bool = True,
        max_years_between_matches: int | None = None,
        is_prev: bool = False,
        hash_id: str | bytes | None = None,
    ) -> None: ...
    # Most return value depend on ret_type, which can be passed in both as a method argument and as
    # a constructor argument.
    def get_next(self, ret_type: _RetType | None = None, start_time: float | datetime.datetime | None = None) -> Any: ...
    def get_prev(self, ret_type: _RetType | None = None) -> Any: ...
    def get_current(self, ret_type: _RetType | None = None) -> Any: ...
    def set_current(self, start_time: float | datetime.datetime | None, force: bool = True) -> float: ...
    def __iter__(self) -> Self: ...
    def next(
        self, ret_type: _RetType | None = None, start_time: float | datetime.datetime | None = None, is_prev: bool | None = None
    ) -> Any: ...
    __next__ = next
    def all_next(self, ret_type: _RetType | None = None) -> Iterator[Any]: ...
    def all_prev(self, ret_type: _RetType | None = None) -> Iterator[Any]: ...
    def iter(self, ret_type: _RetType | None = ...) -> Iterator[Any]: ...
    def is_leap(self, year: int) -> bool: ...
    @classmethod
    def expand(cls, expr_format: str, hash_id: str | bytes | None = None) -> tuple[list[list[str]], dict[str, Any]]: ...
    @classmethod
    def is_valid(cls, expression: str, hash_id: str | bytes | None = None) -> bool: ...
    @classmethod
    def match(cls, cron_expression: str, testdate: float | datetime.datetime | None, day_or: bool = True) -> bool: ...

def croniter_range(
    start: float | datetime.datetime,
    stop: float | datetime.datetime,
    expr_format: str,
    ret_type: _RetType | None = None,
    day_or: bool = True,
    exclude_ends: bool = False,
    _croniter: type[croniter] | None = None,
) -> Iterator[Any]: ...

class HashExpander:
    cron: croniter
    def __init__(self, cronit: croniter) -> None: ...
    @overload
    def do(
        self,
        idx: int,
        hash_type: Literal["r"],
        hash_id: None = None,
        range_end: int | None = None,
        range_begin: int | None = None,
    ) -> int: ...
    @overload
    def do(
        self, idx: int, hash_type: str, hash_id: ReadableBuffer, range_end: int | None = None, range_begin: int | None = None
    ) -> int: ...
    @overload
    def do(
        self,
        idx: int,
        hash_type: str = "h",
        *,
        hash_id: ReadableBuffer,
        range_end: int | None = None,
        range_begin: int | None = None,
    ) -> int: ...
    def match(self, efl: Unused, idx: Unused, expr: str, hash_id: Unused = None, **kw: Unused) -> Match[str] | None: ...
    def expand(
        self,
        efl: object,
        idx: int,
        expr: str,
        hash_id: ReadableBuffer | None = None,
        match: Match[str] | None | Literal[""] = "",
        **kw: object,
    ) -> str: ...

EXPANDERS: OrderedDict[str, HashExpander]
