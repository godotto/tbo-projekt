from project.books.models import Book
import unittest



# correct inputs
correct_name_inputs = [
    "Transmetropolitan",
    "Invincible",
    "Asteroid i półkotapczan. O polskim wzornictwie powojennym",
    "Nineteen Eighty-Four",
    "Der Process"
]

correct_author_inputs = [
    "Warren Ellis",
    "Robert Kirkman",
    "Katarzyna Jasiołek",
    "George Orwell",
    "Franz Kafka"
]

correct_year_inputs = [
    1997,
    2003,
    2020,
    1949,
    1925
]

correct_book_type_inputs = [
    "2days",
    "5days",
    "10days"
]

correct_status_inputs = [
    "available"
]

# incorrect inputs
incorrect_name_author_inputs = [
    None,
    "",
    "\0",
    "\n",
    "\t",
    120
]

incorrect_year_inputs = [
    "1997",
    None,
    -50
]

incorrect_book_type_inputs = [
    "qwertyuiop",
    None,
    1
]

incorrect_status_inputs = [
    "qwertyuiop",
    1234,
    None
]

# XSS injection inputs
xss_injection_inputs = [
    '"-prompt(8)-"',
    "'-prompt(8)-'",
    '";a=prompt,a()//',
    "';a=prompt,a()//",
    "'-eval(\"window[\'pro\'%2B\'mpt\'](8)\")-'",
    '"-eval(\"window[\'pro\'%2B\'mpt\'](8)\")-"',
    '"onclick=prompt(8)>"@x.y',
    '"onclick=prompt(8)><svg/onload=prompt(8)>"@x.y',
    "<image/src/onerror=prompt(8)>",
    "<img/src/onerror=prompt(8)>",
    "<image src/onerror=prompt(8)>",
    "<img src/onerror=prompt(8)>",
    "<image src =q onerror=prompt(8)>",
    "<img src =q onerror=prompt(8)>"
]

# SQL injection inputs
sql_injection_inputs = [
    "' or \"",
    "-- or #", 
    "' OR '1",
    "' OR 1 -- -",
    '" OR "" = "',
    '" OR 1 = 1 -- -',
    "' OR '' = '",
    "'='",
    "'LIKE'",
    "'=0--+",
    " OR 1=1",
    "' OR 'x'='x",
    "' AND id IS NULL; --"
]

# extreme cases inputs
generate_extreme_string_inputs = lambda n: 'a' * n
extreme_string_inputs = [
    generate_extreme_string_inputs(10000),
    generate_extreme_string_inputs(100000),
    generate_extreme_string_inputs(1000000),
    generate_extreme_string_inputs(10000000)
]

extreme_year_inputs = [
    1999 ** 2,
    1999 ** 3,
    1999 ** 4,
    1999 ** 5,
    1999 ** 6,
]

class CorrectInputTests(unittest.TestCase):
    def test_names(self):
        try:
            for name in correct_name_inputs:
                Book(name, correct_author_inputs[0], correct_year_inputs[0], correct_book_type_inputs[0], correct_status_inputs[0])
        except Exception as err:
            self.fail(f"Correct data raised an exception {err=}, {type(err)=}")

    def test_authors(self):
        try:
            for author in correct_author_inputs:
                Book(correct_name_inputs[0], author, correct_year_inputs[0], correct_book_type_inputs[0], correct_status_inputs[0])
        except Exception as err:
            self.fail(f"Correct data raised an exception {err=}, {type(err)=}")

    def test_years(self):
        try:
            for year in correct_year_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], year, correct_book_type_inputs[0], correct_status_inputs[0])
        except Exception as err:
            self.fail(f"Correct data raised an exception {err=}, {type(err)=}")

    def test_book_types(self):
        try:
            for book_type in correct_book_type_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], correct_year_inputs[0], book_type, correct_status_inputs[0])
        except Exception as err:
            self.fail(f"Correct data raised an exception {err=}, {type(err)=}")

    def test_statuses(self):
        try:
            for status in correct_status_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], correct_year_inputs[0], correct_book_type_inputs[0], status)
        except Exception as err:
            self.fail(f"Correct data raised an exception {err=}, {type(err)=}")

class IncorrectInputTests(unittest.TestCase):
    def test_names(self):
        with self.assertRaises(TypeError):
            for name in incorrect_name_author_inputs:
                Book(name, correct_author_inputs[0], correct_year_inputs[0], correct_book_type_inputs[0], correct_status_inputs[0])

    def test_authors(self):
        with self.assertRaises(TypeError):
            for author in incorrect_name_author_inputs:
                Book(correct_name_inputs[0], author, correct_year_inputs[0], correct_book_type_inputs[0], correct_status_inputs[0])

    def test_years(self):
        with self.assertRaises(TypeError):
            for year in incorrect_year_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], year, correct_book_type_inputs[0], correct_status_inputs[0])

    def test_book_types(self):
        with self.assertRaises(TypeError):
            for book_type in incorrect_book_type_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], correct_year_inputs[0], book_type, correct_status_inputs[0])

    def test_statuses(self):
        with self.assertRaises(TypeError):
            for status in incorrect_status_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], correct_year_inputs[0], correct_book_type_inputs[0], status)

class XssInjectionTests(unittest.TestCase):
    def test_names(self):
        with self.assertRaises(TypeError):
            for name in xss_injection_inputs:
                Book(name, correct_author_inputs[0], correct_year_inputs[0], correct_book_type_inputs[0], correct_status_inputs[0])

    def test_authors(self):
        with self.assertRaises(TypeError):
            for author in xss_injection_inputs:
                Book(correct_name_inputs[0], author, correct_year_inputs[0], correct_book_type_inputs[0], correct_status_inputs[0])

    def test_years(self):
        with self.assertRaises(TypeError):
            for year in xss_injection_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], year, correct_book_type_inputs[0], correct_status_inputs[0])

    def test_book_types(self):
        with self.assertRaises(TypeError):
            for book_type in xss_injection_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], correct_year_inputs[0], book_type, correct_status_inputs[0])

    def test_statuses(self):
        with self.assertRaises(TypeError):
            for status in xss_injection_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], correct_year_inputs[0], correct_book_type_inputs[0], status)

class SqlInjectionTests(unittest.TestCase):
    def test_names(self):
        with self.assertRaises(TypeError):
            for name in sql_injection_inputs:
                Book(name, correct_author_inputs[0], correct_year_inputs[0], correct_book_type_inputs[0], correct_status_inputs[0])

    def test_authors(self):
        with self.assertRaises(TypeError):
            for author in sql_injection_inputs:
                Book(correct_name_inputs[0], author, correct_year_inputs[0], correct_book_type_inputs[0], correct_status_inputs[0])

    def test_years(self):
        with self.assertRaises(TypeError):
            for year in sql_injection_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], year, correct_book_type_inputs[0], correct_status_inputs[0])

    def test_book_types(self):
        with self.assertRaises(TypeError):
            for book_type in sql_injection_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], correct_year_inputs[0], book_type, correct_status_inputs[0])

    def test_statuses(self):
        with self.assertRaises(TypeError):
            for status in sql_injection_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], correct_year_inputs[0], correct_book_type_inputs[0], status)

class ExtremeCasesTests(unittest.TestCase):
    def test_names(self):
        with self.assertRaises(TypeError):
            for name in extreme_string_inputs:
                Book(name, correct_author_inputs[0], correct_year_inputs[0], correct_book_type_inputs[0], correct_status_inputs[0])

    def test_authors(self):
        with self.assertRaises(TypeError):
            for author in extreme_string_inputs:
                Book(correct_name_inputs[0], author, correct_year_inputs[0], correct_book_type_inputs[0], correct_status_inputs[0])

    def test_years(self):
        with self.assertRaises(TypeError):
            for year in extreme_year_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], year, correct_book_type_inputs[0], correct_status_inputs[0])

    def test_book_types(self):
        with self.assertRaises(TypeError):
            for book_type in extreme_string_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], correct_year_inputs[0], book_type, correct_status_inputs[0])

    def test_statuses(self):
        with self.assertRaises(TypeError):
            for status in extreme_string_inputs:
                Book(correct_name_inputs[0], correct_author_inputs[0], correct_year_inputs[0], correct_book_type_inputs[0], status)