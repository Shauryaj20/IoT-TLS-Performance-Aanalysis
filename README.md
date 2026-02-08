# IoT-TLS-Performance-Analysis
Benchmarking RSA vs. ECC Cipher Suites for secure MQTT communication in resource-constrained IoT environment simulation.

# IoT Security: RSA vs. ECC Performance Analysis 🔒

![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Protocol](https://img.shields.io/badge/Protocol-MQTT%20%2F%20TLS-3C873A?style=for-the-badge&logo=mqtt&logoColor=white)
![Focus](https://img.shields.io/badge/Focus-Cryptography%20%26%20Security-red?style=for-the-badge)

## 📌 Research Overview
Secure communication is critical for IoT, but traditional encryption (like RSA) can be too heavy for battery-powered devices.

This project is a **quantitative performance analysis** comparing two industry-standard TLS Cipher Suites to determine the most efficient protocol for resource-constrained IoT networks.

We simulated an IoT client-broker environment using **MQTT** to benchmark **RSA** (Traditional) against **ECC** (Elliptic Curve Cryptography).

## 🧪 The Experiment
I ran **15 automated trials** connecting a Python-based IoT client to a test broker (`test.mosquitto.org`), measuring:
1.  **Handshake Time:** How long it takes to establish a secure connection.
2.  **CPU Overhead:** The processing power consumed during encryption.

### Cipher Suites Tested
| Suite Type | Specification |
| :--- | :--- |
| **RSA (Standard)** | `TLS_DHE_RSA_WITH_AES_256_GCM_SHA384` |
| **ECC (Lightweight)** | `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256` |

## 📊 Key Findings
Our analysis confirms that **ECC is significantly superior** for IoT applications.

| Metric | RSA (Standard) | ECC (Proposed) | Impact |
| :--- | :--- | :--- | :--- |
| **Avg Handshake Time** | 6724 ms | **5638 ms** | ⚡ **16.1% Faster** |
| **Avg CPU Usage** | 2.19% | **1.79%** | 🔋 **18% More Efficient** |

> **Conclusion:** ECC provides the same level of security while reducing connection latency by **~1 second** per session, making it the ideal choice for battery-dependent IoT sensors.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:**
    * `paho-mqtt`: For implementing the MQTT Client.
    * `psutil`: For measuring real-time CPU performance.
    * `ssl`: For handling the TLS Cipher suite specifications.

## 📸 Visual Analysis
![Handshake Comparison](<TLS performance graphs.png>)
*Figure 1: Average TLS Handshake time (Lower is better).*_____________________*Figure 2: Average CPU usage (Lower is better).*

## 🔧 Run the Benchmark
```bash
# Clone the repo
git clone [https://github.com/Shauryaj20/IoT-TLS-Performance-Analysis.git](https://github.com/Shauryaj20/IoT-TLS-Performance-Analysis.git)

# Install requirements
pip install paho-mqtt psutil

# Run the benchmark script
python benchmark_ciphers.py
