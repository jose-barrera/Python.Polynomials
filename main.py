from monomial import Monomial
from polynomial import Polynomial

print('This program defines some polynomials and performs')
print('operations between them.')
print()

polynomials = []
# + 5 x^11 + 25 x^8 - 17 x^5
polynomials.append(Polynomial())
polynomials[0].append(Monomial(5, 11))
polynomials[0].append(Monomial(25, 8))
polynomials[0].append(Monomial(-17, 5))
# + 2 x^4 - x^3 + 5 x - 5
polynomials.append(Polynomial())
polynomials[1].append(Monomial(2, 4))
polynomials[1].append(Monomial(-1, 3))
polynomials[1].append(Monomial(5, 1))
polynomials[1].append(Monomial(-5, 0))
# + 15 x^11
polynomials.append(Polynomial())
polynomials[2].append(Monomial(15, 11))
# + 1
polynomials.append(Polynomial())
polynomials[3].append(Monomial(1, 0))

print('POLYNOMIALS AND THEIR PROPERTIES')
print()
for i in range(len(polynomials)):
    print('P' + str(i+1) + '(x) = ' + str(polynomials[i]))
    print('* Coefficients: ' + str(polynomials[i].coefficients))
    print('* Exponents: ' + str(polynomials[i].exponents))
    print('* Degree: ' + str(polynomials[i].degree))
    print()

print('EVALUATION OF POLYNOMIALS')
print()
values = [-2.4, -1.7, 0, 1, 3, 7.7]
for value in values:
    print('P1(' + str(value) + ') = ' + str(polynomials[0].evaluate(value)))
    print('P2(' + str(value) + ') = ' + str(polynomials[1].evaluate(value)))
    print('P3(' + str(value) + ') = ' + str(polynomials[2].evaluate(value)))
    print('P4(' + str(value) + ') = ' + str(polynomials[3].evaluate(value)))
    print()

print('OPERATION BETWEEN POLYNOMIALS')
print()
for i in range(len(polynomials)):
    for j in range(i+1, len(polynomials)):
        print('P' + str(i+1) + '(x) and P' + str(j+1) + '(x)')
        print('* SUM: ' + str(polynomials[i].add(polynomials[j])))
        print('* DIFFERENCE: ' + str(polynomials[i].subtract(polynomials[j])))
        print('* PRODUCT: ' + str(polynomials[i].multiply(polynomials[j])))
        print()

print()
print('THANK YOU FOR USING THIS PROGRAM!')
