"""Loading helpers for Paradoxical Voodoo kernels."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict

from .models import AGIKernel, KernelConfig, KernelRegistry
from .operators import OPERATORS


def load_kernels(path: Path | None = None) -> KernelRegistry:
    """Load all kernel definitions from disk and resolve operators."""

    base_path = path or Path(__file__).resolve().parent / "kernels"
    if not base_path.exists():
        raise FileNotFoundError(f"Kernel directory not found: {base_path}")

    kernels: Dict[str, AGIKernel] = {}
    for definition_path in sorted(base_path.glob("*.json")):
        data = json.loads(definition_path.read_text())
        config = KernelConfig.from_dict(data)
        kernel = config.to_kernel(OPERATORS)
        kernels[kernel.canonical_name] = kernel
        for alias in kernel.aliases:
            kernels[alias] = kernel
    return KernelRegistry(kernels=kernels, operators=OPERATORS)


__all__ = ["load_kernels"]
