# _wheel_poetry

This is a demo Python wheel created using Poetry. It contains a simple module with a function that returns a greeting message.

## Instructions

1. Navigate to the `_wheel_poetry` folder:

   ```bash
   cd /Users/Jibamy/wasm/py.js/pyodide/_wheel_poetry
   ```

2. Install Poetry if not already installed:

   ```bash
   pip install poetry
   ```

3. Install dependencies:

   ```bash
   poetry install
   ```

4. Run tests:

   ```bash
   poetry run pytest
   ```

5. Build the wheel:

   ```bash
   poetry build
   ```

This will generate a `.whl` file in the `dist` folder.

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
