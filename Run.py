#! usr/bin/python3

import os, random, time
from rich import print as cetak
from rich.panel import Panel as nel

# warna
M2, H2, K2, P2, B2, U2, O2, C2, J2 = ["[#FF0000]", "[#00FF00]", "[#FFFF00]", "[#FFFFFF]", "[#1e00ff]", "[#b900ff]", "[#EB6000]", "[#00fbff]", "[#ff14cf]"]
acak = [M2, H2, K2, B2, U2, O2, P2, C2, J2]
warna2 = random.choice(acak)
til =f"{M2}● {K2}● {H2}●"
ken = f'{M2}›{K2}›{H2}› '
tod = f' {H2}‹{K2}‹{M2}‹'


# apa aja
khodam = random.choice(['Raja Iblis','Ohio RizZ','Ambatukam','Harimau aw','Gunderwo Slebew','Lucinta Luna','Mas Adi','Om Ripan','Vina Garut','Kura-Kura Mesir','Ular Kaki 1','Bebek Kaki 2','Bakwan Jagung','Cina Setan'])

# logo
def logo():
    log = nel.fit(f'''{til}
{warna2},--. ,--.,--.               ,--.                  
|  .'   /|  ,---.  ,---.  ,-|  | ,--,--.,--,--,--.
|  .   ' |  .-.  || .-. |' .-. |' ,-.  ||        |
|  |\   \|  | |  |' '-' '\ `-' |\ '-'  ||  |  |  |
`--' '--'`--' `--' `---'  `---'  `--`--'`--`--`--'
''',title=f'{ken}{P2}Banner{tod}',style='#ff0000')
    cetak(log)
    
def cek():
    os.system('clear')
    logo()
    cetak(nel(f'{P2}         Cek Khodam Kalian Sekarang !!!',width=54,style='#FF0000'))
    cekk = input('\n[•] Tulis Nama: ')
    print('\n[!] Sedang Mengecek Khodam...');time.sleep(2)
    print('\n')
    cetak(nel('[#00FF00]     {}[#FFFFFF] Kamu Mempunya Khodam [#00FF00]{}'.format(cekk,khodam),width=54,style='#FF0000'));os.popen('play-audio Data/Audio/a.mp3')
    last = input('\n  <[Press Enter]>')
    cek()

if __name__=='__main__':
    try:
        os.system('clear')
        os.system('pkg i -y play-audio')
        os.popen('play-audio Data/Audio/music.mp3')
    except:pass
    cek()
