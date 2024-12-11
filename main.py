import yt_dlp

def download_video(url, save_path='./'):
    ydl_opts = {
        'outtmpl': save_path + '/%(title)s.%(ext)s',
        'format': 'mp4',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Video başarıyla indirildi.")
    except Exception as e:
        print(f"İndirme sırasında hata oluştu: {e}")

while True:
    url = input("YouTube video URL'sini girin (çıkmak için 'q' yazın): ")

    if url.lower() == 'q':
        print("Programdan çıkılıyor.")
        break

    download_video(url)
