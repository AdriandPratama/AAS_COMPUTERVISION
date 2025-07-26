## Nama : Adriand Pratama
## NIM : 4222201036
## Kelas : Robotika pagi A semester 6



# OCR Plat Nomor Kendaraan (VLM + LMStudio + Python)

Proyek ini bertujuan untuk melakukan **Optical Character Recognition (OCR)** pada plat nomor kendaraan menggunakan **Visual Language Model (VLM)** yang dijalankan di **LMStudio** dan diintegrasikan dengan Python.

---

## **1. Fitur Utama**
- Mengirim gambar ke model multimodal (misalnya `llava-llama-3-8b-v1_1`) di LMStudio.
- Menghasilkan prediksi plat nomor kendaraan.
- Menghitung **Character Error Rate (CER)** untuk mengevaluasi akurasi.
- Menyimpan hasil ke dalam file `results.csv` dengan format:
  ```
  image, ground_truth, prediction, CER_score
  ```

---

## **2. Persiapan**
### **A. Kebutuhan**
- Python 3.9+
- LMStudio (dijalankan lokal pada `http://127.0.0.1:1234`)
- Dataset: [Indonesian License Plate Dataset](https://www.kaggle.com/datasets/juanthomaswijaya/indonesian-license-plate-dataset)

### **B. Install Library**
Jalankan perintah berikut:
```bash
pip install requests editdistance pillow
```

---

## **3. Cara Menjalankan**
1. Jalankan LMStudio pada mode server:
   - Pastikan API LM Studio aktif `http://127.0.0.1:1234`.
2. Pastikan struktur folder seperti ini:
   ```
   project/
   ├─ main.py
   ├─ data.csv        # File label ground truth
   ├─ test/           # Folder gambar uji
   ├─ README.md       # File penjelasan instruksi code
   └─ results.csv     # Hasil output (akan dibuat otomatis)
   ```
3. Jalankan program:
   ```bash
   python main.py
   ```

---

## **4. Output**
- Program akan menampilkan hasil prediksi di terminal:
  ```
  Memproses B1234XYZ.jpg...
   → Ground Truth : B1234XYZ
   → Prediksi     : B1234XYZ
   → CER          : 0.0000
  ```
- Semua hasil tersimpan di file `results.csv`.

---

## **5. Evaluasi CER**
Character Error Rate dihitung dengan rumus:
```
CER = (S + D + I) / N
```
- **S** = jumlah karakter salah (substitusi).
- **D** = jumlah karakter yang dihapus.
- **I** = jumlah karakter yang disisipkan.
- **N** = jumlah karakter pada ground truth.

---

## **6. Referensi**
- [LMStudio Documentation](https://lmstudio.ai/docs/python/llm-prediction/image-input)
- [Indonesian License Plate Dataset](https://www.kaggle.com/datasets/juanthomaswijaya/indonesian-license-plate-dataset)

---

## **7. Video Penjelasan**
Video penjelasan proyek ini dapat dilihat di YouTube ([Video penjelasan code](https://youtu.be/ZCQYcXgHY5E)).
