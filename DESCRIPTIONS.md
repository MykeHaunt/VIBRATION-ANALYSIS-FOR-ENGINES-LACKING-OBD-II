```markdown
# VIBRATION ANALYSIS FOR ENGINES LACKING OBD II 🔧📊

[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
```
**Professional-grade vibration diagnostics for pre-OBD II engines**  
Detect valve train anomalies, combustion irregularities, and mechanical wear using advanced signal processing and machine learning.

![Realtime Dashboard Preview](docs/assets/dashboard_preview.gif)

## 🌟 Key Features
- **Real-Time Dashboard**  
  Monitor RMS vibration levels, FFT spectra, and anomaly severity in real time.
- **Knock Type Detection**  
  Identify 4 distinct failure modes: knock, tap, ping, and detonation.
- **Component Failure Prediction**  
  Map vibration patterns to specific engine components (valves, pistons, timing chain).
- **RPM-Specific Protocols**  
  Guided testing sequences for accurate diagnosis at critical RPM ranges.
- **Safety Enforcement**  
  Automatic shutdown recommendations for over-vibration conditions.

## 🚀 Quick Start
### Prerequisites
- MacOS 12.3+ (Monterey or newer)
- Homebrew package manager
- Python 3.11+

### Installation
```bash
# Clone repository
git clone "https://github.com/yourusername/VIBRATION-ANALYSIS-FOR-ENGINES-LACKING-OBD-II.git"
cd "VIBRATION ANALYSIS FOR ENGINES LACKING OBD II"

# Set up environment
brew install python@3.11
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Launch Dashboard
```bash
python src/core/engine_analysis.py
```
Access the dashboard at: `http://localhost:8050`

## 🔍 Detailed Usage
### 1. Data Acquisition
Place vibration data (CSV/PDF) in `examples/sample_data/`. Format requirements:
```csv
timestamp,X_RMS,Y_RMS,Z_RMS,X_Accel,Y_Accel,Z_Accel
0.000,0.4614,1.0039,0.7738,2.0,1.0,1.0
```

### 2. RPM Testing Protocol 🎚️
Follow precise RPM holds for accurate diagnosis:
```bash
# Execute test sequence
python src/core/rpm_protocol.py --min-rpm 800 --max-rpm 4000

# Expected output
[PROTOCOL] Stage 1/3: Holding at 1500 RPM (valve train analysis)
[ANALYSIS] Detected valve clearance issues: 87% confidence
```

### 3. Interpretation Guide
| Parameter          | Normal Range   | Danger Threshold | Associated Components      |
|---------------------|----------------|-------------------|----------------------------|
| X-Axis RMS         | 0.2-0.8 m/s²   | >1.5 m/s²        | Timing chain, Camshaft     |
| Y-Axis Dominant Freq | 1-4 kHz        | >8 kHz           | Pistons, Connecting rods   |
| Z-Axis FFT Peak    | <0.15 g²/Hz    | >0.3 g²/Hz       | Valve train, Lifters       |

## 📚 Documentation
### Core Components
- **`/src/core/engine_analysis.py`**  
  Real-time visualization and data processing backbone.
- **`/src/models/knock_detector.py`**  
  Machine learning models for anomaly classification.
- **`/docs/TESTING_PROCEDURE.md`**  
  Step-by-step engine diagnosis protocol.

### Safety Systems ⚠️
```python
SAFETY_LIMITS = {
    'max_rms': 2.5,       # m/s²
    'max_temperature': 110, # °C
    'min_oil_pressure': 15 # psi
}
```
The system automatically triggers shutdown recommendations when thresholds are exceeded.

## 🛠️ Development
### Contribution Guidelines
1. Fork the repository
2. Create feature branch: `git checkout -b feature/new-detection-algorithm`
3. Submit pull request with detailed testing documentation

### Testing Framework
```bash
# Run validation suite
python -m pytest tests/ --verbose
```

## 📜 Legal & Compliance
By using this software, you agree to:
- [LIABILITY WAIVER](docs/LIABILITY.md)  
- [SAFETY PROTOCOLS](docs/ENGINE_SAFETY.md)  
- [GDPR COMPLIANCE](docs/COMPLIANCE.md)  

## 📊 Realtime Dashboard Features
1. **Vibration Intensity Matrix**  
   Color-coded 3D representation of XYZ axis vibrations.
2. **Frequency Heatmap**  
   Live FFT analysis with anomaly highlighting.
3. **Component Health Score**  
   AI-generated wear prediction for critical engine parts.
4. **Historical Trend Analysis**  
   Compare current readings to baseline profiles.

## ⚙️ Supported Engines
- Toyota 5A-FE (Primary Validation Platform)
- GM 2.2L Ecotec
- Ford Kent Crossflow
- Honda D-Series

## 📬 Contact
For commercial licensing and industrial applications:  
📧 diagnostics@vibrationanalysis.com  
☎️ +1 (800) 555-ENGINE

---

**Disclaimer**: This system supplements but does not replace professional mechanical inspection. Always verify predictions with physical teardown analysis.  

![Engine Schematic](docs/assets/engine_schematic.png)
``` 
