"""Lazy data loading for minecraft-data using Pooch."""

import os
import tarfile
import pooch

# Supported Minecraft versions
SUPPORTED_VERSIONS = ["1.20.6", "1.21.6"]

# SHA256 hash for the master branch tarball from GitHub
# This contains all Minecraft versions including 1.20.6 and 1.21.6
MINECRAFT_DATA_HASH = (
    "sha256:bb05d6355b7383b569d7ef7413a13946e78521f2a05986c8c6236bbff53a7d3c"
)

# Create Pooch instance for lazy data downloads
DATA_FETCHER = pooch.create(
    path=pooch.os_cache("minecraft_data"),
    base_url="https://github.com/PrismarineJS/minecraft-data/archive/",
    env="MINECRAFT_DATA_DIR",  # Allow override with environment variable
    registry={
        "master.tar.gz": MINECRAFT_DATA_HASH,
    },
)


def _extract_tarball():
    """Extract the minecraft-data tarball if not already extracted."""
    cache_dir = os.environ.get("MINECRAFT_DATA_DIR", pooch.os_cache("minecraft_data"))
    tarball_path = os.path.join(cache_dir, "master.tar.gz")
    extract_path = os.path.join(cache_dir, "minecraft-data-master")

    # If already extracted, return the path
    if os.path.isdir(extract_path):
        return extract_path

    # Download if not present
    if not os.path.exists(tarball_path):
        DATA_FETCHER.fetch("master.tar.gz")

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
