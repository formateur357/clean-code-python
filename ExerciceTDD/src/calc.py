def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def apply_rate(amount: float, rate: float) -> float :
    if rate <= 0:
        raise ValueError("rate must be > 0")
    return round(amount * rate, 2)

class Counter:
    def __init__(self, start: int = 0):
        self._start = int(start)
        self._value = int(start)

    @property
    def value(self) -> int :
        return self._value
    
    def increment(self) -> None :
        self._value += 1

    def reset(self) -> None :
        self._value = self._start