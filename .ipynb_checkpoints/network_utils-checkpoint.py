
"""network_stability.ipynb
Visualizing Jacobian interaction networks via Graphviz.

Requirements:
  - numpy
  - graphviz (Python bindings + Graphviz binaries on PATH)
"""

import numpy as np
import graphviz


def draw_network(jacobian_matrix,
                 nodes,
                 output_path='network',
                 label_fontsize=14,
                 graph_size='8,8',
                 dpi=100,
                 engine='dot'):
    """
    Render and save the interaction network of a Jacobian matrix.

    Parameters
    ----------
    jacobian_matrix : numpy.ndarray, shape (n,n)
        Square Jacobian where entry [i,j] is (f_i)_x_j.
    nodes : list of str
        Length-n list of node names in the same order as the matrix axes.
    output_path : str
        Base filename (without extension) to save the image to.
    label_fontsize : int
        Font size for edge labels.
    graph_size : str
        Graphviz `size` attribute (e.g., '8,8').
    dpi : int
        Resolution of the output image.
    engine : str
        Graphviz layout engine.

    Returns
    -------
    graphviz.Digraph
        The Digraph object (image is also saved).
    """

    if jacobian_matrix.shape[0] != jacobian_matrix.shape[1]:
        raise ValueError("Jacobian matrix must be square.")
    if jacobian_matrix.shape[0] != len(nodes):
        raise ValueError("Number of nodes must match the size of the Jacobian matrix.")

    dot = graphviz.Digraph(format='png')
    dot.engine = engine
    dot.attr(dpi=str(dpi))
    dot.attr(rankdir='LR', size=graph_size, ratio='compress')
    # Set Node attributes
    # dot.attr('node',
    #          shape='ellipse',
    #          style='filled,setlinewidth(2)',
    #          color='black',
    #          fillcolor='lightgoldenrodyellow',
    #          fontname='Helvetica',
    #          fontsize=str(label_fontsize),
    #          fixedsize='true',
    #          width='1.0',
    #          height='0.5',
    #          margin='0.1') 
    

    dot.attr('node',
             shape='circle',
             style='filled,setlinewidth(2)',
             color='black',
             fillcolor='lightgoldenrodyellow',
             fontname='Helvetica',
             fontsize=str(label_fontsize))
    
    #Set edge attributes
    dot.attr('edge',
             fontname='Helvetica',
             fontsize=str(label_fontsize),
             penwidth='2')

    ## Draw the graph
    n = jacobian_matrix.shape[0] # Shape of the Jacobian Matrix
    for i in range(n):
        dot.node(nodes[i])  # Declare the node 'EXPLICITLY'
        for j in range(n):
            value = jacobian_matrix[i, j]
            if value == 0:
                continue

            if i == j:
                label = " " if value > 0 else " "
                color = "blue" if value > 0 else "red"
                arrowhead = "normal" if value > 0 else "tee"
                dot.edge(nodes[i], nodes[i],
                         color=color,
                         label=label,
                         arrowhead=arrowhead)
            else:
                label = " " if value > 0 else " "
                color = "blue" if value > 0 else "red"
                arrowhead = "normal" if value > 0 else "tee"
                dot.edge(nodes[j], nodes[i],  # j --> i
                         color=color,
                         label=label,
                         arrowhead=arrowhead)

    dot.render(output_path, view=False)
    return dot

