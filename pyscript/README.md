# PyScript

PyScript is a framework that allows you to run Python code directly in the browser. It integrates with WebAssembly to bring the power of Python to the web.

## Features

- Run Python code in the browser
- Integrate with existing JavaScript libraries
- Use Python packages from PyPI
- Easy to use and integrate

## Installation

To install PyScript, include the following script in your HTML file:

```html
<script src="https://pyscript.net/latest/pyscript.js"></script>
```

## Usage

Here is a simple example of how to use PyScript:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PyScript Example</title>
    <script src="https://pyscript.net/latest/pyscript.js"></script>
</head>
<body>
    <py-script>
        print("Hello, PyScript!")
    </py-script>
</body>
</html>
```

## Documentation

For more information, visit the [official PyScript documentation][docs].

## Contributing

Contributions are welcome! Please read the [contributing guidelines][contributing] before getting started.

## License

This project is licensed under the MIT License. See the [LICENSE][license] file for details.

[docs]: https://pyscript.net/docs
[contributing]: CONTRIBUTING.md
[license]: LICENSE
[example]: [pyscript-pandas](https://pyscript.com/@examples/pandas/latest?files=README.md,main.py,index.html)