from typing import TypeVar, List

T = TypeVar('T')
def first(container: List[T]) -> T:
    return container[0]

def first_2(container: List[T]) -> T:
    print(container)
    return "a" # mypy raises: Incompatible return value type (got "str", expected "T")
  
if __name__ == "__main__":
    list_one: List[str] = ["a", "b", "c"]
    print(first(list_one))
    print(first_2(list_one))

    list_two: List[int] = [1, 2, 3]
    print(first(list_two))
    print(first_2(list_two))
