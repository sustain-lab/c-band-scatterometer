import numpy as np


def cross_section(C: float, I: np.ndarray, Q: np.ndarray, \
        d: float, A: float, ref: np.ndarray=None) -> np.ndarray:
    """
    Returns the normalized radar cross-section.
    
    Parameters
    ----------
    C : float
        Calibration constant
    I : float
        In-phase signal
    Q : float
        Quadrature signal
    d : float
        Range [m]
    A : float
        Illuminuated area [m^2]
    ref : np.ndarray
        Reference signal (optional).
        If present, normalize the result with it.
    
    Returns
    -------
    out : np.ndarray
        Array of cross-section
    """
    return C * signal_intensity(I, Q, ref) * d**4 / A


def signal_intensity(I: np.ndarray, Q: np.ndarray, ref: np.ndarray=None) \
                     -> np.ndarray:
    """
    Returns the sum of squares of the in-phase and quadrature signals.

    Parameters
    ----------
    I : np.ndarray
        In-phase signal
    Q : np.ndarray
        Quadrature signal
    ref : np.ndarray
        Reference signal (optional).
        If present, normalize the result with it.

    Returns
    -------
    res : np.ndarray
        Array of signal intensity
    """
    res = I**2 + Q**2
    return res if not ref else res / np.absolute(ref)
