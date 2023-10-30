[![Linux/Mac/Windows build status](
  https://circleci.com/gh/dwave-examples/feature-selection-notebook.svg?style=shield)](
  https://circleci.com/gh/dwave-examples/feature-selection-notebook)

# Feature Selection

This notebook develops a QPU programming model for an optimization problem that
selects a subset and demonstrates it using Ocean software's
[dwave-hybrid](https://docs.ocean.dwavesys.com/en/stable/docs_hybrid/sdk_index.html)
on an example of feature selection for machine learning.

The notebook has the following sections:

1. **What is Feature Selection?** defines and explains the feature-selection problem.
2. **Feature Selection by Mutual Information** describes a particular method of
   feature selection that is demonstrated in this notebook.
3. **Solving Feature Selection on a Quantum Computer** shows how such optimization
   problems can be formulated for solution on a D-Wave quantum computer.
4. **Example Application: Predicting Survival of Titanic Passengers** demonstrates
   the use of
   [Kerberos](https://docs.ocean.dwavesys.com/en/stable/docs_hybrid/reference/reference.html),
   an out-of-the-box classical-quantum
   [hybrid](https://docs.ocean.dwavesys.com/en/stable/docs_hybrid/sdk_index.html)
   sampler, to select optimal features for a public-domain dataset.

## What is Feature Selection?

Statistical and machine-learning models use sets of input variables ("features")
to predict output variables of interest. Feature selection can be part of the model
design process: selecting from a large set of potential features a highly informative
subset simplifies the model and reduces dimensionality.

For systems with large numbers of potential input information&mdash;for example,
weather forecasting or image recognition&mdash;model complexity and required compute
resources can be daunting. Feature selection can help make such models tractable.

However, optimal feature selection can itself be a hard problem. This example
introduces a powerful method of optimizing feature selection based on a complex
probability calculation. This calculation is submitted for solution to a quantum
computer.

![Example Solution](images/feature_selection_titanic.png)

## Installation

You can run this example without installation in cloud-based IDEs that support 
the [Development Containers specification](https://containers.dev/supporting)
(aka "devcontainers").

For development environments that do not support ``devcontainers``, install 
requirements:

    pip install -r requirements.txt

If you are cloning the repo to your local system, working in a 
[virtual environment](https://docs.python.org/3/library/venv.html) is 
recommended.

## Usage

Your development environment should be configured to 
[access Leap’s Solvers](https://docs.ocean.dwavesys.com/en/stable/overview/sapi.html).
You can see information about supported IDEs and authorizing access to your 
Leap account [here](https://docs.dwavesys.com/docs/latest/doc_leap_dev_env.html).  

The notebook can be opened by clicking on the 
``01-feature-selection.ipynb`` file in VS Code-based IDEs. 

To run a locally installed notebook:

```bash
jupyter notebook
```

## License

See [LICENSE](LICENSE.md) file.
