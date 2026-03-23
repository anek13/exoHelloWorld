#!/bin/bash
#SBATCH --job-name=helloworld
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G
#SBATCH --time=00:05:00
#SBATCH --output=logs/%j.out

module load apptainer

# Create folders to prevent "not found" errors
mkdir -p logs data/final

# Provide the environment variable the Python script needs
export APPTAINERENV_OUTPUT_DIR="data/final"

# THE BYPASS: We use 'exec' instead of 'run' to avoid the broken %runscript.
# We point directly to the isolated Python inside the container's virtual environment!
apptainer exec \
  --bind .:/app \
  --pwd /app \
  --env PYTHONPATH="/app/src" \
  ./containers/env.sif \
  /opt/venv/bin/python scripts/say_hello.py
