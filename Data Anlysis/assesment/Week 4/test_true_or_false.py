from unittest import TestCase
import Tests


class TestTrue_or_false(TestCase):
    def test_true_or_false(self):
        self.assertTrue(Tests.true_or_false(10,1),'incorect')
