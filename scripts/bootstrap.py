"""Helpers for running scripts from anywhere in the repository."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Optional


def find_repo_root(marker_dir: str = "vibe_code") -> Optional[Path]:
    """Return the repository root by walking up until ``marker_dir`` is found."""

    current = Path(__file__).resolve().parent
    for parent in [current] + list(current.parents):
        if (parent / marker_dir).exists():
            return parent
    return None


def add_repo_root_to_path(marker_dir: str = "vibe_code") -> Path:
    """Ensure the repository root is on ``sys.path`` and return it."""

    root = find_repo_root(marker_dir) or Path(__file__).resolve().parent
    root_str = str(root)
    if root_str not in sys.path:
        sys.path.insert(0, root_str)
    return root
