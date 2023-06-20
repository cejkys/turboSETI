import os
import glob
import sys

sys.path.insert(0, '/home/science/turbo_seti/turbo_seti/find_doppler')

import find_doppler

from turbo_seti.find_doppler.kernels import Kernels

kernels = Kernels(gpu_backend=False, precision=2)

file_path = "/home/science/turbo_seti/data/test.h5"
result_path = "/home/science/turbo_seti/results/"

if os.path.exists(os.path.join(file_path, "test.dat")):
    os.remove(os.path.join(result_path, "test.dat"))
    os.remove(os.path.join(result_path, "test.log"))

events = find_doppler.FindDoppler(file_path, max_drift=2.0, snr=10.0, out_dir=result_path, obs_info=None, n_coarse_chan=1, kernels=kernels)
events.search()
