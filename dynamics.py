from audio import *

"""
This file is in charge of Dynamic Sine wave Generation (DSG)
as well as Scripted Sine wave Generation (SSG)

While running:
we're going to gradually construct a sine wave.
Adjusting the frequency along the way.
"""


def routine(initial_freq, end_freq, duration, dynamic = False):
    """Set up data to implement a slur effect"""
    #   The number of samples we'll use for the wave
    samples = int(44100 * duration)

    #   Generate time points across the duration; Store rate of change of t
    t = np.linspace(0, duration, samples, endpoint=False)
    dt = duration / samples

    #   Generate the wave with DSG or SSG
    if dynamic:
        return DSG(initial_freq, t, dt, samples)

    else:
        return SSG(initial_freq, end_freq, t, dt, samples)
    

def SSG(start_freq, end_freq, t, dt, samples):
    """Scripted Sine wave Generation:\n
    Construct the wave based on a start and end frequency.\n
    Generate a frequency array, calculate the phase, and return the final wave"""

    fp = np.linspace(start_freq, end_freq, samples)

    phase_increment = 2 * np.pi * fp * dt
    phase = np.cumsum(phase_increment)
    
    return np.sin(phase)


def DSG(initial_freq, t, dt, samples):
    """Dynamic Sine wave Generation:\n
    Dynamically construct the wave based on the value obtained from the pitch wheel."""

    """INCOMPLETE"""
    RUNNING = True
    value = 0

    while RUNNING:
        #   Adjust the value on the pitch wheel
        value -= 1

        #   Get the new frequency based on the pitch wheel
        f = initial_freq * 2 **(get_bend(value) / 12)

    return np.sin(f)


def get_bend(value, bend_range=12):
    """Return the bend value based on the pitch wheel's value,
    Following the Minimoog algorithm."""

    step = 16384 / (2 * bend_range)
    snapped = round((value - 8192) / step) * step + 8192

    bend = ((snapped - 8192) / 8192) * bend_range

    return bend