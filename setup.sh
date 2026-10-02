#!/usr/bin/env bash
# Instalación del skill /static-ads para elvo·. Correr desde esta carpeta: bash setup.sh
set -e
cd "$(dirname "$0")"

echo "→ Instalando dependencias de Python"
python3 -m pip install -r .claude/skills/static-ads/scripts/requirements.txt 2>/dev/null \
  || python3 -m pip install --user -r .claude/skills/static-ads/scripts/requirements.txt \
  || python3 -m pip install --break-system-packages -r .claude/skills/static-ads/scripts/requirements.txt

if [ ! -f .env ]; then
  cp .env.example .env
  echo "→ Creé .env. Ábrelo y pega tu FAL_KEY (https://fal.ai/dashboard/keys)."
fi

python3 - << 'PY'
import importlib, os
for m in ["fal_client", "PIL", "requests"]:
    importlib.import_module(m)
print("✓ Dependencias OK")
key = ""
if os.path.exists(".env"):
    for l in open(".env"):
        if l.startswith("FAL_KEY="):
            key = l.split("=", 1)[1].strip()
print("✓ FAL_KEY configurada" if key else "✗ Falta FAL_KEY en .env")
PY

echo "Listo. Abre Claude Code en esta carpeta (comando: claude) y escribe /static-ads"
