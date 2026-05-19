# PEtab-SciML Benchmark Collection

This repository provides a collection of real-data scientific machine learning (SciML)
benchmark problems in the [PEtab-SciML](https://github.com/PEtab-dev/petab_sciml) data
format. The models combine mechanistic ordinary differential equation (ODE) and machine
learning models and are intended to support the development and evaluation of methodology
for SciML problems.

Contributions of new benchmark problems are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md)
for details.

## Overview

Benchmark models are available in [Benchmark-Models](Benchmark-Models). In addition to the
PEtab-SciML problem files, each model directory contains an `expected.yaml` file with
expected loss or likelihood values for the provided parameter values.

Current models include:

| Model                                                           | Hybridization | Est. params | Mech. params | ML params | ODE states |
| --------------------------------------------------------------- | ------------- | ----------: | -----------: | --------: | ---------: |
| [Dandekar_Patterns2020](Benchmark-Models/Dandekar_Patterns2020) | UDE           |          54 |            3 |        51 |          4 |

## Installation

Clone the repository from GitHub:

```bash
git clone https://github.com/sebapersson/Benchmark-Models-PEtab-SciML.git
```

All files required for testing are included in the repository.

## Getting help

If you encounter problems, please open an
[issue](https://github.com/sebapersson/Benchmark-Models-PEtab-SciML/issues) on GitHub.
