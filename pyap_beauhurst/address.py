"""
    pyap.address
    ~~~~~~~~~~~~~~~~

    Contains class for constructing Address object which holds information
    about address and its components.

    :copyright: (c) 2015 by Vladimir Goncharov.
    :license: MIT, see LICENSE for more details.
"""
from typing import Any, Optional

from pydantic import BaseModel, validator


class Address(BaseModel):
    building_id: Optional[str]
    city: Optional[str]
    country: Optional[str]
    country_id: Optional[str]
    floor: Optional[str]
    full_address: str
    full_street: Optional[str]
    match_end: Optional[str]
    match_start: Optional[str]
    occupancy: Optional[str]
    postal_code: Optional[str]
    region1: Optional[str]
    route_id: Optional[str]
    state: Optional[str]
    street: Optional[str]
    street_name: Optional[str]
    street_number: Optional[str]
    street_type: Optional[str]

    @validator("*", pre=True, allow_reuse=True)
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
