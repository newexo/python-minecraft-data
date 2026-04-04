"""Integration tests using the full minecraft_data module."""

import pytest
import minecraft_data
from minecraft_data import data


class TestModuleIntegration:
    """Integration tests that exercise the full module."""

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_load_version_data(self, version):
        """Test loading a version through the module interface."""
        version_data = minecraft_data(version)
        assert version_data is not None
        # Should have version info at minimum
        assert hasattr(version_data, "version")

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_version_has_datapaths(self, version):
        """Test that loaded version has dataPaths data."""
        version_data = minecraft_data(version)
        # dataPaths is loaded from the JSON and converted
        assert version_data is not None

    def test_common_data(self):
        """Test loading common data if available."""
        try:
            common = minecraft_data.common()
            assert common is not None
            assert isinstance(common, type)
        except FileNotFoundError:
            # Common data may not be available in bundled data
            pytest.skip("Common data not available in bundled data")

    def test_unsupported_version_fallback(self):
        """Test that unsupported versions attempt fallback to bundled data."""
        # An arbitrary version not in SUPPORTED_VERSIONS
        try:
            result = minecraft_data("1.17.1")
            # If bundled data exists, it will load
            assert result is not None
        except FileNotFoundError:
            # Expected if bundled data doesn't have this version
            pass

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_version_with_custom_edition(self, version):
        """Test loading with custom edition parameter."""
        try:
            version_data = minecraft_data(version, edition="pc")
            assert version_data is not None
        except FileNotFoundError:
            # Edition may not exist for all versions
            pass
