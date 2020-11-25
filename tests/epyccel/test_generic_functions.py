 # pylint: disable=missing-function-docstring, missing-module-docstring/
import pytest
import numpy as np
import modules.generic_functions as mod
from pyccel.epyccel import epyccel

@pytest.fixture( params=[
        pytest.param("fortran", marks = [
            pytest.mark.fortran,
            pytest.mark.skip(reason="issue #512")]),
        pytest.param("c", marks = [
            pytest.mark.c]
        )
    ]
)
def language(request):
    return request.param
'''
def test_gen_1(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_gen_1()
    x = modnew.tst_gen_1()
    assert np.array_equal(x, x_expected)

def test_gen_2(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_gen_2()
    x = modnew.tst_gen_2()
    assert np.array_equal(x ,x_expected)

def test_gen_3(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_gen_3()
    x = modnew.tst_gen_3()
    assert np.array_equal(x, x_expected)

def test_gen_4(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_gen_4()
    x = modnew.tst_gen_4()
    assert np.array_equal(x, x_expected)

def test_gen_5(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_gen_5()
    x = modnew.tst_gen_5()
    assert np.array_equal(x, x_expected)

def test_gen_6(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_gen_6()
    x = modnew.tst_gen_6()
    assert np.array_equal(x, x_expected)

def test_gen_7(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_gen_7()
    x = modnew.tst_gen_7()
    assert np.array_equal(x, x_expected)

def test_multi_heads_1(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_multi_heads_1()
    x = modnew.tst_multi_heads_1()
    assert np.array_equal(x, x_expected)

def test_tmplt_1(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_tmplt_1()
    x = modnew.tst_tmplt_1()
    assert np.array_equal(x, x_expected)

def test_multi_tmplt_1(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_multi_tmplt_1()
    x = modnew.tst_multi_tmplt_1()
    assert np.array_equal(x, x_expected)

def test_tmplt_head_1(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_tmplt_head_1()
    x = modnew.tst_tmplt_head_1()
    assert np.array_equal(x, x_expected)

def test_local_overide_1(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_local_overide_1()
    x = modnew.tst_local_overide_1()
    assert np.array_equal(x, x_expected)

def test_tmplt_tmplt_1(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_tmplt_tmplt_1()
    x = modnew.tst_tmplt_tmplt_1()
    assert np.array_equal(x, x_expected)

def test_tmplt_2(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_tmplt_2()
    x = modnew.tst_tmplt_2()
    assert np.array_equal(x, x_expected)

def test_multi_tmplt_2(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_multi_tmplt_2()
    x = modnew.tst_multi_tmplt_2()
    assert np.array_equal(x, x_expected)

def test_default_var_1(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_default_var_1()
    x = modnew.tst_default_var_1()
    assert np.array_equal(x, x_expected)

def test_default_var_2(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_default_var_2()
    x = modnew.tst_default_var_2()
    assert np.array_equal(x, x_expected)

def test_default_var_3(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_default_var_3()
    x = modnew.tst_default_var_3()
    assert np.array_equal(x, x_expected)

def test_default_var_4(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_default_var_4()
    x = modnew.tst_default_var_4()
    assert np.array_equal(x, x_expected)

def test_optional_var_1(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_optional_var_1()
    x = modnew.tst_optional_var_1()
    assert np.array_equal(x, x_expected)

def test_optional_var_2(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_optional_var_2()
    x = modnew.tst_optional_var_2()
    assert np.array_equal(x, x_expected)

def test_optional_var_3(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_optional_var_3()
    x = modnew.tst_optional_var_3()
    assert np.array_equal(x, x_expected)

def test_optional_var_4(language):
    modnew = epyccel(mod, language = language)
    x_expected = mod.tst_optional_var_4()
    x = modnew.tst_optional_var_4()
    assert np.array_equal(x, x_expected)

def test_int_types(language):
    f1 = epyccel(mod.int_types , language = language, verbose=True)
    f2 = mod.int_types

    for i in range(400):
        assert f1(10, 5) == f2(10, 5)
        assert f1(np.int(15) , np.int(10)) == f2(np.int(15) , np.int(10))
        assert f1(np.int16(5), np.int16(4)) == f2(np.int16(5), np.int16(4))
        assert f1(np.int8(4), np.int8(7)) == f2(np.int8(4), np.int8(7))
        assert f1(np.int32(155), np.int32(177)) == f2(np.int32(155), np.int32(177))
        assert f1(np.int64(166), np.int64(255)) == f2(np.int64(166), np.int64(255))

def test_float_types(language):
    f1 = epyccel(mod.float_types , language = language, verbose=True)
    f2 = mod.float_types

    for i in range(400):
        assert f1(10.5, 5.5) == f2(10.5, 5.5)
        assert f1(np.float(15.5) , np.float(10.5)) == f2(np.float(15.5) , np.float(10.5))
        assert f1(np.float32(155.2), np.float32(177.1)) == f2(np.float32(155.2), np.float32(177.1))
        assert f1(np.float64(166.6), np.float64(255.6)) == f2(np.float64(166.6), np.float64(255.6))
'''
def test_complex_types(language):
    f1 = epyccel(mod.complex_types , language = language, verbose=True)
    f2 = mod.complex_types

    for i in range(1000):
        assert f1(complex(1, 2.2), complex(1, 2.2)) == f2(complex(1, 2.2), complex(1, 2.2))
        assert f1(np.complex(15.5, 2.0) , np.complex(10.5, 3.4)) == f2(np.complex(15.5, 2.0) , np.complex(10.5, 3.4))
        np.isclose(f1(np.complex64(15.5 + 2.0j) , np.complex64(10.5 + 3.4j)), f2(np.complex64(15.5 + 2.0j) , np.complex64(10.5 + 3.4j)), rtol = 1e-7, atol = 1e-8)


def test_mix_types_1(language):
    f1 = epyccel(mod.mix_types_1 , language = language, verbose=True)
    f2 = mod.mix_types_1

    for i in range(1000):
        assert f1(complex(1, 2), 15, np.int16(5)) == f2(complex(1, 2), 15, np.int16(5))
        assert f1(complex(1, 2), 15, True) == f2(complex(1, 2), 15, True)
        assert f1(complex(1, 2), 7.0, np.int16(5)) == f2(complex(1, 2), 7.0, np.int16(5))
        assert f1(complex(1, 2), 7.0, False) == f2(complex(1, 2), 7.0, False)
        assert f1(15, 14, np.int16(2012)) == f2(15, 14, np.int16(2012))
        assert f1(15, 14, True) == f2(15, 14, True)
        assert f1(15, 7.0, np.int16(2012)) == f2(15, 7.0, np.int16(2012))
        assert f1(15, 14, False) == f2(15, 14, False)


def test_mix_types_2(language):
    f1 = epyccel(mod.mix_types_2 , language = language, verbose=True)
    f2 = mod.mix_types_2

    for i in range(1000):
        assert f1(-1, -1) == f2(-1, -1)
        assert f1(np.int32(4), np.int32(16)) == f2(np.int32(4), np.int32(16))
        assert f1(np.int16(4), np.int16(4)) == f2(np.int16(4), np.int16(4))
        assert f1(5.7, -1.2) == f2(5.7, -1.2)
        assert f1(complex(7.2, 3.12), complex(7.2, 3.12)) == f2(complex(7.2, 3.12), complex(7.2, 3.12))
        assert f1(np.float32(16), np.float32(16)) == f2(np.float32(16), np.float32(16))