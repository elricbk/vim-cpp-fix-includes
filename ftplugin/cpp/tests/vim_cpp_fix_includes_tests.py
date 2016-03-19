import unittest
import vim_cpp_fix_includes as sut


@unittest.skip("Don't forget to test!")
class VimCppFixIncludesTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.vim_cpp_fix_includes_example()
        self.assertEqual("Happy Hacking", result)
