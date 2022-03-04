"""Class Monomial."""


class Monomial:
    """
    Implemntation of class Monomial.

    A monomial M(x) is a product of powers of the variable x
    having nonnegative integer exponents and a real coefficient.
    ---------------------------------------------------------
    This class represents a monomial and has the following:

    Attributes
    ----------
    * coefficient (read-only)
    * exponent (read-only)

    Methods
    -------
    * add
    * substract
    * multiply
    * divide
    * evaluate

    Notes
    -----
    1. To add or sustract two monomial, both must have equal
       exponents. The result is also a monomial.
    2. To multiply two monomials, there are no restrictions.
       The result is also a monomial.
    3. To divide two monomials, coefficient of divisor must
       be different than zero, and exponent of dividend must
       be equal or greater than the exponent of divisor. The
       result is also a monomial.
    """

    # ====================================================================
    # CONSTRUCTORS
    # ====================================================================

    # Default values correspond to  M(x) = 0
    def __init__(self, coefficient=0, exponent=0):

        # Exponent must be a nonnegative integer.
        if exponent >= 0:
            self.__coefficient = coefficient
            self.__exponent = exponent
        else:
            # Throws a runtime error.
            raise ValueError('Exponent must be a nonnegative integer.')

    # ====================================================================
    # PROPERTIES
    # ====================================================================

    @property
    def coefficient(self):
        """Coefficient of monominal (real value)."""
        return self.__coefficient

    @property
    def exponent(self):
        """Exponent of monominal (nonnegative integer value)."""
        return self.__exponent

    # ====================================================================
    # METHODS
    # ====================================================================

    def add(self, monomial):
        """Add another monomial to self."""
        result = None
        # To add monomials, both exponents must be equal.
        if self.__exponent == monomial.exponent:
            result = Monomial(self.__coefficient + monomial.coefficient,
                              self.__exponent)
        else:
            raise Exception('ADD: Invalid operation.')
        return result

    def subtract(self, monomial):
        """Subtract another monomial from self."""
        result = None
        # To subtract monomials, both exponents must be equal.
        if self.__exponent == monomial.exponent:
            result = Monomial(self.__coefficient - monomial.coefficient,
                              self.__exponent)
        else:
            raise Exception('SUBTRACT: Invalid operation.')
        return result

    def multiply(self, monomial):
        """Multipliy self with another monomial."""
        return Monomial(self.__coefficient*monomial.coefficient,
                        self.__exponent+monomial.exponent)

    def divide(self, divisor):
        """Divide self by another monomial."""
        result = None
        # To divide monomials, coefficient of divisor must be different
        # than zero and exponent of dividend must be equal or greater than
        # exponent of divisor.
        if (divisor.coefficient != 0 and self.__exponent >= divisor.exponent):
            result = Monomial(self.__coefficient / divisor.coefficient,
                              self.__exponent - divisor.exponent)
        else:
            raise Exception('DIVIDE: Invalid operation.')
        return result

    def evaluate(self, value):
        """Evaluate monomial with a real value."""
        return self.__coefficient * value ** self.__exponent

    def __str__(self):
        """Generate a string representation of monomial."""
        # String representation of sign is '+' or '-' depending
        # if coefficient is positive or negative.
        sign = '+ ' if self.__coefficient >= 0 else '- '

        # String representation of coefficient is the absolute
        # value of the coefficient.
        coefficient = str(abs(self.__coefficient))

        # If exponent is 0, power is equal to '1'
        # if exponent is 1, string representation of power is 'x'
        # if exponent is greater than 1, string representation of
        # power is 'x^' followed by exponent value.
        if self.__exponent == 0:
            power = ''
        elif self.__exponent == 1:
            power = ' x'
        else:
            power = ' x^' + str(self.__exponent)

        # SPECIAL CASE: Coefficient is 0, consequently the
        # monomial is zero.
        if self.__coefficient == 0:
            result = '+ 0'
        else:
            result = sign + coefficient + power
            # '1x' is commonly written as only 'x'.
            result = result.replace(' 1 x', ' x')

        return result
