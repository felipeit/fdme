from typing import Any


class ErrorsMixin:
    def register_errors(self, errors: list[BaseException]) -> Any:
        if not hasattr(self, "_errors"):
            self._errors: set[BaseException] = set()
        self._errors.update(errors)

    @property
    def errors(self) -> list[BaseException]:
        return list(self._errors)