


import numpy as np
from scipy.signal import resample


def downsample(data, current_sample_rate, target_sample_rate=12000, multiCh=True):

    def downsample_data(data, current_rate, target_rate):
        num_samples = int(len(data) * target_rate / current_rate)
        return resample(data, num_samples)

    if not multiCh:
        downsampled_data = downsample_data(data, current_sample_rate, target_sample_rate)
    else:
        downsampled_data = np.zeros((data.shape[0], int(data.shape[1] * target_sample_rate / current_sample_rate)))
        for i in range(data.shape[0]):
            downsampled_data[i, :] = downsample_data(data[i, :], current_sample_rate, target_sample_rate)

    return downsampled_data


