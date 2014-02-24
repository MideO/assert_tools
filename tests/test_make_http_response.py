from nose.tools import assert_equal, assert_raises
from assert_tools.rest import (
    as_http_response,
    UnsupportedObject
)
from util import MockHttpResponse, MockRequestsResponse


def test_as_http_response_support_for_httplib():
    mock_http_response = MockHttpResponse()
    result = as_http_response(*mock_http_response())
    assert_equal(mock_http_response(), result)


def test_as_http_response_support_for_requests():
    mock_requests_response = MockRequestsResponse()
    mock_http_response = MockHttpResponse()
    result = as_http_response(mock_requests_response())
    assert_equal(mock_http_response(), result)


def test_as_http_response_invalid_object():
    assert_raises(UnsupportedObject, as_http_response, 'foo')
