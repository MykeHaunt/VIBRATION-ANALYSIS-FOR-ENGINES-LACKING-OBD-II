from src.core.safety_monitor import SafetyMonitor

def test_safety_monitor():
    monitor = SafetyMonitor()
    # Normal values should generate no alerts
    rms_values = {'x': 1.0, 'y': 1.0, 'z': 1.0}
    temp = 100
    pressure = 18
    alerts = monitor.check(rms_values, temp, pressure)
    assert len(alerts) == 0

    # Overlimit conditions should generate alerts
    rms_values = {'x': 2.0, 'y': 2.0, 'z': 2.0}
    temp = 115
    pressure = 10
    alerts = monitor.check(rms_values, temp, pressure)
    assert len(alerts) >= 3