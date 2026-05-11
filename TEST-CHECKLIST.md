# 🧪 Sunrise Intelligence — Test Checklist

## INSTRUCCIONES
Abre `sunrise-intelligence.html` en navegador y sigue estos tests:

---

## ✅ CORE NAVIGATION

- [ ] **Sidebar visible** — Logo "☀ Sunrise Intelligence" en esquina superior izquierda
- [ ] **Botones de nav** — "📊 Dashboard" (activo) y "⚙ Admin" (gris)
- [ ] **Clientes listados** — Ves "📊 Todos los clientes" + 11 clientes individuales
- [ ] **Cliente seleccionado** — Background oscuro en cliente activo, inversión visible ($)

---

## 📊 DASHBOARD VIEW

### Vista: Todos los clientes
- [ ] **Topbar title** — Dice "Resumen global — todos los clientes"
- [ ] **Badges** — "⬡ LIVE · Windsor.ai" + "últimos 30 días"
- [ ] **Tabs visible** — Dashboard (activo), Mappings, Conexiones, Objetivos KPI
- [ ] **KPI cards** — Inversión total, ROAS global, CPA promedio, Leads/Ventas totales
- [ ] **Chart: Inversión por canal** — Barras Meta vs Google
- [ ] **Chart: Conversiones por cliente** — Líneas con leyenda
- [ ] **Chart: Distribución de spend** — Pie chart con 11 colores

### Vista: Cliente individual (ej. MrClick)
- [ ] **Topbar title** — Dice "MrClick Chile"
- [ ] **Cliente highlight** — Sidebar muestra MrClick seleccionado (borde naranja)
- [ ] **KPI cards** — Spend MrClick ($1.5K), Revenue ($3.2K), ROAS (2.1x), conversiones (45)
- [ ] **Campañas** — Tabla con campañas de MrClick, conversiones, status (OK/warning)
- [ ] **Charts actualizan** — Gráficos muestran solo datos de MrClick

---

## ⚙️ ADMIN VIEW

### Tab: Mappings
- [ ] **Selecciona cliente** — Ej. Skinology
- [ ] **Área de mapeos visible** — Sección gris con label "Mapeos de campañas"
- [ ] **Input text area** — Puedes escribir JSON como `{"campaign_orig": "campaign_mapped"}`
- [ ] **Botón Guardar** — Click guarda (actualmente sin persistencia, pero no da error)

### Tab: Conexiones
- [ ] **Estado Meta** — "✓ activo" (verde) o "⚠ revisar" (amarillo)
- [ ] **Estado Google** — "✓ activo" o "✕ off"
- [ ] **Estado GA4** — Muestra status
- [ ] **Estado Shopify** — Muestra status (si aplica)

### Tab: Objetivos KPI
- [ ] **Selecciona cliente** — Ej. Constructora Nahmias
- [ ] **Métrica dropdown** — Puedes elegir: Inversión, ROAS, CPA, Leads, etc
- [ ] **Valor objetivo** — Input para setear meta mensual (ej. "2.5x ROAS")
- [ ] **Tabla KPIs actual** — Muestra KPIs activos del cliente

---

## 🤖 IA FEATURES

- [ ] **Botón "Interpretá esto"** — Visible en topbar (naranja)
- [ ] **Click IA** — Botón se deshabilita (loading...), luego se activa de nuevo
- [ ] **Respuesta IA** — Aparece análisis contextual (ej. "MrClick está en $1.5K, recomendación es...")
- [ ] **Context** — La IA menciona cliente, período, competencia, KPIs (= funciona bien)

---

## ⬇️ EXPORT

- [ ] **Botón PPTX** — Visible en topbar (naranja)
- [ ] **Click PPTX** — Muestra alert "PPTX en construcción" (placeholder OK, no error)

---

## 🎨 UI/UX

- [ ] **Sidebar colors** — Dark (#111) con accent naranja (#F97316)
- [ ] **Main content** — Light background (#fff)
- [ ] **Hover states** — Buttons tienen hover (background change)
- [ ] **Active states** — Cliente/tab activo tiene borde/background distinct
- [ ] **Scroll** — Content scrolls si hay muchos clientes/datos
- [ ] **Responsive** — Redimensiona ventana, layout se adapta (no se rompe)

---

## 🐛 EDGE CASES

- [ ] **Sin cliente seleccionado** — Vista por defecto es "Todos"
- [ ] **Switch clientes rápido** — No hay memory leaks, charts destruyen bien
- [ ] **Console clean** — Abre DevTools → Console, no hay errores rojo
- [ ] **Campos en Admin** — Input fields permiten texto sin limpieza de HTML

---

## 📈 CHARTS ESPECÍFICAS

- [ ] **Chart 1: Inversión por canal** — Barras Meta (naranja) vs Google (azul)
- [ ] **Chart 2: Conversiones por cliente** — Línea con tooltip
- [ ] **Chart 3: Distribución spend (pie)** — Colores varían por cliente
- [ ] **Chart 4: Performance histórico** — Línea mostrando trend
- [ ] **Chart 5: Scatter ROI vs Spend** — Puntos dispersados
- [ ] **Chart 6: Heatmap de campañas** — Tabla coloreada por performance

---

## 🔐 SECURITY

- [ ] **Datos locales** — No se envían a internet (son mock)
- [ ] **Console sin tokens** — No ves API keys ni credenciales en código
- [ ] **Inputs sanitized** — Escribir `<script>alert(1)</script>` en mapping no ejecuta

---

## ✅ PERFORMANCE

- [ ] **Carga inicial** — < 2 seg
- [ ] **Switch cliente** — < 500ms (sin lag)
- [ ] **Resize ventana** — Suave, no parpadea
- [ ] **Charts rendering** — Animación suave de líneas/barras

---

## 📋 SUMMARY

### Si todo está ✓
**Status: 🟢 LISTO PARA PRODUCCIÓN**
- Plataforma funciona bien
- Datos mock muestran estructura correcta
- UI/UX limpia y responsive
- Próximo paso: conectar Windsor.ai real

### Si falta algo ✗
Documenta cuál fail y reporta:
- Qué test falló
- Qué esperabas vs qué pasó
- Screenshot / console error
- Reproduce step-by-step

---

**Tiempo estimado de test completo:** 10-15 min  
**Navegador recomendado:** Chrome/Safari (no IE)  
**Resolve issues con:** DevTools (Cmd+Option+I)

¡Buena suerte! 🚀
