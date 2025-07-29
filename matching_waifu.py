import os
import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

waifu_folder = "waifu"

# Ambil semua file gambar
waifu_files = sorted([
    f for f in os.listdir(waifu_folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

# Pilih 100 waifu acak
sampled_waifu = random.sample(waifu_files, 100)

# Bikin skor jarak acak (semakin kecil makin mirip)
fake_results = []
for name in sampled_waifu:
    fake_distance = round(random.uniform(0.5, 1.2), 4)
    fake_results.append((name, fake_distance))

# Urutin yang paling 'mirip'
fake_results.sort(key=lambda x: x[1])
top_matches = fake_results[:3]

# Print hasilnya
print("💘 Top 3 Waifu Tercocok (versi random):")
for i, (name, dist) in enumerate(top_matches, 1):
    print(f"{i}. {name} - Skor: {dist}")

# Tampilkan gambarnya
plt.figure(figsize=(12, 4))
for idx, (name, dist) in enumerate(top_matches):
    img_path = os.path.join(waifu_folder, name)
    img = mpimg.imread(img_path)
    plt.subplot(1, 3, idx + 1)
    plt.imshow(img)
    plt.title(f"{name}\nSkor: {dist}")
    plt.axis('off')

# Tanpa judul atas:
# plt.suptitle("❤️ Top 3 Waifu ", fontsize=16)

plt.tight_layout()
plt.show()
