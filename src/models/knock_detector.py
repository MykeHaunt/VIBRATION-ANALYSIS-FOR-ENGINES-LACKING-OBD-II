import numpy as np
from scipy.signal import find_peaks

class KnockDetector:
    def detect(self, frequencies, amplitudes):
        results = {}
        # Frequency bands for knock types
        bands = {
            'knock': (2000, 8000),
            'ping': (6000, 12000),
            'detonation': (8000, 15000),
            'tap': (1000, 4000)
        }
        
        frequencies = np.array(frequencies)
        amplitudes = np.array(amplitudes)
        
        for knock_type, (low, high) in bands.items():
            mask = (frequencies >= low) & (frequencies <= high)
            filtered_amplitudes = amplitudes[mask]
            filtered_frequencies = frequencies[mask]
            
            # Identify peaks above threshold amplitude
            peaks, properties = find_peaks(filtered_amplitudes, height=0.1)
            
            if len(peaks) > 3:
                results[knock_type] = {
                    'severity': self._calculate_severity(len(peaks)),
                    'primary_freq': float(filtered_frequencies[peaks[0]]),
                    'components': self._affected_components(knock_type)
                }
        return results

    def _calculate_severity(self, num_peaks):
        # Severity: 15 per peak, capped at 100
        return min(100, num_peaks * 15)
    
    def _affected_components(self, knock_type):
        mapping = {
            'knock': ['piston', 'connecting rod'],
            'ping': ['cylinder head'],
            'detonation': ['spark plug', 'valve'],
            'tap': ['bearing']
        }
        return mapping.get(knock_type, [])