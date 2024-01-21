from project.customers.models import Customer
import unittest
import string

# ZASADY
# Name/City | Od 3 do 64 znaków, nie mogą być puste/ dozwolone cyfry, spacje i znaki specjalne: "-", ".", "/"
# Age | 1 do 3 znaków, tylko cyfry

DIGIT_CHARACTERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
CORRECT_CHARACTERS = list(string.ascii_letters) + DIGIT_CHARACTERS + ["-", ".", "/", " "]
INCORRECT_CHARACTERS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '<', '>', '?', ';', '\'', '\\', '\"', '|', '[', ']', '{', '}', '`', '~']

class CustomerCorrectData(unittest.TestCase):
    def test_correct_min_length(self):
        Customer('a'*3, 'a'*3, 1)
    def test_correct_max_length(self):
        Customer('a'*64, 'a'*64, 999)
    def test_correct_name_city_street_appNo_characters(self):
        for c in CORRECT_CHARACTERS:
            Customer(c*3, c*3, 123)
    def test_correct_pesel_age_characters(self):
        for d in DIGIT_CHARACTERS:
            Customer('a'*3, 'a'*3, d)

class CustomerIncorrectData(unittest.TestCase):
    def test_not_enough_char(self):
        with self.assertRaises(ValueError):
            Customer('a'*2, 'a'*2, None)
    def test_too_much_char(self):
        with self.assertRaises(ValueError):
            Customer('a'*65, 'a'*65, 1000)
    def test_incorrect_characters(self):
        with self.assertRaises(ValueError):
            for c in INCORRECT_CHARACTERS:
                Customer(c*3, c*3, c)
    def test_not_a_digit_in_pesel_age(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, 'a'*3, "abc")    

class CustomerExtremeValues(unittest.TestCase):
    def test_extreme_length_values(self):
        for p in range(2, 11):
            with self.assertRaises(ValueError):
                Customer('a'*10**p, 'a'*10**p, 10*10**p)

class CustomerJavascriptInjections(unittest.TestCase):
    def test_javascript_injection_name(self):
        with self.assertRaises(ValueError):
            Customer("<b <script>alert(1)</script>0", 'a'*3, 1)
    def test_javascript_injection_city(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, "<b <script>alert(1)</script>0", 1)
    def test_javascript_injection_age(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, 'a'*3, "<b <script>alert(1)</script>0")
    def test_javascript_injection_pesel(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, 'a'*3, 1)
    def test_javascript_injection_street(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, 'a'*3, 1)
    def test_javascript_injection_appNo(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, 'a'*3, 1)

class CustomerSQLInjections(unittest.TestCase):
    def test_sql_injection_name(self):
        with self.assertRaises(ValueError):
            Customer("abcd; DROP TABLE CUSTOMERS", 'a'*3, 1)
    def test_sql_injection_city(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, "abcd; DROP TABLE CUSTOMERS", 1)
    def test_sql_injection_age(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, 'a'*3, "24; DROP TABLE CUSTOMERS")
    def test_sql_injection_pesel(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, 'a'*3, 1)
    def test_sql_injection_street(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, 'a'*3, 1)
    def test_sql_injection_appNo(self):
        with self.assertRaises(ValueError):
            Customer('a'*3, 'a'*3, 1)

if __name__ == '__main__':
    unittest.main()