import os
import csv
import requests
import base64
import editdistance

# --- Konfigurasi ---
LMSTUDIO_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
TEST_FOLDER = "F:/SEMESTER_6/COMPUTERVISION/anacondacomputervision/project_uas3/test"
LABEL_FILE = "data.csv"   # File CSV yang berisi ground truth
RESULT_FILE = "results.csv"

# --- Hitung CER ---
def calculate_cer(pred, truth):
    return editdistance.eval(pred, truth) / len(truth) if truth else 1.0

def encode_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')
# --- Fungsi OCR ke LMStudio ---
def ocr_lmstudio(image_path):
    img_b64 = encode_image(image_path)
    payload = {
        "model": "llava-llama-3-8b-v1_1",
        "messages": [
            {"role": "system", "content": "You are an OCR assistant. Only output a valid license plate number."},
            {"role": "user", "content": [
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}},
                {"type": "text", "text": "ONLY return the license plate number in this format: B1234XYZ. No words, no spaces, no explanation."}
            ]}
        ],
        "temperature": 0,
        "max_tokens": 20
    }

    response = requests.post(LMSTUDIO_API_URL, json=payload)
    result = response.json()
    raw_prediction = result.get("choices", [{}])[0].get("message", {}).get("content", "").strip().upper()

    # 1. Cari pola plat nomor Indonesia
    import re
    match = re.search(r"[A-Z]{1,2}\d{1,4}[A-Z]{1,3}", raw_prediction)
    if match:
        return match.group(0)
    else:
        # 2. Fallback: hanya huruf/angka max 9 karakter
        cleaned = ''.join(c for c in raw_prediction if c.isalnum())
        return cleaned[:9]

# --- Load Ground Truth dari data.csv ---
gt_dict = {}
with open(LABEL_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        gt_dict[row["image"]] = row["data"]

# --- Proses Semua Gambar & Simpan Hasil ---
with open(RESULT_FILE, "w", newline="") as res_file:
    writer = csv.writer(res_file)
    writer.writerow(["image", "ground_truth", "prediction", "CER_score"])

    for file in os.listdir(TEST_FOLDER):
        if file.lower().endswith(".jpg"):
            image_path = os.path.join(TEST_FOLDER, file)
            ground_truth = gt_dict.get(file, "")
            prediction = ocr_lmstudio(image_path)
            cer = calculate_cer(prediction, ground_truth)
            print(f"Memproses {file}...")
            print(f"  → Ground Truth : {ground_truth}")
            print(f"  → Prediksi     : {prediction}")
            print(f"  → CER          : {cer:.4f}")
            writer.writerow([file, ground_truth, prediction, cer])
