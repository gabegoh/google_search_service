import uuid
import datetime
from typing import Any, Literal

from pydantic import BaseModel


class GoogleSearchResponse(BaseModel):
    search_id: str  # unique identifier for
    # this google search
    search_term: str
    response: str | None
    status_code: int
    is_deleted: bool  # flag for indicating
    # if it is deleted. Don't really delete for audit purposes
    created_at: datetime.datetime

    @staticmethod
    def create(
        search_term: str, status_code: int, response: str | None = None
    ) -> "GoogleSearchResponse":
        """
        Smart constructor
        Automatically creates a unique 122 bits
        unique identifier string, and a created_at datetime
        """
        return GoogleSearchResponse(
            search_id=str(uuid.uuid4()),
            search_term=search_term,
            status_code=status_code,
            response=response,
            is_deleted=False,
            created_at=datetime.datetime.now(datetime.UTC),
        )

    def model_dump(
        self,
        *,
        mode: Literal["json", "python"] | str = "python",
        include: set[int] | set[str] | dict[int, Any] | dict[str, Any] | None = None,
        exclude: set[int] | set[str] | dict[int, Any] | dict[str, Any] | None = None,
        by_alias: bool = False,
        exclude_unset: bool = False,
        exclude_defaults: bool = False,
        exclude_none: bool = False,
        round_trip: bool = False,
        warnings: bool = True
    ) -> dict[str, Any]:
        serialized: dict[str, Any] = super().model_dump(
            mode=mode,
            include=include,
            exclude=exclude,
            by_alias=by_alias,
            exclude_unset=exclude_unset,
            exclude_defaults=exclude_defaults,
            exclude_none=exclude_none,
            round_trip=round_trip,
            warnings=warnings,
        )
        serialized["created_at"] = serialized["created_at"].strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        return serialized
