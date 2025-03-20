# Build Python Wheel

This folder is intended for building Python wheels that can be used with Pyodide. Add your Python source files and setup scripts here to create distributable `.whl` files.

## Folder Structure Example

1. Traditional Method  
Here is an example of how your project folder structure might look:

```sh
mypackage/
    mypackage/
        __init__.py
        module1.py
        module2.py
    setup.py
    README.md
    LICENSE
```

## Sample: Building a Python Wheel

1. Create a `setup.py` file in this folder with the following content:

   ```python
   from setuptools import setup

   setup(
       name="highcharts_image",
       version="0.1",
       packages=["generate_highcharts_image"],
   )

   ```

2. Create a folder named `example_package` and add an `__init__.py` file inside it:

   ```python
   # example_package/__init__.py
   def hello():
       return "Hello, Pyodide!"
   ```

3. Run the following command to build the wheel:

   ```bash
   python3 setup.py bdist_wheel
   ```

4. The generated `.whl` file will be located in the `dist` folder.

# _wheel_tradition

This folder contains Python wheels for dependencies used in the Pyodide project.  
Place the `generate_highcharts_image` wheel and its dependencies here.
