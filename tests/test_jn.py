# Copyright 2021 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import unittest

def run_jn(jn, timeout):

    open_jn = open(jn, "r", encoding='utf-8')
    notebook = nbformat.read(open_jn, nbformat.current_nbformat)
    open_jn.close()

    preprocessor = ExecutePreprocessor(timeout=timeout, kernel_name='python3')
    preprocessor.allow_errors = True
    preprocessor.preprocess(notebook, {'metadata': {'path': os.path.dirname(jn)}})

    return notebook

def collect_jn_errors(nb):

    errors = []
    for cell in nb.cells:
        if 'outputs' in cell:
            for output in cell['outputs']:
                if output.output_type == 'error':
                    errors.append(output)

    return errors

def embedding_fail(error_list):
    return error_list and error_list[0].evalue == 'no embedding found'

def robust_run_jn(jn, timeout, retries):

    run_num = 1
    notebook = run_jn(jn, timeout)
    errors = collect_jn_errors(notebook)

    while embedding_fail(errors) and run_num < retries:
        run_num += 1
        notebook = run_jn(jn, timeout)
        errors = collect_jn_errors(notebook)

    return notebook, errors

def cell_text(nb, cell):
    return nb["cells"][cell]["outputs"][0]["text"]

def cell_output(nb, cell, part, data_type):
    return nb["cells"][cell]["outputs"][part][data_type]

jn_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
jn_file = os.path.join(jn_dir, '01-feature-selection.ipynb')

class TestJupyterNotebook(unittest.TestCase):

    def test_jn(self):
        # Smoketest
        MAX_EMBEDDING_RETRIES = 3
        MAX_RUN_TIME = 100

        nb, errors = robust_run_jn(jn_file, MAX_RUN_TIME, MAX_EMBEDDING_RETRIES)

        self.assertEqual(errors, [])

        # Section Illustrative Toy Problem, code cell 2 (plot_toy_signals)
        self.assertIn("image/png", cell_output(nb, 6, 0, "data"))

        # Section Illustrative Toy Problem, code cell 4 (plot_two_var_model)
        self.assertIn("Standard deviation", cell_text(nb, 10))

        # Section Illustration of Shannon Entropy, code cell 1 (plot_se)
        self.assertIn("image/png", cell_output(nb, 16, 0, "data"))

        # Section Illustration of CSE, code cell 1
        self.assertIn("H(in1)", cell_text(nb, 20))

        # Section Mutual Information on the Toy Problem, code cell 1 (plot_mi)
        self.assertIn("image/png", cell_output(nb, 24, 0, "data"))

        # Section Mutual Information on the Toy Problem, code cell 2 (plot_lingress)
        self.assertIn("image/png", cell_output(nb, 26, 0, "data"))

        # Section Conditional Mutual Information, code cell 2
        self.assertIn("I(out;in2|in1)", cell_text(nb, 31))

        # Section MIQUBO on the Toy Problem, code cell 1
        self.assertIn("in1:", cell_text(nb, 36))

        # Section MIQUBO on the Toy Problem, code cell 2
        self.assertIn("('in1', 'in2')", cell_text(nb, 38))

        # Section MIQUBO on the Toy Problem, code cell 3 (plot_solutions)
        self.assertIn("image/png", cell_output(nb, 40, 0, "data"))

        # Section Penalizing Non-k Selections, code cell 1 (plot_solutions)
        self.assertIn("image/png", cell_output(nb, 43, 0, "data"))

        # Section Example Application: Predicting, code cell 1 (plot_mi)
        self.assertIn("image/png", cell_output(nb, 47, 0, "data"))

        # Section Exact Versus Good Solutions, code cell 1
        self.assertIn("image/png", cell_output(nb, 49, 1, "data"))

        # Section Building the MI-Based BQM, code cell 1
        self.assertIn("8", cell_text(nb, 53))
