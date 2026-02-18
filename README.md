# Satoshi’s Sandbox 🏜️ | Professional Bitcoin Wallet Explorer

**Satoshi’s Sandbox** is a high-performance, open-source Bitcoin balance checker and wallet tracking dashboard. Built for developers and crypto-privacy advocates, it provides a sleek, premium dark interface to monitor multiple public BTC addresses without compromising your private keys.

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)](https://www.python.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/J4yB33/satoshis-sandbox/blob/main/Satoshi_Sandbox_Colab.ipynb)

## 📖 Description
Whether you are auditing a portfolio or tracking on-chain movements, Satoshi’s Sandbox offers a real-time window into the Bitcoin blockchain. Unlike standard explorers, this tool is designed to be **self-hosted** or run in the cloud via **Google Colab**, giving you a private, network-accessible dashboard that runs on any local server or Raspberry Pi.

It leverages redundant API layers to ensure your **GBP (£)** and **USD ($)** valuations are always live, matching the accuracy of institutional banking apps while providing the raw on-chain data that power-users require.

## 🚀 Key Features
- **Instant Multi-Wallet Sync**: Track Bech32, SegWit, and Legacy addresses in a single view.
- **Live Currency Engine**: Toggle between **GBP** and **USD** with a single click, powered by redundant exchange rate APIs.
- **On-Chain Analytics**: View Satoshis, total transaction counts, and detailed history for every wallet.
- **Zero-Config Memory**: Integrated browser Local Storage remembers your wallets so you don't have to.
- **Premium Dark UI**: A professional dark-mode aesthetic optimized for low-light environments and professional workstations.

## 📸 Screenshots
### Initial Page 
<img width="775" height="383" alt="Initial Dashboard" src="https://github.com/user-attachments/assets/0bd3fac2-92f2-4d39-bf26-6c24c4bd396b" />

### Live Tracking State
<img width="783" height="861" alt="Live Data View" src="https://github.com/user-attachments/assets/02c70acf-e8ad-4035-bc4a-b61a86aae3c1" />

## 🛠️ Usage Options

### Option 1: Google Colab (Cloud)
1. Click the **Open In Colab** badge at the top of this README.
2. Run the notebook cells to install dependencies and initialize the secure tunnel.
3. Access your dashboard via the generated public URL.

### Option 2: Local Installation
1. **Clone the project**:
   ```bash
   git clone [https://github.com/J4yB33/satoshis-sandbox.git](https://github.com/J4yB33/satoshis-sandbox.git)
   cd satoshis-sandbox
Environment Setup:

Bash
python3 -m venv venv
source venv/bin/activate
pip install flask requests
Launch:

Bash
python3 app.py
Access the UI at http://localhost:5000 or your server's local IP.

🤝 Contributing
This is an open-source project. Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

⚖️ License
Distributed under the MIT License. See LICENSE for more information.

Keywords: Bitcoin Balance Checker, BTC Portfolio Tracker, Open Source Crypto Dashboard, Satoshi Tracker, Blockchain Explorer UI, Python Bitcoin Tool, Premium Dark Mode.
