"""Lint the curated PEtab SciML benchmark problems.

See `.github/workflows/ci.yml` for dependencies.
"""

from __future__ import annotations

from pathlib import Path

import petab.v2 as petab
import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_DIR = REPO_ROOT / "Benchmark-Models"
PROBLEM_YAMLS = sorted(BENCHMARK_DIR.glob("*/problem.yaml"))


@pytest.mark.parametrize(
    "problem_yaml",
    PROBLEM_YAMLS,
    ids=[str(p.relative_to(REPO_ROOT)) for p in PROBLEM_YAMLS],
)
def test_lint(problem_yaml: Path):
    """Each curated PEtab SciML problem must pass the linter."""
    problem = petab.Problem.from_yaml(problem_yaml)
    results = problem.validate()
    assert not results.has_errors(), (
        f"Validation errors in {problem_yaml.relative_to(REPO_ROOT)}:\n"
        + "\n".join(str(result) for result in results)
    )
