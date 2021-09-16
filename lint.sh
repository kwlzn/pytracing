#!/usr/bin/env bash
set -euo pipefail
pre-commit run -v -a
flake8 . --config=setup.cfg
