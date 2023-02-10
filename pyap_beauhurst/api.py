"""
    pyap.api
    ~~~~~~~~~~~~~~~~

    This module contains address parser API functions.

    :copyright: (c) 2015 by Vladimir Goncharov.
    :license: MIT, see LICENSE for more details.
"""
from typing import Any, List, Optional

import pyap_beauhurst.address

from . import parser


def parse(
    some_text: str, **kwargs: Any
) -> List[Optional[pyap_beauhurst.address.Address]]:
    """Creates request to AddressParser
    and returns list of Address objects
    """
    ap = parser.AddressParser(**kwargs)
    return ap.parse(some_text)
