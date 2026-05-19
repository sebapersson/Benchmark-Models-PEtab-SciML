# Ko_NeurIPS2023

A second-order neural ordinary differential equation (neural ODE) model of double-pendulum
dynamics [1].

## Implementation details

The implementation follows the double-pendulum benchmark from the original publication, with
two differences.

First, we use Swish activation functions instead of the activation functions used in the
original study.

Second, we use a 70/30 split for the training and test data instead of the 50/50 split used
in the original study, as the latter led to not correlation between training and validation
loss.

## References

1. Ko, Joon-Hyuk, et al. "Homotopy-based training of neuralodes for accurate dynamics
   discovery." _Advances in Neural Information Processing Systems_ 36 (2023): 64725-64752.
