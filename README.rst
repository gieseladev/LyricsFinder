LyricsFinder
============

LyricsFinder is a modular and easily expandable Python Package that is
used to extract lyrics from music and return them in a JSON-formatted
body, with abilities such as caching. By having the ability to use a
combination of a Google Custom Search Engine and a set of extractors for
several sources, lyrics are attained with much higher accuracy and
generally from the best desired source.

Requirements
~~~~~~~~~~~~

-  **Python 3.6+** with ``pip``

-  **[Strongly Recommended]:** A `Google Developer API Key`_ with the
   ‘Custom Search’ API enabled. This link should take one there once
   logged in.

*Note: While the Google tools aren’t technically required for this
project, much of the beneficial functionality depends on such
keys/search engines. However, direct searching/parsing from a supported
URL source is possible to incorporate with this package, though not the
recommended way to utilize it (unless one requires a specific
application requirement/design need).*

The following modules will be ***automatically*** downloaded and
installed as part of the standard setup:

.. code:: prolog

    beautifulsoup4
    requests

Installation
------------

    **Note that** ``sudo`` or ``sudo -H`` may be required to install
    depending on your system setup. If any permission errors occur,
    please use the sudo flags.

..

    **This package can easily be installed with one of ``pip`` or
    ``pip3`` as follows:**

.. code:: bash


    pip install lyricsfinder  # if pip matches Python 3.6+


    pip3 install lyricsfinder # if pip3 matches Python 3.6+

**Ensure your ``pip`` version matches that of Python.**

Many systems will allocate ``pip3`` to **Python 3.6+**, so ``pip3`` can
be used if your system has this installed. (``pip`` will, in this case,
be associated with **Python 2.7.x**)

    **Alternatively, you can install directly (ensure
    ``python3 --version`` is 3.6 or greater):**

.. code:: bash

    python3 -m pip install -U https://github.com/GieselaDev/LyricsFinder/archive/master.zip

..

    **From Source (slower/manual way):**

.. code:: bash

    $ git clone https://github.com/GieselaDev/LyricsFinder.git
    $ cd LyricsFinder
    $ python3 -m pip install .

..

    **Testing the package (optional):**

You may use ```pytest```_ to test the package.

Basic Usage
-----------

You can now import the package ``lyricsfinder`` as normal within your
project.

\```python import lyricsfinder

lyrics

.. _Google Developer API Key: https://console.developers.google.com/apis/library/customsearch.googleapis.com/?q=sear&id=8a9b6e90-7182-4ba2-a6f5-b7063dc57275
.. _``pytest``: https://docs.pytest.org/en/latest/
