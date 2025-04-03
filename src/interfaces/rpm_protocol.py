import time

class RPMTester:
    PROTOCOL_STAGES = {
        'warmup': {'rpm': (800, 1000), 'duration': 300},
        'low_range': {'rpm': (1500, 1600), 'duration': 120},
        'mid_range': {'rpm': (2500, 2600), 'duration': 60},
        'high_range': {'rpm': (3000, 3100), 'duration': 30}
    }

    def execute_protocol(self):
        for stage, params in self.PROTOCOL_STAGES.items():
            print(f"Starting {stage} test: Target RPM {params['rpm'][0]} - {params['rpm'][1]}")
            self._hold_rpm(params['rpm'], params['duration'])
            analysis = self._analyze_stage(params['rpm'])
            self._generate_report(stage, analysis)

    def _hold_rpm(self, target_range, duration):
        # Interface to control physical RPM systems; using a delay as a placeholder.
        print(f"Holding RPM in range {target_range} for {duration} seconds...")
        time.sleep(1)  # Placeholder for actual duration delay

    def _analyze_stage(self, target_range):
        # Placeholder for stage-specific analysis
        return {"status": "analysis complete", "rpm_range": target_range}

    def _generate_report(self, stage, analysis):
        print(f"Report for {stage}: {analysis}")