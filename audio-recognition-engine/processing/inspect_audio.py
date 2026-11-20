import matplotlib
import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt

print("matplotlib backend:", matplotlib.get_backend())


audio_path = "../dataset/reference/sample.wav" # locate our audio recording

audio_data, sample_rate = sf.read(audio_path, always_2d=True) # loading the audio

print("AUDIO INSPECTION") # audio inspection
print("----------------")

print("sample rate:", sample_rate, "Hz")
print("Audio shape:", audio_data.shape)
print("Data type:", audio_data.dtype)

total_samples = len(audio_data) # calculating the duration
duration = total_samples / sample_rate

print("Total samples:", total_samples)
print("Duration:", duration, "seconds")


print("\nFirst 10 samples:")
print(audio_data[:10])


print("\nSIGNAL ANALYSIS")
print("----------------")

channel_peaks = np.max(np.abs(audio_data), axis=0) #peak amplitude for each channel

# print("left channel peak:", channel_peaks[0])
# print("right channel peak:", channel_peaks[1])

rms = np.sqrt(np.mean(audio_data**2, axis=0)) #RMS amplitude for each channel
for channel in range(audio_data.shape[1]):
    print(f"Channel {channel + 1} peak:",
          channel_peaks[channel])

    print(f"Channel {channel + 1} RMS:",
          rms[channel])
nonzero_frames = np.flatnonzero(np.any(audio_data != 0, axis=1)) #finding first fraim containing a nonzero value
if len(nonzero_frames) > 0:
    print("first nonzero frame:", nonzero_frames[0])
    print("time of first nonzero frame:",
          nonzero_frames[0] / sample_rate, "seconds")
else:
    print("Audio contains only zero-valued samples.")


time = np.arange(len(audio_data)) / sample_rate # time axis 

plt.figure(figsize=(14,6))

for channel in range(audio_data.shape[1]):
    plt.plot(time, audio_data[:, channel],
             label=f"channel{channel + 1}")

plt.title("audio waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()