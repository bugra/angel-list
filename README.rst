Python API for Angellist
=========================
.. image:: http://img.shields.io/pypi/v/angel.svg?style=flat
    :target: https://pypi.python.org/pypi/angel

.. image:: http://jenkins.jarenglover.com/job/angel-list/badge/icon
    :target: http://jenkins.jarenglover.com/job/angel-list

.. image:: http://img.shields.io/pypi/dm/angel.svg?style=flat
    :target: https://pypi.python.org/pypi/angel

Angel is an MIT Licensed Python library to access API of Angellist.
It currently supports Python 2.7 and in development. It does not use
any external libraries and has extensive test coverage.


Example
--------

    from angel import angel

    al = angel.AngelList(CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN)

    first_page_jobs = al.get_jobs(page=1)

Some capabilities of module are `here <http://nbviewer.ipython.org/urls/gist.githubusercontent.com/bugra/5236ca2c69695d2afa37/raw/f8ad23c7678880729e745377cfc9e75201a6b05a/Examples%20from%20Module>`_.

Features
--------
#. No external dependencies
#. Consistent Api for different features of Angellist - NOTE: All requests will need to be authenticated with access token
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
#. Your personal access token needs to be approved for the jobs endpoint - i.e. added to the "approved list"
#. My token hasn't been approved for the job endpoint yet, thus I don't run those test in my jenkins build.  

Test
----
#. Create a `config.py` file under the `angel` directory.
#. Put your credentials in the following way.
#. Run the `test.py` under the `test` directory.
#. Make sure that all tests are green.

  CLIENT_ID =

  CLIENT_SECRET =

  ACCESS_TOKEN =

  MY_NAME =

  TWITTER_URL =

  ONLINE_BIO_URL =

  LINKEDIN_URL =

  GITHUB_URL =

  EMAIL =

  ANGELLIST_URL =

  ID =



