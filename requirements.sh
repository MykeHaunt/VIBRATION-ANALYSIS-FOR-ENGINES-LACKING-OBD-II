# Install Homebrew if missing
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python and dependencies
brew install python@3.11
python -m venv venv
source venv/bin/activate
pip install numpy scipy pandas scikit-learn dash plotly pdfplumber python-socketio
