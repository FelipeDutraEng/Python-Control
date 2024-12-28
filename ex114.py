import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://www.cursoemvideo.com.br')
except urllib.error.URLError:
    print('O site Curso em Vídeo não está acessível no momento.')
else:
    print('Consegui acessar o site Curso em Vídeo com sucesso!')
    print(site.read())