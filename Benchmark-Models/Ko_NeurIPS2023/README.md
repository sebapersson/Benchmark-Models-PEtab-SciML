# Ko_NeurIPS2023

A second-order inspired neural ordinary differential equation (neural ODE) model of
double-pendulum dynamics [1].

## Implementation details

The implementation follows the double-pendulum benchmark from the original publication, with
two differences.

First, a 70/30 split is used for training and validation data instead of the 50/50 split
used in the original study, as the latter led to non-correlation between training and
validation loss.

Second, the original publication scales the time span by the maximum training time. This
scaling is implemented directly in the PEtab measurement tables. For example, the final
training time point is 1.0.

## Other notes

Both training and validation data are provided. The corresponding PEtab-SciML problems can
be built using the respective YAML files.

The provided nominal values do not correspond to an optimal fit, so lower loss values can be
achieved when training the model.

## References

1. Ko, Joon-Hyuk, et al. "Homotopy-based training of neuralodes for accurate dynamics
   discovery." _Advances in Neural Information Processing Systems_ 36 (2023): 64725-64752.
