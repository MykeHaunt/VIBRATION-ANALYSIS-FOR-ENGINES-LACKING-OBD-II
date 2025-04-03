from scipy.signal import find_peaks

class KnockAnalyzer:
    DETECTION_THRESHOLDS = {
        'knock': {'freq_range': (2000, 8000), 'min_amplitude': 0.15},
        'ping': {'freq_range': (6000, 12000), 'min_amplitude': 0.2},
        'detonation': {'freq_range': (8000, 15000), 'min_amplitude': 0.3},
        'tap': {'freq_range': (1000, 4000), 'min_amplitude': 0.1}
    }

    def analyze_peaks(self, frequencies, amplitudes):
        results = {}
        for knock_type, params in self.DETECTION_THRESHOLDS.items():
            mask = (frequencies >= params['freq_range'][0]) & \
                   (frequencies <= params['freq_range'][1])
            peaks, _ = find_peaks(amplitudes[mask], height=params['min_amplitude'])
            
            if len(peaks) > 3:  # Minimum peaks for confirmation
                results[knock_type] = {
                    'severity': len(peaks),
                    'primary_frequency': frequencies[mask][peaks[0]],
                    'affected_components': self.get_affected_components(knock_type)
                }
        return results

    def get_affected_components(self, knock_type):
        component_map = {
            'knock': ['Valves', 'Lifters', 'Pushrods'],
            'ping': ['Combustion Chamber', 'Spark Plugs'],
            'detonation': ['Pistons', 'Connecting Rods'],
            'tap': ['Timing Chain', 'Camshaft']
        }
        return component_map.get(knock_type, [])
