from abc import ABC, abstractclassmethod

class TextSupplier(ABC):
    @abstractclassmethod
    def get_text(self) -> str:
        ...

