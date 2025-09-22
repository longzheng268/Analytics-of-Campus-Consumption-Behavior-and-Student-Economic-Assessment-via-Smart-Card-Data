# Tests Directory

This directory contains test files for the Campus Consumption Analytics project.

## Test Files

- `test_basic.py`: Basic functionality tests including module imports and class instantiation

## Running Tests

```bash
# Install pytest if not already installed
pip install pytest

# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_basic.py -v

# Run tests with coverage (if pytest-cov is installed)
pytest tests/ --cov=core --cov=configs -v
```

## Test Coverage

The tests cover:
- ✅ Module imports
- ✅ Configuration validation  
- ✅ Class instantiation
- ✅ Method existence checks
- ✅ Required package availability