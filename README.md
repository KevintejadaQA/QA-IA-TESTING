# QA-IA-TESTING
My proyect QA
# 🤖 QA Automation Framework + API Testing

Proyecto de automatización de pruebas enfocado en validación de APIs REST y generación dinámica de casos de prueba.

---

## 🧠 Descripción

Este proyecto simula un flujo real de QA Automation donde los casos de prueba son generados dinámicamente y ejecutados contra una API pública.

El objetivo es demostrar habilidades en:

* Automatización de pruebas API
* Diseño de frameworks de testing escalables
* Uso de Pytest como motor de ejecución
* Validación de respuestas HTTP

---

## ⚙️ Tecnologías utilizadas

* Python
* Pytest
* Requests
* JSON para manejo de datos de test

---

## 🚀 ¿Qué hace este proyecto?

1. Genera casos de prueba automáticamente en formato JSON
2. Ejecuta pruebas contra una API REST pública
3. Valida códigos de estado HTTP esperados
4. Reporta resultados mediante Pytest

---

## 📂 Estructura del proyecto

```
qa-ai-testing/
│
├── ai/
│   └── test_generator.py        # Generador de casos de prueba
│
├── tests/
│   └── test_api.py              # Ejecución de tests con Pytest
│
├── data/
│   └── generated_tests.json     # Casos generados dinámicamente
│
├── requirements.txt
└── README.md
```

---

## ▶️ Cómo ejecutar el proyecto

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

### 2. Generar casos de prueba

```bash
python ai/test_generator.py
```

---

### 3. Ejecutar tests

```bash
pytest -v
```

---

## 🧪 Casos de prueba cubiertos

* Validación de endpoints válidos
* Manejo de endpoints inválidos
* Verificación de códigos HTTP esperados

---

## 💡 Valor del proyecto

Este proyecto demuestra la capacidad de:

* Diseñar automatización desde cero
* Trabajar con APIs REST
* Estructurar tests mantenibles
* Separar generación de datos y ejecución de tests

---

## 📈 Posibles mejoras

* Integración con CI/CD (GitHub Actions)
* Reportes HTML de ejecución
* Extensión a testing de UI con Playwright
* Validaciones de schema de respuestas

---

## 📫 Contacto

📧 [kevinitadacampos@gmail.com](mailto:kevinitadacampos@gmail.com)

💼 LinkedIn: https://www.linkedin.com/in/kevin-tejada-campos/

---

⭐ Proyecto desarrollado como parte de mi evolución en QA Automation Engineer
