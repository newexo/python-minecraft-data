"""Tests for minecraft_data module structure and basic functionality."""

import sys

import minecraft_data


class TestModuleStructure:
    """Tests for the minecraft_data module."""

    def test_module_is_callable(self):
        """The minecraft_data module should be callable."""
        assert callable(minecraft_data)

    def test_module_has_common_method(self):
        """The minecraft_data module should have a common method."""
        assert hasattr(minecraft_data, "common")
        assert callable(minecraft_data.common)

    def test_module_is_in_sys_modules(self):
        """The minecraft_data module should be in sys.modules."""
        assert "minecraft_data" in sys.modules

    def test_custom_module_class(self):
        """The minecraft_data module should use a custom module class."""
        # The __class__ should be named 'mod'
        assert minecraft_data.__class__.__name__ == "mod"
