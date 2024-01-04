from uneedtest import TestCase


class TestAll(TestCase):
    @classmethod
    def set_up_class(cls):
        cls.class_value = "class value"
        cls.add_class_cleanup(lambda _: _)

    def set_up(self):
        self.value = "instance value"

    def test_set_up(self):
        assert self.value == "instance value"

    def test_set_up_class(self):
        assert self.class_value == "class value"

    def test_do_class_cleanups(self):
        assert len(self._class_cleanups) == 1
        self.do_class_cleanups()
        assert len(self._class_cleanups) == 0

    def test_add_type_equality_func(self):
        class _SomeClass:
            pass

        def _compare(this, that, msg=None):
            return True

        self.add_type_equality_func(_SomeClass, _compare)

        some = _SomeClass()
        other = _SomeClass()
        self.assert_equal(some, other)

    def test_skip_test(self):
        self.skip_test("")
        raise Exception("We should not get here")

    def test_redirects_assertion_methods(self):
        # Just testing some methods, as they all are implemented as redirection
        self.assert_equal(1, 1)
        self.fail_if_equal(2, 1)
        with self.assert_raises(Exception):
            raise Exception()

    def test_legacy_methods_still_work(self):
        self.assertEqual(1, 1)
        self.failIfEqual(2, 1)
        with self.assertRaises(Exception):
            raise Exception()
