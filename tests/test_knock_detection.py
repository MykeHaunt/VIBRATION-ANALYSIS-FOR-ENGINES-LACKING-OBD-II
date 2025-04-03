import numpy as np
from src.models.knock_detector import KnockDetector

def test_knock_detection():
    detector = KnockDetector()
    frequencies = np.linspace(1000, 15000, 50)
    amplitudes = np.random.rand(50) * 0.05
    # Boost amplitudes in the 'knock' band (2000-8000 Hz)
    for i, freq in enumerate(frequencies):
        if 2000 <= freq <= 8000:
            amplitudes[i] += 0.2
    results = detector.detect(frequencies, amplitudes)
    assert 'knock' in results and results['knock']['severity'] > 0