# ABC analysis

Performs and visualizes an ABC analysis. This package is a Python implementation of the R package [**ABCanalysis**][abcanalysis-link].

[abcanalysis-link]: https://CRAN.R-project.org/package=ABCanalysis

## Where to get it
The source code is hosted on GitHub at: https://github.com/viessmann/abc_analysis

```sh
# First installation via PyPI
pip install abc_analysis
```

```sh
# Update via PyPI
pip install abc_analysis --upgrade
```

## Basic usage

```python
from abc_analysis import abc_analysis, abc_plot

# Perform an ABC analysis on a numeric vector (without plotting)
dctAnalysis = abc_analysis([1, 15, 25, 17, 2, 3, 5, 6, 2, 3, 22])

# Perform an ABC analysis with plotting
dctAnalysis = abc_analysis([1, 15, 25, 17, 2, 3, 5, 6, 2, 3, 22], True)

# Plot saved results of an ABC analysis
abc_plot(dctAnalysis)
```

## Dependencies
- [pandas](https://pandas.pydata.org): 0.22.0 or higher
- [NumPy](http://www.numpy.org): 1.14.0 or higher
- [scipy](https://www.scipy.org/): 1.1.0 or higher
- [matplotlib](https://matplotlib.org/): 2.2.2 or higher