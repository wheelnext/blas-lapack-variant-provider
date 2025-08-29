# blas-lapack-variant-provider

This is a plugin for the proposed [wheel variants implementation](
https://github.com/wheelnext/pep_xxx_wheel_variants) that provides
BLAS/LAPACK library selection.

This plugin always returns a fixed list of supported variants, and so
can be used as a build-time plugin.

## Usage

Namespace: `blas_lapack`

Plugin API: `blas_lapack_variant_provider` (can be inferred from `requires`)

Example use in `pyproject.toml`:

```toml
[variant.providers.blas_lapack]
requires = ["blas-lapack-variant-provider"]
plugin-use = "build"
```

## Provided properties
### blas_lapack :: provider

Values: `accelerate`, `openblas`, `mkl`

Indicates which BLAS/LAPACK implementation is used.
