import httplib2
import requests
from assert_tools import assert_equal
from assert_tools.rest.response_json import responses


def make_api_call(url, method, args, kwargs):
    """
    Make an appropriate call with httplib2
    """
    client = httplib2.Http()
    return client.request(url, method=method, *args, **kwargs)


class UnsupportedObject(Exception):
    pass


class UnsupportedResponseCode(Exception):
    pass


def as_http_response(response, content=None):
    if isinstance(response, httplib2.Response):
        return response, content
    elif isinstance(response, requests.Response):
        r = httplib2.Response({})
        r.status = response.status_code
        return r, response.content

    raise UnsupportedObject(
        "Unsupported Object expected {0} or {1} got {2}".format(
            httplib2.Response, requests.Response, type(response))
    )


def dict_as_http_response(data_dict):
    if isinstance(data_dict, dict):
        if any(i in data_dict.keys() for i in ['status', 'body']):
            r = httplib2.Response({})
            r.status = data_dict.get('status', 200)
            body = data_dict.get('body', '')
            return r, body
    raise UnsupportedObject("Unsupported Object expected {0} got {1}".format(
        dict, type(data_dict)))


def assert_response_equal(actual_response, expected_response):
    try:
        expected_data_dict = responses[expected_response]
    except KeyError:
        raise UnsupportedResponseCode(
            'Unsuported response code, supported response codes: {0}'.format(
                responses.keys()))

    expected_response, _ = dict_as_http_response(expected_data_dict)
    actual_response, _ = as_http_response(actual_response)
    assert_equal(expected_response.status, actual_response.status)


def assert_response_ok(expected_response):
    assert_response_equal(expected_response, 'OK')


def assert_response_succeed(expected_response):
    assert_response_equal(expected_response, 'SUCCESS')


def assert_response_not_allow(expected_response):
    assert_response_equal(expected_response, 'NOT_ALLOWED')


def assert_response_forbidden(expected_response):
    assert_response_equal(expected_response, 'FORBIDDEN')


def assert_response_denied(expected_response):
    assert_response_equal(expected_response, 'DENY')


def assert_response_bad_request(expected_response):
    assert_response_equal(expected_response, 'BAD_REQUEST')


def assert_response_content_equal(expected_data_dict, actual_response):
    _, expected_content = dict_as_http_response(
        expected_data_dict)
    _, actual_content = as_http_response(actual_response)
    assert_equal(expected_content, actual_content)

