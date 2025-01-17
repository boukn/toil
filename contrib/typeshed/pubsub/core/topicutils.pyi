from .topicexc import TopicNameError as TopicNameError
from textwrap import TextWrapper as TextWrapper
from typing import Sequence, Tuple

UNDERSCORE: str
ALL_TOPICS: str

class WeakNone:
    def __call__(self) -> None: ...

def smartDedent(paragraph: str) -> str: ...
def validateName(topicName: str): ...
def stringize(topicName: Sequence[str]) -> str: ...
def tupleize(topicName: str) -> Tuple[str, ...]: ...
