#!/usr/bin/env python3
from gpiozero import OutputDevice
import subprocess
import time
def get_temperature():
    """
    Get the temperature of raspberry pi
    :return:
    """
    gather_output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
    current_temperature = gather_output.stdout.decode()
    try:
        return float(current_temperature.split('=')[1].split('\'')[0])
    except (IndexError, ValueError):
        raise RuntimeError('Could not parse temperature output.')

if __name__ == '__main__':
    temp = get_temperature()
    print(temp)