# scROCK

scROCK (single-cell Refinement Of Cluster Knitting) is an algorithm for correcting cluster labels for scRNA-seq data, based on [Xinchuan Zeng and Tony R. Martinez. 2001. An algorithm for correcting mislabeled data. Intell. Data Anal. 5, 6 (December 2001), 491–502.](https://dl.acm.org/doi/10.5555/1294000.1294004).


## Installation

```pip install https://github.com/dos257/ADE/tarball/master```

For private repository use:
```pip install git+https://{token}@github.com/dos257/ADE.git```

Use keys `--upgrade --no-deps --force-reinstall` for forced update from git repository.


## Usage

If `X` is log1p-preprocessed `numpy.array` of shape `(n_samples, n_genes)` and `y` is clustering labels (from Leiden algorithm),

```python
from scrock import scrock
y_fixed = scrock(X, y)
```
