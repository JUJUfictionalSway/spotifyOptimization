import soundfile as sf
import numpy as np

audio_path = "dataset/reference/sample.wav" #locate our audio recording

audio_data, sample_rate = sf.read(audio_path) #loading the audio

print("AUDIO INSPECTION") #audio inspection
print("----------------")

print("sample rate:", sample_rate, "Hz")
print("Audio shape:", audio_data.shape)
print("Data type:", audio_data.dtype)

total_samples = len(audio_data) #calculating the duration
duration = total_samples / sample_rate

print("Total samples:", total_samples)
print("Duration:", duration, "seconds")


print("\nFirst 10 samples:")
print(audio_data[:10])