# 🏛️ 天工企業決策競技場 (Tiangong Enterprise Decision Arena)
> **Sovereign-E-Tiangong-Decision-Arena** | 三軌盲測 ✕ 300 題約束滿意評測 ✕ 靜態 GitHub Pages SPA 交付基建

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Verification](https://img.shields.io/badge/Checks-100%25_PASS-brightgreen.svg)](tests/run_all_checks.py)
[![Type II Error](https://img.shields.io/badge/Type_II_Error-0.0%25-success.svg)](datasets/enterprise_ale_benchmark.json)

---

## 🧭 核心願景 (Vision & First Principle)
傳統 LLM Benchmark 測寫代碼與做高數，無法打動中小企業老闆。
企管大模型必須在真實「**人機料法環**」衝突下接受殘酷盲測！

本競技場實施 **「純背景先行 ➔ 三軌分流作答 ➔ 統一開箱拆解」**：
1. **軌道 1（拷打外部 LLM）**：一鍵複製題幹貼給 ChatGPT/Claude，看其如何踩入排班與法律幻覺。
2. **軌道 2（中立單選盲測）**：包含天工最佳解、Type II 致命漏報陷阱、Type I 保守誤殺陷阱。
3. **軌道 3（主管硬核自填）**：供 40+ 資深生管/廠長直接手打老經驗調度對策。

---

## 📦 評審最小四套件 (Judge Minimal Delivery Kit)
- **1. 乾淨介面**：`web/index.html` (純靜態 SPA，託管於 GitHub Pages，零後端伺服器依賴)。
- **2. 終端 CLI**：`python src/cli.py --list` / `python src/cli.py --eval CASE_HR_001`。
- **3. 核心 Engine**：`src/engine.py` (離線形式化驗證器與真值對齊引擎)。
- **4. 一鍵跑測**：`python tests/run_all_checks.py` (零第三方依賴，<10ms 快速通過)。

---

## 🚀 快速上手 (Quick Start)

### 終端 CLI 評測
```bash
# 查看所有測試案例
python src/cli.py --list

# 評測特定情境 (包含 LLM 與 天工大腦雙軌對決)
python src/cli.py --eval CASE_HR_001
```

### 一鍵跑測驗收 (<10ms)
```bash
python tests/run_all_checks.py
```

---

## 📜 開源許可與免責聲明
- 本專案採用 **Apache License 2.0** 開源授權。
- **免責聲明**：所有案例均採用合成模擬數據 (Synthetic Data)，旨在評測決策演算法之約束滿意能力。實際生產環境調度決策，最終法律責任由企業授權之自然人主管承擔。
