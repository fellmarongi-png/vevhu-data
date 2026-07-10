import csv
import os
from collections import defaultdict

repo_dir = '/home/ec2-user/vevhu-data'
master_csv_path = os.path.join(repo_dir, 'master_vevhu_database.csv')

if not os.path.exists(master_csv_path):
    print("Error: master_vevhu_database.csv not found! Run consolidate_database.py first.")
    exit(1)

with open(master_csv_path, 'r', encoding='utf-8') as f:
    records = list(csv.DictReader(f))

total = len(records)
active = [r for r in records if r['Record Status'] == 'Active']
crossed_out = [r for r in records if r['Record Status'] == 'Crossed Out']
blank = [r for r in records if r['Record Status'] == 'Blank Row']

stands = defaultdict(list)
ids = defaultdict(list)
cells = defaultdict(list)

missing_stand = []
missing_id = []
missing_cell = []

for r in records:
    if r['Record Status'] == 'Blank Row':
        continue
    st = r['Stand No']
    id_val = r['ID No']
    cell_val = r['Cell No']
    
    if st:
        stands[st].append(r)
    else:
        missing_stand.append(r)
        
    if id_val:
        ids[id_val].append(r)
    else:
        missing_id.append(r)
        
    if cell_val:
        cells[cell_val].append(r)
    else:
        missing_cell.append(r)

dup_stands = {k: v for k, v in stands.items() if len(v) > 1}
dup_ids = {k: v for k, v in ids.items() if len(v) > 1}
dup_cells = {k: v for k, v in cells.items() if len(v) > 1}

# Format Stand Conflicts Table
stand_rows_md = []
for st, rows in sorted(dup_stands.items(), key=lambda x: x[0]):
    if st.lower() in ['', 'no', 'no stand', 'no stand no', 'stand no']:
        continue
    
    primary = rows[0]
    others = rows[1:]
    
    primary_desc = f"{primary['Name & Surname']} (ID: `{primary['ID No'] or 'Missing'}`, Batch: {primary['Batch Source']})"
    others_desc = ' / '.join([f"{r['Name & Surname']} (ID: `{r['ID No'] or 'Missing'}`, Batch: {r['Batch Source']})" for r in others])
    
    statuses = [r['Record Status'] for r in rows]
    names_set = set([r['Name & Surname'].lower() for r in rows])
    
    if 'Crossed Out' in statuses and 'Active' in statuses:
        audit_status = "**Re-registered** (some records Crossed Out)"
    elif len(names_set) == 1:
        audit_status = "**Exact Duplicate Entry**"
    elif len(rows) > 2:
        audit_status = f"**Multi-Assignment Conflict** ({len(rows)} occupants)"
    else:
        audit_status = "Dual Registration"
        
    stand_rows_md.append(f"| **{st}** | {primary_desc} | {others_desc} | {audit_status} |")

# Format ID Conflicts Table
id_rows_md = []
for id_val, rows in sorted(dup_ids.items(), key=lambda x: x[0]):
    stands_assigned = ', '.join([f"Stand {r['Stand No'] or 'Missing'} ({r['Batch Source']})" for r in rows])
    names = ' / '.join([r['Name & Surname'] for r in rows])
    names_set = set([r['Name & Surname'].lower() for r in rows])
    
    if len(names_set) == 1:
        notes = "**Multi-Stand Owner** or Duplicate Record"
    else:
        notes = "Family Joint / Shared ID Registration"
        
    id_rows_md.append(f"| `{id_val}` | {names} | {stands_assigned} | {notes} |")

report_content = f"""# Master Data Quality & Audit Report (Consolidated Batches)

## Executive Summary
This report summarizes the consolidation, data cleansing, and multi-batch quality audit across all extracted ledger batches.

* **Total Records Analyzed:** {total}
* **Active Records:** {len(active)} ({len(active)/total*100:.1f}%)
* **Crossed-Out Records:** {len(crossed_out)} ({len(crossed_out)/total*100:.1f}%)
* **Blank Ledger Rows:** {len(blank)} ({len(blank)/total*100:.1f}%)
* **Consolidated Master Dataset:** [`master_vevhu_database.csv`](./master_vevhu_database.csv)

---

## 1. Multi-Batch Deduplication Audit

### A. Stand Number Conflicts ({len(stand_rows_md)} Instances)
Stands assigned to multiple records or re-registered across batches:

| Cleaned Stand No | Primary Record | Secondary / Duplicate Record | Audit Status |
| :--- | :--- | :--- | :--- |
""" + '\n'.join(stand_rows_md) + """

### B. Duplicate National ID Numbers ({len(id_rows_md)} Instances)
Members owning multiple stands or family joint registrations:

| National ID No | Member Name | Assigned Stands | Notes |
| :--- | :--- | :--- | :--- |
""" + '\n'.join(id_rows_md) + """

---

## 2. Missing & Incomplete Data Audit

* **Records Missing Stand Number:** {len(missing_stand)} non-blank records
* **Records Missing National ID:** {len(missing_id)} non-blank records
* **Records Missing Cell Number:** {len(missing_cell)} non-blank records

---

## 3. Recommended Actions & Next Steps

1. **Resolve Stand Conflicts:** Review multi-assigned stands with physical ledger verification.
2. **Flag Superseded Records:** Mark crossed-out duplicates as superseded in the master database.
3. **Build Interactive Search Tool:** Implement Stage 3 (Interactive Web Search Dashboard) to allow instant searching and filtering of active vs crossed-out stands.
"""

# Save locally to project dir
with open(os.path.join(repo_dir, 'DATA_QUALITY_AUDIT_REPORT.md'), 'w', encoding='utf-8') as f:
    f.write(report_content)

# Save to artifacts directory as well
artifacts_dir = '/home/ec2-user/.gemini/antigravity-cli/brain/379676f9-c685-4f83-9763-d14354094d92'
if os.path.exists(artifacts_dir):
    with open(os.path.join(artifacts_dir, 'data_quality_audit.md'), 'w', encoding='utf-8') as f:
        f.write(report_content)

print("Generated audit report files successfully!")
