"""
Defines cages made from building blocks with 3 functional groups.

"""

import numpy as np

from .base import CageTopology,  _CageVertex
from ..topology_graph import Edge


class OnePlusOne(CageTopology):
    """
    Represents a capsule cage topology graph.

    See :class:`.CageTopology` for more details and examples.

    .. image::

    Attributes
    ----------
    vertices : :class:`tuple` of :class:`.Vertex`
        The vertices which make up the topology graph.

    edges : :class:`tuple` of :class:`.Edge`
        The edges which make up the topology graph.

    """

    _x = 1
    vertices = (
        _CageVertex(_x, 0., 0.),
        _CageVertex(-_x, 0., 0.),

    )
    edges = (
        Edge(vertices[0], vertices[1], position=np.array([0, 1, 0])),
        Edge(vertices[0], vertices[1], position=np.array([0, -1, 1])),
        Edge(vertices[0], vertices[1], position=np.array([0, -1, -1]))
    )

    num_windows = 3
    num_window_types = 1


class TwoPlusTwo(CageTopology):
    """
    Represents a tetrahedron cage topology graph.

    See :class:`.CageTopology` for more details and examples.

    .. image::

    Attributes
    ----------
    vertices : :class:`tuple` of :class:`.Vertex`
        The vertices which make up the topology graph.

    edges : :class:`tuple` of :class:`.Edge`
        The edges which make up the topology graph.

    """

    _x = 1
    vertices = (
        _CageVertex(_x, 0, -_x/np.sqrt(2)),
        _CageVertex(-_x, 0, -_x/np.sqrt(2)),
        _CageVertex(0, _x, _x/np.sqrt(2)),
        _CageVertex(0, -_x, _x/np.sqrt(2))
    )

    edges = (
        Edge(vertices[0], vertices[1]),
        Edge(vertices[0], vertices[2]),
        Edge(vertices[0], vertices[3]),

        Edge(vertices[1], vertices[2]),
        Edge(vertices[1], vertices[3]),

        Edge(vertices[2], vertices[3])
    )

    num_windows = 4
    num_window_types = 1


class FourPlusFour(CageTopology):
    """
    Represents a cube cage topology graph.

    See :class:`.CageTopology` for more details and examples.

    .. image::

    Attributes
    ----------
    vertices : :class:`tuple` of :class:`.Vertex`
        The vertices which make up the topology graph.

    edges : :class:`tuple` of :class:`.Edge`
        The edges which make up the topology graph.

    """

    _x = 1
    vertices = (
        _CageVertex(-_x, _x, -_x),
        _CageVertex(-_x, -_x, -_x),
        _CageVertex(_x, _x, -_x),
        _CageVertex(_x, -_x, -_x),

        _CageVertex(-_x, _x, _x),
        _CageVertex(-_x, -_x, _x),
        _CageVertex(_x, _x, _x),
        _CageVertex(_x, -_x, _x)
    )

    edges = (
        Edge(vertices[0], vertices[1]),
        Edge(vertices[0], vertices[2]),
        Edge(vertices[0], vertices[4]),
        Edge(vertices[1], vertices[3]),
        Edge(vertices[1], vertices[5]),
        Edge(vertices[2], vertices[6]),
        Edge(vertices[2], vertices[3]),
        Edge(vertices[3], vertices[7]),
        Edge(vertices[4], vertices[6]),
        Edge(vertices[4], vertices[5]),
        Edge(vertices[5], vertices[7]),
        Edge(vertices[6], vertices[7])
    )

    num_windows = 6
    num_window_types = 1
