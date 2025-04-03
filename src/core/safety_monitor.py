class SafetyMonitor:
    def __init__(self):
        self.thresholds = self._load_thresholds()
    
    def _load_thresholds(self):
        # Thresholds can be later loaded from a config file if needed
        return {
            'rms': {'x': 1.5, 'y': 1.8, 'z': 2.0},
            'temperature': 110,  # Celsius
            'oil_pressure': 15   # psi
        }
    
    def check(self, rms_values, temp, pressure):
        alerts = []
        for axis, value in rms_values.items():
            if value > self.thresholds['rms'][axis]:
                alerts.append(f"⚠️ Vibration overlimit on axis {axis.upper()}! Immediate shutdown recommended.")
        if temp > self.thresholds['temperature']:
            alerts.append("🔥 Coolant temperature critical!")
        if pressure < self.thresholds['oil_pressure']:
            alerts.append("⛽ Low oil pressure detected!")
        return alerts