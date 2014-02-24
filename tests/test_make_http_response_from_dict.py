from nose.tools import assert_equal, assert_raises

from assert_tools.rest import (
    UnsupportedObject,
    dict_as_http_response)
from util import MockHttpResponse


def test_dict_as_http_response():
    mock_http_response = MockHttpResponse()
    data_dict = {'status': 200, 'body': {234: 'bcd'}}
    result = dict_as_http_response(data_dict)
    assert_equal(mock_http_response(**data_dict), result)


def test_dict_as_http_response_malformed_dict():
    data_dict = {'bar': 200, 'foo': {234: 'bcd'}}
    assert_raises(UnsupportedObject, dict_as_http_response, data_dict)


def test_dict_as_http_response_not_dict():
    not_dict = [4356789]
    assert_raises(UnsupportedObject, dict_as_http_response, not_dict)