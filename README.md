# 🌅 Sunrise Intelligence Pro — Dashboard Transversal

Dashboard inteligente para gestionar todos tus clientes de agencia digital con integración **REAL** a Windsor.ai.

## 📋 Instalación & Deploy

### Paso 1: Descargar el archivo

Descarga `sunrise-intelligence-pro-v2.html` de outputs.

### Paso 2: Meterlo en tu carpeta

```bash
cp sunrise-intelligence-pro-v2.html ~/Documents/Apps/sunrise-intelligence/index.html
```

### Paso 3: Git commit & push

```bash
cd ~/Documents/Apps/sunrise-intelligence

git add index.html
git commit -m "feat: Update dashboard with real Windsor.ai integration"
git push origin main
```

### Paso 4: Verificar en línea

Abre: `https://almelnick.github.io/sunrise-intelligence/`

O localmente:
```bash
python3 -m http.server 8000
# Luego: http://localhost:8000/
```

---

## 🎯 Cómo usar el Dashboard

### 1️⃣ Seleccionar cliente

Dropdown en la esquina superior izquierda. Ej: "Paimun Vida Natural"

### 2️⃣ Vincular cuentas Windsor

- Click **"⚙ Admin"** → Tab **"Perfil"**
- Sección **"🔗 Vincular Cuentas"**
- Selecciona:
  - **META ADS:** ej "CP - Mr Click Chile"
  - **GOOGLE ADS:** ej "PAIMUN"
  - **GA4:** ej "Mr Click Chile - GA4"
  - (WooCommerce solo para ecommerce)

Cada selección se guarda automáticamente.

### 3️⃣ Habilitar extracción

- Checkbox: **"Extraer datos de este cliente"** ✅
- Selecciona qué métricas quieres traer (checkboxes)
- Core (siempre): Spend, Conversions, Sessions

### 4️⃣ Sincronizar con Windsor

- Button: **"🔄 Sincronizar con Windsor"**
- Espera a que diga "✓ Sincronizado"
- Los datos se guardan en localStorage

### 5️⃣ Ver datos en Dashboard

- Click **"📊 Dashboard"**
- Tab **"Overview"**
- Ves los KPIs con datos reales de las últimas 24 horas

---

## 📊 Qué trae cada fuente

### Meta Ads
- ✅ Spend (inversión)
- ✅ Conversions (conversiones)
- ✅ Revenue (ingresos, si ecommerce)
- ⚙️ CTR, CPC, Reach, Engagement (opcionales)

### Google Ads
- ✅ Spend (inversión)
- ✅ Conversions (conversiones)
- ⚙️ CTR, CPC, Impressions (opcionales)

### GA4
- ✅ Sessions (sesiones)
- ✅ Conversion Rate (tasa de conversión)
- ⚙️ Users, Bounce Rate (opcionales)

### WooCommerce (ecommerce only)
- ✅ Orders (órdenes)
- ✅ Revenue (ingresos)
- ✅ AOV (valor promedio de orden)
- ⚙️ Top Products, Repeat Rate (opcionales)

---

## 🔐 Almacenamiento

Todo se guarda en **localStorage** del navegador:
- Configuración de clientes
- Cuentas vinculadas
- Datos extraídos
- Métricas seleccionadas

**No se sube a servidores.** Todo es local.

---

## 🚀 Features en desarrollo

- ✅ Vincular cuentas Windsor
- ✅ Sincronizar datos en tiempo real
- ⏳ Exportar a PPTX
- ⏳ Dashboards por rol (CMO, Media Planner, etc)
- ⏳ Alertas inteligentes
- ⏳ Recomendaciones AI

---

## 🐛 Troubleshooting

### "Account no disponible" al sincronizar

→ Verifica que la cuenta esté vinculada en Windsor.ai
→ Recarga el dashboard y vuelve a intentar

### Los datos no se guardan

→ Abre DevTools (F12) → Application → Local Storage
→ Verifica que `sunrise_profiles` esté en la lista

### Error de CORS al abrir local

→ Usa servidor local: `python3 -m http.server 8000`
→ No abras con `file://` directamente

---

## 📞 Contacto

Alan Melnick
Sunrise Latam
alan@sunriselatam.com

---

**Última actualización:** Mayo 2026
**Versión:** 2.0 (Windsor.ai Integration)
