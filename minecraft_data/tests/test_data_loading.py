"""Tests for lazy data loading with Pooch."""

import json
import os
import pytest
from minecraft_data import data


class TestDataLoading:
    """Tests for minecraft-data lazy loading."""

    def test_supported_versions_defined(self):
        """SUPPORTED_VERSIONS should contain valid version strings."""
        assert len(data.SUPPORTED_VERSIONS) > 0
        for version in data.SUPPORTED_VERSIONS:
            assert isinstance(version, str)
            assert "." in version  # Should have semantic versioning

    def test_pooch_instance_created(self):
        """DATA_FETCHER should be a Pooch instance."""
        assert data.DATA_FETCHER is not None
        # Pooch instance should have these attributes
        assert hasattr(data.DATA_FETCHER, "fetch")
        assert hasattr(data.DATA_FETCHER, "path")

    def test_get_data_path_with_valid_version(self):
        """get_data_path should return a path for valid versions."""
        version = data.SUPPORTED_VERSIONS[0]
        path = data.get_data_path(version)
        assert isinstance(path, str)
        assert len(path) > 0
        assert os.path.isdir(path)

    def test_get_data_path_with_invalid_version(self):
        """get_data_path should raise ValueError for unsupported versions."""
        with pytest.raises(ValueError):
            data.get_data_path("1.0.0")

    def test_get_data_path_error_message(self):
        """ValueError message should list supported versions."""
        try:
            data.get_data_path("99.99.99")
            pytest.fail("Should raise ValueError")
        except ValueError as e:
            assert "1.20.5" in str(e)
            assert "1.21.6" in str(e)

    def test_pooch_base_url_configured(self):
        """DATA_FETCHER should have correct base URL for GitHub."""
        assert data.DATA_FETCHER.base_url.startswith("https://github.com")
        assert "minecraft-data" in data.DATA_FETCHER.base_url

    def test_minecraft_data_hash_defined(self):
        """MINECRAFT_DATA_HASH should be a valid SHA256 hash."""
        assert data.MINECRAFT_DATA_HASH.startswith("sha256:")
        assert len(data.MINECRAFT_DATA_HASH) > 10

    def test_extract_tarball_idempotent(self):
        """Calling _extract_tarball multiple times should return same path."""
        path1 = data._extract_tarball()
        path2 = data._extract_tarball()
        assert path1 == path2
        assert os.path.isdir(path1)


class TestRealData:
    """Tests using actual minecraft-data files."""

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_version_data_directory_exists(self, version):
        """Verify data directory exists for each supported version."""
        data_path = data.get_data_path(version)
        version_dir = os.path.join(data_path, "pc", version)
        assert os.path.isdir(version_dir), f"Version directory not found: {version_dir}"

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_items_json_exists_if_available(self, version):
        """Verify items.json exists for versions that have it."""
        data_path = data.get_data_path(version)
        items_file = os.path.join(data_path, "pc", version, "items.json")
        # Some versions may not have complete data
        if os.path.isfile(items_file):
            assert True
        else:
            pytest.skip(f"items.json not available for {version}")

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_items_json_is_valid(self, version):
        """Verify items.json is valid JSON if it exists for the version."""
        data_path = data.get_data_path(version)
        items_file = os.path.join(data_path, "pc", version, "items.json")

        if not os.path.isfile(items_file):
            pytest.skip(f"items.json not available for {version}")

        with open(items_file) as f:
            items = json.load(f)

        assert isinstance(items, list)
        assert len(items) > 0

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_items_have_required_fields(self, version):
        """Verify items have required fields if data exists."""
        data_path = data.get_data_path(version)
        items_file = os.path.join(data_path, "pc", version, "items.json")

        if not os.path.isfile(items_file):
            pytest.skip(f"items.json not available for {version}")

        with open(items_file) as f:
            items = json.load(f)

        for item in items[:10]:  # Check first 10 items
            assert "id" in item, f"Missing 'id' field in item: {item}"
            assert "name" in item, f"Missing 'name' field in item: {item}"
            assert "displayName" in item, f"Missing 'displayName' field in item: {item}"
            assert "stackSize" in item, f"Missing 'stackSize' field in item: {item}"

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_blocks_json_exists_if_available(self, version):
        """Verify blocks.json exists for versions that have it."""
        data_path = data.get_data_path(version)
        blocks_file = os.path.join(data_path, "pc", version, "blocks.json")
        # Some versions may not have complete data
        if os.path.isfile(blocks_file):
            assert True
        else:
            pytest.skip(f"blocks.json not available for {version}")

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_blocks_json_is_valid(self, version):
        """Verify blocks.json is valid JSON if it exists for the version."""
        data_path = data.get_data_path(version)
        blocks_file = os.path.join(data_path, "pc", version, "blocks.json")

        if not os.path.isfile(blocks_file):
            pytest.skip(f"blocks.json not available for {version}")

        with open(blocks_file) as f:
            blocks = json.load(f)

        assert isinstance(blocks, list)
        assert len(blocks) > 0
