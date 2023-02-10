""" Tests for CANADA address parser """

import pytest

import pyap_beauhurst.source_CA.data as data_ca
from test_utils import execute_matching_test


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("ZERO ", True),
        ("one ", True),
        ("two ", True),
        ("Three ", True),
        ("FoUr ", True),
        ("FivE ", True),
        ("six ", True),
        ("SEvEn ", True),
        ("Eight ", True),
        ("Nine ", True),
        # negative assertions
        ("Nidnes", False),
        ("One", False),
        ("two", False),
        ("onetwothree ", False),
    ],
)
def test_zero_to_nine(input_data: str, match_expectation: bool) -> None:
    """test string match for zero_to_nine"""
    execute_matching_test(input_data, match_expectation, data_ca.zero_to_nine)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("tEN ", True),
        ("TWENTY ", True),
        ("tHirtY ", True),
        ("FOUrty ", True),
        ("fifty ", True),
        ("sixty ", True),
        ("seventy ", True),
        ("eighty ", True),
        ("NINety ", True),
        # negative assertions
        ("ten", False),
        ("twenTY", False),
        ("sixtysixsty ", False),
        ("one twenty ", False),
    ],
)
def test_ten_to_ninety(input_data: str, match_expectation: bool) -> None:
    """test string match for ten_to_ninety"""
    execute_matching_test(input_data, match_expectation, data_ca.ten_to_ninety)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("Hundred ", True),
        ("HuNdred ", True),
        # negative assertions
        ("HuNDdred", False),
        ("HuNDdred hundred ", False),
    ],
)
def test_hundred(input_data: str, match_expectation: bool) -> None:
    """tests string match for a hundred"""
    execute_matching_test(input_data, match_expectation, data_ca.hundred)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("Thousand ", True),
        ("thOUSAnd ", True),
        # negative assertions
        ("thousand", False),
        ("THoussand ", False),
        ("THoussand", False),
        ("THOUssand THoussand ", False),
    ],
)
def test_thousand(input_data: str, match_expectation: bool) -> None:
    """tests string match for a thousand"""
    execute_matching_test(input_data, match_expectation, data_ca.thousand)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions (words)
        ("One Thousand And Fifty Nine ", True),
        ("Two hundred and fifty ", True),
        ("Three hundred four ", True),
        ("Thirty seven ", True),
        ("FIFTY One ", True),
        ("Three hundred Ten ", True),
        # positive assertions (numbers)
        ("1 ", True),
        ("15 ", True),
        ("44 ", True),
        ("256 ", True),
        ("256 ", True),
        ("1256 ", True),
        ("32457 ", True),
        # negative assertions (words)
        ("ONE THousszz22and FIFTY and four onde", False),
        ("ONE one oNe and onE Three", False),
        # negative assertions (numbers)
        ("536233", False),
        ("111111", False),
        ("1111ss11", False),
        ("123 456", False),
    ],
)
def test_street_number(input_data: str, match_expectation: bool) -> None:
    """tests positive exact string match for a street number"""
    execute_matching_test(input_data, match_expectation, data_ca.street_number)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("N. ", True),
        ("N ", True),
        ("S ", True),
        ("West ", True),
        ("eASt ", True),
        ("NW ", True),
        ("SE ", True),
        # negative assertions
        ("NW.", False),
        ("NW. ", False),
        ("NS ", False),
        ("EW ", False),
    ],
)
def test_post_direction(input_data: str, match_expectation: bool) -> None:
    """tests string match for a post_direction"""
    execute_matching_test(input_data, match_expectation, data_ca.post_direction)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("Street ", True),
        ("St. ", True),
        ("St.", True),
        ("Blvd.", True),
        ("Blvd. ", True),
        ("RD", True),
        ("Cir", True),
        ("Highway ", True),
        ("Hwy ", True),
        ("Ctr", True),
        ("Sq.", True),
        ("Street route 5 ", True),
        ("blvd", True),
        # negative assertions
        # TODO
    ],
)
def test_street_type(input_data: str, match_expectation: bool) -> None:
    """tests string match for a street id"""
    execute_matching_test(input_data, match_expectation, data_ca.street_type)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("floor 3 ", True),
        ("floor 11 ", True),
        ("floor 15 ", True),
        ("1st floor ", True),
        ("2nd floor ", True),
        ("15th floor ", True),
        ("16th. floor ", True),
        # negative assertions
        ("16th.floor ", False),
        ("1stfloor ", False),
    ],
)
def test_floor(input_data: str, match_expectation: bool) -> None:
    """tests string match for a floor"""
    execute_matching_test(input_data, match_expectation, data_ca.floor)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("bldg m ", True),
        ("Building F ", True),
        ("bldg 2 ", True),
        ("building 3 ", True),
        ("building 100 ", True),
        ("Building ", True),
        ("building one ", True),
        ("Building three ", True),
        # negative assertions
        ("bldg", False),
        ("bldgm", False),
        ("bldg100 ", False),
    ],
)
def test_building(input_data: str, match_expectation: bool) -> None:
    """tests string match for a building"""
    execute_matching_test(input_data, match_expectation, data_ca.building)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("suite 900 ", True),
        ("Suite #2 ", True),
        ("suite #218 ", True),
        ("suite J7 ", True),
        ("suite 102A ", True),
        ("suite a&b ", True),
        ("Suite J#200 ", True),
        ("suite 710-327 ", True),
        ("Suite A ", True),
        ("ste A ", True),
        ("Ste 101 ", True),
        ("ste 502b ", True),
        ("ste 14-15 ", True),
        ("ste E ", True),
        ("ste 9E ", True),
        ("Suite 1800 ", True),
        ("Apt 1B ", True),
        ("Rm. 52 ", True),
    ],
)
def test_occupancy(input_data: str, match_expectation: bool) -> None:
    """tests exact string match for a place id"""
    execute_matching_test(input_data, match_expectation, data_ca.occupancy)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("po box 108", True),
        ("Po Box 53485", True),
        ("P.O. box 119", True),
        ("PO box 1070", True),
        # negitive assertions
        ("POb ox1070", False),
        ("boxer 123", False),
    ],
)
def test_po_box(input_data: str, match_expectation: bool) -> None:
    """tests string match for a po box"""
    execute_matching_test(input_data, match_expectation, data_ca.po_box)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("T2P 1H3", True),
        ("T2P1H3", True),
        ("L1W3E6", True),
        ("L4N 8G1", True),
        ("J8Y 3G5", True),
        ("J9A 1L8", True),
        # positive assertions
        ("1", False),
        ("23", False),
        ("456", False),
        ("4567", False),
        ("750621", False),
        ("95130-642", False),
        ("95130-64212", False),
    ],
)
def test_postal_code(input_data: str, match_expectation: bool) -> None:
    """test exact string match for postal code"""
    execute_matching_test(input_data, match_expectation, data_ca.postal_code)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("Quebec", True),
        ("Nova Scotia", True),
        ("Colombie-Britannique", True),
        ("New Brunswick", True),
        ("Quebec", True),
        ("Québec", True),
        ("Territoires Du Nord-Ouest", True),
    ],
)
def test_region1(input_data: str, match_expectation: bool) -> None:
    """test exact string match for province"""
    execute_matching_test(input_data, match_expectation, data_ca.region1)


@pytest.mark.parametrize(
    ("input_data", "match_expectation"),
    [
        # positive assertions
        ("CANADA", True),
        ("Canada", True),
    ],
)
def test_country(input_data: str, match_expectation: bool) -> None:
    """test exact string match for country"""
    execute_matching_test(input_data, match_expectation, data_ca.country)
