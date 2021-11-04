import numpy as np


def normalized_radar_cross_section(
    calibration_constant: float,
    inphase_signal: np.ndarray,
    quadrature_signal: np.ndarray,
    distance: np.ndarray,
    area: float) -> np.ndarray:
    """Returns the normalized radar cross-section given input calibration
    constant, inphase and quadrature signals, distance from target, and the
    illuminated area."""
    return calibration_constant * (inphase_signal**2 + quadrature_signal**2) \
        * distance**4 / area
