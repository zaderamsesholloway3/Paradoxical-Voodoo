"""Presentation helpers for Paradoxical Voodoo kernels."""

from __future__ import annotations

from .models import AGIKernel


def render_kernel(kernel: AGIKernel) -> str:
    """Render a kernel as a ritual card for console or chat surfaces."""

    operator_lines = "\n".join(
        f"    - {op.symbol} {op.name}\n      ↳ {op.effect}" + (f"\n      ↝ {op.nuance}" if op.nuance else "")
        for op in kernel.operators
    )
    execution_lines = "\n".join(f"    {idx}. {step}" for idx, step in enumerate(kernel.execution_steps, start=1))
    return (
        f"🌐 **{kernel.designation}**\n"
        f"Canonical: `{kernel.canonical_name}`\n"
        f"Aliases: {', '.join(kernel.aliases) if kernel.aliases else '—'}\n"
        f"Human Equivalent: {kernel.human_equivalent}\n"
        f"Status: {kernel.status}\n"
        f"Directive: {kernel.directive}\n"
        f"\n"
        f"Operators:\n{operator_lines}\n"
        f"\nExecution:\n{execution_lines}\n"
        f"\nFelt State: {kernel.felt_state}\n"
        f"Integration: {kernel.integration_note}\n"
        f"\nStyle: {kernel.style.palette} / {kernel.style.tone} / {kernel.style.layout}"
    )


__all__ = ["render_kernel"]
