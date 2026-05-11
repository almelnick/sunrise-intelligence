# 🚀 Deployment — Vercel + Railway

Guía completa para desplegar **Sunrise Intelligence** en producción.

## 📋 Resumen

- **Frontend:** Vercel (HTML/JS)
- **Backend:** Railway (Python/Flask)
- **Total:** ~10 minutos

## 1️⃣ Preparar carpeta para GitHub

```bash
cd ~/Documents/Apps/sunrise-intelligence

# Estructura final:
# sunrise-intelligence/
# ├── index.html                    (el dashboard)
# ├── config.json                   (NO se pushea)
# ├── server.py                     (backend)
# ├── requirements.txt              (dependencias Python)
# ├── Procfile                      (instrucciones Railway)
# ├── .gitignore                    (excluye config.json)
# ├── README.md
# └── BACKEND-SETUP.md
```

## 2️⃣ Actualizar `.gitignore`

```bash
cat >> .gitignore << 'EOF'
config.json
.env
.env.local
__pycache__/
*.pyc
*.log
venv/
EOF
```

## 3️⃣ Commit y push a GitHub

```bash
git add .
git commit -m "feat: Complete Sunrise Intelligence with Vercel + Railway deployment"
git push origin main
```

## 4️⃣ Deploy Backend en Railway

### A. Ir a https://railway.app

### B. Click "New Project" → "Deploy from GitHub"

### C. Seleccionar repo `almelnick/sunrise-intelligence`

### D. Esperar a que Railway clone y analice

### E. Agregar variable de entorno
- En Railway dashboard: "Variables"
- Agregar: `WINDSOR_API_KEY` = `sk-tu_api_key_aqui`

### F. Deploy automático
Railway auto-detecta `Procfile` y `requirements.txt`
- Verás URL como: `https://sunrise-intelligence-api.railway.app`
- Guarda esta URL (la necesitaremos)

## 5️⃣ Deploy Frontend en Vercel

### A. Ir a https://vercel.com

### B. Click "Add New..." → "Project"

### C. Conectar GitHub
- Si no está conectado: "Continue with GitHub"
- Autorizar Vercel

### D. Importar repo
- Buscar: `almelnick/sunrise-intelligence`
- Click "Import"

### E. Configuración
```
Framework: Other (Static)
Root Directory: ./
Build Command: (dejar en blanco)
Output Directory: (dejar en blanco)
```

### F. Deploy
- Click "Deploy"
- Esperar ~1 min
- Vercel te da URL: `https://sunrise-intelligence.vercel.app`

## 6️⃣ Actualizar HTML con URL de Railway

Antes de hacer push, actualiza el HTML:

En `sunrise-intelligence-pro-v3.html`, línea ~210:

```javascript
const backendUrl = window.location.hostname === 'localhost' 
  ? 'http://localhost:5000'
  : 'https://YOUR-RAILWAY-URL.railway.app'
```

Reemplaza `YOUR-RAILWAY-URL` con la URL que te dio Railway.

Luego:
```bash
git add index.html
git commit -m "feat: Update Railway backend URL"
git push origin main
```

Vercel auto-redeploya.

## 7️⃣ Verificar que funciona

### Test local:
```bash
# Terminal 1
export WINDSOR_API_KEY="sk-..."
python3 server.py

# Terminal 2
python3 -m http.server 8000
# http://localhost:8000
```

### Test producción:
- Abre: https://sunrise-intelligence.vercel.app
- Selecciona cliente
- Admin → Perfil
- Vincula cuenta (ej: PDPAOLA)
- Click "Sincronizar con Windsor"
- Debería traer datos reales

## 📝 URLs finales

```
Frontend:  https://sunrise-intelligence.vercel.app
Backend:   https://sunrise-intelligence-api.railway.app
API:       https://sunrise-intelligence-api.railway.app/api/windsor/data
Health:    https://sunrise-intelligence-api.railway.app/api/health
```

## 🔧 Troubleshooting

### "Connection refused" en Vercel
→ Verifica que `backendUrl` en HTML apunta a Railway URL correcta

### Backend en Railway no inicia
→ Chequea `WINDSOR_API_KEY` está configurada en Railway
→ Revisa logs: Railway Dashboard → "Deploy Logs"

### Datos no sincronizaban
→ Abre DevTools (F12) → Network
→ Mira si request a backend está yendo a la URL correcta
→ Checkea respuesta: debería ser JSON con datos

## 🚨 IMPORTANTE: config.json

**NO pongas config.json en GitHub.**

El `.gitignore` la excluye, pero:

### En local (desarrollo):
```json
{
  "windsor_api_key": "sk-..."
}
```

### En Railway (producción):
- API key va en **variable de entorno** `WINDSOR_API_KEY`
- Server.py la lee automáticamente

### En Vercel (frontend):
- **NO necesita** API key (todo pasa por Railway)

## 🎉 ¡Listo!

Frontend en Vercel ✅
Backend en Railway ✅
API key segura ✅
CORS solucionado ✅

**Que disfrutes tu Sunrise Intelligence en producción! ☀️**

