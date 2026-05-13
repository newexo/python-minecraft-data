"""Lazy data loading for minecraft-data using Pooch."""

import os
import tarfile
import pooch

# Supported Minecraft versions
SUPPORTED_VERSIONS = ["1.20.6", "1.21.6"]

# SHA256 hash for the 3.110.1 release tarball from GitHub
# This is a stable, immutable release that includes all supported Minecraft versions
MINECRAFT_DATA_HASH = (
    "sha256:375a1c0267f395d0a04c01873ca9bae70e23e6bc32b9057d2893ce0a77d86a4a"
)

# Create Pooch instance for lazy data downloads
DATA_FETCHER = pooch.create(
    path=pooch.os_cache("minecraft_data"),
    base_url="https://github.com/PrismarineJS/minecraft-data/archive/refs/tags/",
    env="MINECRAFT_DATA_DIR",  # Allow override with environment variable
    registry={
        "3.110.1.tar.gz": MINECRAFT_DATA_HASH,
    },
)


def _extract_tarball():
    """Extract the minecraft-data tarball if not already extracted."""
    cache_dir = os.environ.get("MINECRAFT_DATA_DIR", pooch.os_cache("minecraft_data"))
    tarball_path = os.path.join(cache_dir, "3.110.1.tar.gz")
    extract_path = os.path.join(cache_dir, "minecraft-data-3.110.1")

    # If already extracted, return the path
    if os.path.isdir(extract_path):
        return extract_path

    # Download if not present
    if not os.path.exists(tarball_path):
        DATA_FETCHER.fetch("3.110.1.tar.gz")

    # Extract tarball
    with tarfile.open(tarball_path, "r:gz") as tar:
        tar.extractall(path=cache_dir)

    return extract_path


def get_data_path(version: str) -> str:
    """Get the path to the minecraft-data directory for a given version.

    Args:
        version: Minecraft version (e.g., '1.20.6')

    Returns:
        Path to the data directory for use with tools.convert()

    Raises:
        ValueError: If version is not in SUPPORTED_VERSIONS
        FileNotFoundError: If version data directory is not found after extraction
    """
    if version not in SUPPORTED_VERSIONS:
        raise ValueError(
            f"Version {version} not supported. "
            f"Supported versions: {', '.join(SUPPORTED_VERSIONS)}"
        )

    extract_path = _extract_tarball()
    data_dir = os.path.join(extract_path, "data")
    version_data_path = os.path.join(data_dir, "pc", version)

    if not os.path.isdir(version_data_path):
        raise FileNotFoundError(
            f"Minecraft data for version {version} not found at {version_data_path}"
        )

    # Return the data directory (as expected by tools.convert)
    return data_dir
