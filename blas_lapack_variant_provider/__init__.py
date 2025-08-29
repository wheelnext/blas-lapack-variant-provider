"""BLAS/LAPACK wheel variant provider"""

from __future__ import annotations

from dataclasses import dataclass

__version__ = "0"
namespace = "blas_lapack"
dynamic = False

_blas_providers = ["accelerate", "openblas", "mkl"]


@dataclass(frozen=True)
class VariantFeatureConfig:
    name: str

    # Acceptable values in priority order
    values: list[str]


@dataclass(frozen=True)
class VariantProperty:
    namespace: str
    feature: str
    value: str


def get_supported_configs(
    known_properties: frozenset[VariantProperty] | None,
) -> list[VariantFeatureConfig]:
    return [
        VariantFeatureConfig("provider", _blas_providers),
    ]


def validate_property(variant_property: VariantProperty) -> bool:
    assert variant_property.namespace == namespace
    return (
        variant_property.feature == "provider"
        and variant_property.value in _blas_providers
    )
