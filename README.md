# 🌍 SolarPunk Resource Management Ecosystem

<p align="center">
  <ins><b>AI-Driven Data Governance & Compliance Integration</b></ins><br>
  <sub>Connecting Python AI Models with ServiceNow Cloud Architecture</sub>
</p>

---

## 📊 SYSTEM ARCHITECTURE
[Python Local Environment]                    [ServiceNow Cloud Platform]
AI Simulation Script                           Table: Solar Diagnostics
(send_ai_data.py)                              (Custom Data Model)
│                                               │
▼                                               ▼
REST API POST   ──────────────────────────►   Before Insert Trigger
(Data Payload: 5% Solar)                       (JS Business Rule Automation)
│
▼
Compliance Action
(Status Forced to CRITICAL)
## 🚀 PROJECT OVERVIEW

This repository showcases a complete end-to-end integration between a local machine-learning environment (**Python**) and an enterprise cloud platform (**ServiceNow**). It implements a **SolarPunk** sustainable ecosystem framework, demonstrating how data governance, ITIL principles, and automated compliance rules can safeguard critical infrastructure data.

### Key Capabilities Demonstrated:
* **Inbound Integrations:** Using Python to authenticate and push telemetry data directly to a secure cloud database via REST Table API.
* **Data Governance & Guardrails:** Configuring automated server-side triggers to intercept, validate, and manipulate incoming AI data *before* it is committed to the database.
* **Access Control (ACLs):** Establishing secure role-based access to protect sensitive sustainability data from unauthorized changes.

---

## 🧠 THE BILINGUAL COGNITIVE WORKFLOW

> **"Code is universal, but logic flows in the language of the mind."**

You will notice a mix of **English** and **Portuguese** across the code comments, database labels, and system logs. This is a deliberate, strategic reflection of a bilingual cognitive workflow. 

* **Global Technical Standards:** System names, API endpoints, variable definitions, and documentation are kept in English to comply with international development standards.
* **Native Logic Mapping:** Deep technical logic, architectural notes, and complex problem-solving strategies are framed in Portuguese. 

This approach ensures rapid, error-free development while building highly complex systems, bridging global tech frameworks with intuitive cognitive mapping.

---

## 🛠️ TECHNOLOGIES USED

| Technology | Role in Project |
| :--- | :--- |
| **Python 3** | Simulates AI telemetry data and manages the REST API pipeline. |
| **ServiceNow** | Cloud infrastructure, custom data models, and access control management. |
| **JavaScript (ES6)** | Powers the server-side Business Rules for real-time data interception. |
| **REST API / JSON** | Secure data serialization and cross-platform communication protocol. |

---

## ⚡ AUTOMATION SCENARIO & BUSINESS LOGIC

The core value of this project lies in its **automated risk mitigation**. 

1. **The Trigger:** The Python script simulates an AI model predicting a critical drop in solar energy generation (**5% radiation** output).
2. **The Interception:** A ServiceNow **Before Business Rule** intercepts the payload before it saves.
3. **The Compliance Action:** The platform overrides the status, triggers an emergency system flag, and enforces a high-priority water recycling routine to save resources.

### The Server-Side Logic (JavaScript):
```javascript
(function executeRule(current, previous) {
    // If AI predicts solar radiation falls below 10%
    if (current.solar_radiation_predicted < 0.10) {
        current.system_status = "CRITICAL: Low energy predicted. Conserving water.";
        gs.addErrorMessage("Solarpunk Alert: Emergency water-saving mode activated.");
    } else {
        current.system_status = "Optimal Operation";
    }
})(current, previous);
