"""
Shared pytest configuration for the automated test suite.

This file adds the project directory to Python's module search path,
allowing all test files to import project modules without modifying
individual test files.
"""

import sys
from pathlib import Path


# Absolute path to the project's source directory.
PROJECT_DIR = Path(__file__).resolve().parent.parent / "project"

# Add the project directory to Python's module search path.
sys.path.insert(0, str(PROJECT_DIR))