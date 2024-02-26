import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from time import sleep

# df = pd.read_csv("photodiode validation 50hz long test.txt")

with open("experiment see LED/experiment1.txt") as f:
    lines = f.readlines()

time = []
led0 = []
led1 = []
sensor_val = []
slave_ttl = []

for i in lines:
    data = i.split(",")
    time.append(int(data[0]))
    led0.append(int(data[1][0]))
    led1.append(int(data[1][1]))
    sensor_val.append(int(data[1][2:-2]))
    slave_ttl.append(int(data[1][-2]))

df = pd.DataFrame(data={"Time":np.asarray(time),
                     "LED0":np.asarray(led0),
                     "LED1":np.asarray(led1),
                     "Photodiode":np.asarray(sensor_val),
                     "Slave":np.asarray(slave_ttl)})

df["Time"] -= df["Time"][0]
df["Time"] /= 1e9


print(df.head())


df_led1, df_led0 = df.groupby(["LED0"])
df_led0 = df_led0[1]
df_led1 = df_led1[1]

df_led0.index = range(len(df_led0))
df_led1.index = range(len(df_led1))

photodiode_df = df_led0.merge(df_led1, how='left', left_index=True,
                              right_index=True)

fig, (ax0, ax1) = plt.subplots(2)
ax0.plot(photodiode_df["Time_y"], photodiode_df["Photodiode_y"] -
         photodiode_df["Photodiode_x"], color="green")
ax1.plot(df_led0["Time"], df_led0["Photodiode"], color="magenta")
ax1.plot(df_led1["Time"], df_led1["Photodiode"], color="blue")
plt.tight_layout()
plt.show()


# ############
# ### FREQ ###
# ############
plt.hist(np.diff(df["Time"]), bins=500, label="ALL")
plt.hist(np.diff(df_led0["Time"]), bins=500, label="LED0")
plt.hist(np.diff(df_led1["Time"]), bins=500, label="LED1")
plt.legend()
plt.show()


# ############
# ### Diff ###
# ############
plt.plot(df["Time"][:-1], np.diff(df["Time"]), label="ALL")
plt.plot(df_led0["Time"][:-1], np.diff(df_led0["Time"]), label="LED0")
plt.plot(df_led1["Time"][:-1], np.diff(df_led1["Time"]), label="LED1")
plt.legend()
plt.show()