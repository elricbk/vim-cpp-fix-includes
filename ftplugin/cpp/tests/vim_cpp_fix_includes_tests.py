import unittest
import vim_cpp_fix_includes as sut

class FindIncludeRangeTest(unittest.TestCase):
    def test_for_basic_case_returns_expected_result(self):
        buf = ['#include <string>']

        start, end = sut.find_include_range(buf)

        self.assertEqual(start, 0)
        self.assertEqual(end, 1)

    def test_for_includes_not_from_first_line_returns_expected_result(self):
        buf = ['', '#include <string>', '#include <vector>']

        start, end = sut.find_include_range(buf)

        self.assertEqual(start, 1)
        self.assertEqual(end, 3)

    def test_given_trailing_empty_lines_doesnt_treat_them_as_includes(self):
        buf = ['', '#include <string>', '', '']

        start, end = sut.find_include_range(buf)

        self.assertEqual(start, 1)
        self.assertEqual(end, 2)

    def test_given_empty_lines_between_directives_includes_them_in_result(self):
        buf = ['', '#include <string>', '', '#include <vector>']

        start, end = sut.find_include_range(buf)

        self.assertEqual(start, 1)
        self.assertEqual(end, 4)

    def test_given_no_includes_in_file_returns_none(self):
        buf = ['', '<string>', '', '<vector>']

        start, end = sut.find_include_range(buf)

        self.assertIsNone(start)
        self.assertIsNone(end)
