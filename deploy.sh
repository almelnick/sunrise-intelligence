#!/bin/bash

# Script de deploy para Sunrise Intelligence Dashboard
# Uso: bash deploy.sh

set -e

REPO_PATH="$HOME/Documents/Apps/sunrise-intelligence"
FILE_URL="https://storage.googleapis.com/sunrise-intelligence/sunrise-intelligence-pro-v2.html"

echo "🌅 Sunrise Intelligence — Deploy Script"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# 1. Verificar que la carpeta existe
if [ ! -d "$REPO_PATH" ]; then
    echo "❌ Error: Carpeta no encontrada en $REPO_PATH"
    exit 1
fi

cd "$REPO_PATH"
echo "✓ Carpeta: $REPO_PATH"

# 2. Crear backup
echo "📦 Creando backup..."
if [ -f "index.html" ]; then
    cp index.html "index.html.backup.$(date +%s)"
    echo "✓ Backup creado"
fi

# 3. Descargar archivo (o copiar si ya lo tienes)
echo "📥 Descargando archivo..."
if [ -f "sunrise-intelligence-pro-v2.html" ]; then
    echo "✓ Archivo encontrado localmente"
else
    echo "⚠️  Descarga el archivo manualmente: sunrise-intelligence-pro-v2.html"
    echo "   Y colócalo en: $REPO_PATH/"
    exit 1
fi

# 4. Renombrar a index.html para servir
cp sunrise-intelligence-pro-v2.html index.html
echo "✓ Archivo actualizado: index.html"

# 5. Git commit
echo ""
echo "🔧 Git commit..."
git add index.html
git commit -m "feat: Update Sunrise Intelligence Dashboard with real Windsor.ai integration"
echo "✓ Commit realizado"

# 6. Git push
echo ""
echo "🚀 Git push..."
git push origin main
echo "✓ Push realizado"

# 7. Resumen
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Deploy completado!"
echo ""
echo "Próximos pasos:"
echo "1. Abre: https://almelnick.github.io/sunrise-intelligence/"
echo "2. O localmente: http://localhost:8000/"
echo "   (python3 -m http.server 8000)"
echo ""
echo "Para sincronizar con Windsor:"
echo "1. Selecciona cliente"
echo "2. Admin → Perfil"
echo "3. Vincula cuentas (Meta, Google, GA4)"
echo "4. Habilita 'Extraer datos'"
echo "5. Click 'Sincronizar con Windsor'"
echo ""
