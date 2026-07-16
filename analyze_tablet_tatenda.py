import csv
import os
from collections import defaultdict

repo_dir = '/home/ec2-user/vevhu-data'
master_csv = os.path.join(repo_dir, 'master_vevhu_database.csv')

print("=== STARTING DETAILED ANOMALY ANALYSIS FOR TABLET AND TATENDA BATCHES ===")

# Categorize source batches:
# Tablet files: batch_tablet_200.csv, batch_tablet_300.csv, batch_tablet_non_standard.csv
# Tatenda files: batch_tat_200.csv, batch_tat_300.csv, batch_tat_kambarami.csv, batch_tat_madzimai.csv
# Others (physical ledger transcription): batch_15july_work.csv, batch_200_first_batch.csv, batch_200m2.csv, etc.

tablet_files = {'batch_tablet_200.csv', 'batch_tablet_300.csv', 'batch_tablet_non_standard.csv'}
tatenda_files = {'batch_tat_200.csv', 'batch_tat_300.csv', 'batch_tat_kambarami.csv', 'batch_tat_madzimai.csv'}

# Stats containers
tablet_stats = defaultdict(int)
tatenda_stats = defaultdict(int)

# We want to identify specific records and print summaries
tablet_records_total = 0
tatenda_records_total = 0

with open(master_csv, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for r in reader:
        source = r.get('Batch Source', '')
        status = r.get('Record Status', '')
        
        # Check standard fields for anomalies
        stand = r.get('Cleaned Stand No', '')
        name = r.get('Name & Surname', '')
        id_no = r.get('Cleaned ID No', '')
        cell = r.get('Cleaned Cell No', '')
        comments = r.get('Comments', '')
        
        is_tablet = source in tablet_files
        is_tatenda = source in tatenda_files
        
        if is_tablet:
            tablet_records_total += 1
        elif is_tatenda:
            tatenda_records_total += 1
            
        stats = tablet_stats if is_tablet else (tatenda_stats if is_tatenda else None)
        if not stats:
            continue
            
        # 1. Missing Stand No
        if not stand or stand.strip() == '':
            stats['Missing Stand No'] += 1
            
        # 2. Missing Name
        if not name or name.strip() == '' or 'no details' in name.lower():
            stats['Missing Name / No Details'] += 1
            
        # 3. Missing or Invalid ID
        if not id_no or id_no.strip() == '':
            stats['Missing National ID'] += 1
        elif len(id_no) < 5:  # very short
            stats['Invalid/Short National ID'] += 1
            
        # 4. Passport numbers (Zimbabwe passport starts with two letters e.g. AE, AD followed by 6 digits)
        # We clean them but they are flagged as passport
        raw_id = r.get('ID No', '')
        if raw_id and any(prefix in raw_id.upper() for prefix in ['AE', 'AD', 'PN', 'PP']):
            stats['Passport Used instead of ID'] += 1
            
        # 5. Invalid Cell number
        if not cell or cell.strip() == '':
            stats['Missing Cell No'] += 1
        else:
            # Cleaned cell should be 9 or 10 digits local, or 12/13 digits international
            cleaned_cell = cell.replace(' ', '').replace('-', '').replace('+', '')
            if not (len(cleaned_cell) in [9, 10, 12, 13] and cleaned_cell.isdigit()):
                stats['Invalid Cell Format'] += 1
                
        # 6. Crossed out
        if status == 'Crossed Out':
            stats['Crossed Out Records'] += 1
            
        # 7. Cabins or Tuckshops in comments
        if comments:
            comments_lower = comments.lower()
            if 'cabin' in comments_lower:
                stats['Cabin Structures'] += 1
            if 'tuckshop' in comments_lower or 'tuck shop' in comments_lower:
                stats['Tuckshop Structures'] += 1
            if 'cottage' in comments_lower:
                stats['Cottages'] += 1
            if 'unfinished' in comments_lower or 'structure only' in comments_lower or 'slab' in comments_lower:
                stats['Unfinished Structures'] += 1

print(f"Total Records Analyzed:")
print(f"  Tablet App: {tablet_records_total}")
print(f"  Tatenda: {tatenda_records_total}")

print("\n--- TABLET APP DATA ANOMALIES ---")
for k, v in sorted(tablet_stats.items()):
    print(f"  {k}: {v} ({(v/tablet_records_total)*100:.1f}%)")

print("\n--- TATENDA DATA ANOMALIES ---")
for k, v in sorted(tatenda_stats.items()):
    print(f"  {k}: {v} ({(v/tatenda_records_total)*100:.1f}%)")

# List some specific critical examples of anomalies
print("\n=== EXAMPLES OF CRITICAL ISSUES IN TABLET/TATENDA DATA ===")
with open(master_csv, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    printed = 0
    for r in reader:
        source = r.get('Batch Source', '')
        name = r.get('Name & Surname', '')
        stand = r.get('Cleaned Stand No', '')
        id_no = r.get('Cleaned ID No', '')
        cell = r.get('Cleaned Cell No', '')
        comments = r.get('Comments', '')
        
        if source in tablet_files or source in tatenda_files:
            # Find a record with multiple missing details
            is_bad = False
            reasons = []
            if not name or 'no details' in name.lower() or name.strip() == '':
                is_bad = True
                reasons.append("Missing Name")
            if not stand:
                is_bad = True
                reasons.append("Missing Stand")
            if not id_no:
                is_bad = True
                reasons.append("Missing ID")
                
            if is_bad and printed < 10:
                print(f"Source: {source} | Stand: {stand or 'MISSING'} | Name: {name or 'MISSING'} | ID: {id_no or 'MISSING'} | Cell: {cell or 'MISSING'} | Reasons: {', '.join(reasons)}")
                printed += 1
                
print("=== END ANALYSIS ===")
