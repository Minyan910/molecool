"""
Functions associated with the molecule.

"""


import numpy as np
from .measure import calculate_distance
      
def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    """
    Find the bonds in a molecule based on distance criteria.

    Parameters
    ----------
    coordinates : np.ndarray
        Molecular geometry
    max_bond, min_bond : float
        Maximum and minimum distance criteria

    Returns
    -------
    bonds : list

    Example
    -------
    >>> coordinates = np.array([[0.0, 0.0, 1.0],[1.0, 2.0, 3.0]])
    >>> build_bond_list(coordinates,max_bond=1,min_bond=0.1)
    1.0
    """

    if min_bond < 0.0:
        raise ValueError("The minimum distance should be equal to or larger than zero.")

    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds


