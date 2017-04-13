from ..molecular.topologies.cage import *
from ..molecular import StructUnit3, StructUnit2, Cage
import os
from os.path import join

test_dir = 'cage_topology_tests'
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
data_dir = os.path.join(os.getcwd(), 'data', 'cage_topologies')

# 3 + 4 topology tests.
def test_SixPlusEight():
    bb1 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    bb2 = StructUnit3(join(data_dir, 'amine4.mol'))
    c = Cage([bb1, bb2], SixPlusEight())
    c.write(join(test_dir, 'SixPlusEight.pdb'))


# 2 + 4 topolgy tests.
def test_TwoPlusFour():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'amine4.mol'))
    c = Cage([bb1, bb2], TwoPlusFour())
    c.write(join(test_dir, 'TwoPlusFour.pdb'))


def test_ThreePlusSix():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'amine4.mol'))
    c = Cage([bb1, bb2], ThreePlusSix())
    c.write(join(test_dir, 'ThreePlusSix.pdb'))


def test_FourPlusEight():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'amine4.mol'))
    c = Cage([bb1, bb2], FourPlusEight())
    c.write(join(test_dir, 'FourPlusEight.pdb'))


def test_SixPlusTwelve():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'amine4.mol'))
    c = Cage([bb1, bb2], SixPlusTwelve())
    c.write(join(test_dir, 'SixPlusTwelve.pdb'))


def test_TenPlusTwenty():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'amine4.mol'))
    c = Cage([bb1, bb2], TenPlusTwenty())
    c.write(join(test_dir, 'TenPlusTwenty.pdb'))


# 3 + 3 cage topologies.
def test_OnePlusOne():
    bb1 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    bb2 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    c = Cage([bb1, bb2], OnePlusOne())
    c.write(join(test_dir, 'OnePlusOne.pdb'))


def test_TwoPlusTwo():
    bb1 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    bb2 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    c = Cage([bb1, bb2], TwoPlusTwo())
    c.write(join(test_dir, 'TwoPlusTwo.pdb'))


def test_FourPlusFour():
    bb1 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    bb2 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    c = Cage([bb1, bb2], FourPlusFour())
    c.write(join(test_dir, 'FourPlusFour.pdb'))


# 2 + 3 cage topologies.
def test_TwoPlusThree():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    c = Cage([bb1, bb2], TwoPlusThree())
    c.write(join(test_dir, 'TwoPlusThree.pdb'))


def test_FourPlusSix():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    c = Cage([bb1, bb2], FourPlusSix())
    c.write(join(test_dir, 'FourPlusSix.pdb'))


def test_FourPlusSix2():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    c = Cage([bb1, bb2], FourPlusSix2())
    c.write(join(test_dir, 'FourPlusSix2.pdb'))


def test_SixPlusNine():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    c = Cage([bb1, bb2], SixPlusNine())
    c.write(join(test_dir, 'SixPlusNine.pdb'))


def test_EightPlusTwelve():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    c = Cage([bb1, bb2], EightPlusTwelve())
    c.write(join(test_dir, 'EightPlusTwelve.pdb'))


def test_Dodecahedron():
    bb1 = StructUnit2(join(data_dir, 'amine2.mol'))
    bb2 = StructUnit3(join(data_dir, 'aldehyde3.mol'))
    c = Cage([bb1, bb2], Dodecahedron())
    c.write(join(test_dir, 'Dodecahedron.pdb'))