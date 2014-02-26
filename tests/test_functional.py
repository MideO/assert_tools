from mock import patch, MagicMock

from assert_tools import rest
from assert_tools.rest.response_json import responses
from util import MockHttpResponse


_find_funcs = lambda function_matcher, module: [
    getattr(module, func) for func in dir(module) if func.startswith(
        function_matcher)]


def _look_up(code, func_list):
    for func in func_list:
        if code.lower() in func.func_name:
            return func


def test_assert_get_request_returns_status_codes():
    assertions = _find_funcs('assert_get_request', rest)
    for k, v in responses.items():
        mock_http_response = MockHttpResponse()
        assertion = _look_up(k, assertions)
        with patch('assert_tools.rest.make_api_call',
                   MagicMock(return_value=mock_http_response(**v))):
            yield assertion, 'http://test.url', v["body"], {}


def test_assert_post_request_returns_status_codes():
    assertions = _find_funcs('assert_post_request', rest)
    for k, v in responses.items():
        mock_http_response = MockHttpResponse()
        assertion = _look_up(k, assertions)
        with patch('assert_tools.rest.make_api_call',
                   MagicMock(return_value=mock_http_response(**v))):
            yield assertion, 'http://test.url', v["body"], {}


def test_assert_put_request_returns_status_codes():
    assertions = _find_funcs('assert_put_request', rest)
    for k, v in responses.items():
        mock_http_response = MockHttpResponse()
        assertion = _look_up(k, assertions)
        with patch('assert_tools.rest.make_api_call',
                   MagicMock(return_value=mock_http_response(**v))):
            yield assertion, 'http://test.url', v["body"], {}


def test_assert_delete_request_returns_status_codes():
    assertions = _find_funcs('assert_delete_request', rest)
    for k, v in responses.items():
        mock_http_response = MockHttpResponse()
        assertion = _look_up(k, assertions)
        with patch('assert_tools.rest.make_api_call',
                   MagicMock(return_value=mock_http_response(**v))):
            yield assertion, 'http://test.url', v["body"], {}