"""BLAS/LAPACK wheel variant provider"""

from __future__ import annotations

from dataclasses import dataclass

__version__ = "0.0.2"
namespace = "blas_lapack"
is_build_plugin = True

_blas_providers = ["accelerate", "openblas", "mkl"]


@dataclass(frozen=True)
class VariantFeatureConfig:
    name: str
    # Acceptable values in priority order
    values: list[str]
    multi_value: bool = False


@dataclass(frozen=True)
class VariantProperty:
    namespace: str
    feature: str
    value: str


def get_supported_configs() -> list[VariantFeatureConfig]:
    return [
        VariantFeatureConfig("provider", _blas_providers),
    ]


get_all_configs = get_supported_configs
