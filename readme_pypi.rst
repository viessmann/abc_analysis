ABC analysis
============

Performs and visualizes an ABC analysis with automated limit detection. 

This package is a Python implementation of the R package `ABCanalysis <https://CRAN.R-project.org/package=ABCanalysis>`_

Basic Usage
^^^^^^^^^^^

.. code-block:: python

    from abc_analysis import abc_analysis, abc_plot
    
    # Perform an ABC analysis on a numeric vector (without plotting)
    dctAnalysis = abc_analysis([1, 15, 25, 17, 2, 3, 5, 6, 2, 3, 22])
    
    # Perform an ABC analysis with plotting
    dctAnalysis = abc_analysis([1, 15, 25, 17, 2, 3, 5, 6, 2, 3, 22], True)
    
    # Plot saved results of an ABC analysis
    abc_plot(dctAnalysis)

.. image:: https://github.com/viessmann/abc_analysis/blob/master/doc/images/abc_plot.png