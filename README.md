[![Linux/Mac/Windows build status](
  https://circleci.com/gh/dwave-examples/feature-selection-notebook.svg?style=svg)](
  https://circleci.com/gh/dwave-examples/feature-selection-notebook)

# Feature Selection Jupyter Notebook

This notebook develops a QPU programming model for an optimization problem that
selects a subset and demonstrates it using D-Wave Ocean's stack of tools,
including *dwave-hybrid*, on an example of feature selection for machine learning.

## Usage

To enable notebook extensions[^1]:

```bash
jupyter contrib nbextension install --sys-prefix
jupyter nbextension enable toc2/main
jupyter nbextension enable exercise/main
jupyter nbextension enable exercise2/main
jupyter nbextension enable python-markdown/main

```

To run the notebook:

```bash
jupyter notebook
```

[^1]: Leap's IDE, which runs VS Code, does not support all notebook extensions.  

## License

See [LICENSE](LICENSE.md) file.
