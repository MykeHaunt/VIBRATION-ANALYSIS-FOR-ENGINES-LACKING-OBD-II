import argparse
from src.core.engine_analysis import EngineDashboard
from src.interfaces.rpm_protocol import RPMTester

def main():
    parser = argparse.ArgumentParser(description='Engine Vibration Analysis CLI')
    parser.add_argument('--mode', choices=['dashboard', 'rpm_test'], required=True, help='Select mode of operation')
    parser.add_argument('--profile', type=str, help='Engine profile to use')
    args = parser.parse_args()
    
    if args.mode == 'dashboard':
        if not args.profile:
            parser.error("--profile is required for dashboard mode")
        dashboard = EngineDashboard()
        dashboard.app.run_server(debug=True)
    elif args.mode == 'rpm_test':
        tester = RPMTester()
        tester.execute_protocol()

if __name__ == '__main__':
    main()