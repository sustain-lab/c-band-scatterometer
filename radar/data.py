import h5py
import numpy as np


def load(filename):
    f = h5py.File(filename)
    keys = [key for key in f['datasets'].keys()]
    nm = len(keys)
    im = 1024
    time = np.zeros((nm))
    ref = np.zeros((nm, im), dtype=np.csingle)
    hpol = np.zeros((nm, im), dtype=np.csingle)
    vpol = np.zeros((nm, im), dtype=np.csingle)
    for n, key in enumerate(keys):
        time[n] = f['datasets'][key]['time'][0]
        ref[n,:] = f['datasets'][key]['ref'][:]
        hpol[n,:] = f['datasets'][key]['hpol'][:]
        vpol[n,:] = f['datasets'][key]['vpol'][:]
    return time - time[0], ref, hpol, vpol
