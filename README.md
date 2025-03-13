

---

#### **1. Script Purpose**  
Generates **all possible 6-character password combinations** (1 starting character + 5 generated characters) for security testing.  
**Warning**: For educational/ethical use only (e.g., penetration testing with authorization).

---

#### **2. Key Components**
- **Character Set**: 94 characters (lowercase, uppercase, numbers, symbols).  
- **Parallel Processing**: Uses `ProcessPoolExecutor` to generate passwords starting with each character in parallel.  
- **Compression**: Automatically compresses files into `.7z` archives when they reach **10 GB** (uncompressed).  
- **Resume Support**: Tracks progress via existing `.7z` archives to avoid redundant work.

---

#### **3. Core Functions**
| Function | Purpose |
|----------|---------|
| `extraire_dernier_mot(archive)` | Extracts the last password from a `.7z` archive. |
| `trouver_progres(caractere)` | Finds the last generated password for a starting character. |
| `mot_to_compteur(mot)` | Converts a password to a numeric counter for progress tracking. |
| `compteur_to_mot(compteur)` | Converts a numeric counter back to a password. |
| `generer_pour_caractere(caractere)` | Generates all combinations for a starting character, manages file creation/compression. |

---

#### **4. Performance Metrics**
- **Total Combinations**: \( 94^6 = 689\ 869\ 781\ 056 \) (~690 billion).  
- **Uncompressed Size**: \( 689\ \text{B} \times 7 \text{ bytes} = 4.83\ \text{TB} \).  
- **Compressed Size**: ~2.4 TB (with 7z level 3 compression).  

| Storage Type | Write Speed | Estimated Time |
|--------------|-------------|----------------|
| **HDD SATA** | 100-150 MB/s | 13-17 days. |
| **SSD NVMe** | 2-3 GB/s | 12-24 hours. |

---

#### **5. Hardware Requirements**
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **CPU** | 4 cores | 8+ cores (e.g., Ryzen 7 5800X). |
| **RAM** | 4 GB | 16 GB (for compression level 9). |
| **Storage** | 5 TB HDD | 4 TB SSD NVMe. |
| **Software** | 7-Zip installed. |

---

#### **6. Ethical & Legal Notes**
⚠️ **Critical Warnings**:  
- Generates **4.83 TB of sensitive data** (passwords).  
- Unauthorized use for malicious purposes is **illegal**.  
- Ensure physical security for storage devices.  

---

#### **7. Customization Options**
- **Adjust Compression**: Change `7z` command flags (e.g., `-mx=9` for maximum compression).  
- **Modify Character Set**: Edit the `caracteres` list.  
- **File Size Limit**: Adjust `10 * 1024**3` (10 GB) in `generer_pour_caractere`.  

---

