from typing import TypeVar, Sequence, Callable

T = TypeVar('T')
R = TypeVar('R')


class Seq:
    def __init__(self, sequence: Sequence[T]) -> None:
        self.sequence = sequence
        self.index = 0

    def map(self, function: Callable[[T], R]) -> 'Seq[R]':
        return Seq(map(function, self.sequence))

    def filter(self, function: Callable[[T], bool]) -> 'Seq[T]':
        return Seq(filter(function, self.sequence))

    def take(self, n: int) -> list[T]:
        result = []
        for i in range(n):
            try:
                result.append(self.sequence[self.index])
                self.index += 1
            except IndexError:
                break
        return result


if __name__ != '__main__':
    pass
