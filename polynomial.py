"""Class Polynomial."""

from monomial import Monomial


class Polynomial:
    """
    Implementation of class Polynomial.

    A polynomial P(x) is a sum of monomials of the variable x.
    ----------------------------------------------------------
    self.__class represents a polynomial and has the following:

    Attributes
    ----------
    * coefficients (read-only)
    * exponents (read-only)
    * degree (read-only)

    Methods
    -------
    * append
    * add
    * substract
    * multiply
    * evaluate

    Notes
    -----
    1. self.__class keeps a simplified collection of monomials,
       sorted from largest to smallest degree.
    2. It has alwyas at least one monomial, even when its value
       is zero.
    """

    # ====================================================================
    # CONSTRUCTORS
    # ====================================================================

    def __init__(self):
        # Creates a new empty list
        self.__terms = []
        # Add the monomial equal to zero
        self.__terms.append(Monomial())

    # ====================================================================
    # PROPERTIES
    # ====================================================================

    @property
    def coefficients(self):
        """Coefficients of polynomial (list of real values)."""
        # Traverse the list of monomials extracting
        # their coefficients.
        return [monomial.coefficient for monomial in self.__terms]

    @property
    def exponents(self):
        """Exponents of polynomial (list of nonnegative integer values)"."""
        # Traverse the list of monomials extracting
        # their exponents.
        return [monomial.exponent for monomial in self.__terms]

    @property
    def degree(self):
        """Degree of polynomial (nonnegative integer value)."""
        # It is assumed that list of terms is sorted from
        # largest to smallest, so the monomial with largest
        # degree is the first one.
        return self.__terms[0].exponent

    # ====================================================================
    # METHODS
    # ====================================================================

    def append(self, monomial):
        """Append a monomial."""
        # This method assures that the list of terms is
        # always simplified (cannot exist multiple terms
        # with same degree) and sorted from largest to
        # smaller degree.

        # The monomial to add must be different than zero.
        if monomial.coefficient != 0:
            # If the actual polynomial is zero, internal list
            # only contains one monomial and this monomial will
            # be replaced with the one received.
            if len(self.__terms) == 1 and self.__terms[0].coefficient == 0:
                self.__terms[0] = monomial
            else:
                appended = False
                i = 0
                while not appended and i < len(self.__terms):
                    # If the exponent of the monomial to append is greater
                    # than the exponent of the monomial [i] analyzed, it
                    # means that monomial to append does not exists in the
                    # polynomial, so it is inserted in the currente position
                    # to maintain the order of the list.
                    if monomial.exponent > self.__terms[i].exponent:
                        self.__terms.insert(i, monomial)
                        appended = True
                    # If the exponent of the monomial to append is equal to
                    # the exponent of the monomial [i] analyzed, perform
                    # addition between monomials and replaces the current
                    # monomial in the case the sum of the monomials is zero,
                    # removes the current monomial from the list.
                    elif monomial.exponent == self.__terms[i].exponent:
                        if self.__terms[i].coefficient + monomial.coefficient != 0:
                            self.__terms[i] = self.__terms[i].add(monomial)
                        else:
                            self.__terms.pop(i)
                            appended = True
                    # Go to the next monomial in the internal list.
                    else:
                        i += 1
                # If monomial has not been appended at self.__point, append it
                # at the end of the list.
                if not appended:
                    self.__terms.append(monomial)
                # If the list becomes empty, it means that the polynomial is
                # zero, so append a monomial equal to zero.
                if len(self.__terms) == 0:
                    self.__terms.append(Monomial())
                # If the list has only one monomial and its coefficient is
                # zero, it means the that polynomial is zero, so replace
                # with a monomial equal to zero (self.__is only for consistency
                # of monomial representation).
                elif len(self.__terms) == 1 and self.__terms[0].coefficient == 0:
                    self.__terms[0] = Monomial()

    def add(self, polynomial):
        """Add another polynomial to self."""
        result = Polynomial()
        # Traverse to add the terms of self.__polynomial
        for monomial in self.__terms:
            result.append(Monomial(monomial.coefficient, monomial.exponent))
        # Traverse to add the terms of received polyomial
        for monomial in polynomial.__terms:  # pylint: disable=W0212
            result.append(Monomial(monomial.coefficient, monomial.exponent))
        return result

    def subtract(self, polynomial):
        """Subtract another monomial from self."""
        result = Polynomial()
        # Traverse to add the terms of self.__polynomial
        for monomial in self.__terms:
            result.append(Monomial(monomial.coefficient, monomial.exponent))
        # Traverse to add the inverse terms of received polyomial
        for monomial in polynomial.__terms:  # pylint: disable=W0212
            result.append(Monomial(-monomial.coefficient, monomial.exponent))
        return result

    def multiply(self, polynomial):
        """Multipliy self with another monomial."""
        result = Polynomial()
        # Traverse the terms of self.__polynomial
        for m1 in self.__terms:
            # Traverse to terms of received polyomial
            for m2 in polynomial.__terms:  # pylint: disable=W0212
                # Multiply each pair of monomials and
                # add to product
                result.append(m1.multiply(m2))
        return result

    def evaluate(self, value):
        """Evaluate plynomial with a real value."""
        result = 0
        # To evaluate the polynomial, sum all values of
        # its internal monomials.
        for monomial in self.__terms:
            result += monomial.evaluate(value)
        return result

    def __str__(self):
        """Generate a string representation of polynomial."""
        result = ''
        # To convert the polynomial to string, concatenate
        # all string representations of its internal monomials.
        for monomial in self.__terms:
            result += (" " + str(monomial))
        return result.strip()
