from abc import ABC, abstractmethod


class String(ABC):
    """Represent abstraction of a `string` data type."""

    @abstractmethod
    def __str__(self) -> str:
        pass


class Information(ABC):
    """Abstract interface for some information object."""

    @abstractmethod
    def display(self) -> str:
        pass
