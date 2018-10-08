from typing import Any, Tuple
from stats.types import String


class Url(String):
    """Gather url components together."""

    def __init__(self, *url_elements: Any) -> None:
        self._url: Tuple[Any] = url_elements

    def __str__(self) -> str:
        return f"{'/'.join(map(str, self._url))}"
