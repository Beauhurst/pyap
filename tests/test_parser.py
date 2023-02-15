""" Test for parser classes """

import pytest

import pyap_beauhurst as ap
from pyap_beauhurst import address, exceptions as e, parser


def test_api_parse() -> None:
    test_address = (
        "xxx 225 E. John Carpenter Freeway, " + "Suite 1500 Irving, Texas 75062 xxx"
    )
    addresses = ap.parse(test_address, country="US")
    assert isinstance(addresses[0], address.Address)
    assert (
        str(addresses[0].full_address)
        == "225 E. John Carpenter Freeway, Suite 1500 Irving, Texas 75062"
    )


def test_address_class_init() -> None:
    addr = address.Address(
        state="USA ",
        city="CityVille, ",
        street=" Street 1b ",
        full_address="Street 1b CityVille USA",
    )
    assert addr.state == "USA"

    assert addr.city == "CityVille"

    assert addr.street == "Street 1b"

    assert addr.dict() == {
        "building_id": None,
        "city": "CityVille",
        "country": None,
        "country_id": None,
        "floor": None,
        "full_address": "Street 1b CityVille USA",
        "full_street": None,
        "match_end": None,
        "match_start": None,
        "occupancy": None,
        "postal_code": None,
        "region1": None,
        "route_id": None,
        "state": "USA",
        "street": "Street 1b",
        "street_name": None,
        "street_number": None,
        "street_type": None,
    }

    assert str(addr) == "Street 1b CityVille USA"


def test_no_country_selected_exception() -> None:
    with pytest.raises(e.NoCountrySelected):
        parser.AddressParser()


def test_country_detection_missing() -> None:
    with pytest.raises(e.CountryDetectionMissing):
        parser.AddressParser(country="TheMoon")


def test_normalize_string() -> None:
    address_parser = parser.AddressParser(country="US")
    raw_string = """\n The  quick      \t, brown fox      jumps over the lazy dog,
    ‐ ‑ ‒ – — ―
    """
    clean_string = ", The quick, brown fox jumps over the lazy dog, - - - - - -, "
    assert address_parser._normalize_string(raw_string) == clean_string


def test_combine_results() -> None:
    address_parser = parser.AddressParser(country="US")
    raw_dict = {"test_one": None, "test_one_a": 1, "test_two": None, "test_two_b": "2"}
    assert address_parser._combine_results(raw_dict) == {"test_one": 1, "test_two": "2"}


def test_parse_address() -> None:
    address_parser = parser.AddressParser(country="US")
    parse_result = address_parser.parse("No address here")
    assert not parse_result

    address_parser = parser.AddressParser(country="US")
    _parse_address_result = address_parser._parse_address("No address here")
    assert not _parse_address_result

    address_parser = parser.AddressParser(country="US")
    test_address = (
        "xxx 225 E. John Carpenter Freeway, " + "Suite 1500 Irving, Texas 75062 xxx"
    )

    addresses = address_parser.parse(test_address)
    assert isinstance(addresses[0], address.Address)
    assert (
        addresses[0].full_address
        == "225 E. John Carpenter Freeway, Suite 1500 Irving, Texas 75062"
    )
