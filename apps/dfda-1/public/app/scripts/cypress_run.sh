#!/bin/bash
set +x
set -e
PARENT_SCRIPT_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/$(basename "${BASH_SOURCE[0]}")" && SCRIPT_FOLDER=$(dirname "${PARENT_SCRIPT_PATH}")
# shellcheck source=./log_start.sh
cd "${SCRIPT_FOLDER}" && cd .. && export IONIC_PATH="$PWD" && source "$IONIC_PATH"/scripts/log_start.sh "${BASH_SOURCE[0]}"
npm run cy:run
if [[ ! -f success-file ]]; then
  echo 'success-file is not there, aborting.'
  exit 1
else
  echo "success-file exists so running ghostinspector tests..."
fi
# shellcheck source=./log_end.sh
source "$IONIC_PATH"/scripts/log_end.sh "${BASH_SOURCE[0]}"
