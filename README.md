<div align="center">

```
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                            ▀▄
                              ▀▄
                                ▀
```

```
 ▄▄▄   ▄▄    ▄▄▄▄       ▄▄▄▄   ▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄
 ███   ██   ██▀▀██    ██▀▀▀▀█  ▀▀▀██▀▀▀  ██▀▀▀▀▀▀
 ██▀█  ██  ██    ██  ██▀          ██     ██
 ██ ██ ██  ██    ██  ██           ██     ███████
 ██  █▄██  ██    ██  ██▄          ██     ██
 ██   ███   ██▄▄██    ██▄▄▄▄█     ██     ██▄▄▄▄▄▄
 ▀▀   ▀▀▀    ▀▀▀▀       ▀▀▀▀      ▀▀     ▀▀▀▀▀▀▀▀
```

```
    ▄▄    ▄▄▄    ▄▄▄ ▄▄▄▄▄▄▄▄       ▄▄▄▄▄  ▄▄▄▄▄     ▄▄▄▄▄▄▄▄ ▄▄      ▄▄
   ████    ██▄  ▄██  ██▀▀▀▀▀▀       ▀▀▀██  ██▀▀▀██   ▀▀▀██▀▀▀ ██      ██
   ████     ██▄▄██   ██                ██  ██    ██     ██    ▀█▄ ██ ▄█▀
  ██  ██     ▀██▀    ███████           ██  ██    ██     ██     ██ ██ ██
  ██████      ██     ██                ██  ██    ██     ██     ███▀▀███
 ▄██  ██▄     ██     ██           █▄▄▄▄▄██  ██▄▄▄██      ██     ███  ███
 ▀▀    ▀▀     ▀▀     ▀▀            ▀▀▀▀▀    ▀▀▀▀▀        ▀▀     ▀▀▀  ▀▀▀
```

```
  ██████████████████████
                        ███
                           ███
                              ██
```

---

# TCP PORT SCANNER

[![Python](https://img.shields.io/badge/Python-3.x-1a1a1a?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Socket](https://img.shields.io/badge/lib-socket-2a2a2a?style=for-the-badge&logoColor=white)]()
[![Codespaces](https://img.shields.io/badge/env-codespaces-1a1a1a?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/codespaces)
[![Status](https://img.shields.io/badge/status-building-3a3a3a?style=for-the-badge)]()
[![License](https://img.shields.io/badge/license-MIT-2a2a2a?style=for-the-badge)]()

</div>

---

## ¿Qué es NOCTE?

> **NOCTE** es un escáner de puertos TCP construido desde cero en Python 3, usando únicamente la librería estándar `socket`. Desarrollado en **GitHub Codespaces** como proyecto de entrada a la ciberseguridad ofensiva y defensiva. Escanea puertos en cualquier host y determina cuáles están **abiertos**, **cerrados** o **filtrados**.

Cada línea de código fue escrita de forma incremental y con intención. Sin magia. Sin dependencias. Solo red, lógica y Python.

---

## Estructura del proyecto

```
tcp-port-scanner/
│
├── main.py              ← núcleo del scanner
├── README.md            ← este archivo
├── .gitignore           ← ignora venv y temporales
└── venv/                ← entorno virtual (no sube a git)
```

---

## Stack técnico

| Capa | Tecnología | Rol |
|------|-----------|-----|
| Lenguaje | `Python 3.x` | Core del scanner |
| Networking | `socket` stdlib | Conexiones TCP raw |
| Entorno | `GitHub Codespaces` | Laboratorio cloud |
| SO Base | `Ubuntu Linux` | Infraestructura |
| IDE | `VS Code Web` | Editor integrado |

---

## Instalación

```bash
# clonar
git clone https://github.com/TU_USUARIO/tcp-port-scanner.git
cd tcp-port-scanner

# entorno virtual
python3 -m venv venv
source venv/bin/activate

# ejecutar
python3 main.py
```

---

## Fundamentos teóricos

<details>
<summary><strong>¿Qué es un Socket TCP?</strong></summary>

Un **socket** es el punto final de una comunicación entre dos procesos en red. En TCP/IP queda definido por tres cosas: la dirección IP del host, el número de puerto (0–65535) y el protocolo. Sin sockets no hay red.

</details>

<details>
<summary><strong>TCP Three-Way Handshake</strong></summary>

Para saber si un puerto está abierto, NOCTE intenta iniciar una conexión TCP completa:

```
Scanner                    Target
   │                         │
   │──── SYN ───────────────►│   quiero conectar
   │                         │
   │◄─── SYN-ACK ────────────│   OK, acepto       ← PUERTO ABIERTO
   │  ó                      │
   │◄─── RST ────────────────│   rechazado        ← PUERTO CERRADO
   │  ó                      │
   │      (sin respuesta)    │                    ← PUERTO FILTRADO
```

</details>

<details>
<summary><strong>Interpretación de resultados</strong></summary>

| Estado | Significado | Señal TCP |
|--------|------------|-----------|
| `ABIERTO` | Servicio activo aceptando conexiones | SYN-ACK recibido |
| `CERRADO` | Puerto accesible pero sin servicio | RST recibido |
| `FILTRADO` | Firewall bloqueando el tráfico | Sin respuesta / timeout |

</details>

---

## Fases de desarrollo

```
[✅] FASE 1 — Configuración del entorno
[🔄] FASE 2 — Fundamentos de red (Sockets + TCP Handshake)
[⏳] FASE 3 — Código incremental
[⏳] FASE 4 — Análisis e interpretación de resultados
[⏳] FASE 5 — Refactor + CLI + output profesional
```

---

## Output objetivo

```
╔══════════════════════════════════════╗
║          NOCTE  v1.0                 ║
║          AYF  ·  JDTW               ║
╚══════════════════════════════════════╝

  target   →  scanme.nmap.org
  range    →  1 — 1024
  start    →  2025-01-01 00:00:00

  ──────────────────────────────────────
  [+]  22    OPEN     SSH
  [+]  80    OPEN     HTTP
  [-]  23    CLOSED
  [-]  443   CLOSED
  ──────────────────────────────────────

  2 open ports found
  duration: 4.32s
```

---

## Disclaimer

```
  uso ético y legal únicamente

  esta herramienta fue creada con fines educativos.
  solo úsala en sistemas que poseas o tengas
  permiso explícito para escanear.

  el uso no autorizado puede ser ilegal
  en tu jurisdicción.
```

---

<div align="center">

```
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                            ▀▄
                              ▀▄
                                ▀
```

**NOCTE** · built in codespaces · python 3
`AYF` · `JDTW`

</div>