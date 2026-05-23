# python-minecraft-data

Provide easy access to [minecraft-data](https://github.com/PrismarineJS/minecraft-data) in Python.

This is a fork of the original [python-minecraft-data](https://github.com/SpockBotMC/python-minecraft-data) with modern packaging infrastructure and lazy data loading using [Pooch](https://www.fatiando.org/pooch/).

## Features

- **Lazy data loading** — Data is downloaded on-demand using Pooch and cached locally
- **Efficient caching** — Downloaded data is cached in `~/.cache/minecraft_data` (configurable)
- **Modern packaging** — Built with Poetry and PEP 517/518 standards
- **Comprehensive tests** — 90%+ code coverage with pytest
- **CI/CD ready** — GitHub Actions workflow with coverage enforcement

## Installation

Clone and install from source:

```bash
git clone https://github.com/newexo/python-minecraft-data
cd python-minecraft-data
poetry install
```

## Usage

```python
import minecraft_data

# Load a specific version
mc_data = minecraft_data("1.21.6")

# Access version info
print(mc_data.version)

# Access items, blocks, etc. (if available for that version)
if hasattr(mc_data, 'items'):
    print(mc_data.items)
```

## Supported Versions

Currently supported for detailed testing:
- `1.20.5`
- `1.21.6`

Other versions in the [minecraft-data](https://github.com/PrismarineJS/minecraft-data) repository are accessible but may have incomplete data.

### Upstream data availability: full vs. stub versions

The [PrismarineJS minecraft-data](https://github.com/PrismarineJS/minecraft-data) repository does not ship full gameplay data for every Minecraft version. Some patch releases are published as **stubs** — directories containing only `version.json` (and occasionally `dataPaths.json`) — because their game data is unchanged from the previous full-data release. The stub still exists so that `version.json` can carry the correct protocol version number, but `items.json`, `blocks.json`, `recipes.json`, etc. are absent.

For the 1.20 and 1.21 series, the versions that ship **full data** (item/block/recipe/language/etc. JSON files) are:

- **1.20 series:** `1.20`, `1.20.2`, `1.20.3`, `1.20.5`
- **1.21 series:** `1.21.1`, `1.21.3`, `1.21.4`, `1.21.5`, `1.21.6`, `1.21.8`, `1.21.9`, `1.21.11`

**Stub-only versions** (e.g. `1.20.1`, `1.20.4`, `1.20.6`, `1.21`) are still accessible via `get_data_path()` but only expose `version.json`. If you need full gameplay data for one of those versions, use the nearest preceding full-data version from the list above.

## Data Source

This library provides Python access to the [PrismarineJS minecraft-data](https://github.com/PrismarineJS/minecraft-data) project, which contains comprehensive Minecraft game data in JSON format.

## Configuration

### Custom cache location

Set the `MINECRAFT_DATA_DIR` environment variable to use a custom cache directory:

```bash
export MINECRAFT_DATA_DIR=/custom/path/to/minecraft/data
python your_script.py
```

## Development

### Run tests

```bash
make test
```

### Run linting and formatting

```bash
make check      # Format, lint, and test
make format     # Black formatting
make lint       # Flake8 linting
```

### Coverage

```bash
make coverage           # Terminal report
make coverage-html      # HTML report
```

## License

MIT — See [LICENSE](LICENSE) for details.

## Attribution

- **Original author**: [Vito Gamberini](https://github.com/rom1504)
- **Game data source**: [PrismarineJS minecraft-data](https://github.com/PrismarineJS/minecraft-data)
- **Maintained fork**: [Reuben Brasher](https://github.com/Rkbrasher)
