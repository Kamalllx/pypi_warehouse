# PyPI Warehouse 🏭

A collection of lightweight, focused Python utility packages that solve real-world development problems.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## 📦 Packages

| Package | Description | Install | PyPI |
|---------|-------------|---------|------|
| [**envmaster**](./packages/envmaster) | Type-safe environment variable management | `pip install envmaster` | [![PyPI](https://img.shields.io/pypi/v/envmaster)](https://pypi.org/project/envmaster/) |
| [**pylogfmt-rj**](./packages/pylogfmt-rj) | Beautiful, structured console logging | `pip install pylogfmt-rj` | [![PyPI](https://img.shields.io/pypi/v/pylogfmt-rj)](https://pypi.org/project/pylogfmt-rj/) |
| [**pycachely-rj**](./packages/pycachely-rj) | Simple in-memory caching with TTL support | `pip install pycachely-rj` | [![PyPI](https://img.shields.io/pypi/v/pycachely-rj)](https://pypi.org/project/pycachely-rj/) |
| [**pyretryit-rj**](./packages/pyretryit-rj) | Smart retry decorator with exponential backoff | `pip install pyretryit-rj` | [![PyPI](https://img.shields.io/pypi/v/pyretryit-rj)](https://pypi.org/project/pyretryit-rj/) |
| [**pyvaliddict-rj**](./packages/pyvaliddict-rj) | Dictionary schema validation | `pip install pyvaliddict-rj` | [![PyPI](https://img.shields.io/pypi/v/pyvaliddict-rj)](https://pypi.org/project/pyvaliddict-rj/) |
| [**pytimefunc-rj**](./packages/pytimefunc-rj) | Function execution timing utilities | `pip install pytimefunc-rj` | [![PyPI](https://img.shields.io/pypi/v/pytimefunc-rj)](https://pypi.org/project/pytimefunc-rj/) |
| [**pycliprog-rj**](./packages/pycliprog-rj) | Lightweight CLI progress bars | `pip install pycliprog-rj` | [![PyPI](https://img.shields.io/pypi/v/pycliprog-rj)](https://pypi.org/project/pycliprog-rj/) |
| [**pyprojectcheck-rj**](./packages/pyprojectcheck-rj) | Validate pyproject.toml files | `pip install pyprojectcheck-rj` | [![PyPI](https://img.shields.io/pypi/v/pyprojectcheck-rj)](https://pypi.org/project/pyprojectcheck-rj/) |

## 🚀 Quick Start

```bash
# Install any package
pip install envmaster pyretryit-rj pycachely-rj

# Or install all packages
pip install envmaster pylogfmt-rj pycachely-rj pyretryit-rj pyvaliddict-rj pytimefunc-rj pycliprog-rj pyprojectcheck-rj
```

## 📖 Package Highlights

### pyretryit-rj - Smart Retries
```python
from retryit import retry

@retry(max_attempts=3, delay=1, backoff=2)
def fetch_data():
    # Automatically retries on failure
    return requests.get("https://api.example.com/data")
```

### envmaster - Environment Variables Made Easy
```python
from envmaster import env

DATABASE_URL = env.str("DATABASE_URL", required=True)
DEBUG = env.bool("DEBUG", default=False)
MAX_CONNECTIONS = env.int("MAX_CONNECTIONS", default=10)
```

### pycachely-rj - Simple Caching
```python
from cachely import cache

@cache(ttl=300)  # Cache for 5 minutes
def expensive_computation(x):
    return x ** 100
```

### pylogfmt-rj - Pretty Logging
```python
from logfmt import Logger

log = Logger("myapp")
log.info("Server started", port=8080)
log.error("Connection failed", host="db.example.com")
```

## 🛠️ Development

```bash
# Clone the repository
git clone https://github.com/RedJohnx/pypi_warehouse.git
cd pypi_warehouse

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## 📄 License

MIT License - see [LICENSE](./LICENSE) for details.