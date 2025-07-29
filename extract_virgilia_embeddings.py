import os
import numpy as np
import cv2
from keras_facenet import FaceNet

# Inisialisasi model FaceNet
embedder = FaceNet()

# Path folder gambar Virgilia
virgilia_dir = "dataset/virgilia"

# Cek apakah foldernya ada
if not os.path.exists(virgilia_dir):
    raise Exception(f"❌ Folder tidak ditemukan: {virgilia_dir}")

embeddings = []

# Loop semua gambar di folder
for filename in os.listdir(virgilia_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(virgilia_dir, filename)
        print(f"📷 Processing: {img_path}")

        # Baca gambar
        img = cv2.imread(img_path)
        if img is None:
            print(f"❌ Gagal membaca gambar: {img_path}")
            continue

        # Dapatkan embedding wajah
        embedding = embedder.embeddings([img])[0]
        embeddings.append(embedding)

# Simpan embeddings ke file
if embeddings:
    embeddings_array = np.mean(embeddings, axis=0)  # Ambil rata-rata kalau banyak
    os.makedirs("dataset", exist_ok=True)
    np.save("dataset/virgilia_embeddings.npy", embeddings_array)
    print(f"\n✅ Embedding Virgilia berhasil disimpan ke dataset/virgilia_embeddings.npy")
else:
    print("❌ Tidak ada embedding yang berhasil diambil.")
