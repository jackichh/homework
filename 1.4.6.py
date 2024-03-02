class Polynom:
    def __init__(self):
        self.__data = {}

    def _process_line(self, line):
        rec = line.split()
        try:
            assert len(rec) == 2, "Invalid line format"
            pwr = int(rec[0])
            try:
                assert pwr >= 0
            except AssertionError:
                print("Negative power", rec)
                return

            coef = float(rec[1])

            try:
                assert pwr not in self.__data
                self.__data[pwr] = coef
            except AssertionError:
                print("Power already has coefficient", rec)
                return

        except Exception as e:
            print(e.args, rec)
            return

    def read_form_file(self, file_name):
        self.__data = {}
        with open(file_name) as f:
            for line in f:
                self._process_line(line.strip())

    #
    def read_from_keyboard(self):
        self.__data = {}
        print("Input powers & coefficients, or empty line to stop")
        while True:
            s = input()
            if s == "":
                break
            self._process_line(s)

    #
    def show(self):
        print(self.__data)

    def evaluate_at_x(self, x):
        result = 0
        for pwr, cf in self.__data.items():
            result += x ** pwr * cf
        return result

    # 'getter' for coefficients
    def get_coefficient(self, pwr):
        return self.__data.get(pwr, 0.0)

    # setter for coefficients
    def set_coefficients(self, coefficients_dict):
        assert isinstance(coefficients_dict, dict)
        self.__data = coefficients_dict.copy()

    def get_powers(self):
        return self.__data.keys()

    @staticmethod
    def add(polynom1, polynom2):
        dict_of_coefficients = {}
        powers1 = polynom1.get_powers()
        powers2 = polynom2.get_powers()
        for power in set(powers1) | set(powers2):
            coefficient = polynom1.get_coefficient(power) + polynom2.get_coefficient(power)
            dict_of_coefficients[power] = coefficient
        res = Polynom()
        res.set_coefficients(dict_of_coefficients)
        return res

    @staticmethod
    def subtract(polynom1, polynom2):
        dict_of_coefficients = {}
        powers1 = polynom1.get_powers()
        powers2 = polynom2.get_powers()
        for power in set(powers1) | set(powers2):
            coefficient = polynom1.get_coefficient(power) - polynom2.get_coefficient(power)
            dict_of_coefficients[power] = coefficient
        res = Polynom()
        res.set_coefficients(dict_of_coefficients)
        return res

    @staticmethod
    def multiply(polynom1, polynom2):
        dict_of_coefficients = {}
        powers1 = polynom1.get_powers()
        powers2 = polynom2.get_powers()
        for power1 in set(powers1):
            for power2 in set(powers2):
                coefficient = polynom1.get_coefficient(power1) * polynom2.get_coefficient(power2)
                dict_of_coefficients[power1 + power2] = dict_of_coefficients.get(power1 + power2, 0) + coefficient
        res = Polynom()
        res.set_coefficients(dict_of_coefficients)
        return res


"""q(x) = P1(x) + P2(x) * P1(x) - P2(x)"""
"""h(x) = P2(x) * (P1(x) - P2(x))**2"""

P1 = Polynom()
P1.read_form_file('input01.txt')

P2 = Polynom()
P2.read_form_file('input02.txt')

q = Polynom.add(Polynom.subtract(P1, P2), Polynom.multiply(P1, P2))
h = Polynom.multiply(P2, Polynom.multiply(Polynom.subtract(P1, P2), Polynom.subtract(P1, P2)))

q.show()
h.show()

while True:
    x = input("Enter a real value: ")
    try:
        x = float(x)
        break
    except Exception as e:
        print(e.args)

with open('output.txt', 'w') as f:
    f.write(str(q.evaluate_at_x(x)) + '\n')
    f.write(str(h.evaluate_at_x(x)))