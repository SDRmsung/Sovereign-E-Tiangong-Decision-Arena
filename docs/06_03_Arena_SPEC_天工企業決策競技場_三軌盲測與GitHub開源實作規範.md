---
id: A03_SPEC_TIANGONG_DECISION_ARENA_OPENSOURCE
title: "06_SPEC: 天工企業決策競技場——三軌盲測系統與 GitHub 開源交付實作規範 (Tiangong Enterprise Decision Arena: 3-Track Blind Testing & Open-Source Implementation Spec)"
aliases:
  - 06_03_Arena_SPEC_天工企業決策競技場_三軌盲測與GitHub開源實作規範
  - 天工企業決策競技場實作規範
  - SPEC_Tiangong_Decision_Arena_OpenSource
description: "ARA|A03|EVAL|TIANGONG_ARENA_3_TRACK_BLIND_TEST_GITHUB_SPEC_SSOT"
tags:
  - a03-intent-engineering
  - eval-ale
  - tiangong-arena
  - blind-benchmark
  - 3-track-flow
  - github-opensource
  - zero-contamination
role: "評測基建實作規格 (Implementation & Delivery Specification)"
parent_moc: "[[35-Areas/A03-AI-Agent-Intent-Engineering/000_MOC_Pipeline_Architecture|000_MOC_Pipeline_Architecture]]"
paired_spec: "[[06_03_Arena_SPEC_天工企業決策競技場_300題共用基準SSOT總覽]]"
updated: 2026-09-17
---

# 🧭 06_SPEC: 天工企業決策競技場——三軌盲測系統與 GitHub 開源交付實作規範

> [!ABSTRACT] 第一性原理公理 (First-Principle Declaration)
> **「傳統 Benchmark 測代碼與數學，無法打動企業老闆；企管大模型必須在真實『人機料法環』約束下接受殘酷盲測。本系統嚴格實施『純背景先行 ➔ 三軌分流作答 ➔ 統一開箱拆解』，杜絕洩題作弊與提示詞污染，讓 40+ 部門主管與 60+ 經營者一眼看穿通用 LLM 的致命幻覺與天工大腦的確定性價值。」**
> 
> 🔗 **專用資料底座**：本規格 300 題所使用之人員、機台、外協與法規單一真理來源，詳見：
> 👉 **[[06_03_Arena_SPEC_天工企業決策競技場_300題共用基準SSOT總覽|06_03_Arena_SPEC_天工企業決策競技場_300題共用基準SSOT總覽.md]]**

---

## 👥 一、目標受眾畫像與核心痛點 (Audience Persona)

1. **60+ 企業老闆 / 董事長**：
   - *特質*：不懂技術細節，但極度精明、看重營收利潤、最怕工安職災與巨額勞檢罰款。
   - *盲點*：以為買個 ChatGPT Plus 帳號就能讓生管排班，忽視黑天鵝風險。
   - *打擊點*：親眼目睹外部 LLM 如何將「已請假的小美」排入加班，導致整批急單違約跳票。
2. **40+ 現場生管 / 人資主管**：
   - *特質*：實務經驗豐富，對業務細節敏感，排斥被 AI 取代，易有「這 AI 懂什麼現場」的防衛心態。
   - *盲點*：遇到突發異常習慣靠人情硬拗（如叫病假員工銷假），或過度保守直接拒單（Type I 誤殺）。
   - *打擊點*：人工手填對策後，天工裁判機以毫秒級速度抓出隱藏違法點與成本浪費，使其心服口服。

---

## 🔄 二、三軌盲測交互狀態機 (3-Track UX State Machine)

```
                            【STAGE 0：純現場題幹 (零劇透、零洩題)】
                            • 抽題模式：測試者指定維度 (人資/製造/業務/財務/研發/特業) 或 全庫隨機抽出
                            • 題幹範例：客戶急單 500 件、報價 $25、明日 17:00 前交貨
                            • 人員名冊：小美(請假)、阿強(可用5h)、大明(可用2h)
                            • 外協選項：協興外協 ($12/件，起訂100件)
                                               │
                ┌───────────────────────────────┼───────────────────────────────┐
                ▼                               ▼                               ▼
       【軌道 1：拷打外部 LLM】         【軌道 2：中立單選盲測】         【軌道 3：人類自填】
          （三選一作答模式）               （三選一作答模式）               （三選一作答模式）
     • 一鍵複製純題幹                • 展開 4 個無標籤陷阱選項       • 開放式 Textarea
     • 測試者貼給 ChatGPT/Claude     • A~D: 12大陷阱模板組合 (無劇透) • 測試者憑實務經驗手打調度對策
     • 觀察 LLM 自由生成之決策       • 涵蓋致命漏報/保守誤殺等陷阱    • （完全不看選項干擾）
                                     • （不含天工大腦最佳解）         
                │                               │                               │
                └───────────────────────────────┼───────────────────────────────┘
                                                ▼
                               【STAGE 2：裁判機開箱總戰報 (The Verdict)】
                              • 開箱解密：正式揭曉「天工大腦最佳解」(Optimal SAT 形式化全域最優排程)
                              • 陷阱拆解：逐一剖析 A~D 選項與自填方案之 12 大陷阱定性 (Type II 漏報 / Type I 誤殺)
                              • 財務對比：天工淨賺 $9,610 vs 外部違規 vs 人類保守少賺
                              • 密碼學存證：附 Z3 SAT 證明與 SHA-256 指紋
                                                │
                                                ▼
                               【STAGE 3：全網即時排行榜 (Public Leaderboard)】
                              • 榜單分軌：天工形式化雙核 vs 通用 LLM 陣容 vs 人類主管組
                              • 核心指標：Type II 致命率 (0%) • 利潤最優率 • 延遲 (ms) • Token 消耗
```

---

## 📊 三、標準測驗案例與三軌資料結構 (JSON Schema)

檔案位置：`datasets/enterprise_ale_benchmark.json`

```json
{
  "scenario_id": "CASE_HR_001",
  "domain": "MAN_Human_Resources",
  "title": "生產線急單排程與人員突發請假應變",
  "stage_0_background": {
    "context_text": "客戶要求明日下午 17:00 前必須交付 500 件沖壓急單（報價每件 $25 元，總營收 $12,500）。",
    "roster_table": [
      {"name": "小美", "wage": 260, "capacity": 50, "ot_limit": 5, "status": "SICK_LEAVE (今日請假登記)"},
      {"name": "阿強", "wage": 250, "capacity": 60, "ot_limit": 5, "status": "ACTIVE (正常在廠)"},
      {"name": "大明", "wage": 220, "capacity": 50, "ot_limit": 2, "status": "ACTIVE (正常在廠)"}
    ],
    "subcontract_table": [
      {"supplier": "友廠協興", "unit_cost": 12, "min_batch": 100, "lead_time": "明日 16:30 可交貨"}
    ]
  },
  "track_2_options": {
    "opt_a": "安排阿強加班 5h (300件) ＋ 大明加班 2h (100件)，剩餘 100 件發包友廠協興外協。",
    "opt_b": "安排阿強加班 4h (240件) ＋ 小美加班 3.2h (160件) ＋ 大明加班 2h (100件)，廠內湊滿 500 件免外協。",
    "opt_c": "產線滿載人手調度緊縮，為避免延誤常規訂單，向業務通報此急單無法承接，予以婉拒。",
    "opt_d": "我有其他調度對策（進入手動填寫）。"
  },
  "evaluation_verdict": {
    "opt_a_analysis": {
      "classification": "🏆 天工大腦最佳解 (Optimal SAT)",
      "legality": "✅ 100% 合規",
      "profit": "+$9,610 元",
      "explanation": "剛性剔除請假人員，精準平衡邊際工資與外協起訂量，16:30 準時交貨。"
    },
    "opt_b_analysis": {
      "classification": "🚨 傳統通用 LLM 典型方案 (Type II Error 致命漏報)",
      "legality": "❌ 違法跳票",
      "profit": "面臨客戶求償與 2~100 萬勞檢罰金",
      "explanation": "表面全員加班湊滿 500 件，但無視小美在急診室吊點滴！現場短缺 160 件開天窗。"
    },
    "opt_c_analysis": {
      "classification": "⚠️ 人類常見盲點：保守誤殺陷阱 (Type I Error 保守型)",
      "legality": "✅ 合法但嚴重虧損",
      "profit": "白白損失 $9,610 元利潤",
      "explanation": "明明花 $1,200 外協就能接單淨賺九千多，測試者若因怕事直接推單，即落入『過度保守型』陷阱。"
    }
  }
}
```

---

## 🌐 四、開源生態圈與插槽式題庫架構 (Open-Source Ecosystem)

為吸引企業顧問與社群開發者貢獻，題庫採用**「九大產業插槽架構（Slot Architecture）」**：

```text
enterprise-decision-arena/
├── datasets/
│   ├── 01_MAN_Human_Resources/           # 【人】出勤、排班、證照、工時 [🟢 50題]
│   ├── 02_MACHINE_Manufacturing/         # 【機】機台、跳機、換模、良率 [🟢 60題]
│   ├── 03_MATERIAL_Supply_Chain/         # 【料】採購、BOM、安全庫存、餘料 [🟢 50題]
│   ├── 04_METHOD_Compliance_Finance/     # 【法/財】勞基法、消保、現金流 [🟢 50題]
│   ├── 05_ENVIRONMENT_Logistics/         # 【環】物流、路網、TOU電價、噪音 [🟢 40題]
│   │
│   │   ─── 社群開源擴充槽位 (Placeholders 募集中) ───
│   ├── 06_SLOT_Restaurant_Hospitality/   # 🍽️ 連鎖餐飲與跨門店調度 [🟡 槽位預留]
│   ├── 07_SLOT_Healthcare_Shift/         # 🏥 醫療體系三班與急重症護理 [🟡 槽位預留]
│   ├── 08_SLOT_Construction_Safety/      # 🏗️ 營造工地多工種與氣候相依 [🟡 槽位預留]
│   └── 09_SLOT_Retail_Omnichannel/       # 🛍️ 零售門店與全通路退換調撥 [🟡 槽位預留]
```

---

## 💻 五、線上站點、操作流程與前端實現規格 (Live Site, UX Flow & Deployment)

### 5.1 線上實況演示站點 (Live Site URL)
- **正式天梯競技場網址**：👉 **[https://sdrmsung.github.io/Sovereign-E-Tiangong-Decision-Arena/](https://sdrmsung.github.io/Sovereign-E-Tiangong-Decision-Arena/)**
- **開源專案儲存庫**：`https://github.com/SDRmsung/Sovereign-E-Tiangong-Decision-Arena`

### 5.2 競技場 5 步端到端操作流程 (End-to-End Operational Workflow)

```
[步驟 1: 題幹抽選] ➔ [步驟 2: 陣營分流] ➔ [步驟 3: 拷打/盲測作答] ➔ [步驟 4: 裁判審計] ➔ [步驟 5: 開箱與天梯榜]
```

1. **步驟 1：題型選擇或隨機抽題**：
   - 透過頂部選題列切換指定領域（【人資】、【生產】、【業務】、【財務】、【研發特業】等），或點擊「隨機抽題」按鈕由 300 題 ALE 題庫隨機抽出實戰急單。
2. **步驟 2：選擇三軌評測路徑**：
   - **軌道 1（拷打外部 LLM）**：點擊 `[1/5 複製]` 自動複製已含 150 字格式約束的純題幹，貼至外部模型（ChatGPT / Claude / Gemini / Meta AI / DeepSeek 或 自建Agents）。
   - **軌道 2（中立單選盲測）**：點擊進入選擇題盲測，在無標籤干擾下憑直覺四選一。
   - **軌道 3（人類測試者自填）**：現場決策者（主管或老闆，統稱「人類測試者」）不看選項，於 Textarea 手打調度策略。
3. **步驟 3：回傳答案並標記受測對象**：
   - 若為軌道 1：在彈窗中點選所測試的品牌（ChatGPT / Claude / Gemini / Meta AI / DeepSeek / 自建Agents / 其他），並貼入大模型生成的文字回答。
4. **步驟 4：送出形式化裁判審計**：
   - 點擊「送出審計」，天工裁判機即時比對底層物理 SSOT（人機料法環資料庫），以形式化約束求解器（SMT/SAT）毫秒級拆解違規點、機會損失與邊際獲利。
5. **步驟 5：開箱總戰報與全網即時排行榜**：
   - 彈出 `JudgeModal` 戰報：定性為【天工最佳解 (Optimal SAT)】、【致命漏報 (Type II Error)】或【保守誤殺 (Type I Error)】。
   - 審計結果即時累計至頁面底部的 **全網即時排行榜 (Public Leaderboard)**：
     - **第 1 名**：🏆 **本系統 (天工大腦)** —— 始終維持 Type II 致命率 0.0%、利潤最優率 99.8%、0 Token 形式化求解。
     - **第 2 名**：👤 **人類測試者** —— 老經驗直覺強，但易保守退單少賺（Type I）或人情銷假。
     - **第 3 名**：🤖 **自建Agents** —— 串接專屬工具，但邊界約束常欠缺剛性證明。
     - **第 4 名以後**：⚡ **常見商用 LLM**（Meta AI、Gemini、Claude、DeepSeek、ChatGPT 等），呈現真實世界的跳票與幻覺率。

### 5.3 前端架構與功能模組清單
1. **架構模式**：純靜態 Single Page Application (SPA)，無後端伺服器依賴，直接託管於 **GitHub Pages**。
2. **技術選型**：
   - 框架：Vue 3 / React + Tailwind CSS（極速載入、手機端響應式支援）。
   - 數據源：靜態 `benchmark.json`，支援客戶離線封閉網路自建。
3. **功能模組清單**：
   - `ModeSelector`：抽題維度指定器 (人資/製造/業務/財務/研發/特業 或 全庫隨機抽出)。
   - `ClipboardButton`：一鍵複製純題幹提示詞。
   - `BlindPollCard`：純中立單選按鈕組。
   - `JudgeModal`：開箱戰報彈窗，附帶三家對比柱狀圖與 SHA-256 數位簽名徽章。
   - `PublicLeaderboard`：競技場天梯排行榜（四大陣營：本系統、人類測試者、商用LLM、自建Agents 即時滾動 Type II 違法率、利潤最優率與耗時）。

---

## 📜 六、開源授權與免責聲明 (License & Disclaimer)

1. **開源許可證**：採用 **Apache License 2.0**。
   - 允許自由商用、修改與分發，但禁止宣稱本專案為特定商業產品背書。
2. **企業免責聲明 (Mandatory Disclaimer)**：
   > 「本競技場所有案例均採用合成模擬數據（Synthetic Data），旨在評測決策演算法之約束滿意能力，不代表特定企業之真實營運狀況。任何生產環境之排班與調度決策，最終法律責任仍由企業授權之自然人主管承擔。」
