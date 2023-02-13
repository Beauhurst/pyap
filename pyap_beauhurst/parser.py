"""
    pyap.parser
    ~~~~~~~~~~~~~~~~

    This module contains AddressParser class which connects all the
    functionality of the package in one place.

    :copyright: (c) 2015 by Vladimir Goncharov.
    :license: MIT, see LICENSE for more details.
"""

import importlib
import re
from typing import Any, Dict, List, Optional, Union

from . import address, exceptions as e, utils


class AddressParser:
    country: str
    clean_text: str

    def __init__(self, **kwargs: Any):
        """Initialize with custom arguments"""

        for k, v in kwargs.items():
            # store country id in uppercase
            if k == "country":
                v = v.upper()
            setattr(self, k, v)
        try:
            # import detection rules
            package = "pyap_beauhurst" + ".source_" + self.country + ".data"
            data = importlib.import_module(package)
            self.rules = data.full_address

        except AttributeError:
            raise e.NoCountrySelected(
                "No country specified during library initialization.", "Error 1"
            ) from None

        except ImportError:
            raise e.CountryDetectionMissing(
                'Detection rules for country "{country}" not found.'.format(
                    country=self.country
                ),
                "Error 2",
            ) from None

    def parse(self, text: str) -> List[Optional[address.Address]]:
        """
        Returns a list of addresses found in text together with parsed address parts
        """
        results: List[Optional[address.Address]] = []
        self.clean_text = self._normalize_string(text)

        # get addresses
        address_matches = utils.finditer(self.rules, self.clean_text)

        if address_matches:
            # append parsed address info
            results: List[Optional[address.Address]] = list(  # type: ignore[no-redef]
                map(self._parse_address, address_matches)
            )

        return results

    def _parse_address(self, match: Union[re.Match, str]) -> Optional[address.Address]:
        """Parses address into parts"""
        if isinstance(match, str):
            # If the address is passed as a match it saves doing the match twice
            match: Optional[re.Match] = utils.match(  # type: ignore[no-redef]
                self.rules, match, flags=re.VERBOSE | re.U
            )
        if match:
            if isinstance(match, re.Match):
                match_as_dict = match.groupdict()
                match_as_dict.update({"country_id": self.country})
                # combine results
                cleaned_dict = self._combine_results(match_as_dict)
                cleaned_dict["match_start"] = match.start()
                cleaned_dict["match_end"] = match.end()
                # create object containing results
                return address.Address(**cleaned_dict)

        return None

    @staticmethod
    def _combine_results(
        match_as_dict: Dict[str, Union[str, int, None]]
    ) -> Dict[str, Union[str, int, None]]:
        """Combine results from different parsed parts:
        we look for non-empty results in values like
        'postal_code_b' or 'postal_code_c' and store
        them as main value.

        So 'postal_code_b':'123456'
            becomes:
           'postal_code'  :'123456'
        """
        keys: List[str] = []
        vals: List[Union[str, int, None]] = []
        for k, v in match_as_dict.items():
            if k[-2:] in "_a_b_c_d_e_f_g_h_i_j_k_l_m":
                if v:
                    # strip last 2 chars: '..._b' -> '...'
                    keys.append(k[:-2])
                    vals.append(v)
            else:
                if k not in keys:
                    keys.append(k)
                    vals.append(v)
        return dict(zip(keys, vals))

    @staticmethod
    def _normalize_string(text: str) -> str:
        """Prepares incoming text for parsing:
        removes excessive spaces, tabs, newlines, etc.
        """
        conversion = {
            # newlines
            r"\r*(\n\r*)+": ", ",
            r"\s*(\,\s*)+": ", ",
            # replace excessive empty spaces
            r"\s+": " ",
            # convert all types of hyphens/dashes to a
            # simple old-school dash
            # from http://utf8-chartable.de/unicode-utf8-table.pl?
            # start=8192&number=128&utf8=string-literal
            "‐": "-",
            "‑": "-",
            "‒": "-",
            "–": "-",
            "—": "-",
            "―": "-",
        }
        for find, replace in conversion.items():
            text = re.sub(find, replace, text, flags=re.UNICODE)
        return text
