from abc import ABC, abstractmethod


class String(ABC):
    """Represent abstraction of a `string` data type."""

    @abstractmethod
    def __str__(self) -> str:
        pass


class Information(ABC):
    """Abstract interface for some information object."""

    @abstractmethod
    def retrieve(self) -> str:
        pass


class NotAvailable(String):
    """Represent not available string if it is empty."""

    def __init__(self, data: str = '') -> None:
        self._data = data

    def __str__(self) -> str:
        if not self._data:
            return 'N/A'
        return self._data
