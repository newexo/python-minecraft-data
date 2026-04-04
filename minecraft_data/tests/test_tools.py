"""Tests for the tools module."""

import pytest
from minecraft_data import data, tools


class TestTools:
    """Tests for minecraft_data.tools functions."""

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_convert_loads_version(self, version):
        """Test that convert can load a version's data."""
        data_path = data.get_data_path(version)
        result = tools.convert(data_path, version)
        assert isinstance(result, dict)
        # Should have some data files
        assert len(result) > 0

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_convert_has_version_info(self, version):
        """Test that convert includes version info."""
        data_path = data.get_data_path(version)
        result = tools.convert(data_path, version)
        assert "version" in result

    def test_commondata_loads_common(self):
        """Test that commondata can load common data."""
        data_path = data.get_data_path(data.SUPPORTED_VERSIONS[0])
        result = tools.commondata(data_path)
        assert isinstance(result, dict)
        # Common data should have content
        assert len(result) > 0

    @pytest.mark.parametrize("version", data.SUPPORTED_VERSIONS)
    def test_convert_handles_missing_files(self, version):
        """Test that convert gracefully handles missing optional files."""
        # convert() should not fail even if some files are missing
        data_path = data.get_data_path(version)
        result = tools.convert(data_path, version)
        # Should return a dict even if some keys are missing
        assert isinstance(result, dict)
