# Contributing

First, thank you for taking the time to contribute to the PEtab-SciML Benchmark Collection.
Contributions help advance SciML method development and benchmarking for the wider
community.

## Ways to contribute

We welcome contributions of new benchmark models.

## Adding a new benchmark model

To add a new benchmark model, please make sure that the following checklist is fulfilled.

- [ ] The PEtab-SciML problem is based on a peer-reviewed and published model.
- [ ] The problem ID follows the format
      `{LAST_NAME_OF_FIRST_AUTHOR}_{ABBREVIATED_JOURNAL_NAME}{YEAR_OF_PUBLICATION}`.
- [ ] The problem ID is included in the pull request title.
- [ ] There is a GitHub issue for the problem.
  - [ ] The problem ID is included in the issue title.
  - [ ] The issue contains a brief model description.
  - [ ] The issue and pull request are linked to each other.
  - [ ] Differences between the implementation and the original publication are described.
  - [ ] The source of the nominal parameters is stated, for example whether they were taken
        from the original publication or obtained by fitting.
- [ ] The SBML file is included.
  - [ ] The SBML file is annotated with a reference to the original publication.
  - [ ] The SBML model `id` and `name` attributes match the problem ID.
- [ ] The PEtab-SciML files are included.
  - [ ] The PEtab-SciML problem is valid according to the PEtab-SciML linter.
  - [ ] An `expected.yaml` file is provided with the expected likelihood/objective function
        value for the provided nominal parameter values.
- [ ] The main repository README has been updated.
  - [ ] The model is included in the overview table.
  - [ ] The overview table includes the model ID, hybridization form, number of estimated
        parameters, number of mechanistic parameters, number of ML parameters to estimate,
        and number of ODE states.
- [ ] The benchmark model directory contains a brief README with:
  - [ ] the reference to the original publication,
  - [ ] a short model description,
  - [ ] notes on relevant differences from the original publication, if any.

Although PEtab-SciML builds on PEtab v2 and supports model formats beyond SBML, this
benchmark collection currently accepts only SBML-based models, as SBML is the most widely
used format among tools supporting PEtab-SciML.
