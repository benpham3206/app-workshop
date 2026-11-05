#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

required_files=(README.md GOAL.md STATUS.md ARCHITECTURE.md AGENTS.md SECURITY.md
  Makefile config/catalog.json config/schema/project.schema.json tooling/scaffold.py
  scripts/verify-repo.sh scripts/security-check.sh)

failed=0
open_braces='{'
open_braces="${open_braces}{"
project_token="${open_braces}PROJECT_NAME}}"
year_token="${open_braces}YEAR}}"

for path in "${required_files[@]}"; do
  if [[ ! -f "$path" ]]; then
    printf 'missing required file: %s\n' "$path" >&2
    failed=1
  fi
done

project_files() {
  if git -C "$root" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    git -C "$root" ls-files -z --cached --others --exclude-standard
  else
    find . \( -name .git -o -name node_modules -o -name .venv -o -name venv -o -name vendor \
      -o -name target -o -name dist -o -name build -o -name .next -o -name .turbo \
      -o -name .cache -o -name __pycache__ \) -prune -o -type f -print0
  fi
}

while IFS= read -r -d '' path; do
  case "${path#./}" in
    templates/*) continue ;;
  esac
  if grep -Fq -e "$project_token" -e "$year_token" "$path" 2>/dev/null; then
    printf 'unreplaced template token found: %s\n' "$path" >&2
    failed=1
  fi
done < <(project_files)

if ! bash scripts/security-check.sh; then
  failed=1
fi

if [[ "$failed" -ne 0 ]]; then
  exit 1
fi

printf 'repository contract: PASS\n'
