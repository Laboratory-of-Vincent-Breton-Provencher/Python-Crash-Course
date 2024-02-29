import numpy as np
import matplotlib.pyplot as plt

def generate_noisy_action_potential():
    """Function that generate an array containing one action per row. The
    position of the action potential (AP) is random and there is noise induced
    in the dataset.

    Returns:
        np.array: Array containing the noisy data of the action potential.
    """

    # Initialise the data array
    array_size = (500, 1000)
    data = np.ones(array_size)

    # Generate time and action potential in the time
    time = np.linspace(0, array_size[1], array_size[1])
    action_potential = 5 * np.exp(-0.08 * time)

    # Random position of the AP
    for i in range(data.shape[0]):
        data[i, :] *= np.roll(action_potential, np.random.randint(100, 900))

    # Add noise and np.nan in the data
    noisy_data = np.random.normal(data, 0.5)
    noisy_data.ravel()[np.random.choice(noisy_data.size, 200, replace=False)] = np.nan

    return noisy_data

ap = generate_noisy_action_potential()


fig, (ax1, ax2, ax3) = plt.subplots(ncols=3)

ax1.imshow(ap)

aligned_ap = np.zeros((ap.shape[0], 100))

for i in range(500):
    ap_row = ap[i,:]
    ap_max_pos = np.nanargmax(ap_row)
    aligned_ap[i,:] = ap_row[ap_max_pos-30: ap_max_pos+70]

ax2.imshow(aligned_ap)


mean_of_signal = np.nanmean(aligned_ap, axis=0)
std_of_signal = np.nanstd(aligned_ap, axis=0)

ax3.plot(mean_of_signal)
ax3.fill_between(np.arange(0, 100), mean_of_signal-std_of_signal, mean_of_signal + std_of_signal, alpha=0.2)
plt.tight_layout()
plt.show()
