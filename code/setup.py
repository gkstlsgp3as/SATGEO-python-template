# -*- coding: utf-8 -*-
"""
@Time          : 2024/12/18 00:00
@Author        : Shinhye Han
@File          : setup.py
@Noice         : 
@Description   : Setup script for creating the environment and installing dependencies.

@Modificattion :
    @Author    :
    @Time      :
    @Detail    :
"""

import os
import subprocess
import sys


def run_command(command):
    """Run a shell command."""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error: Command failed with exit code {result.returncode}")
        sys.exit(result.returncode)


def create_conda_env(env_name="my_env", python_version="3.9"):
    """Create a conda environment."""
    run_command(f"conda create -n {env_name} python={python_version} gdal -y")


def activate_conda_env(env_name="my_env"):
    """Activate the conda environment."""
    if os.name == "nt":
        run_command(f"conda activate {env_name}")
    else:
        print(f"Run `conda activate {env_name}` manually if needed.")


def install_dependencies(requirements_file="requirements.txt", use_torch=False, use_tensorflow=False):
    """Install dependencies."""
    # Install dependencies from requirements.txt
    run_command(f"pip install -r {requirements_file}")

    # Install PyTorch if selected
    if use_torch:
        torch_command = (
            "pip install torch==1.12.1+cu113 torchvision==0.13.1+cu113 "
            "torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu113"
        )
        run_command(torch_command)

    # Install TensorFlow if selected
    if use_tensorflow:
        tensorflow_command = "pip install tensorflow-gpu==2.5.1"
        run_command(tensorflow_command)


def main():
    env_name = input("Enter the name of the conda environment (default: my_env): ") or "my_env"
    python_version = input("Enter the Python version (default: 3.9): ") or "3.9"

    print("\n=== Step 1: Create Conda Environment ===")
    create_conda_env(env_name, python_version)

    print("\n=== Step 2: Activate Conda Environment ===")
    activate_conda_env(env_name)

    print("\n=== Step 3: Install Dependencies ===")
    use_torch = input("Do you want to install PyTorch? (y/n, default: n): ").strip().lower() == "y"
    use_tensorflow = input("Do you want to install TensorFlow? (y/n, default: n): ").strip().lower() == "y"
    install_dependencies(use_torch=use_torch, use_tensorflow=use_tensorflow)

    print("\n=== Setup Completed ===")
    print(f"Activate your environment with `conda activate {env_name}` and start working!")


if __name__ == "__main__":
    main()
