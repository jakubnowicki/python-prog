from typing import Any, Mapping, Optional, Sequence, Tuple, Union
from pytypes import typechecked

class Result:
    def __init__(
        self,
        fixed: Sequence[str],
        named: Mapping[str, str],
        spans: Mapping[int, Tuple[int, int]],
    ) -> None:
        self.fixed = fixed
        self.named = named
        self.spans = spans

    def __getitem__(self, item: Union[int, str]) -> str:
        return str(item)

    def __repr__(self) -> str:
        return "Result(...)"

def parse(
    format: str,
    string: str,
    evaluate_result: bool = True,
    case_sensitive: bool = False,
) -> Optional[Result]:
    if evaluate_result:
        return Result([], {}, {})
    return None

@typechecked
def policz_cos(a: int, b: str = "") -> int:
    temp: int  # jeszcze nie ma takiej zmiennej
    factor: int = 2
    temp = a * len(b) * factor
    return temp

parse("format", "str")
policz_cos(1, "abc")
policz_cos(1.5, ["a", "b"])

# mypy typehints.py
# pip install pytypes