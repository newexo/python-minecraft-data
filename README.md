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
- `1.20.6`
- `1.21.6`

Other versions in the [minecraft-data](https://github.com/PrismarineJS/minecraft-data) repository are accessible but may have incomplete data.

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
