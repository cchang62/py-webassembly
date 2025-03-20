# Building a Wheel in `_wheel_poetry`

This document outlines the steps to build a Python wheel in the `_wheel_poetry` folder using Poetry.

## Prerequisites

1. Ensure you have Python installed (preferably version 3.7 or higher).
2. Install Poetry by following the instructions at [Poetry's official website](https://python-poetry.org/docs/#installation).
3. Verify that you have all necessary dependencies installed for your project.

## Steps to Build the Wheel

1. **Navigate to the `_wheel_poetry` folder**:

   ```bash
   cd /Users/Jibamy/wasm/py.js/pyodide/_wheel_poetry
   ```

2. **Install dependencies**:
   Run the following command to install the dependencies specified in `pyproject.toml`:

   ```bash
   poetry install
   ```

3. **Build the wheel**:
   Use Poetry to build the wheel:

   ```bash
   poetry build
   ```

   This will generate a `.whl` file in the `dist/` directory.

4. **Verify the wheel**:
   Check the contents of the `dist/` directory to ensure the wheel was created successfully:

   ```bash
   ls dist/
   ```

## Notes

- If you encounter any issues during the build process, ensure that your `pyproject.toml` and `poetry.lock` files are correctly configured.
- For more information on Poetry commands, refer to the [Poetry CLI documentation](https://python-poetry.org/docs/cli/).

## Cleaning Up

To clean up the environment or remove build artifacts, you can use the following commands:

- Remove the virtual environment created by Poetry:

  ```bash
  poetry env remove python
  ```

- Delete the `dist/` directory:

  ```bash
  rm -rf dist/
  ```

## Additional Resources

- [Poetry Documentation](https://python-poetry.org/docs/)
- [PEP 517 and PEP 518](https://www.python.org/dev/peps/pep-0517/)
