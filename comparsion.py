from asammdf import MDF
import matplotlib.pyplot as plt
import os
import glob
from itertools import zip_longest
import numpy as np
import time
import sys

data_origin_path = r"./LOGS"
data_origin = r"./LOGS/HONDA_SRR6+___20240704___SW11FFF5_COT_001.mf4"
data_merged = r"./LOGS/merged_data/HONDA_SRR6+___20240704___SW11FFF5_COT_001_ORCAS.mf4"
mdf_origin = MDF(data_origin)
mdf_merged = MDF(data_merged)

chn_db = mdf_origin.channels_db
channels_origin = list(chn_db.keys())
chn_db = mdf_merged.channels_db
channels_merged = list(chn_db.keys())

if not channels_origin == channels_merged:
    exit("Channels are different, cannot compare.")

channels = channels_origin
del channels_origin, channels_merged, data_origin, mdf_origin
channels.remove("MF4Frame")             # Delet MF4Frame channel.
channels.remove("MF4Frame.DataBytes")   # Delet because of a MemoryError.

origin_file_list = glob.glob(os.path.join(data_origin_path, '*.mf4'))

signal_merged = mdf_merged.get(channels[19])
data_merged = signal_merged.samples
timestamps_merged = signal_merged.timestamps

timestamps_origin_length = 0
for data_file in origin_file_list:
    #print("Reading file " + data_file + " ...")
    mdf_origin = MDF(data_file)
    #print("Reading origin data for channel" + channel + "...")
    signal_origin = mdf_origin.get(channels[19])
    data_origin = signal_origin.samples
    timestamps_origin = signal_origin.timestamps

    timestamps_origin_length = timestamps_origin_length + timestamps_origin.size
    timestamps_merged_length = timestamps_merged.size
    print(f"{data_file} has {timestamps_origin.size} of timestmps.")
    #print(f"Last three timestamps of {data_file} are {timestamps_origin[-3]}, {timestamps_origin[-2]}, {timestamps_origin[-1]},")
    #print(f"while the coresponding timestamps in merged data are {timestamps_merged[timestamps_origin_length-2]}, {timestamps_merged[timestamps_origin_length-1]}, {timestamps_merged[timestamps_origin_length]}.")

print(f"Merged data has {timestamps_merged_length} timestamps,")
print(f"while original data has {timestamps_origin_length} timestamps in total.")

 
""" 
    i = 0                            # Log the posion in merged data
    for data, timestamp in zip_longest(data_origin, timestamps_origin, fillvalue = None):
        print('Timestamp: ', end="")
        print(timestamp, end="")
        print("...", end="")
        print("Origin is " + str(data) + ", merged is " + str(data_merged[i]) + "...", end="")
        if data == data_merged[i]:
            print("OK.")
        else:
            print("Not OK.")
            print("In channel " + channel + " #" + str(i))
            print("Oringally is " + str(data) + " but " + str(data_merged) + " after merging.")
            exit()
        i = i + 1
"""

#origin_file_list = glob.glob(os.path.join(data_origin_path, '*.mf4'))
#print(origin_file_list)

#for data_file in origin_file_list:
#    mdf_origin = MDF(data_file)

#for signal in signals:
#    signal_origin = mdf_origin.get(signal)
#    data = signal_origin.samples
#    print(type(data))


#signal_merged = mdf_merged.get(signals[1])
#data = signal.samples
#print(data[-1])
#timestamps = signal.timestamps