# coding: utf-8

from pyccel.complexity.operation import OpComplexity
from os.path import join, dirname

def test_1():
    filename = 'ex1.py'
    print ("==== " + filename + " ====")
    this_folder = dirname(__file__)
    inputs = join(this_folder, "inputs")
    filename = join(inputs, filename)
    complexity = OpComplexity(filename)
    print complexity.cost()

def test_2():
    filename = 'ex2.py'
    print ("==== " + filename + " ====")
    this_folder = dirname(__file__)
    inputs = join(this_folder, "inputs")
    filename = join(inputs, filename)
    complexity = OpComplexity(filename)
    print complexity.cost()

def test_3():
    filename = 'ex3.py'
    print ("==== " + filename + " ====")
    this_folder = dirname(__file__)
    inputs = join(this_folder, "inputs")
    filename = join(inputs, filename)
    complexity = OpComplexity(filename)
    print complexity.cost()

def test_4():
    filename = 'ex4.py'
    print ("==== " + filename + " ====")
    this_folder = dirname(__file__)
    inputs = join(this_folder, "inputs")
    filename = join(inputs, filename)
    complexity = OpComplexity(filename)
    print complexity.cost()

##############################################
if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
