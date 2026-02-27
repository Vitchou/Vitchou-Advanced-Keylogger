# Vitchou : Advanced KeyLogger

```text
 ____   ____.__  __         .__                   
 \   \ /   /|__|/  |_  ____ |  |__   ____  __ __  
  \   Y   / |  \   __\/ ___\|  |  \ /  _ \|  |  \ 
   \     /  |  ||  | \  \___|   Y  \(  <_> )  |  /
    \___/   |__||__|  \___  >___|  / \____/|____/ 
                          \/     \/               

```

> **Cybersecurity Research Project**: A high-performance, asynchronous telemetry agent designed to demonstrate advanced data exfiltration and endpoint monitoring techniques.

---

## 🌟 Overview

**Vitchou APEX Ultra** is a resilient Python-based telemetry agent. Unlike standard scripts, it focuses on **operational security (OPSEC)**, data integrity through local persistence, and stealthy network communication.

## 🛠️ Core Technical Features

* **Asynchronous Engine**: Built on `asyncio` for non-blocking key-capture and network operations.
* **Hybrid Crypto Pipeline**:
* **Compression**: `zlib` (Level 9) to minimize data footprints.
* **Encryption**: Full **AES-256 (Fernet)** symmetric encryption for all exfiltrated data.


* **Persistent Buffering**: Integrated **SQLite WAL** (Write-Ahead Logging) database. If the target loses internet access, logs are stored locally and encrypted until a connection is restored.
* **Stealth Tactics**:
* **Idle Detection**: Data exfiltration only triggers after a period of user inactivity (default: 30s).
* **Randomized Jitter**: Uses random delays to break traffic patterns and bypass heuristic-based network monitors.
* **Anti-VM Protection**: Self-terminates if VirtualBox, VMware, or QEMU environment is detected.


* **Deep Contextual Logging**: Captures active window titles, timestamps, user sessions, and asynchronous clipboard events.

---

## 🚀 Installation & Usage

### 1. Requirements

```bash
pip install -r requirements.txt

```

### 2. Configuration

Update the `CONFIG` block in `VLogger.py`:

* `MASTER_KEY`: Your unique 32-byte encryption key.
* `REPORT_URL`: Your secure exfiltration endpoint.

### 3. Execution

```bash
python VLogger.py

```

### 4. Decryption

Use the dedicated `decryptor.py` tool to restore original telemetry from the encrypted payloads received at your endpoint.

---

## ⚠️ Disclaimer

This tool is for **educational and authorized security testing only**. The author is not responsible for any misuse. Unauthorized use of this tool against systems you do not own is illegal.
