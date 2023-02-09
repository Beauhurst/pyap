# -*- coding: utf-8 -*-

"""
    pyap.address
    ~~~~~~~~~~~~~~~~

    Contains class for constructing Address object which holds information
    about address and its components.

    :copyright: (c) 2015 by Vladimir Goncharov.
    :license: MIT, see LICENSE for more details.
"""


class Address(object):
    def __init__(self, **args):
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

    def as_dict(self):
        # Return parsed address parts as a dictionary
        return self.data_as_dict

    def __repr__(self):
        # Address object is represented as textual address
        address = ""
        try:
            address = self.full_address
        except AttributeError:
            pass

        return address
