from pytube import YouTube

link=input("Ingrese la URL del video: ")
yt =YouTube(link)
videos =yt.streams.all()

video =list(enumerate(videos))

for i in video:
    print(i)

print("Escoja la opción deseada para descargar en ese formato")
dn_option =int(input("Ingrese la Opcion: "))

dn_video =videos[dn_option]
dn_video.download()

print("descarga exitosa")
