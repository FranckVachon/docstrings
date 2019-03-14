"""

.. _title:

==========================================================
This content from __init__.py (a package-level docu)
==========================================================
Pour un standalone package (e.g. utilisatble en command-line):
    Décrire la syntaxe d'usage & tout le nécessaire d'utilisation (librairies à installer si pertinent etc.)

    * python3 somePackage.py - -someFlag some_argument
    * Ou encore mieux voir optionlists_.

Pour un package interne (e.g. importable à l'intérieur du programme seulement):
    Résumer les responsabilités et particularité d'utilisation

Quelques examples de mise en page pour les intéressé(s)
--------------------------------------------------------

`See also <https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard>`_ for more stuff

Variable descriptions....
Note: single line return (like so) seem to be ignore. Put a full blank line between sections if you want them to actually show separately.

`my_vars` : float, optional

They suggest that `my_vars` should be enclosed in backticks (rendre les variables aisées à reconnaître dans le text)

This will be *italics* and this will be **bold** and ``this will be monospace whatever that means``

This will bring you on `StackOverflow <https://stackoverflow.com/>`_


Using definition
    This is pretty useful for long texts/classes/modules/methods. Term to define must be a one-liner. Then tab text below - all of the following paragraphs starting with the tabbed text will be "the definition"


.. _optionlists:

Option lists (see a 2nd subtitle)
----------------------------------
-f  must have at least 2 spaces between the -flag & the description for it to count as such.
--input  I think this look pretty doh.

Simple tables
-------------------------------
Explain logical stuff & summarize:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

Fancier tables
-----------------

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

Internal references
--------------------------
Internal crossreferences, like  how to do title_.


 """
