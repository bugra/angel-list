Python API for Angellist 
=========================

Angel is a MIT Licensed Python library to access API of Angellist.
It currently supports Python 2.x and in development. It does not use
any external libraries, so it should work out of the box.


.. code-block:: pycon
  >>> angel = AngelList(config.CLIENT_ID, config.CLIENT_SECRET, config.ACCESS_TOKEN)

...

Requests allow you to send HTTP/1.1 requests. You can add headers, form data,
multipart files, and parameters with simple Python dictionaries, and access the
response data in the same way. It's powered by httplib and `urllib3
<https://github.com/shazow/urllib3>`_, but it does all the hard work and crazy
hacks for you.


Features
--------


Installation
------------

To install angel, simply:
.. code-block:: bash

$ pip install angel


Documentation
-------------


Contribute
----------
#. Fork `the repository`_ on GitHub from the **master** branch.
#. Create a branch in the following format **username-feature**.
#. Write the test for the bug fix or feature.
#. Send a pull request.

.. _`the repository`: http://github.com/bugra/angel-list
