import urllib.request
import urllib

try:
    site = urllib.request.urlopen('https://www.google.com.br/')
except:
    print ('O site google não está acessível no momento')
else:
    print ('Conseguir acessar o site google')
    print (site.read())