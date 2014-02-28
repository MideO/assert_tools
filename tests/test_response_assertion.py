from assert_tools import assert_raises
from assert_tools.rest import assert_response_equal, UnsupportedResponseCode, \
    UnsupportedObject, assert_response_content_equal
from assert_tools.rest.response_json import responses
from util import MockHttpResponse


def test_assert_response_equal():
    """
    Tests :py:func:`assert_tools.assert_response_equal`.

    Tests that :py:func:`assert_tools.assert_response_equal`
    passes when given `httplib2 Response`
    """
    mock_http_response = MockHttpResponse()
    data_dict = {'status': 200, 'body': {234: 'bcd'}}
    assert_response_equal(mock_http_response(**data_dict)[0], 'OK')


def test_assert_response_content_equal():
    """
    Tests :py:func:`assert_tools.assert_response_content_equal`.

    Tests that :py:func:`assert_tools.assert_response_content_equal`
    passes when expected content and actual content are equal
    """
    mock_http_response = MockHttpResponse()
    data_dict = {'status': 200, 'body': {234: 'bcd'}}
    assert_response_content_equal(
        mock_http_response(**data_dict)[1], data_dict['body'])


def test_assert_response_equal_unsupported_response_code():
    """
    Tests :py:func:`assert_tools.assert_response_equal`.

    Tests that :py:func:`assert_tools.assert_response_equal` raises
    :py:class:`assert_tools.UnsupportedResponseCode when give an
     unknown code, see :py:data:`assert_tools.response_json.responses`

    """
    mock_http_response = MockHttpResponse()
    data_dict = {'status': 200, 'body': {234: 'bcd'}}
    assert_raises(UnsupportedResponseCode, assert_response_equal,
                  *(mock_http_response(**data_dict)[0], 'HJSHD'))


def test_assert_response_equal_unsupported_object():
    """
    Tests :py:func:`assert_tools.assert_response_equal`.

    Tests that :py:func:`assert_tools.assert_response_equal` raises
    :py:class:`assert_tools.UnsupportedObject when give an
     none `httplib2 Response` object
    """
    assert_raises(UnsupportedObject, assert_response_equal,
                  *('blah blah blah', 'OK'))


def test_assert_response_equal_all_supported_codes():
    """
    Tests :py:func:`assert_tools.assert_response_equal` and
    :py:data:`assert_tools.response_json.responses`.

    Tests that :py:func:`assert_tools.assert_response_equal` supports all keys
    in :py:data:`assert_tools.response_json.responses`
    """
    for i in responses.keys():
        mock_http_response = MockHttpResponse()
        data_dict = {'status': responses[i]['status'], 'body': {234: 'bcd'}}
        yield assert_response_equal, mock_http_response(**data_dict)[0], i