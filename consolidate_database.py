import csv
import glob
import os
import re

repo_dir = '/home/ec2-user/vevhu-data'
batch_files = sorted(glob.glob(os.path.join(repo_dir, '**/batch_*.csv'), recursive=True))

all_records = []

print(f"Found batch files for consolidation: {[os.path.relpath(f, repo_dir) for f in batch_files]}")

for b_file in batch_files:
    batch_name = os.path.basename(b_file)
    with open(b_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader, start=1):
            get_val = lambda k: (row.get(k) or '').strip()
            
            file_name = get_val('File Name')
            stand_no = get_val('Stand No')
            name = get_val('Name & Surname')
            id_no = get_val('ID No')
            cell_no = get_val('Cell No')
            comp_yes = get_val('Compliance Yes')
            comp_no = get_val('Compliance No')
            comments = get_val('Comments')
            
            # Determine Record Status
            is_blank = not (stand_no or name or id_no or cell_no or comments)
            is_crossed_out = '[CROSSED OUT]' in comments or 'crossed out' in comments.lower() or '[crossed out]' in comments.lower()
            
            if is_blank:
                status = 'Blank Row'
            elif is_crossed_out:
                status = 'Crossed Out'
            else:
                status = 'Active'
                
            # Cleaned Stand No
            cleaned_stand = re.sub(r'\s+', ' ', stand_no).strip()
            
            # Cleaned Name
            cleaned_name = re.sub(r'\s+', ' ', name).strip()
            if cleaned_name.endswith('.'):
                cleaned_name = cleaned_name[:-1].strip()
                
            # Cleaned ID No
            cleaned_id = re.sub(r'\s+', ' ', id_no).strip()
            
            # Cleaned Cell No
            cleaned_cell = re.sub(r'\s+', ' ', cell_no).strip()
            
            rec = {
                'Batch Source': batch_name,
                'File Name': file_name,
                'Row Index': str(idx),
                'Stand No (Raw)': stand_no,
                'Cleaned Stand No': cleaned_stand,
                'Name & Surname (Raw)': name,
                'Cleaned Name': cleaned_name,
                'ID No (Raw)': id_no,
                'Cleaned ID No': cleaned_id,
                'Cell No (Raw)': cell_no,
                'Cleaned Cell No': cleaned_cell,
                'Compliance Yes': comp_yes,
                'Compliance No': comp_no,
                'Comments': comments,
                'Record Status': status
            }
            all_records.append(rec)

print(f'Total records read: {len(all_records)}')

# Write master_vevhu_database.csv
master_csv_path = os.path.join(repo_dir, 'master_vevhu_database.csv')
if all_records:
    fieldnames = list(all_records[0].keys())
    with open(master_csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_records)
    print(f'Saved master database to {master_csv_path}')
else:
    print('Error: No records found to write!')
