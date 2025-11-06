# Service Tutorials — Authoring Guide

Each service MUST provide a tutorial at `docs/services/{service_name}.md`.

## File Structure
- One service → one file.
- Use only Markdown with fenced code blocks.
- Keep each section concise and task-oriented.

## Required Sections
1. **Overview**  
   One or two lines, focused on the end result.

2. **Prerequisites**  
   - Required binaries (versions)  
   - Environment variables (with examples)  
   - Required files/paths

3. **Inputs**  
   A table with: `name | type | required | default | description`.

4. **Step-by-step**  
   Numbered list. Each step debe poder ejecutarse tal cual.  
   Proveer bloques de código para CLI, Make, Python, HTTP, etc.

5. **Example run**  
   Un caso completo: input realista → comando → salida esperada (recortada si es larga).

6. **Output**  
   Artifacts generados (rutas, formatos, tamaño aproximado, schema si aplica).

7. **Common errors**  
   Tabla: `symptom | cause | fix`.

> Nota: No incluir justificaciones de diseño aquí. Eso vive en `docs/agent/01_ARCHITECTURE.md`.