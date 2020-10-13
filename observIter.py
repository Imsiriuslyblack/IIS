from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator


class Subject(ABC):
    @abstractmethod
    def attach(self, observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    _state = None
    _observer = None

    def attach(self, observer) -> None:
        print('Подписан')
        self._observer = observer

    def notify(self, collection) -> None:
        self._observer.update(collection)

    def some_business_logic(self) -> None:
        collection = Auto()
        collection.add_item("BMW")
        collection.add_item("AUDI")
        collection.add_item("TOYOTA")

        self.notify(collection)


class Observer(ABC):
    @abstractmethod
    def update(self, collection) -> None:
        pass


class AudiObserver(Observer):
    def update(self, collection) -> None:
        for elem in collection:
            if elem == 'AUDI':
                print('Итератор на AUDI')


class AutoIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class Auto(Iterable):
    def __init__(self, collection = []) -> None:
        self._collection = collection

    def __iter__(self) -> AutoIterator:
        return AutoIterator(self._collection)

    def get_reverse_iterator(self) -> AutoIterator:
        return AutoIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


if __name__ == "__main__":

    subject = ConcreteSubject()

    observer_audi = AudiObserver()
    subject.attach(observer_audi)
    subject.some_business_logic()
