# Philipps_NPJSystBiolAppl2025

A universal differential equation (UDE) model of phosphorylation-dependent STAT5A/STAT5B
dimerization [1, 2]. The mechanistic ODE model of Boehm et al. [1] is kept unchanged.
The observable mapping of the relative STAT5A abundance (`rSTAT5A_rel`) is replaced by a
feed-forward neural network. The network takes all eight model species as input. The
observables `pSTAT5A_rel` and `pSTAT5B_rel` keep their mechanistic formulas. This
corresponds to the problem `boehm_observable_ab_ratio` in Philipps et al. [2].

## Implementation details

The implementation follows the original publication [2], which built on the PEtab
(version 1) implementation `Boehm_JProteomeRes2014` of the Boehm model from the PEtab
benchmark collection [3]. The SBML model, measurements, observable formulas, parameter
bounds, and the values of the fixed parameters `ratio` and `specC17` are taken from that
implementation. Here, it is converted to PEtab version 2 with the PEtab-SciML extension.

The neural network has one hidden layer with 10 neurons and ReLU activation, and it
receives the unnormalized species concentrations as input. This is the architecture of the
best-performing UDE (#923), which is analyzed in Fig. 7 of [2]. The mechanistic parameters
(rate constants), the noise parameters, and the neural network parameters are estimated.

## Training in the original publication

The nominal parameter values were obtained in [2] with the following set-up (UDE #923 of
the experiment `2024_11_20_Boehm_observable_ab_ratio` in the
[UDE pipeline](https://github.com/m-philipps/ude_pipeline_systemsbio)):

- Data: the experimental data from [1], as provided in [3]. Every fifth time point,
  starting with the second (t = 2.5, 30, 100 min), is used for validation, and the
  remaining time points are used for training. Both training and validation data are
  provided here, and the corresponding PEtab-SciML problems can be built using the
  respective YAML files.
- Parameters: the mechanistic and noise parameters were estimated through a bounded tanh
  reparameterization, which is equivalent to estimating log-transformed parameters within
  the bounds `[1e-5, 1e5]`. Start points for the mechanistic and noise parameters were
  sampled by Latin hypercube sampling.
- Objective: Gaussian negative log-likelihood of the training data, averaged over the data
  points, without regularization.
- Optimization: 500 epochs of the Adam optimizer with learning rate 0.0180644560551626,
  followed by 333 epochs of BFGS with backtracking line search. Gradients were computed with
  Zygote. The parameters with the lowest validation loss were retained, which was reached at
  epoch 585 (epoch 85 of BFGS).
- ODE solver: `KenCarp4` from OrdinaryDiffEq.jl with default tolerances (absolute tolerance
  1e-6, relative tolerance 1e-3).

## References

1. Boehm, M. E., Adlung, L., Schilling, M., Roth, S., Klingmüller, U., and Lehmann, W. D.
   Identification of isoform-specific dynamics in phosphorylation-dependent STAT5
   dimerization by quantitative mass spectrometry and mathematical modeling. _Journal of
   Proteome Research_ 13(12), 5685-5694 (2014).
2. Philipps, M., Schmid, N., and Hasenauer, J. Current state and open problems in universal
   differential equations for systems biology. _npj Systems Biology and Applications_
   11(1), 101 (2025).
3. Hass, H., Loos, C., Raimúndez-Álvarez, E., Timmer, J., Hasenauer, J., and Kreutz, C.
   Benchmark problems for dynamic modeling of intracellular processes. _Bioinformatics_
   35(17), 3073-3082 (2019).
