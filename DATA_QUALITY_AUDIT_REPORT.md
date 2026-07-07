# Master Data Quality & Audit Report (Batches 1 - 8)

## Executive Summary
This report summarizes the consolidation, data cleansing, and multi-batch quality audit across all 8 extracted ledger batches (`batch_1.csv` through `batch_5.csv`, `batch_200m2.csv`, `batch_300m2.csv`, and `batch_madzimai.csv`).

* **Total Records Analyzed:** 890
* **Active Records:** 757 (85.1%)
* **Crossed-Out Records:** 59 (6.6%)
* **Blank Ledger Rows:** 74 (8.3%)
* **Consolidated Master Dataset:** [`master_vevhu_database.csv`](./master_vevhu_database.csv)

---

## 1. Multi-Batch Deduplication Audit

### A. Stand Number Conflicts (59 Instances)
Stands assigned to multiple records or re-registered across batches:

| Cleaned Stand No | Primary Record | Secondary / Duplicate Record | Audit Status |
| :--- | :--- | :--- | :--- |
| **1052** | Wellmah Gamanya (ID: `15-128978 Q 15`, Batch: batch_1.csv) | Beatre Ciati (ID: `63-877786 Q 63`, Batch: batch_4.csv) | **Re-registered** (some records Crossed Out) |
| **14** | Spencer Zenda (ID: `63-152790S734`, Batch: batch_3.csv) | Maxioell maxwel Chatora (ID: `04-134739f04`, Batch: batch_300m2.csv) | **Re-registered** (some records Crossed Out) |
| **1463** | Morgan Sekai (ID: `63-1046107 F 75`, Batch: batch_200m2.csv) | Absent Absai Matagg (ID: `24-181122C11`, Batch: batch_5.csv) | Dual Registration |
| **1548** | Ndaizivei Mbamba (ID: `18-057624B18`, Batch: batch_3.csv) | Enera Chiwara (ID: `27-178349H27`, Batch: batch_3.csv) | Dual Registration |
| **1560** | Austin Matsiuke (ID: `79-1259227 R 83`, Batch: batch_1.csv) | Mary Josiyasi (ID: `63-137844 P 63`, Batch: batch_2.csv) | Dual Registration |
| **1617** | Colin Chikutirgwe (ID: `63-925316 F 34`, Batch: batch_1.csv) | Dickson Chigariro (ID: `63-122635 Y 18`, Batch: batch_200m2.csv) | Dual Registration |
| **1780** | Grace Sagara (ID: `63-1237241K34`, Batch: batch_3.csv) | Owen Matenda (ID: `13-170002T13`, Batch: batch_5.csv) | Dual Registration |
| **1830** | Mabbie Sedze (ID: `34-056376 P 34`, Batch: batch_1.csv) | Patrick chando (ID: `07-108658 B 07`, Batch: batch_4.csv) | Dual Registration |
| **1976** | Aman White Abudula (ID: `63-1640867 J 63`, Batch: batch_200m2.csv) | Zgoriri Tamai (ID: `38-189033 S 38`, Batch: batch_200m2.csv) | Dual Registration |
| **2** | Rosemary nyamuba (ID: `50-10760750P`, Batch: batch_300m2.csv) | Margret / Manyundwa (ID: `22274349y*40 / J04`, Batch: batch_300m2.csv) / Selina Dick (ID: `63-2657882K63`, Batch: batch_300m2.csv) | **Multi-Assignment Conflict** (3 occupants) |
| **2024** | Prescious Mango (ID: `86-037309 Q 86`, Batch: batch_200m2.csv) | Jacob & Melody Chitaitai & Mapako (ID: `42-229243A42`, Batch: batch_3.csv) | Dual Registration |
| **2095** | Emmanuel Garwe (ID: `63-752503Y11`, Batch: batch_3.csv) | Jane. nyanhango (ID: `63-1210826y34`, Batch: batch_300m2.csv) | Dual Registration |
| **2155** | Eddmore Masinire (ID: `63-1311460H32`, Batch: batch_5.csv) | James Chidhimira (ID: `22-145205Z22`, Batch: batch_5.csv) | Dual Registration |
| **2174** | Esinath Shona (ID: `77-049388J77`, Batch: batch_300m2.csv) | Shephard Murero (ID: `63-987799E05`, Batch: batch_5.csv) | Dual Registration |
| **2212** | Caston Mukungurutse (ID: `18-057063 T 18`, Batch: batch_200m2.csv) | Caroline Mudzingwa (ID: `63-1317682W38`, Batch: batch_3.csv) | Dual Registration |
| **2219** | Magdlenicosi Mosotsha (ID: `26-151900 C 26`, Batch: batch_200m2.csv) | Victor T Dzekereke (ID: `10-01 / 63-986979 N 63`, Batch: batch_4.csv) | **Re-registered** (some records Crossed Out) |
| **2234** | Emelda Chopandu (ID: `63-1478641 B 63`, Batch: batch_200m2.csv) | Nyembesi Tirhire (ID: `12-065264R12`, Batch: batch_3.csv) | Dual Registration |
| **2236** | Chipo Chivege (ID: `25-111973 X80`, Batch: batch_2.csv) | Timothy Muvengwa (ID: `18-034369Z18`, Batch: batch_3.csv) / Philemon Mudhimbo (ID: `71-0445392Z71`, Batch: batch_5.csv) | **Multi-Assignment Conflict** (3 occupants) |
| **2238** | Concilia Runzuenzue (ID: `59-034345 Q 49`, Batch: batch_1.csv) | Joseph Chimbwanda (ID: `47-053353Y47`, Batch: batch_3.csv) | Dual Registration |
| **2240** | Stella Josiyasi (ID: `63-1292561 Q 63`, Batch: batch_200m2.csv) | Tapiwa Chimukombero (ID: `48-134433K48`, Batch: batch_3.csv) | Dual Registration |
| **2243** | Charles Mahwire (ID: `04-096730 R 04`, Batch: batch_200m2.csv) | Virginia Kusaya (ID: `49-076231 D 49`, Batch: batch_4.csv) | Dual Registration |
| **2255** | Ivyjoy Bingwa (ID: `63-2189335 V 27`, Batch: batch_200m2.csv) | Jonh Mushakavanhu (ID: `08-261535D07`, Batch: batch_5.csv) | Dual Registration |
| **2273** | EDNAH Chipezaani (ID: `32-170273 M32`, Batch: batch_2.csv) | Zulectzo Willard Mangana (ID: `45-139441 U 45`, Batch: batch_200m2.csv) | Dual Registration |
| **2291** | Patrcic Chilukwe (ID: `42-230432 S 42`, Batch: batch_1.csv) | Media Karosawa (ID: `47-106772 M 47`, Batch: batch_200m2.csv) | Dual Registration |
| **2297** | Mercland Mundanga (ID: `63-1337541 S 27`, Batch: batch_200m2.csv) | Miriam Kamota (ID: `68-074753 W 68`, Batch: batch_4.csv) | Dual Registration |
| **2400** | Aaron Mudhimbu (ID: `71-051300 J 71`, Batch: batch_200m2.csv) | Laron Sabola (ID: `63-991375 R 63`, Batch: batch_200m2.csv) | Dual Registration |
| **2401** | EUNICE NKOMA (ID: `75-260447 H 75`, Batch: batch_1.csv) | Phineas Marashasimba (ID: `63-397429Y27`, Batch: batch_3.csv) | Dual Registration |
| **2416** | Andrew Muranda (ID: `32-129706 S32`, Batch: batch_2.csv) | Emanuel Chatikobo (ID: `18-069066*07`, Batch: batch_300m2.csv) | Dual Registration |
| **2464** | Gariat Mupiro & Zione Bhulaimu Zione Bhulaimu (ID: `15-132518 N 42 / 68-060184 K 68`, Batch: batch_2.csv) | Samuel Musariwa (ID: `27-140086 S 27`, Batch: batch_300m2.csv) | **Re-registered** (some records Crossed Out) |
| **2491** | Crispen Tigere (ID: `32-190449 S 86`, Batch: batch_200m2.csv) | Crispen Tigere (ID: `32-190144 9 S 80`, Batch: batch_300m2.csv) | **Exact Duplicate Entry** |
| **2613** | Fred Alice Laderera (ID: `27-152247L27`, Batch: batch_3.csv) | Lazarus Jim (ID: `48-160132T48`, Batch: batch_5.csv) | **Re-registered** (some records Crossed Out) |
| **2656** | Kennedy Mungure (ID: `63-1127718 N 42`, Batch: batch_200m2.csv) | Lee Chiripamberi (ID: `42-166643G42`, Batch: batch_300m2.csv) | Dual Registration |
| **2698** | Elson Tazvitya (ID: `83-087537P83`, Batch: batch_5.csv) | Elson Tazvitya (ID: `83-087537P83`, Batch: batch_5.csv) | **Exact Duplicate Entry** |
| **2791** | Evelyn Muendesi (ID: `70-205399 Q 70`, Batch: batch_1.csv) | Evelyn Mwendesi (ID: `70-205399G70`, Batch: batch_3.csv) | **Re-registered** (some records Crossed Out) |
| **2822** | LOT RASEKE (ID: `63-2306027 J 15`, Batch: batch_1.csv) | Benard nyatondo (ID: `75-201330m42`, Batch: batch_300m2.csv) | Dual Registration |
| **2858** | Joseph Mahlahla (ID: `63-1075967 M 44`, Batch: batch_2.csv) | Muchaneta Muvunde (ID: `63-624791W22`, Batch: batch_3.csv) | Dual Registration |
| **2911** | Sekai Marizanye (ID: `63-1378736 J 63`, Batch: batch_300m2.csv) | Sekai Marizani (ID: `63-1378736 J 63`, Batch: batch_300m2.csv) | Dual Registration |
| **3** | Tellmore mano Tariro mano (ID: `03-1272000R43`, Batch: batch_300m2.csv) | PRIVILEDGE RUZIYE (ID: `18-107305 C 18`, Batch: batch_madzimai.csv) | **Re-registered** (some records Crossed Out) |
| **3002** | Lowencia Duvu (ID: `48-258456 G 58`, Batch: batch_200m2.csv) | Taurai Kupara (ID: `63-1539424 V 42`, Batch: batch_4.csv) | Dual Registration |
| **3100** | Tapiwa Baiso (ID: `75-377837 F 75`, Batch: batch_200m2.csv) | Tapiwa Baiso (ID: `75-377837 F 75`, Batch: batch_300m2.csv) | **Exact Duplicate Entry** |
| **43** | Benard Chivhako (ID: `71-092982E71`, Batch: batch_3.csv) | Richard Tsingano (ID: `49-060987 J 49`, Batch: batch_4.csv) | **Re-registered** (some records Crossed Out) |
| **48** | Believe Makwata (ID: `13-2001085P13`, Batch: batch_3.csv) | Knowledge gambiza (ID: `27-221624W22`, Batch: batch_5.csv) | Dual Registration |
| **5** | Julias Chimbwedza (ID: `07-090475M-07`, Batch: batch_300m2.csv) | Onismore Matariranwe (ID: `04-071550y77`, Batch: batch_300m2.csv) | Dual Registration |
| **6** | Mathias Makutu (ID: `47-126324P04`, Batch: batch_300m2.csv) | Tatenda Masiki (ID: `07-203396E-07`, Batch: batch_300m2.csv) | Dual Registration |
| **6040** | Michael Kubiku (ID: `27-166936 C 27`, Batch: batch_200m2.csv) | TAWANDA MACHAKA (ID: `58-285282 R 23`, Batch: batch_4.csv) | Dual Registration |
| **6045** | Tynwald Ruvengo (ID: `03-1335731 P 70`, Batch: batch_200m2.csv) | Sabina Chidya (ID: `27-240909H27`, Batch: batch_3.csv) | **Re-registered** (some records Crossed Out) |
| **6124** | Sample Chiota (ID: `70-127221 P71`, Batch: batch_2.csv) | Thulani N Majeni (ID: `66-041156 P 66`, Batch: batch_200m2.csv) | Dual Registration |
| **6144** | Tinashe Musonza (ID: `63-1557629 H 24`, Batch: batch_2.csv) | Alice Chitait (ID: `32-100155 X 32`, Batch: batch_2.csv) / James Makombe (ID: `48-103493E48`, Batch: batch_5.csv) | **Multi-Assignment Conflict** (3 occupants) |
| **6340** | Memory Chandengenda (ID: `47-233122 Z 47`, Batch: batch_200m2.csv) | Gabriel F Akupangani (ID: `50-067934 R 50`, Batch: batch_4.csv) | Dual Registration |
| **703** | Delynn Garikai (ID: `59-009699B43`, Batch: batch_300m2.csv) | TinieL Tsodzo (ID: `18-079322L18`, Batch: batch_5.csv) | Dual Registration |
| **712** | Rosemary Nyambara (ID: `63-1153234S50`, Batch: batch_3.csv) | washington T mandizvidza (ID: `63-1227839Q80`, Batch: batch_300m2.csv) | Dual Registration |
| **785** | DAVID MURONZA (ID: `71-055309 F 71`, Batch: batch_1.csv) | Constantine Muzanenhamo (ID: `63-1217797 A 77`, Batch: batch_200m2.csv) | Dual Registration |
| **788** | Richard Magorosi (ID: `Missing`, Batch: batch_3.csv) | Tichaona Karindi (ID: `63-771918 Y 49`, Batch: batch_300m2.csv) | Dual Registration |
| **823** | Sholcombishi Mangwengwe (ID: `77-054372 T 77`, Batch: batch_200m2.csv) | David Chimudima (ID: `70-284888R70`, Batch: batch_3.csv) | Dual Registration |
| **90** | Llyod Siclube (ID: `08-874081 P 29`, Batch: batch_1.csv) | Hildah Zakeyo (ID: `37-083931 V 38`, Batch: batch_4.csv) | Dual Registration |
| **937** | Gibson Chinyepera (ID: `63-1307832 P 77`, Batch: batch_300m2.csv) | Gibson Chinyapera (ID: `63-1307832 P 77`, Batch: batch_300m2.csv) | Dual Registration |
| **952** | Tichaona Madubeko (ID: `77-019611S*77`, Batch: batch_3.csv) | Sibusisiwe & Sibanda / Philip Kadzakata (ID: `29-299459 M 03 / 63-971391 V 63`, Batch: batch_4.csv) | **Re-registered** (some records Crossed Out) |
| **New** | Dampton Pona (ID: `63-242047 N 63`, Batch: batch_200m2.csv) | Shamiso Maitenhodze (ID: `24-118110 L 24`, Batch: batch_200m2.csv) / Radson Sibanda (ID: `08-828678 N 03`, Batch: batch_200m2.csv) / Kudakwashe Seremani (ID: `63-157736 4 J 80`, Batch: batch_200m2.csv) | **Multi-Assignment Conflict** (4 occupants) |
| **New 78** | Christine Marandure (ID: `63-3272154 X 18`, Batch: batch_1.csv) | Maxwell Mbuva (ID: `38-108112 K 38`, Batch: batch_1.csv) | Dual Registration |

### B. Duplicate National ID Numbers ({len(id_rows_md)} Instances)
Members owning multiple stands or family joint registrations:

| National ID No | Member Name | Assigned Stands | Notes |
| :--- | :--- | :--- | :--- |
| `06-072598Z06` | Mercy Munenge / Ramsey Munenge | Stand Missing (batch_5.csv), Stand Missing (batch_5.csv) | Family Joint / Shared ID Registration |
| `27-201088Z27 / 27-2010558Z27` | Melody Chiwara / Petronella Chiwara | Stand 2235 (batch_3.csv), Stand 33 (batch_3.csv) | Family Joint / Shared ID Registration |
| `63-1280776F77` | Paul & Fungisai Samakanda / Zindonda / Paul & Fungisai Samakanda / Zindonda | Stand 2622 (batch_3.csv), Stand 2623 (batch_3.csv) | **Multi-Stand Owner** or Duplicate Record |
| `63-1307832 P 77` | Gibson Chinyepera / Gibson Chinyapera | Stand 937 (batch_300m2.csv), Stand 937 (batch_300m2.csv) | Family Joint / Shared ID Registration |
| `63-1378736 J 63` | Sekai Marizanye / Sekai Marizani | Stand 2911 (batch_300m2.csv), Stand 2911 (batch_300m2.csv) | Family Joint / Shared ID Registration |
| `63-1467030F85` | Godknows Godknows / Tirivenhamo / Godknows Tirivenhamo | Stand Missing (batch_5.csv), Stand Missing (batch_5.csv) | Family Joint / Shared ID Registration |
| `75-377837 F 75` | Tapiwa Baiso / Tapiwa Baiso | Stand 3100 (batch_200m2.csv), Stand 3100 (batch_300m2.csv) | **Multi-Stand Owner** or Duplicate Record |
| `83-087537P83` | Elson Tazvitya / Elson Tazvitya | Stand 2698 (batch_5.csv), Stand 2698 (batch_5.csv) | **Multi-Stand Owner** or Duplicate Record |

---

## 2. Missing & Incomplete Data Audit

* **Records Missing Stand Number:** {len(missing_stand)} non-blank records
* **Records Missing National ID:** {len(missing_id)} non-blank records
* **Records Missing Cell Number:** {len(missing_cell)} non-blank records

---

## 3. Recommended Actions & Next Steps

1. **Resolve Stand Conflicts:** Review multi-assigned stands (e.g. Stands 2236, 6144, 2, etc.) with physical ledger verification.
2. **Flag Superseded Records:** Mark crossed-out duplicates (e.g. Stand 1052 in Batch 4) as superseded in the master database.
3. **Build Interactive Search Tool:** Implement Stage 3 (Interactive Web Search Dashboard) to allow instant searching and filtering of active vs crossed-out stands.
