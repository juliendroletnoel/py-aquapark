from abc import ABC, abstractmethod


class IntegerRange:
    def __init__(self,
                 min_amount: int,
                 max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(self, instance: object, name: str) -> None:
        self.protected_name = "_" + name

    def __get__(self, instance: object, owner: object) -> object:
        return getattr(instance, self.protected_name)

    def __set__(self, instance: object, value: object) -> None:
        if not isinstance(value, int):
            raise TypeError(f"{value} must be integer")
        if value < self.min_amount or value > self.max_amount:
            raise ValueError(f"{value} must be between {self.min_amount} "
                             f"and {self.max_amount}")

        setattr(instance, self.protected_name, value)


class Visitor:
   def __init__(self,
                name: str,
                age: int,
                weight: int,
                height: int) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class SlideLimitationValidator(ABC):

    def __init__(self,
                 age: int,
                 weight: int,
                 height: int) -> None:
        self.age = age
        self.weight = weight
        self.height = height


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    age = IntegerRange(4, 14)
    height = IntegerRange(80, 120)
    weight = IntegerRange(20, 50)
    
    def __init__(self,
                 age: int,
                 height: int,
                 weight: int) -> None:
        super().__init__(age, height, weight)


class AdultSlideLimitationValidator(SlideLimitationValidator):
    age = IntegerRange(14, 60)
    height = IntegerRange(120, 220)
    weight = IntegerRange(50, 120)

    def __init__(self,
                 age: int,
                 height: int,
                 weight: int) -> None:
        super().__init__(age, height, weight)


class Slide:
    def __init__(self,
                 name: str,
                 limitation_class: SlideLimitationValidator) -> None:
        self.name = name
        self.limition_class = limitation_class


def can_access(visitor: Visitor, slide: Slide) -> bool:
    validator = None

    try:
        validator = None
    except TypeError:
        return False
    except ValueError:
        return False

    return True
