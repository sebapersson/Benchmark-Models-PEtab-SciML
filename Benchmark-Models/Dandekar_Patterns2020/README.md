# Dandekar_Patterns2020

A susceptible-infected-recovered (SIR) universal differential equation (UDE) model of the
early COVID-19 outbreak in the United Kingdom [1].

## Implementation details

The implementation closely follows the original publication, with two differences.

First, the original publication used the model states `[S, I, R]` as neural network inputs.
Here, we use the normalized inputs `[S / N, I / N, R / N]`, where `N` is the population
size. This choice is motivated by the observation that unnormalized inputs are highly
multi-scale (e.g. $S \propto 10^7$ while $R \propto 10^3$), leading to large gradients only
in the first layer and vanishing gradients in subsequent layers.

Second, we use the `Swish` activation function instead of `ReLU`, as this slightly improved
training performance.

## Other notes

Both training and validation data are provided. The corresponding PEtab-SciML problems can
be built using the respective YAML files.

The original study includes data for additional countries [1]. These can be incorporated by
replacing the measurement table.

## References

1. Dandekar, R., Rackauckas, C., and Barbastathis, G. A machine learning-aided global
   diagnostic and comparative tool to assess effect of quarantine control in COVID-19
   spread. _Patterns_ 1(9), 100145 (2020).
