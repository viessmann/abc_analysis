# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 10:52:59 2019

@author: ghlt@viessmann.com
"""

from pythena.abc_analysis import abc_analysis, abc_clean_data, abc_curve

import pandas as pd
import pytest

class TestABC(object):
    def test_abc_analysis(self):
        lstInput = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        dictOutput = abc_analysis(lstInput)
        assert dictOutput["Aind"] == [6, 7, 8]
    
    def test_wrong_input_type(self):
        with pytest.raises(TypeError):
            dfInput = pd.DataFrame([[1, 2, 3], [4, 5, 6]], 
                                   columns={"a", "b", "c"})
            abc_analysis(dfInput)
    
    def test_empty_input(self):
        with pytest.raises(ValueError):
            abc_analysis([])
    
    def test_too_short_input(self):
        with pytest.raises(ValueError):
            abc_analysis([1, 2])
    
    def test_abc_clean_data(self):
        psInput = pd.Series([1, 2, -1, 4, -2, 0])
        psOutput = abc_clean_data(psInput)
        psTest = pd.Series([1, 2, 0, 4, 0, 0])
        assert psOutput.equals(psTest)
    
    def test_strings_contained(self):
        with pytest.raises(ValueError):
            psInput = pd.Series([1, 2, -1, 4, 'foo', 'bar'])
            abc_clean_data(psInput)
    
    def test_abc_curve(self):
        psInput = pd.Series([1, 2, 3, 4, 5, 6])
        dictOutput = abc_curve(psInput)
        fltOutput = round(dictOutput["Curve"]["Yield"].sum(), 6)
        assert fltOutput == 64.784286