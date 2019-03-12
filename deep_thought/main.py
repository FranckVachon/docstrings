"""
Module (.e.g monfichier.py) devrait contenir:
    * Un one-liner pour classe exportée (e.g. utilisable de l'extérieur)
    * Lister les exceptions lancées
"""

class SomeClass:
    """ Docstring pour une class devrait contenir:

        * résumer son comportement, lister ses méthodes publiques et variables d'instances.

        * Si la classe est destinée à être sous-classée (e.g. Class Animal sous-classée par Chient, Chat....) alors lister les interfaces pertinentes pour ces sous-classes.

    **Exemple: Docstring de la class SomeClass (ci-bas):**

    SomeClass n'a pas un comportement intéressant ni pertinent. On pourrait la sous-classer pour utiliser *SomeClass.some_complicated_method* mais celle-ci ne fait absolument rien non plus.

    """
    def __init__(self, a=None):
        """ 
        Constructeur:
            Assigne ``a = True``. Ne sert vraiment à rien. Lève un ``KeyError`` si on tente de remplacer la valeur par défaut `a=None`. Ne pas tenter de passer un argument à ce constructeur.
        """
        if a:
            raise KeyError

        a = True

    def some_complicated_method(self, arg1, kwarg2=None):
        """
        Docstring pour une méthode:
            * One-liner résumant ce que fait la méthode (e.g. pourquoi elle existe/est disponible publiquement).
            * Description des arguments (types, valeurs par défaut)
            * Description des valeurs retournées (type et ce que cela représente)

        `arg1` est de n'importe quel type. Ne sert absolument à rien.

        `kwarg2` optionel. N'importe quel type. Défaut: ``None``. Ne sert absolument à rien non plus.

        *return* un string ayant pour valeur ``some more stuff``
        """

        return "some more stuff"


class Subclass(SomeClass):
    """ Une sous-class qui étend SomeClass. Ne sert à rien non plus mais elle permet de retourner la valeur 42 si on en a besoin."""

    def __init__(self):
        """ Ne prend aucun argument et appel init. """
        super().__init__()

    def another_method(self, arg1=0):
        """ Une autre méthode inutile.

        `arg1` int (optionel). Peut importe sa valeur, le résultat de la méthode est le même. Il est donc vraiment, vraiment très optionel.
        `return` 42
        """

        return 42
