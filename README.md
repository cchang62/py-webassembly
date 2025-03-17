# Pyodide and WebAssembly Demo

This repository demonstrates how to use Pyodide with WebAssembly (Wasm) to run Python code in the browser.

## Table of Contents

- [Pyodide and WebAssembly Demo](#pyodide-and-webassembly-demo)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
  - [Usage](#usage)
    - [Example](#example)
  - [Contributing](#contributing)
  - [License](#license)
  - [References](#references)

## Introduction

Pyodide is a Python distribution for the browser and Node.js based on WebAssembly. It allows you to run Python code directly in the browser, making it possible to leverage Python's extensive ecosystem of libraries in web applications.

## Getting Started

To get started with this demo, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/pyodide-wasm-demo.git
    cd pyodide-wasm-demo
    ```

2. Open `index.html` in your web browser to see the demo in action.

## Usage

This demo includes a simple example of running Python code in the browser using Pyodide. You can modify the `index.html` and `main.js` files to experiment with different Python scripts and see the results in real-time.

### Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pyodide and Wasm Demo</title>
    <script src="https://cdn.jsdelivr.net/pyodide/v0.18.1/full/pyodide.js"></script>
</head>
<body>
    <h1>Pyodide and WebAssembly Demo</h1>
    <textarea id="python-code" rows="10" cols="50">print("Hello, Pyodide!")</textarea>
    <button onclick="runPython()">Run Python</button>
    <pre id="output"></pre>

    <script>
        async function loadPyodideAndPackages() {
            window.pyodide = await loadPyodide();
        }

        async function runPython() {
            let code = document.getElementById("python-code").value;
            let output = await pyodide.runPythonAsync(code);
            document.getElementById("output").innerText = output;
        }

        loadPyodideAndPackages();
    </script>
</body>
</html>
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or suggestions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## References

- [認識Service Worker](https://medium.com/@b09112332/%E8%AA%8D%E8%AD%98service-worker-f2d2e74bd3c0)
- [Bringing Python to the Web](https://karay.me/2022/07/12/bringing-python-to-the-web.html)
- [Pyodide Service Worker Usage](https://pyodide.org/en/stable/usage/service-worker.html)
- [Pyodide - Pandas Tutor](https://blog.pyodide.org/posts/pandastutor/#step-1-create-a-self-contained-pandas-tutor-wheel)
- [Pyodide - init try](https://abstreamace.com/sglab/2022/08/03/pyodide-%E5%88%9D%E9%AB%94%E9%A9%97/)