import yt_dlp

def download_video(url, save_path='./'):
    # Video ve sesin birleşik olduğu MP4 formatını seç
    ydl_opts = {
        'outtmpl': save_path + '/%(title)s.%(ext)s',  # Video dosyasının kaydedileceği yol
        'format': 'mp4',  # Video ve sesin birleşik olduğu MP4 formatını indir
        'noplaylist': True,  # Playlist indirilmeyecek
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Video indir
            print("Video başarıyla indirildi.")
    except Exception as e:
        print(f"İndirme sırasında hata oluştu: {e}")

# Kullanıcıdan video URL'sini al
while True:
    url = input("YouTube video URL'sini girin (çıkmak için 'q' yazın): ")

    # Çıkmak için 'q' kontrolü
    if url.lower() == 'q':
        print("Programdan çıkılıyor.")
        break

    # Video indir
    download_video(url)
