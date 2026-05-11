# ⚡ Sunrise Intelligence — Quick Start

## 🚀 EN 2 MINUTOS

### 1. Descarga & Abre
```bash
# El archivo ya está en outputs:
open /mnt/user-data/outputs/sunrise-intelligence.html
```

### 2. Navega
- **Lado izquierdo:** Selecciona cliente o "📊 Todos"
- **Arriba:** Elige Dashboard o Admin
- **Tabs:** Dashboard → Mappings → Conexiones → Objetivos KPI

### 3. Features
- 🤖 **"Interpretá esto"** → IA analiza tus datos (Claude API)
- ⬇️ **"PPTX"** → Genera reporte para enviar a cliente
- ⚙️ **Admin** → Configura nomenclaturas de campañas + objetivos KPI

---

## 🔧 CÓMO CONECTAR DATOS REALES

### Opción A: Windsor.ai (recomendado)
Ya tenés MCP de Windsor.ai. Edita el archivo y cambia:

```javascript
// Línea ~635: async function triggerIA()
// Remplaza los datos mock:

const clientData = await fetch('https://api.windsor.ai/v2/accounts', {
  headers: { 'Authorization': 'Bearer YOUR_WINDSOR_TOKEN' }
}).then(r => r.json());

// Luego mapea a CLIENTS[i].meta, CLIENTS[i].gads, etc.
```

### Opción B: n8n Webhook
Crea un n8n flow que:
1. Pulla datos de Meta/Google Ads cada hora
2. Envía a un endpoint tuyo
3. Actualiza un JSON que el HTML levanta

```javascript
// En renderDashboard():
const clientData = await fetch('https://tu-vercel.com/api/client/' + clientId)
  .then(r => r.json());
```

### Opción C: Supabase (si pasas a Next.js)
```javascript
import { supabase } from '@/lib/supabase'

const { data: clients } = await supabase
  .from('clients')
  .select('*')
  .eq('agency_id', 'sunrise_latam')
```

---

## 💾 IMPLEMENTAR PERSISTENCIA (LocalStorage)

Por ahora, las configs de Mappings y Objetivos KPI NO persisten. Para agregar:

```javascript
// En saveMap() y saveKPI():
function saveMap(input) {
  const cid = state.clientId;
  const mappings = JSON.parse(input.value || '{}');
  
  // ✅ Agregar esta línea:
  localStorage.setItem('mappings_' + cid, JSON.stringify(mappings));
  
  // ... resto del código
}

// Al cargar:
function renderMappings() {
  const stored = localStorage.getItem('mappings_' + state.clientId);
  const mappings = stored ? JSON.parse(stored) : {};
  // ... render con datos guardados
}
```

---

## 📤 EXPORT PPTX — Implementar

El botón de PPTX ahora muestra `alert()`. Para hacerlo real:

### Opción 1: PptxGenJS (cliente)
```html
<script src="https://cdn.jsdelivr.net/npm/pptxgenjs/dist/pptxgen.umd.js"></script>
```

```javascript
function exportPPTX() {
  const prs = new PptxGenJS();
  const c = getClient();
  
  // Slide 1: Portada
  prs.addSlide().addText(`${c.name} — Reporte de Performance`, {
    x: 0.5, y: 2.5, w: 9, h: 1, fontSize: 44, bold: true, color: 'F97316'
  });
  
  // Slide 2: KPIs
  const kpiSlide = prs.addSlide();
  kpiSlide.addText('KPIs Principales', { x: 0.5, y: 0.5, w: 9, h: 0.5, fontSize: 28, bold: true });
  
  // ... agregar charts, tablas, etc
  
  prs.save('Reporte_' + c.name + '.pptx');
}
```

### Opción 2: n8n (backend, recomendado)
Crea un webhook n8n que:
1. Recibe `{ clientId, period }`
2. Junta datos de Windsor.ai
3. Genera PPTX con `python-pptx` o similar
4. Retorna URL o archivo en base64

```javascript
// En el HTML:
async function exportPPTX() {
  const response = await fetch('https://tu-n8n.com/webhook/generate-pptx', {
    method: 'POST',
    body: JSON.stringify({
      clientId: state.clientId,
      period: '30d'
    })
  });
  
  const blob = await response.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `Reporte_${getClient().name}.pptx`;
  a.click();
}
```

---

## 🎯 CHECKLIST DE IMPLEMENTACIÓN

- [ ] **Día 1:** Abre el HTML, prueba navegación
- [ ] **Día 2:** Conecta datos reales (Windsor.ai o n8n)
- [ ] **Día 3:** Implementa export PPTX
- [ ] **Día 4:** Agrega persistencia (localStorage o Supabase)
- [ ] **Día 5:** Deploy a Vercel (versión Next.js)

---

## 🔗 ARCHIVOS

- `sunrise-intelligence.html` — Plataforma lista para usar
- `PLATFORM-REVIEW.md` — Documentación completa
- `QUICKSTART.md` — Este archivo

---

**Tips:**
- Para debuggear: abre DevTools (Cmd+Option+I) → Console
- Los datos actuales son mock — no edites CLIENTS manualmente, usa admin panel
- Cada cambio de cliente destroye charts viejos (memory cleanup)

¡Listo! 🚀
