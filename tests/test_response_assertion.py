from nose.tools import assert_raises
from assert_tools.rest import assert_response_equal, UnsupportedResponseCode, \
    UnsupportedObject, assert_response_content_equal
from assert_tools.rest.response_json import responses
from util import MockHttpResponse


def test_assert_response_equal():
    mock_http_response = MockHttpResponse()
    data_dict = {'status': 200, 'body': {234: 'bcd'}}
    assert_response_equal(mock_http_response(**data_dict)[0], 'OK')


def test_assert_response_content_equal():
    mock_http_response = MockHttpResponse()
    data_dict = {'status': 200, 'body': {234: 'bcd'}}
    assert_response_content_equal(
        mock_http_response(**data_dict)[1], data_dict['body'])


def test_assert_response_equal_unsupported_response_code():
    mock_http_response = MockHttpResponse()
    data_dict = {'status': 200, 'body': {234: 'bcd'}}
    assert_raises(UnsupportedResponseCode, assert_response_equal,
                  *(mock_http_response(**data_dict)[0], 'HJSHD'))


def test_assert_response_equal_unsuported_object():
    assert_raises(UnsupportedObject, assert_response_equal,
                  *('skjonsvods', 'OK'))


def test_assert_response_equal_all_supported_codes():
    for i in responses.keys():
        mock_http_response = MockHttpResponse()
        data_dict = {'status': responses[i]['status'], 'body': {234: 'bcd'}}
        yield assert_response_equal, mock_http_response(**data_dict)[0], i