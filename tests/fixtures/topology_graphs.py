import pytest
import stk


@pytest.fixture(scope='session')
def ab_chain3():
    return stk.polymer.Linear('AB', 3)


@pytest.fixture(scope='function')
def tmp_ab_chain3():
    return stk.polymer.Linear('AB', 3)


@pytest.fixture(scope='session')
def ab_chain6():
    return stk.polymer.Linear('AB', 6)


@pytest.fixture(scope='session')
def honeycomb_lattice():
    return stk.cof.Honeycomb((3, 3, 1))
