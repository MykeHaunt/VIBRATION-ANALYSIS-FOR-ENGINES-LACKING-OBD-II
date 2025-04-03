import dash
from dash import html, dcc
from dash.dependencies import Output, Input
from src.models.knock_detector import KnockDetector
from src.core.safety_monitor import SafetyMonitor
from src.utils.fft_analyzer import FFTAnalyzer
from src.core.data_processor import DataProcessor

class EngineDashboard:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.knock_analyzer = KnockDetector()
        self.safety_monitor = SafetyMonitor()
        
        self.app.layout = self._create_layout()
        self._register_callbacks()
    
    def _create_layout(self):
        return html.Div([
            dcc.Interval(id='data-stream', interval=1000, n_intervals=0),
            html.Div(id='safety-alerts'),
            html.Div([
                dcc.Graph(id='rms-gauge'),
                dcc.Graph(id='fft-heatmap')
            ]),
            html.Div(id='component-health')
        ])
    
    def _register_callbacks(self):
        @self.app.callback(
            [Output('rms-gauge', 'figure'),
             Output('fft-heatmap', 'figure'),
             Output('component-health', 'children'),
             Output('safety-alerts', 'children')],
            [Input('data-stream', 'n_intervals')]
        )
        def update_dashboard(n):
            raw_data = DataProcessor.get_live_data()
            processed = FFTAnalyzer.process(raw_data)
            
            # Safety checks
            safety_status = self.safety_monitor.check(
                processed['rms'],
                processed['temperature'],
                processed['oil_pressure']
            )
            
            # Knock analysis
            knock_results = self.knock_analyzer.detect(
                processed['frequencies'],
                processed['amplitudes']
            )
            
            return (
                self._create_rms_gauge(processed['rms']),
                self._create_heatmap(processed['fft']),
                self._create_component_report(knock_results),
                self._create_safety_alerts(safety_status)
            )
    
    def _create_rms_gauge(self, rms):
        # Placeholder implementation for RMS gauge
        return {
            'data': [{'type': 'indicator', 'value': rms.get('x', 0)}],
            'layout': {'title': 'RMS Vibration Gauge'}
        }
    
    def _create_heatmap(self, fft_data):
        # Placeholder implementation for FFT heatmap
        return {
            'data': [{'z': fft_data}],
            'layout': {'title': 'FFT Heatmap'}
        }
    
    def _create_component_report(self, knock_results):
        # Generate a report of knock results
        report = []
        for k_type, details in knock_results.items():
            report.append(f"{k_type.upper()} detected with severity {details.get('severity', 'N/A')} at primary frequency {details.get('primary_freq', 'N/A')} Hz.")
        return html.Ul([html.Li(item) for item in report])
    
    def _create_safety_alerts(self, alerts):
        # Display safety alerts as a list
        return html.Div([html.P(alert) for alert in alerts])

if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser(description='Engine Vibration Analysis Dashboard')
    parser.add_argument('--profile', type=str, required=True, help='Engine profile to use')
    parser.add_argument('--protocol', type=str, choices=['full', 'partial'], default='full', help='RPM test protocol mode')
    args = parser.parse_args()
    
    dashboard = EngineDashboard()
    dashboard.app.run_server(debug=True)