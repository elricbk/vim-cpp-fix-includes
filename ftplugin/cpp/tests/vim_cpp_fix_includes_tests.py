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
        
class ExtractCppIdentifierTests(unittest.TestCase):
    def test_given_single_word_idetifier_extracts_it(self):
        self.assertEqual(
            sut.extract_cpp_identifier('test', 0),
            'test'
        )

    def test_given_identifier_with_underscore_extracts_it(self):
        self.assertEqual(
            sut.extract_cpp_identifier('starts_with(s1, s2);', 0),
            'starts_with'
        )

    def test_given_identifier_with_namespace_extracts_it(self):
        self.assertEqual(
            sut.extract_cpp_identifier('std::string test;', 4),
            'std::string'
        )

    def test_given_space_at_cursor_returns_none(self):
        self.assertIsNone(
            sut.extract_cpp_identifier('s1 test;', 2)
        )

    def test_given_column_less_than_zero_returns_none(self):
        self.assertIsNone(
            sut.extract_cpp_identifier('test', -1)
        )

    def test_given_too_big_column_returns_none(self):
        self.assertIsNone(
            sut.extract_cpp_identifier('test', 4)
        )
