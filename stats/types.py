from abc import ABC, abstractmethod


class String(ABC):
    """Represent abstraction of a `string` data type."""

    @abstractmethod
    def __str__(self) -> str:
        pass


class StampTime(ABC):
    """Represent abstraction of time stamp interface."""

    @abstractmethod
    def today(self) -> str:
        pass

    @abstractmethod
    def yesterday(self) -> str:
        pass

    @abstractmethod
    def tomorrow(self) -> str:
        pass
