# Copyright 2021 D-Wave Systems Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

"""Helper functions related to D-Wave systems
"""

import dwave_networkx as dnx

def qpu_working_graph(qpu):
    "Return a dwave_networkx graph representing the working graph of a given QPU."

    dnx_graphs = {'chimera': dnx.chimera_graph, 'pegasus': dnx.pegasus_graph}

    dnx_graph = dnx_graphs[qpu.properties["topology"]["type"].lower()]

    return dnx_graph(qpu.properties["topology"]["shape"][0],
                     node_list=qpu.nodelist,
                     edge_list=qpu.edgelist)
