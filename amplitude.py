import numpy as np
import matplotlib.pyplot as plt
from modules import write, get_quarter, C3


"""
Modulating a sine wave's amplitude using np.geomspace()
"""

# Synthesis settings
fs = 44100               # Sample rate (Hz)
duration = get_quarter(30)          # Short duration for a vocal stab (seconds)
f = C3                 # Sine wave frequency (Hz), about E4

# Time samples
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Basic sine wave
sine = np.sin(2 * np.pi * f * t)

# Geometric amplitude envelope (from 1 to near 0 over the sound's length)
amplitudes = np.geomspace(1.0, 0.01, num=sine.size)

# Apply the envelope
modulated = amplitudes * sine
write(modulated)

# Plot for visualization
plt.figure(figsize=(10, 4))
plt.plot(t, modulated, color = 'red')
plt.title('Geometrically Modulated Sine Wave (Synthetic "Ha" Envelope)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
# plt.locator_params(axis='x', nbins=5)
plt.show()
