.. assert_tools documentation master file, created by
   sphinx-quickstart on Tue Mar  4 10:31:48 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to assert_tools's documentation!
========================================
A Python Unit/Functional test library, with custom assertions for RESTful API
verbs (GET, POST, PUT DELETE), all unittest2 assert* converted to pep8 style
functions and custom assertions for http status code


.. toctree::
    :maxdepth: 2

    modules

usage
=====
.. code-block:: python

    from assert_tools import assert_equal
    def func():
        return 2
    def test_func():
        assert_equal(2, func())

More interesting stuff with RESTful api..
Small bottle server to run as SUT: server.py

.. code-block:: python

    from bottle import route, run, response, request
    def do():
        if request.GET.get('code'):
            response.status = int(request.GET.get('code'))
        else:
            response.status = 200
        return request.body

    @route('/goo', method='GET')
    def response_get(): return do()

    @route('/goo', method='DELETE' )
    def response_delete(): return do()

    @route('/goo', method='PUT')
    def response_put(): return do()

    @route('/goo', method='POST')
    def response_post(): return do()

    run(host='localhost', port=8080, debug=True)


Test Code: test_server.py

.. code-block:: python

    import httplib2
    from assert_tools.rest import assert_response_ok, assert_delete_request_returns_success_status_code)
    from requests import get

    def test_get_server_base_url():
        assert_response_ok(get('http://localhost:8080/goo'))
        client = httplib2.Http()
        assert_response_ok(client.request('http://localhost:8080/goo', 'GET'))

    def test_server_response_to_delete():
        assert_delete_request_returns_success_status_code(
            'http://localhost:8080/goo?code=201',
            expected_content='abc', request_kwargs={'body':'abc'})



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

