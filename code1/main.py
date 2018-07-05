
#import sample
import random
import urllib.request

name = random.randrange(1,1000)
print(name)

def hook( f = 0 , s=0 , t=0 ):
    total = f*s
    print(int(total/t * 100))

def download(url):
    full_name=str(name)+".mp4"
    urllib.request.urlretrieve(url, full_name, hook)

download("https://r4---sn-xmjpuxa-qxal.googlevideo.com/videoplayback?expire=1529856775&dur=205.682&pl=24&source=youtube&ratebypass=yes&requiressl=yes&key=cms1&fvip=4&fexp=23709359&lmt=1524767887551239&c=WEB&ei=p24vW6yFHoze1gLFsrzQCw&id=o-AF7xdEdhUCvcBZ_EVvHNmflLv-gTKD6OKzphXroJFfpe&itag=22&ipbits=0&mime=video%2Fmp4&sparams=dur,ei,expire,id,initcwndbps,ip,ipbits,ipbypass,itag,lmt,mime,mip,mm,mn,ms,mv,pl,ratebypass,requiressl,source&ip=88.99.12.165&signature=57BC7710F75DD7E045B08FC7008C052AF5DA2A57.8527298ED2FA29F0770806C5D52277830CB00B00&video_id=Jqs5EaAaueA&title=5+Seconds+Of+Summer+-+Youngblood&redirect_counter=1&rm=sn-4g5ed77z&req_id=3ee01a5d4ec7a3ee&cms_redirect=yes&ipbypass=yes&mip=103.211.55.208&mm=31&mn=sn-xmjpuxa-qxal&ms=au&mt=1529837802&mv=m")


