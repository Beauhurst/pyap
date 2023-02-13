import re

from pyap_beauhurst import utils


def execute_matching_test(
    input_data: str, is_match_expected: bool, pattern: str
) -> None:
    match = utils.match(pattern, input_data, re.VERBOSE)
    is_found = match is not None
    if is_match_expected:
        assert is_found == is_match_expected
        if isinstance(match, re.Match):
            assert match.group(0) == input_data
    else:
        """we check that:
        - input_data should not to match our regex
        - our match should be partial if regex matches some part of string
        """
        if match:
            assert (is_found == is_match_expected) or (match.group(0) != input_data)
