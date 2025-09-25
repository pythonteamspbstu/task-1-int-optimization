import sys
def test_integer_interning():
    interned_numbers = []
    a = -10000
    b = -9999
    for i in range(-10000, 10000):
        c = a + 1
        if (id(b) == id(c)):
            interned_numbers.append(b)
        b += 1
        a += 1

    print("M = ", min(interned_numbers))
    print("N = ", max(interned_numbers))

test_integer_interning()

