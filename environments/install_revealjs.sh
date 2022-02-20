#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd "$(dirname "$0")"; pwd)
PROJECT_ROOT_DIR=$(dirname "${SCRIPT_DIR}")

SITE_PACKAGES_DIR=$(python -c 'import site; print(site.getsitepackages()[0])')
if [ -e "${SITE_PACKAGES_DIR}/sphinx_revealjs/themes/sphinx_revealjs/static/revealjs4" ]; then
  echo 'Reveal.js assets are already installed.'
  exit 0
fi

mkdir -p "${PROJECT_ROOT_DIR}/tools"
wget -O "${PROJECT_ROOT_DIR}/tools/fetch_revealjs.py" https://raw.githubusercontent.com/attakei/sphinx-revealjs/master/tools/fetch_revealjs.py
wget -O "${PROJECT_ROOT_DIR}/package-lock.json" https://raw.githubusercontent.com/attakei/sphinx-revealjs/master/package-lock.json

python "${PROJECT_ROOT_DIR}/tools/fetch_revealjs.py"
# fetch_revealjs.py creates ${PROJECT_ROOT_DIR}/sphinx_revealjs/themes/sphinx_revealjs/static/revealjs4/{dist,plugin,LICENSE}

mv "${PROJECT_ROOT_DIR}/sphinx_revealjs/themes/sphinx_revealjs/static/revealjs4" "${SITE_PACKAGES_DIR}/sphinx_revealjs/themes/sphinx_revealjs/static/"

rm -r "${PROJECT_ROOT_DIR}/"{package-lock.json,tools,var,sphinx_revealjs}
