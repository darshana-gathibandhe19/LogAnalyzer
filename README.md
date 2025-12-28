# 🛡️ LogAnalyzer: Cybersecurity Audit & Threat Detection

### *Automated system for parsing server logs, detecting security anomalies, and visualizing threat patterns.*

---

## 📖 Overview
**LogAnalyzer** is a security-focused automation tool designed to process raw server logs and identify potential vulnerabilities. It automates the extraction of critical data points from unstructured logs, performs data cleaning, and facilitates security auditing through automated reporting and visualization.

---

## 📊 Security Dashboard
<p align="center">
  <img src="log_analyzer_visual.png" width="900" alt="Log Analysis Dashboard">
</p>

---

## 📂 Project Structure
Based on the codebase:

```text
LogAnalyzer/
├── 📄 server_logs.txt         # Raw server logs (Source)
├── 📄 logs_parser.py          # Script for Regex-based parsing and extraction
├── 📄 db_to_csv.py            # Converts processed database logs to CSV for analytics
├── 📄 logs_warehouse.db       # SQLite database for structured log storage
├── 📊 LogAnalyzer_Visual.pbix # Power BI Dashboard for threat visualization
├── 📄 server_logs_clean.csv   # Final cleaned dataset for reporting
└── 📄 README.md               # Project documentation

Key Features
Automated Log Parsing (logs_parser.py): Uses advanced regular expressions to extract IP addresses, timestamps, HTTP methods, and status codes.

Structured Storage (logs_warehouse.db): Migrates unstructured text logs into a relational SQLite database for efficient querying.

Data Transformation (db_to_csv.py): Bridges the gap between the database and visualization tools by automating CSV exports.

Threat Detection: Identifies suspicious patterns such as repeated 401/403 errors (Unauthorized Access) and 500 errors (System Failures).

Interactive Visualization: Uses Power BI to track geographical attack patterns and peak threat hours.

🛠️ Tech Stack
Language: Python 3.9+ (Regex, SQLite3, Pandas)

Database: SQLite

Visualization: Microsoft Power BI

Version Control: Git & GitHub

⚙️ Setup & Installation

1. Clone the repository:
   git clone [https://github.com/darshana-gathibandhe19/LogAnalyzer.git](https://github.com/darshana-gathibandhe19/LogAnalyzer.git)

2. Run the parser to process raw logs:
   python logs_parser.py

3. Export data for visualization:
   python db_to_csv.py

4. Open 'LogAnalyzer_Visual.pbix' in Power BI Desktop to view the audit report.


Based on your local file structure for the LogAnalyzer, here is the accurate and professional README.md. It highlights the Cybersecurity Audit nature of the project and includes the Screenshot section you need.

Final Professional README for LogAnalyzer
Markdown
# 🛡️ LogAnalyzer: Cybersecurity Audit & Threat Detection

### *Automated system for parsing server logs, detecting security anomalies, and visualizing threat patterns.*

---

## 📖 Overview
**LogAnalyzer** is a security-focused automation tool designed to process raw server logs and identify potential vulnerabilities. It automates the extraction of critical data points from unstructured logs, performs data cleaning, and facilitates security auditing through automated reporting and visualization.

---

## 📊 Security Dashboard
<p align="center">
  <img src="log_analyzer_visual.png" width="900" alt="Log Analysis Dashboard">
</p>

---

## 📂 Project Structure
Based on the codebase:

```text
LogAnalyzer/
├── 📄 server_logs.txt         # Raw server logs (Source)
├── 📄 logs_parser.py          # Script for Regex-based parsing and extraction
├── 📄 db_to_csv.py            # Converts processed database logs to CSV for analytics
├── 📄 logs_warehouse.db       # SQLite database for structured log storage
├── 📊 LogAnalyzer_Visual.pbix # Power BI Dashboard for threat visualization
├── 📄 server_logs_clean.csv   # Final cleaned dataset for reporting
└── 📄 README.md               # Project documentation

### 🚀 Key Features
```text
* Automated Log Parsing: Uses advanced regular expressions to extract IP addresses and status codes.
* Structured Storage: Migrates unstructured logs into a relational SQLite database.
* Data Transformation: Automates CSV exports for seamless reporting.
* Threat Detection: Identifies suspicious patterns like unauthorized access attempts.

### 🛠️ Tech Stack
```text
* Language: Python 3.9+ (Regex, SQLite3, Pandas)
* Database: SQLite
* Visualization: Microsoft Power BI
* Version Control: Git & GitHub

### ⚙️ Setup & Installation
```text
1. Clone the repository:
   git clone https://github.com/darshana-gathibandhe19/LogAnalyzer.git
2. Run the parser to process raw logs:
   python logs_parser.py
3. Export data for visualization:
   python db_to_csv.py
4. Open 'LogAnalyzer_Visual.pbix' in Power BI Desktop to view the report.

### 🔮 Future Enhancements
```text
* Real-time Alerting: Integration with Slack/Email APIs for immediate threat notifications.
* Geo-IP Mapping: Automatically mapping source IPs to physical locations.
* Machine Learning: Implementing clustering to detect "Low and Slow" stealth attacks.
* Automated Blocking: Scripting firewall rules to auto-block IPs flagged for brute force.