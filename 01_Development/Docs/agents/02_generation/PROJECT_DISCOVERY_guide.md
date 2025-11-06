# 🎯 Guía: Project Discovery Prompt

## ¿Qué es esto?

Un **asistente conversacional inteligente** que te ayuda a transformar una idea vaga en un proyecto bien definido con documentación completa.

**Perfecto para cuando**:
- ❓ Tienes una idea pero no sabes por dónde empezar
- ❓ No estás seguro qué tecnologías usar
- ❓ Necesitas ayuda definiendo el alcance
- ❓ Quieres documentación profesional desde el inicio

---

## 🚀 Cómo Usar (3 Pasos)

### Paso 1: Prepara tu Idea (30 segundos)

Escribe tu idea en 1-3 frases. Puede ser MUY vaga:

**Ejemplos válidos:**
- ✅ "Quiero una API que muestre stats de Pokémon"
- ✅ "Necesito un dashboard para visualizar datos de ventas"
- ✅ "App para tracking de hábitos diarios"
- ✅ "Sistema de autenticación para mis proyectos"
- ✅ "Bot de Telegram que resume artículos"

**No necesitas saber:**
- ❌ Qué tecnologías usar
- ❌ Cómo estructurar el proyecto
- ❌ Requisitos técnicos detallados
- ❌ Arquitectura o diseño

---

### Paso 2: Inicia la Conversación

1. **Abre Claude o ChatGPT** (conversación nueva)

2. **Copia el prompt completo**:
   - Archivo: `PROJECT_DISCOVERY_prompt.md`
   - Copia TODO el contenido

3. **Adjunta los templates**:
   - `copilot-instructions_template_V02.md`
   - `00_OBJECTIVE_template_v2.md`

4. **Agrega tu idea** al final del prompt:
   ```
   [Pega el prompt completo aquí]
   
   ---
   
   MY PROJECT IDEA:
   [Tu idea aquí]
   
   Help me define my project!
   ```

5. **Envía**

---

### Paso 3: Responde las Preguntas (30-45 min)

El AI te hará preguntas en **5 grupos**:

#### Grupo 1: Alcance y Propósito (5 min)
```
- ¿Es para aprender o producción?
- ¿Quién lo usará?
- ¿Qué problema resuelve?
- ¿Qué es MVP vs futuro?
```

**Tip**: Sé honesto. "Es para aprender" es válido.

#### Grupo 2: Contexto Técnico (5 min)
```
- ¿Qué lenguajes conoces?
- ¿Experiencia con deployment?
- ¿Cuánto tiempo tienes?
- ¿Presupuesto?
```

**Tip**: Tu nivel de experiencia importa para las recomendaciones.

#### Grupo 3: Stack Técnico (10 min)
```
El AI propone:
- Frontend options
- Backend options
- Database options
- Deployment options

Tú apruebas o pides cambios
```

**Tip**: El AI explicará pros/cons. Haz preguntas si no entiendes.

#### Grupo 4: Detalles de Implementación (10 min)
```
- Nombre del proyecto
- Code quality standards
- Testing approach
- Git workflow
- Performance targets
```

**Tip**: Puedes decir "no sé" y el AI sugerirá defaults.

#### Grupo 5: Criterios de Éxito (10 min)
```
- ¿Cuándo está "terminado"?
- ¿Qué es calidad aceptable?
- Timeline realista
- Métricas de éxito
```

**Tip**: Sé realista con los tiempos.

---

## 📄 Resultado Final

Después de responder todo, recibes:

### 1. copilot-instructions.md
- ✅ Configurado para TU stack específico
- ✅ Comandos reales para TUS herramientas
- ✅ Standards adaptados a TU nivel
- ✅ ~270 líneas listas para usar

### 2. 00_OBJECTIVE.md
- ✅ Tu proyecto claramente definido
- ✅ Scope con fases (MVP, v2, v3)
- ✅ Success criteria medibles
- ✅ ~265 líneas profesionales

**Total tiempo**: 45-60 minutos  
**Valor**: Claridad completa + docs production-ready

---

## 💡 Ejemplo Real Completo

### Input Inicial:
```
"Quiero una API que se conecte a https://pokeapi.co/ 
y muestre stats de Pokémon en una web cuando busco por nombre"
```

### Conversación (Resumida):

**AI**: Great! I understand you want a Pokémon stats viewer. Let me ask about scope...

**Usuario**: Es para aprender FastAPI, solo yo lo usaré, quiero terminarlo en 2 semanas.

**AI**: Perfect! For learning FastAPI with 2-week timeline, I recommend:
- Backend: FastAPI + Python 3.11
- Frontend: Simple HTML + Tailwind (or React if you want to learn)
- Database: Not needed (PokeAPI is the data source)
- Deployment: Vercel or Railway (free tier)

**Usuario**: Perfecto, vamos con HTML + Tailwind. No quiero complicarme.

**AI**: Excellent choice! Now let me ask about development standards...

[... más preguntas...]

**AI**: Here's your complete project proposal... [muestra resumen]

**Usuario**: Aprobado!

**AI**: Great! Generating your documentation...

[Genera copilot-instructions.md]
[Genera 00_OBJECTIVE.md]

**AI**: ✅ Done! Here are your files ready to copy to your project.

---

## 🎯 Tips para Mejores Resultados

### ✅ DO (Hacer):

1. **Sé específico en tu experiencia**
   - ❌ "Sé programar"
   - ✅ "2 años Python, básico FastAPI, nunca deployé nada"

2. **Menciona limitaciones reales**
   - ✅ "Solo tengo 5 horas/semana"
   - ✅ "Budget $0 (free tier only)"
   - ✅ "Necesito entregarlo en 1 mes"

3. **Haz preguntas si no entiendes**
   - ✅ "¿Qué es 'horizontal scaling'?"
   - ✅ "¿Por qué recomiendas PostgreSQL vs MySQL?"

4. **Comparte el contexto real**
   - ✅ "Es para mi portfolio de trabajo"
   - ✅ "Quiero aprender React"
   - ✅ "Necesito algo que funcione, no perfecto"

### ❌ DON'T (Evitar):

1. **No digas "lo que sea"**
   - El AI necesita tu input para personalizar

2. **No inventes experiencia que no tienes**
   - Las recomendaciones serán incorrectas

3. **No saltes preguntas**
   - Cada pregunta ayuda a definir mejor el proyecto

4. **No tengas miedo de ser "básico"**
   - Está bien decir "soy principiante" o "proyecto simple"

---

## 🔄 Variaciones del Prompt

### Para Proyectos Empresariales:
Agrega al inicio:
```
CONTEXT: This is for a corporate environment with:
- Team of X developers
- Compliance requirements (GDPR, SOC2, etc.)
- Existing infrastructure on [AWS/GCP/Azure]
- Budget of $X/month
```

### Para Proyectos de Aprendizaje:
Agrega al inicio:
```
CONTEXT: Learning project where I want to:
- Learn [Technology X]
- Build portfolio piece
- Don't need production-grade (learning > perfection)
```

### Para MVPs Rápidos:
Agrega al inicio:
```
CONTEXT: Need to ship FAST:
- Hard deadline: [date]
- Minimum viable features only
- Technical debt acceptable if it ships on time
```

---

## 📊 Comparación: Con vs Sin Discovery

### Sin Discovery (Tradicional):
```
1. Empiezas a codear ❌
2. Te das cuenta que necesitas X
3. Refactorizas todo
4. Cambias de tech stack
5. Reincias desde cero
6. Abandonas el proyecto

Tiempo perdido: Semanas o meses
```

### Con Discovery:
```
1. 45 minutos de discovery ✅
2. Docs claros desde día 1
3. Stack correcto elegido
4. Scope bien definido
5. Desarrollo lineal
6. Proyecto terminado

Tiempo invertido: 45 min
Tiempo ahorrado: Semanas
```

---

## 🎓 Qué Aprenderás del Proceso

Además de los docs, este proceso te enseña:

- ✅ Cómo pensar en arquitectura de software
- ✅ Cómo evaluar trade-offs técnicos
- ✅ Cómo definir scope realista
- ✅ Cómo elegir tech stack apropiado
- ✅ Cómo establecer criterios de éxito

**Es educativo por diseño** - no solo genera docs, te guía en el pensamiento técnico.

---

## ✅ Checklist Pre-Discovery

Antes de empezar, ten claro:
- [ ] Tu idea en 1-3 frases (puede ser vaga)
- [ ] Cuánto tiempo tienes disponible
- [ ] Tu nivel técnico honesto
- [ ] Propósito (aprender/portfolio/producción)
- [ ] Deadline si existe
- [ ] Presupuesto (free tier / can pay)

**No necesitas tener claro**:
- [ ] Tecnologías específicas
- [ ] Arquitectura
- [ ] Requisitos detallados
- [ ] Todo está permitido ser vago ✅

---

## 🚀 Start Now

1. **Copia**: `PROJECT_DISCOVERY_prompt.md`
2. **Adjunta**: Templates (copilot + objective)
3. **Agrega**: Tu idea
4. **Envía**: Al AI
5. **Responde**: Preguntas honestas
6. **Recibe**: Docs completos

**Tiempo total**: ~1 hora  
**Resultado**: Proyecto bien definido + docs profesionales

---

## 💬 Preguntas Frecuentes

### "¿Y si no sé qué tecnología usar?"
✅ Perfecto! Ese es exactamente el caso de uso. El AI preguntará tu contexto y recomendará.

### "¿Y si mi idea es muy básica?"
✅ No hay ideas "muy básicas". Todo proyecto merece buena documentación.

### "¿Y si cambio de opinión a mitad de proceso?"
✅ Puedes pedir al AI que ajuste las recomendaciones en cualquier momento.

### "¿Necesito experiencia técnica avanzada?"
❌ No! El proceso se adapta a tu nivel, desde principiante hasta experto.

### "¿Cuánto dura la conversación?"
⏱️ 45-60 minutos típicamente. Más si es proyecto complejo, menos si es simple.

### "¿Puedo usar esto para proyectos ya empezados?"
✅ Sí! Di "tengo un proyecto existente" y el AI adaptará las preguntas.

---

## 📚 Recursos Relacionados

**Después del Discovery**:
1. Usa `AGENT_GENERATION_prompt.md` para generar arquitectura
2. Lee `USAGE_GUIDE.md` para usar los docs generados
3. Ve `EXAMPLE_*.md` para ver ejemplos completos

**Si te atascas**:
1. `QUICK_REFERENCE.md` - Referencia rápida
2. `INDEX.md` - Navegación completa
3. `README.md` - Overview del sistema

---

## 🎉 Testimoniales Imaginarios

> "Tenía una idea vaga de una API. En 1 hora tenía proyecto definido + docs completos. Increíble!" - Developer A

> "El AI me hizo preguntas que ni yo me había hecho. Evitó que eligiera tech stack equivocado." - Developer B

> "Como PM, uso esto para definir proyectos con el equipo. Todos alineados desde día 1." - Product Manager C

---

**¿Listo para definir tu proyecto?**

Abre `PROJECT_DISCOVERY_prompt.md` y empieza tu conversación! 🚀
