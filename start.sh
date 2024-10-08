#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Activate the virtual environment 'HyDE'
echo "Activating the HyDE virtual environment..."
source /workspace/.HyDE/bin/activate

# Start Jupyter Lab in /workspace/app directory without requiring token or password
echo "Starting Jupyter Lab..."
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token='' --NotebookApp.password='' --notebook-dir=/workspace/app