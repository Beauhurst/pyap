"""
pyap.utils
~~~~~~~~~~~~~~~~

This module provides some utility functions.

:copyright: (c) 2015 by Vladimir Goncharov.
:license: MIT, see LICENSE for more details.
"""
import re
from re import RegexFlag
from typing import List, Optional

DEFAULT_FLAGS = re.VERBOSE | re.UNICODE


def match(
    regex: str, string: str, flags: RegexFlag = DEFAULT_FLAGS
) -> Optional[re.Match]:
    """Utility function for re.match"""
    return re.match(regex, string, flags=flags)


def findall(
    regex: str, string: str, flags: RegexFlag = DEFAULT_FLAGS
) -> List[Optional[re.Match]]:
    """Utility function for re.findall"""
    return re.findall(regex, string, flags=flags)


def finditer(
    regex: str, string: str, flags: RegexFlag = DEFAULT_FLAGS
) -> List[re.Match]:
    """Utility function for re.finditer"""
    return list(re.finditer(regex, string, flags=flags))
