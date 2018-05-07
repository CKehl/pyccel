# coding: utf-8

from sympy.core.expr import AtomicExpr
from sympy.core import Symbol
from sympy import sympify

from .core import Basic

class Macro(AtomicExpr):
    """."""
    _name = '__UNDEFINED__'

    def __new__(cls, argument):
        # TODO add verification

        argument = sympify(argument)
        return Basic.__new__(cls, argument)

    @property
    def argument(self):
        return self._args[0]

    @property
    def name(self):
        return self._name


class MacroSymbol(Symbol):
    """."""
    def __new__(cls, name, is_optional=False, default=None):

        return Basic.__new__(cls, name, is_optional, default)

    @property
    def name(self):
        return self._args[0]

    @property
    def is_optional(self):
        return self._args[1]

    @property
    def default(self):
        return self._args[2]

    def _sympystr(self, printer):
        sstr = printer.doprint
        default = ''
        if not(self.default is None):
            default = '| {}'.format(sstr(self.default))
        name = sstr(self.name)
        txt = '{name} {default}'.format(name=name, default=default)
        if self.is_optional:
            txt = 'optional({})'.format(txt.strip())
        return txt


class MacroShape(Macro):
    """."""
    _name = 'shape'

    def __new__(cls, argument, index=None):
        obj = Macro.__new__(cls, argument)
        obj._index = index
        return obj

    @property
    def index(self):
        return self._index

    def _sympystr(self, printer):
        sstr = printer.doprint
        if self.index is None:
            return 'MacroShape({})'.format(sstr(self.argument))
        else:
            return 'MacroShape({}, {})'.format(sstr(self.argument),
                                               sstr(self.index))



def construct_macro(name, argument, parameter=None):
    """."""
    # TODO add available macros: shape, len, dtype
    if not isinstance(name, str):
        raise TypeError('name must be of type str')

    argument = sympify(argument)
    if name == 'shape':
        return MacroShape(argument, index=parameter)
