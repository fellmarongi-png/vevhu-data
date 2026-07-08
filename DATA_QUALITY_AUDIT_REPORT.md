# Master Data Quality & Audit Report (Batches 1 - 8)

## Executive Summary
This report summarizes the consolidation, data cleansing, and multi-batch quality audit across all 8 extracted ledger batches (`batch_1.csv` through `batch_5.csv`, `batch_200m2.csv`, `batch_300m2.csv`, and `batch_madzimai.csv`).

* **Total Records Analyzed:** 1280
* **Active Records:** 1064 (83.1%)
* **Crossed-Out Records:** 96 (7.5%)
* **Blank Ledger Rows:** 120 (9.4%)
* **Consolidated Master Dataset:** [`master_vevhu_database.csv`](./master_vevhu_database.csv)

---

## 1. Multi-Batch Deduplication Audit

### A. Stand Number Conflicts (100 Instances)
Stands assigned to multiple records or re-registered across batches:

| Cleaned Stand No | Primary Record | Secondary / Duplicate Record | Audit Status |
| :--- | :--- | :--- | :--- |
| **1052** | Wellmah Gamanya (ID: `15-128978 Q 15`, Batch: batch_1.csv) | Beatre Ciati (ID: `63-877786 Q 63`, Batch: batch_4.csv) | **Re-registered** (some records Crossed Out) |
| **1297** | Christopher Nyanji (ID: `07-108464 C 07`, Batch: batch_200m2_7july_2026.csv) | Christopher Munganja (ID: `27-108464C07`, Batch: batch_200m2_7july_2026.csv) | **Re-registered** (some records Crossed Out) |
| **1351** | Simbarashe Munganja (ID: `07-132044 W 07`, Batch: batch_200m2_7july_2026.csv) | Simbarashe Munganja (ID: `27-132044W07`, Batch: batch_200m2_7july_2026.csv) | **Re-registered** (some records Crossed Out) |
| **1456** | Willard Banzi (ID: `70-132974 S 70`, Batch: batch_200m2.csv) | Jonothan Kafumbata (ID: `63-981103 B63`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **1463** | Morgan Sekai (ID: `63-1046107 F 75`, Batch: batch_200m2.csv) | Absent Absai Matagg (ID: `24-181122C11`, Batch: batch_5.csv) | Dual Registration |
| **1512** | Tafadzwa Mhembee (ID: `15-142281 A 15`, Batch: batch_200m2_7july_2026.csv) | Tafadzwa mhembere (ID: `15-142281A15`, Batch: batch_5.csv) | Dual Registration |
| **1548** | Ndaizivei Mbamba (ID: `18-057624B18`, Batch: batch_3.csv) | Enera Chiwara (ID: `27-178349H27`, Batch: batch_3.csv) | Dual Registration |
| **1560** | Austin Matsiuke (ID: `79-1259227 R 83`, Batch: batch_1.csv) | Mary Josiyasi (ID: `63-137844 P 63`, Batch: batch_2.csv) | Dual Registration |
| **16** | Ingidzai Chipfuwa (ID: `48-102952Z48`, Batch: batch_3.csv) | Clayton Sanyamandwe (ID: `34-072397 N 34`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **1617** | Colin Chikutirgwe (ID: `63-925316 F 34`, Batch: batch_1.csv) | Dickson Chigariro (ID: `63-122635 Y 18`, Batch: batch_200m2.csv) | Dual Registration |
| **1654** | Osward Chiworeso (ID: `47-138059 V 47`, Batch: batch_200m2.csv) | Kudzanai Annamore / Mahenga Chibenga (ID: `63-138478 Z 43 / 22-270301 Y 75`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **1780** | Grace Sagara (ID: `63-1237241K34`, Batch: batch_3.csv) | Owen Matenda (ID: `13-170002T13`, Batch: batch_5.csv) | Dual Registration |
| **1830** | Mabbie Sedze (ID: `34-056376 P 34`, Batch: batch_1.csv) | Patrick chando (ID: `07-108658 B 07`, Batch: batch_4.csv) | Dual Registration |
| **1951** | Diymus Mandinenga (ID: `42-194709 N 42`, Batch: batch_200m2.csv) | Didymus Mandivenga (ID: `42-194709N42`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **1962** | Maria Willard (ID: `63-1042470 C 63`, Batch: batch_200m2.csv) | Kudakwashe Shambamuto (ID: `63-914885 A 32`, Batch: batch_200m2_7july_2026.csv) / Kudakwashe Shambamuto (ID: `63-1585140 L 32`, Batch: batch_200m2_7july_2026.csv) | **Re-registered** (some records Crossed Out) |
| **1976** | Aman White Abudula (ID: `63-1640867 J 63`, Batch: batch_200m2.csv) | Zgoriri Tamai (ID: `38-189033 S 38`, Batch: batch_200m2.csv) | Dual Registration |
| **2024** | Prescious Mango (ID: `86-037309 Q 86`, Batch: batch_200m2.csv) | Jacob & Melody Chitaitai & Mapako (ID: `42-229243A42`, Batch: batch_3.csv) | Dual Registration |
| **2028** | Fanwell Murenga (ID: `38-057238 M 38`, Batch: batch_200m2.csv) | JUSTICE SHAYAMANO (ID: `63-1321916 J 18`, Batch: batch_200m2_7july_2026.csv) / Justice Mushayamano (ID: `63-1321916 Y 18`, Batch: batch_200m2_7july_2026.csv) | **Multi-Assignment Conflict** (3 occupants) |
| **2155** | Eddmore Masinire (ID: `63-1311460H32`, Batch: batch_5.csv) | James Chidhimira (ID: `22-145205Z22`, Batch: batch_5.csv) | Dual Registration |
| **2169** | Maggie Chigoya (ID: `Missing`, Batch: batch_200m2_7july_2026.csv) | Tawanda Shava (ID: `63-1017121Z26`, Batch: batch_300m2.csv) | Dual Registration |
| **2195** | Benedict Chilekeshe (ID: `63-423762W42`, Batch: batch_200m2_7july_2026.csv) | Rumbidzai A Janda (ID: `59-111719 L07`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **2207** | Phillip M Denhere (ID: `63-1352039 Q 11`, Batch: batch_1.csv) | CHIPO B ZHOU (ID: `38-241009 N 38`, Batch: batch_200m2_7july_2026.csv) / SEVERA CHIMONYO (ID: `634-096039 L 34`, Batch: batch_200m2_7july_2026.csv) | **Multi-Assignment Conflict** (3 occupants) |
| **2208** | Vengai Mazivise (ID: `63-1191877B04`, Batch: batch_200m2_7july_2026.csv) | Noah CHINDA (ID: `63-157575 K50`, Batch: batch_300m2_7july_2026.csv) / Cephas Manyemba (ID: `34-103771Q34`, Batch: batch_5.csv) | **Re-registered** (some records Crossed Out) |
| **2212** | Caston Mukungurutse (ID: `18-057063 T 18`, Batch: batch_200m2.csv) | Caroline Mudzingwa (ID: `63-1317682W38`, Batch: batch_3.csv) | Dual Registration |
| **2214** | Richard Tikiti (ID: `48-065579 F 42`, Batch: batch_1.csv) | Blessing G Pasipamire (ID: `32-068374C32`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **2218** | Luzaris C Vambe (ID: `63-593140C47`, Batch: batch_200m2_7july_2026.csv) | BEAULAH CHIBUUPE (ID: `68-1364631 C 63`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **2219** | Magdlenicosi Mosotsha (ID: `26-151900 C 26`, Batch: batch_200m2.csv) | Primrose R Chinyu (ID: `43-136787L43`, Batch: batch_200m2_7july_2026.csv) / Victor T Dzekereke (ID: `10-01 / 63-986979 N 63`, Batch: batch_4.csv) | **Re-registered** (some records Crossed Out) |
| **2221** | Edgar Matomba (ID: `63-1016188 L 67`, Batch: batch_200m2_7july_2026.csv) | Biggie Soko (ID: `15-115277J15`, Batch: batch_5.csv) | Dual Registration |
| **2224** | BLESSING MUKAMBACHIZA (ID: `63-1009818 M 42`, Batch: batch_1.csv) | Farisai Zhou (ID: `27-213220 L03`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **2231** | Florence Nhete (ID: `63-102360 5 X 63`, Batch: batch_200m2_7july_2026.csv) | Issiah Mukodza (ID: `50-053056V50`, Batch: batch_300m2.csv) | Dual Registration |
| **2232** | Christopher Chiwandire (ID: `49-035288A49`, Batch: batch_200m2_7july_2026.csv) | Margret / Manyundwa (ID: `22-274349y 40 / J04`, Batch: batch_300m2.csv) | **Re-registered** (some records Crossed Out) |
| **2234** | Emelda Chopandu (ID: `63-1478641 B 63`, Batch: batch_200m2.csv) | Nyembesi Tirhire (ID: `12-065264R12`, Batch: batch_3.csv) | Dual Registration |
| **2236** | Chipo Chivege (ID: `25-111973 X80`, Batch: batch_2.csv) | Timothy Muvengwa (ID: `18-034369Z18`, Batch: batch_3.csv) / Philemon Mudhimbo (ID: `71-0445392Z71`, Batch: batch_5.csv) | **Multi-Assignment Conflict** (3 occupants) |
| **2238** | Concilia Runzuenzue (ID: `59-034345 Q 49`, Batch: batch_1.csv) | Joseph Chimbwanda (ID: `47-053353Y47`, Batch: batch_3.csv) | Dual Registration |
| **2240** | Stella Josiyasi (ID: `63-1292561 Q 63`, Batch: batch_200m2.csv) | Tapiwa Chimukombero (ID: `48-134433K48`, Batch: batch_3.csv) / Juwel Chikuradz a (ID: `50-006384 P 83`, Batch: batch_300m2_7july_2026.csv) | **Multi-Assignment Conflict** (3 occupants) |
| **2243** | Charles Mahwire (ID: `04-096730 R 04`, Batch: batch_200m2.csv) | Virginia Kusaya (ID: `49-076231 D 49`, Batch: batch_4.csv) | Dual Registration |
| **2245** | Julias chimbwedza (ID: `07-090475M-07`, Batch: batch_300m2.csv) | Blessing Chagadana (ID: `63-1571823L86`, Batch: batch_5.csv) | Dual Registration |
| **2255** | Ivyjoy Bingwa (ID: `63-2189335 V 27`, Batch: batch_200m2.csv) | Jonh Mushakavanhu (ID: `08-261535D07`, Batch: batch_5.csv) | Dual Registration |
| **2258** | KENETH SAKWE (ID: `63-1486939 W 61`, Batch: batch_200m2_7july_2026.csv) | Deliwe Matsi (ID: `63-8331237D63`, Batch: batch_5.csv) | Dual Registration |
| **2273** | EDNAH Chipezaani (ID: `32-170273 M32`, Batch: batch_2.csv) | Zulectzo Willard Mangana (ID: `45-139441 U 45`, Batch: batch_200m2.csv) | Dual Registration |
| **2290** | Takawiro Madamombe (ID: `45-124403 N 45`, Batch: batch_1.csv) | SHERYL GWAVAVA (ID: `68-2806586 R 18`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **2291** | Patrcic Chilukwe (ID: `42-230432 S 42`, Batch: batch_1.csv) | Media Karosawa (ID: `47-106772 M 47`, Batch: batch_200m2.csv) | Dual Registration |
| **2297** | Mercland Mundanga (ID: `63-1337541 S 27`, Batch: batch_200m2.csv) | Miriam Kamota (ID: `68-074753 W 68`, Batch: batch_4.csv) | Dual Registration |
| **2362** | Gibson Mushango (ID: `24-085436W24`, Batch: batch_300m2.csv) | Eunice Chamburuka (ID: `63-535085 Z 71`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **2376** | Richard Shambamuto (ID: `63-914885 A32`, Batch: batch_300m2_7july_2026.csv) | TAURAI MUTONHODZA (ID: `63-1415941 Z 83`, Batch: batch_4.csv) | Dual Registration |
| **2400** | Aaron Mudhimbu (ID: `71-051300 J 71`, Batch: batch_200m2.csv) | Laron Sabola (ID: `63-991375 R 63`, Batch: batch_200m2.csv) | Dual Registration |
| **2401** | EUNICE NKOMA (ID: `75-260447 H 75`, Batch: batch_1.csv) | Phineas Marashasimba (ID: `63-397429Y27`, Batch: batch_3.csv) | Dual Registration |
| **2413** | Lorraine Chisango (ID: `63-2404356N18`, Batch: batch_200m2_7july_2026.csv) | Paradzai Francis (ID: `68-063485X86`, Batch: batch_300m2.csv) | **Re-registered** (some records Crossed Out) |
| **2414** | Claude Chidamba (ID: `63-88 / 63-1211868 F 25`, Batch: batch_200m2_7july_2026.csv) | Tapywa J Mukungwa (ID: `75-42292J75`, Batch: batch_300m2.csv) | **Re-registered** (some records Crossed Out) |
| **2416** | Andrew Muranda (ID: `32-129706 S32`, Batch: batch_2.csv) | Emanuel Chatikobo (ID: `18-069066*07`, Batch: batch_300m2.csv) | Dual Registration |
| **2426** | Tstitsi Muzonda (ID: `42-129074 W 44`, Batch: batch_200m2_7july_2026.csv) | Tebithar Evidance Saunyama / Zinge Sanga (ID: `63-1510706E85 / 63-1547114D42`, Batch: batch_300m2.csv) | Dual Registration |
| **2464** | Gariat Mupiro & Zione Bhulaimu Zione Bhulaimu (ID: `15-132518 N 42 / 68-060184 K 68`, Batch: batch_2.csv) | Samuel Musariwa (ID: `27-140086S27`, Batch: batch_300m2.csv) | **Re-registered** (some records Crossed Out) |
| **2491** | Crispen Tigere (ID: `32-190449 S 86`, Batch: batch_200m2.csv) | Crispen Tigere (ID: `32-190144 9 S 80`, Batch: batch_300m2.csv) | **Exact Duplicate Entry** |
| **2599** | Tendai Baera (ID: `63-1077950 S 70`, Batch: batch_300m2_7july_2026.csv) | Hilary V Sazunza (ID: `63-849478 F 24`, Batch: batch_4.csv) | Dual Registration |
| **2613** | Fred Alice Laderera (ID: `27-152247L27`, Batch: batch_3.csv) | Lazarus Jim (ID: `48-160132T48`, Batch: batch_5.csv) | **Re-registered** (some records Crossed Out) |
| **2648** | Delois Zindoga (ID: `18-089451 W 18`, Batch: batch_200m2.csv) | Nyanyiwa Katsa (ID: `49-032416 O 49`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **2656** | Kennedy Mungure (ID: `63-1127718 N 42`, Batch: batch_200m2.csv) | Lee. Chiripamberi (ID: `42-166643G42`, Batch: batch_300m2.csv) | Dual Registration |
| **2660** | Edmore Marapira (ID: `63-1169157F42`, Batch: batch_300m2.csv) | Phillip Nyamuchira (ID: `45-073091 P 45`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **2680** | Cecilia Mutemasango (ID: `86-059116R86`, Batch: batch_200m2_7july_2026.csv) | CECILIA MUTEMASANGO (ID: `86-059116 R 86`, Batch: batch_200m2_7july_2026.csv) | **Re-registered** (some records Crossed Out) |
| **2695** | Gurure Takaitei (ID: `47-087000 W 85`, Batch: batch_2.csv) | Onismore. Matariranwe (ID: `74-071550y77`, Batch: batch_300m2.csv) | Dual Registration |
| **2698** | Elson Tazvitya (ID: `83-087537P83`, Batch: batch_5.csv) | Elson Tazvitya (ID: `83-087537P83`, Batch: batch_5.csv) | **Exact Duplicate Entry** |
| **2703** | Chamunorwa Muzanenhamo (ID: `24-099430g24`, Batch: batch_200m2_7july_2026.csv) | Delynn Garikai (ID: `59-009699B43`, Batch: batch_300m2.csv) | Dual Registration |
| **2743** | Aman Ndengu (ID: `80-036450J80`, Batch: batch_200m2_7july_2026.csv) | Sandra T Jerekete (ID: `63-122499O44`, Batch: batch_3.csv) | Dual Registration |
| **2772** | Samson Kayerenga (ID: `11-056079 B 71`, Batch: batch_200m2_7july_2026.csv) | Samson Kayerenga (ID: `11-056079R71`, Batch: batch_200m2_7july_2026.csv) / James Makahwi (ID: `63-1178863 F 75`, Batch: batch_300m2_7july_2026.csv) | **Multi-Assignment Conflict** (3 occupants) |
| **2791** | Evelyn Muendesi (ID: `70-205399 Q 70`, Batch: batch_1.csv) | Evelyn Mwendesi (ID: `70-205399G70`, Batch: batch_3.csv) | **Re-registered** (some records Crossed Out) |
| **2792** | Anesu S Kachisi (ID: `63-2660877 Q 85`, Batch: batch_200m2.csv) | Theophilars Nyanganza (ID: `63-1532177 S 43`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **2798** | Alfred Mutihwana (ID: `47-229592 M 47`, Batch: batch_300m2_7july_2026.csv) | Alfred Mutihwana (ID: `47-229592 M 47`, Batch: batch_300m2_7july_2026.csv) | **Re-registered** (some records Crossed Out) |
| **2800** | Phirison Hebson (ID: `63-1474803 E 63`, Batch: batch_200m2.csv) | Mafios Musaryurwa (ID: `70-226635 Y 70`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **2802** | NEVER NGANDA (ID: `34-096189 Z 34`, Batch: batch_1.csv) | Tafadzwa Y Magaya (ID: `63-1355021 Y 80`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **2822** | LOT RASEKE (ID: `63-2306027 J 15`, Batch: batch_1.csv) | Benard nyatondo (ID: `75-201330m42`, Batch: batch_300m2.csv) | Dual Registration |
| **2831** | Nyasha Machingauta / Nyakuma (ID: `08-888640P71`, Batch: batch_3.csv) | Nyasha Nyahumba (ID: `08-88864 P 71 / 63-`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **2835** | Genicus N Muriritirwo (ID: `63-2796763 S 18`, Batch: batch_2.csv) | Spiwe G MACHINSAUTA (ID: `63-1073217 Y 80`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **2852** | JELLY NYAMWANDURA (ID: `48-063431 J 48`, Batch: batch_200m2_7july_2026.csv) | Job Grese (ID: `71-147566 K 18`, Batch: batch_300m2_7july_2026.csv) | **Re-registered** (some records Crossed Out) |
| **2858** | Joseph Mahlahla (ID: `63-1075967 M 44`, Batch: batch_2.csv) | Muchaneta Muvunde (ID: `63-624791W22`, Batch: batch_3.csv) / Cleopatra Chilcerema (ID: `63-120376 S54`, Batch: batch_300m2_7july_2026.csv) | **Multi-Assignment Conflict** (3 occupants) |
| **2911** | Sekai Marizanye (ID: `63-1378736 J 63`, Batch: batch_300m2.csv) | Sekai Marizani (ID: `63-1378736 J 63`, Batch: batch_300m2.csv) | Dual Registration |
| **3002** | Lowencia Duvu (ID: `48-258456 G 58`, Batch: batch_200m2.csv) | Taurai Kupara (ID: `63-1539424 V 42`, Batch: batch_4.csv) | Dual Registration |
| **3050** | Edson Mugachi (ID: `42-215828 T 42`, Batch: batch_200m2_7july_2026.csv) | Brighton Chamboko (ID: `49-055333N49`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **3100** | Tapiwa Baiso (ID: `75-377837 F 75`, Batch: batch_200m2.csv) | Tapiwo Baiso (ID: `75-377837F75`, Batch: batch_300m2.csv) | Dual Registration |
| **43** | Benard Chivhako (ID: `71-092982E71`, Batch: batch_3.csv) | Richard Tsingano (ID: `49-060987 J 49`, Batch: batch_4.csv) | **Re-registered** (some records Crossed Out) |
| **48** | Believe Makwata (ID: `13-2001085P13`, Batch: batch_3.csv) | Knowledge gambiza (ID: `27-221624W22`, Batch: batch_5.csv) | Dual Registration |
| **6040** | Michael Kubiku (ID: `27-166936 C 27`, Batch: batch_200m2.csv) | TAWANDA MACHAKA (ID: `58-285282 R 23`, Batch: batch_4.csv) | Dual Registration |
| **6045** | Tynwald Ruvengo (ID: `03-1335731 P 70`, Batch: batch_200m2.csv) | Sabina Chidya (ID: `27-240909H27`, Batch: batch_3.csv) | **Re-registered** (some records Crossed Out) |
| **6058** | Terence Nhingwani (ID: `63-1567421 B71`, Batch: batch_2.csv) | Maxwell Mutesva (ID: `Missing`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |
| **6124** | Sample Chiota (ID: `70-127221 P71`, Batch: batch_2.csv) | Thulani N Majeni (ID: `66-041156 P 66`, Batch: batch_200m2.csv) | Dual Registration |
| **6144** | Tinashe Musonza (ID: `63-1557629 H 24`, Batch: batch_2.csv) | Alice Chitait (ID: `32-100155 X 32`, Batch: batch_2.csv) / James Makombe (ID: `48-103493E48`, Batch: batch_5.csv) | **Multi-Assignment Conflict** (3 occupants) |
| **6178** | Patience Chingaro (ID: `44-078974 C 44`, Batch: batch_200m2.csv) | Mervin Kucherera (ID: `63-910479L42`, Batch: batch_300m2.csv) | Dual Registration |
| **6340** | Memory Chandengenda (ID: `47-233122 Z 47`, Batch: batch_200m2.csv) | Gabriel F Akupangani (ID: `50-067934 R 50`, Batch: batch_4.csv) | Dual Registration |
| **6372** | Nyarai M Mwanda (ID: `71-080664D71`, Batch: batch_200m2_7july_2026.csv) | Lytan Kumbula (ID: `47-091963D47`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **785** | DAVID MURONZA (ID: `71-055309 F 71`, Batch: batch_1.csv) | Constantine Muzanenhamo (ID: `63-1217797 A 77`, Batch: batch_200m2.csv) | Dual Registration |
| **788** | Richard Magorosi (ID: `Missing`, Batch: batch_3.csv) | Tichaona / Karindi (ID: `63-771918Y49`, Batch: batch_300m2.csv) | Dual Registration |
| **810** | ELIZABETH MANDEBVU (ID: `25-038976 S 44`, Batch: batch_1.csv) | Ranganai J Chitewhe (ID: `63-935079A11`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **823** | Sholcombishi Mangwengwe (ID: `77-054372 T 77`, Batch: batch_200m2.csv) | David Chimudima (ID: `70-284888R70`, Batch: batch_3.csv) | Dual Registration |
| **90** | Llyod Siclube (ID: `08-874081 P 29`, Batch: batch_1.csv) | Hildah Zakeyo (ID: `37-083931 V 38`, Batch: batch_4.csv) | Dual Registration |
| **937** | Gibson Chinyopera (ID: `63-1307832P77`, Batch: batch_300m2.csv) | Gibson Chinyopera (ID: `63-1307832P77`, Batch: batch_300m2.csv) | **Exact Duplicate Entry** |
| **952** | Tichaona Madubeko (ID: `77-019611S*77`, Batch: batch_3.csv) | Sibusisiwe & Sibanda / Philip Kadzakata (ID: `29-299459 M 03 / 63-971391 V 63`, Batch: batch_4.csv) | **Re-registered** (some records Crossed Out) |
| **967** | HEZEKIA HWACHI (ID: `27-091913 F 27`, Batch: batch_200m2_7july_2026.csv) | Willard Dutiro (ID: `32-137233 Z 86`, Batch: batch_4.csv) | Dual Registration |
| **New** | Dampton Pona (ID: `63-242047 N 63`, Batch: batch_200m2.csv) | Shamiso Maitenhodze (ID: `24-118110 L 24`, Batch: batch_200m2.csv) / Radson Sibanda (ID: `08-828678 N 03`, Batch: batch_200m2.csv) / Kudakwashe Seremani (ID: `63-157736 4 J 80`, Batch: batch_200m2.csv) / Rudo Samamyanga (ID: `63-1655745Q42`, Batch: batch_200m2_7july_2026.csv) | **Multi-Assignment Conflict** (5 occupants) |
| **New 45** | Chigedzo Taguta (ID: `63-1213589 B 42`, Batch: batch_200m2.csv) | Blessmore Mashama (ID: `61-086957Q61`, Batch: batch_200m2_7july_2026.csv) | Dual Registration |
| **New 78** | Christine Marandure (ID: `63-3272154 X 18`, Batch: batch_1.csv) | Maxwell Mbuva (ID: `38-108112 K 38`, Batch: batch_1.csv) | Dual Registration |
| **Y** | Sarudzai Arufaya (ID: `47 192778 X 49`, Batch: batch_200m2_7july_2026.csv) | Calister Tikiti (ID: `42-138127 L 42`, Batch: batch_300m2_7july_2026.csv) | Dual Registration |

### B. Duplicate National ID Numbers ({len(id_rows_md)} Instances)
Members owning multiple stands or family joint registrations:

| National ID No | Member Name | Assigned Stands | Notes |
| :--- | :--- | :--- | :--- |
| `06-072598Z06` | Mercy Munenge / Ramsey Munenge | Stand Missing (batch_5.csv), Stand Missing (batch_5.csv) | Family Joint / Shared ID Registration |
| `25-20003 56 E 25` | Kudakwashe Mapfumo / Kudakwashe Mapfumo | Stand 15 04 (batch_200m2_7july_2026.csv), Stand 1504 (batch_200m2_7july_2026.csv) | **Multi-Stand Owner** or Duplicate Record |
| `27-201088Z27 / 27-2010558Z27` | Melody Chiwara / Petronella Chiwara | Stand 2235 (batch_3.csv), Stand 33 (batch_3.csv) | Family Joint / Shared ID Registration |
| `34-103771Q34` | Cephas Manyemba / Cephas Manyemba | Stand 2904 (batch_200m2_7july_2026.csv), Stand 2208 (batch_5.csv) | **Multi-Stand Owner** or Duplicate Record |
| `47-229592 M 47` | Alfred Mutihwana / Alfred Mutihwana | Stand 2798 (batch_300m2_7july_2026.csv), Stand 2798 (batch_300m2_7july_2026.csv) | **Multi-Stand Owner** or Duplicate Record |
| `63-1046107 F 75` | Morgan Sekai / Sekai Morgan | Stand 1463 (batch_200m2.csv), Stand 1564 (batch_200m2_7july_2026.csv) | Family Joint / Shared ID Registration |
| `63-1211882 V 18` | TICHAONA T NOORO / TICHAOMA T NDORO | Stand 922 (batch_200m2_7july_2026.csv), Stand 1339 (batch_200m2_7july_2026.csv) | Family Joint / Shared ID Registration |
| `63-1280776F77` | Paul & Fungisai Samakanda / Zindonda / Paul & Fungisai Samakanda / Zindonda | Stand 2622 (batch_3.csv), Stand 2623 (batch_3.csv) | **Multi-Stand Owner** or Duplicate Record |
| `63-1307832P77` | Gibson Chinyopera / Gibson Chinyopera | Stand 937 (batch_300m2.csv), Stand 937 (batch_300m2.csv) | **Multi-Stand Owner** or Duplicate Record |
| `63-1378736 J 63` | Sekai Marizanye / Sekai Marizani | Stand 2911 (batch_300m2.csv), Stand 2911 (batch_300m2.csv) | Family Joint / Shared ID Registration |
| `63-1467030F85` | Godknows Godknows / Tirivenhamo / Godknows Tirivenhamo | Stand Missing (batch_5.csv), Stand Missing (batch_5.csv) | Family Joint / Shared ID Registration |
| `63-833409 P 63` | Charles Mtoso / Charles Mtoso | Stand Missing (batch_300m2_7july_2026.csv), Stand Kambarami (batch_300m2_7july_2026.csv) | **Multi-Stand Owner** or Duplicate Record |
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
