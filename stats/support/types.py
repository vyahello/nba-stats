from abc import ABC, abstractmethod


class String(ABC):
    """Represent abstraction of a `string` data type."""

    @abstractmethod
    def __str__(self) -> str:
        pass
