Octohat
=======

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/glasnt/octohat
   :target: https://gitter.im/glasnt/octohat?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. image:: https://travis-ci.org/glasnt/octohat.svg?branch=master
    :target: https://travis-ci.org/glasnt/octohat
    
.. image:: https://badge.fury.io/py/octohat.svg
    :target: http://badge.fury.io/py/octohat
    
    
It's easy to see your direct `code contributions`_ on GitHub, but what about everything else?

**Octohat** takes a github repo name, and returns a list of every github user that has interacted with a project, but has not committed code. 

Interactions include: 

* raising or commenting on an issue
* raising or commenting on a pull request
* commenting on a commit

"Let's All Build a Hat Rack" (`#LABHR`_) is an original concept by `Leslie Hawthorn`_

WARNING
-------

`octohat in Python <https://github.com/glasnt/octohat>`__ and `octohat
in Ruby <https://github.com/glasnt/octohat-rb>`__ both create callable
``octohat`` entites. Strange things may occur if you try to install both
on your system.


Installation
------------
.. code-block:: 

    pip install octohat

Usage
-----
.. code-block:: 

    octohat [-h] [-g] [-l LIMIT] repo_name

    positional arguments:
      repo_name                githubuser/repo

    optional arguments:
      -g, --generate-html      Generate output as HTML
      -l LIMIT, --limit LIMIT  Limit to the last x Issues/Pull Requests


Define an environment variable for "GITHUB_TOKEN" to use an `authentication token`_ (allows for deeper searching)

Run this repo locally
---------------------

.. code-block::
    git clone https://github.com/glasnt/octohat
    cd octohat
    python3 octohat.py [arguments]


To do
-----
 
* parallel processing
* wiki contributions
* include merge-only contributors as non-code contributors


Code of Conduct
---------------

Octohat operates under a `Code of Conduct`_.


License
-------

Octohat is distributed under the `MIT license`_.

Octohub is Copyright (c) 2013 Alon Swartz (turnkeylinux), used inline under the GPLv3 license. 

.. _MIT license: https://github.com/glasnt/octohat/blob/master/LICENSE
.. _#LABHR: https://twitter.com/search?q=%23LABHR&src=typd
.. _Leslie Hawthorn: http://hawthornlandings.org/2015/02/13/a-place-to-hang-your-hat/
.. _code contributions: https://help.github.com/articles/why-are-my-contributions-not-showing-up-on-my-profile/
.. _authentication token: https://help.github.com/articles/creating-an-access-token-for-command-line-use/
.. _octohub: https://github.com/turnkeylinux/octohub
.. _source: http://stackoverflow.com/a/29202163/124019
.. _Code of Conduct: https://github.com/glasnt/octohat/blob/master/code-of-conduct.md
