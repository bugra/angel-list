Python API for Angellist
=========================

Angel is a MIT Licensed Python library to access API of Angellist.
It currently supports Python 2.x and in development. It does not use
any external libraries, so it should work out of the box.


Example
--------

    from angel import angel

    al = angel.AngelList(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)

    first_page_jobs = al.get_jobs(page=1)





Features
--------
#. No external dependencies
#. Consistent Api for different features of Angellist
#. Test coverage

Installation
------------

To install angel, simply use `pip`:

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


Known Issues
-------------
#. `put` and `delete` methods are not implemented.
#. `scope of investing` is not implemented
#. It does not support Python 3.
