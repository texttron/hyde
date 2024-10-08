#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Set the location for the virtual environment
VENV_DIR="/workspace/.HyDE"

# Check if the virtual environment directory exists, if not, create it
if [ ! -d "$VENV_DIR" ]; then
  echo "Creating a virtual environment in /workspace/.HyDE..."
  python3 -m venv $VENV_DIR
else
  echo "Virtual environment '.HyDE' already exists in /workspace."
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source $VENV_DIR/bin/activate

# Install necessary packages from requirements.txt
if [ -f "/workspace/requirements.txt" ]; then
  echo "Installing packages from requirements.txt..."
  pip install -r /workspace/requirements.txt
else
  echo "requirements.txt file not found!"
  exit 1
fi

# Install Jupyter Notebook
echo "Installing Jupyter Notebook..."
pip install notebook

# Check if the contriever_msmarco_index directory exists
INDEX_DIR="/workspace/app/contriever_msmarco_index"
if [ ! -d "$INDEX_DIR" ]; then
  echo "contriever_msmarco_index directory not found. Downloading and extracting..."
  
  # Download contriever_msmarco_index.tar.gz into /workspace/app
  wget -P /workspace/app https://www.dropbox.com/s/dytqaqngaupp884/contriever_msmarco_index.tar.gz

  # Extract the tar.gz file into /workspace/app
  echo "Extracting contriever_msmarco_index.tar.gz..."
  tar -xvf /workspace/app/contriever_msmarco_index.tar.gz -C /workspace/app
else
  echo "contriever_msmarco_index directory already exists. Skipping download."
fi

echo "Setup complete! The '.HyDE' environment and the contriever_msmarco_index are ready."