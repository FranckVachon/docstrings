"""
More docstrings here
"""

class SomeClass:
    """ Class docstring. A one-line. No spaces before/after the docstring. Used by auto-indexing  """
    def __init__(self):
        """ 
        A constructore - adding details about my cstor here (__init__ is skipped by default)
        """
        a = True

    def some_complicated_method(self, arg1, kwarg2=None):
        """ This is a summary docstring - fits on one line and followed by blankspace

        *arg1* is some stuff

        *kwarg2* is optional and is other stuff (defaults to None)

        *return* some more stuff
        """

        return "some more stuff"


class Subclass(SomeClass):
    """ Class docstring. A one-line. No spaces before/after the docstring. Used by auto-indexing  """

    def __init__(self):
        """ A constructore """
        pass

    def another_method(self, arg1):
        """ This is a summary docstring - fits on one line and followed by blankspace

        :arg `arg1` is some int,
        :return 42
        """

        return 42
