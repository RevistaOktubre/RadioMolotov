import os

BASE_FILE = "base.html"
OUTPUT_FILE = "index.html"
SONGS_FOLDER = "canciones"

# Leer canciones
songs = []
for file in os.listdir(SONGS_FOLDER):
    if file.endswith(".mp3"):
        songs.append(f'"canciones/{file}"')

songs.sort()

# Convertir a string JS
songs_js = ",\n    ".join(songs)

# Leer base
with open(BASE_FILE, "r", encoding="utf-8") as f:
    base_content = f.read()

# Reemplazar placeholder
final_content = base_content.replace("<!-- SONGS_PLACEHOLDER -->", songs_js)

# Escribir index.html
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(final_content)

print("index.html generado correctamente.")