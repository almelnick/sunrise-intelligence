# 🌅 Sunrise Intelligence — Python Backend Setup

Backend Flask que actúa como proxy de Windsor.ai (soluciona CORS).

## 📦 Instalación

### 1. Instalar dependencias

```bash
pip install flask flask-cors requests python-dotenv --break-system-packages
```

### 2. Configurar API key

**Opción A: Variable de entorno**
```bash
export WINDSOR_API_KEY="sk-tu_api_key_aqui"
python3 server.py
```

**Opción B: Crear `.env` en la carpeta**
```bash
# .env
WINDSOR_API_KEY=sk-tu_api_key_aqui
```

Luego:
```bash
python3 server.py
```

## 🚀 Correr el servidor

```bash
cd ~/Documents/Apps/sunrise-intelligence

python3 server.py
```

Debería ver:
```
🌅 Sunrise Intelligence — Windsor.ai Proxy Backend
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Running on http://localhost:5000
✓ Windsor API Key configured: True
```

## 🔗 Endpoints disponibles

### Health check
```
GET http://localhost:5000/api/health
```

Respuesta:
```json
{
  "status": "ok",
  "windsor_configured": true
}
```

### Traer datos de Windsor
```
GET http://localhost:5000/api/windsor/data?connector=google_ads&account_id=771-109-1192&fields=spend,conversions&date_preset=last_30d
```

### Listar conectores
```
GET http://localhost:5000/api/windsor/connectors
```

## 🎯 Cómo funciona

1. **Dashboard HTML** hace fetch a `localhost:5000`
2. **Backend Python** recibe la solicitud
3. **Backend** llama a Windsor.ai API (con API key segura)
4. **Backend** retorna datos al HTML
5. **HTML** muestra datos en dashboard

La API key **NUNCA** sale del servidor backend.

## ⚙️ Correr en background

Si quieres que corra permanentemente:

```bash
# En una terminal separada
nohup python3 server.py > server.log 2>&1 &
```

O con `tmux`:
```bash
tmux new-session -d -s windsor "python3 server.py"
```

## 🐛 Troubleshooting

### "Connection refused" en dashboard
→ Verifica que `python3 server.py` está corriendo

### "Windsor API key not configured"
→ Falta la variable de entorno `WINDSOR_API_KEY`
→ Corre: `export WINDSOR_API_KEY="sk-..."`

### CORS errors todavía
→ Reinicia el servidor backend
→ Limpia cache del navegador (Cmd+Shift+R en Mac)

## 📝 Notas

- El backend corre en `localhost:5000` (local only)
- El HTML en `localhost:8000` (local only)
- No subas `server.py` a GitHub si tiene la API key hardcodeada
- Usa `.env` para credenciales locales

