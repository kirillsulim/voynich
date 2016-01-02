import unittest

from langtools.translate import Translator


class TranslatorTest(unittest.TestCase):

    def test_translate_equals(self):
        tr = Translator("abc", "def")
        self.assertEqual("deefd", tr.trans("abbca"))

    def test_translate_longer(self):
        tr = Translator("abc", "d")
        self.assertEqual("d???d", tr.trans("abbca"))

