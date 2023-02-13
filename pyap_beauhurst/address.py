"""
    pyap.address
    ~~~~~~~~~~~~~~~~

    Contains class for constructing Address object which holds information
    about address and its components.

    :copyright: (c) 2015 by Vladimir Goncharov.
    :license: MIT, see LICENSE for more details.
"""
from typing import Any, Dict


class Address:
    full_address: str
    state: str
    city: str
    street: str

    def __init__(self, **args: Any):
        keys = []
        vals = []
        for k, v in args.items():
            if v and isinstance(v, str):
                v = v.strip(" ,;:")
            # create object variables
            setattr(self, k, v)
            # prepare for dict
            keys.append(k)
            vals.append(v)
        self.data_as_dict = dict(zip(keys, vals))

    def as_dict(self) -> Dict[str, str]:
        # Return parsed address parts as a dictionary
        return self.data_as_dict

    def __repr__(self) -> str:
        # Address object is represented as textual address
        address = ""
        try:
            address = self.full_address
        except AttributeError:
            pass

        return address
