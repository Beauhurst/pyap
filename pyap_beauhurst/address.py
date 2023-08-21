"""
    pyap.address
    ~~~~~~~~~~~~~~~~

    Contains class for constructing Address object which holds information
    about address and its components.

    :copyright: (c) 2015 by Vladimir Goncharov.
    :license: MIT, see LICENSE for more details.
"""
from typing import Any, Optional, Union

from pydantic import BaseModel, field_validator


class Address(BaseModel):
    building_id: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    country_id: Optional[str] = None
    floor: Optional[str] = None
    full_address: str
    full_street: Optional[str] = None
    match_end: Optional[Union[int, str]] = None
    match_start: Optional[Union[int, str]] = None
    occupancy: Optional[str] = None
    postal_code: Optional[str] = None
    region1: Optional[str] = None
    route_id: Optional[str] = None
    state: Optional[str] = None
    street: Optional[str] = None
    street_name: Optional[str] = None
    street_number: Optional[str] = None
    street_type: Optional[str] = None

    @field_validator("*", mode="before")
    @classmethod
    def strip_chars(cls, v: Any) -> Any:
        if isinstance(v, str):
            return v.strip(" ,;:")
        if v:
            return v

    def __str__(self) -> str:
        # Address object is represented as textual address
        address = ""
        try:
            address = self.full_address
        except AttributeError:
            pass

        return address
