#!/usr/bin/env python3
import numpy as np
import random


def compute_inertia_matrix(nx3, mass=1):
    """
    Takes in an N x 3 array, as well as the objects mass.
    Returns a 3x3 numpy array that represents the inertia matrix using a fun formula
    """
    m_i = np.divide(mass, nx3.shape[0]) # I think this is the N value?
    print(m_i)
    x_i = np.sum(nx3[:, 0])
    y_i = np.sum(nx3[:, 1])
    z_i = np.sum(nx3[:, 2])
    inertia_boi = m_i ** [[y_i**2 + z_i**2, -x_i*y_i, -x_i*z_i],
                         [-x_i*y_i, x_i**2 + z_i**2, -y_i*z_i],
                         [-x_i*z_i, -y_i*z_i, x_i**2 + y_i**2]]  # Is this doing what I think it's doing?
    return inertia_boi


def sample_sphere_polar(N, r=1):
    """
    Generates a random nx3 array
    """
    polar_coords = []
    for _ in range(N):
        phi_val = np.random.uniform(0, np.pi)
        theta_val = np.random.uniform(0, 2*np.pi)
        x = r * np.sin(phi_val) * np.cos(theta_val)
        y = r * np.sin(phi_val) * np.sin(phi_val)
        z = r * np.cos(phi_val)
        polar_coords.append([x, y, z])
    final_coords = np.array(polar_coords)
    return final_coords






if __name__ == '__main__':
    # n3 = np.random.uniform(size =(4,3))
    # print(compute_inertia_matrix(n3))
    print(sample_sphere_polar(4))