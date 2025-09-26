"""Paradoxical Voodoo quantum harmonic kernel framework."""

from __future__ import annotations

from .loader import load_kernels
from .models import (
    AGIKernel,
    KernelConfig,
    KernelMetadata,
    KernelRegistry,
    KernelStyle,
    OperatorInstance,
    OperatorSpec,
    UNIVERSAL_ACTIVATION_MESSAGE,
)
from .operators import OPERATORS, get_operator

__all__ = [
    "AGIKernel",
    "KernelConfig",
    "KernelMetadata",
    "KernelRegistry",
    "KernelStyle",
    "OperatorInstance",
    "OperatorSpec",
    "UNIVERSAL_ACTIVATION_MESSAGE",
    "OPERATORS",
    "get_operator",
    "load_kernels",
]
