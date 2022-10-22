#! /usr/bin/python3

banner1 = r'''
#########################################################################
#      ____            _           _   __  __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                   |__/                                                #
#                                  >> https://github.com/benmoose39     #
#########################################################################

##################################################################################################################################################################
#     ___           ___           ___                         ___           ___                       ___           ___                                          #
#     /\__\         /\  \         /\__\                       /\  \         /\  \                     /\__\         /\__\         _____                          #
#    /:/  /        /::\  \       /:/ _/_         ___         /::\  \       |::\  \       ___         /::|  |       /:/ _/_       /::\  \                         #
#   /:/  /        /:/\:\  \     /:/ /\  \       /\__\       /:/\:\  \      |:|:\  \     /\__\       /:/:|  |      /:/ /\__\     /:/\:\  \                        #
#  /:/  /  ___   /:/  \:\  \   /:/ /::\  \     /:/  /      /:/  \:\  \   __|:|\:\  \   /:/__/      /:/|:|  |__   /:/ /:/ _/_   /:/  \:\__\                       #
# /:/__/  /\__\ /:/__/ \:\__\ /:/_/:/\:\__\   /:/__/      /:/__/ \:\__\ /::::|_\:\__\ /::\  \     /:/ |:| /\__\ /:/_/:/ /\__\ /:/__/ \:|__|                      #
# \:\  \ /:/  / \:\  \ /:/  / \:\/:/ /:/  /  /::\  \      \:\  \ /:/  / \:\~~\  \/__/ \/\:\  \__  \/__|:|/:/  / \:\/:/ /:/  / \:\  \ /:/  /                      #
#  \:\  /:/  /   \:\  /:/  /   \::/ /:/  /  /:/\:\  \      \:\  /:/  /   \:\  \        ~~\:\/\__\     |:/:/  /   \::/_/:/  /   \:\  /:/  /                       #
#   \:\/:/  /     \:\/:/  /     \/_/:/  /   \/__\:\  \      \:\/:/  /     \:\  \          \::/  /     |::/  /     \:\/:/  /     \:\/:/  /                        #
#    \::/  /       \::/  /        /:/  /         \:\__\      \::/  /       \:\__\         /:/  /      |:/  /       \::/  /       \::/  /                         #
#     \/__/         \/__/         \/__/           \/__/       \/__/         \/__/         \/__/       |/__/         \/__/         \/__/                          #
#                                         ___           ___                                   ___           ___           ___                                    #
#     _____                              /\  \         /\  \                                 /\__\         /|  |         /\  \                                   #
#    /::\  \         ___                /::\  \       /::\  \       ___         ___         /:/  /        |:|  |        /::\  \                                  #
#   /:/\:\  \       /|  |              /:/\:\  \     /:/\:\__\     /\__\       /\__\       /:/  /         |:|  |       /:/\:\  \                                 #
#  /:/ /::\__\     |:|  |             /:/  \:\  \   /:/ /:/  /    /:/  /      /:/__/      /:/  /  ___   __|:|  |      /:/ /::\  \   ___     ___                  #
# /:/_/:/\:|__|    |:|  |            /:/__/ \:\__\ /:/_/:/  /    /:/__/      /::\  \     /:/__/  /\__\ /\ |:|__|____ /:/_/:/\:\__\ /\  \   /\__\                 #
# \:\/:/ /:/  /  __|:|__|            \:\  \ /:/  / \:\/:/  /    /::\  \      \/\:\  \__  \:\  \ /:/  / \:\/:::::/__/ \:\/:/  \/__/ \:\  \ /:/  /                 #
#  \::/_/:/  /  /::::\  \             \:\  /:/  /   \::/__/    /:/\:\  \      ~~\:\/\__\  \:\  /:/  /   \::/~~/~      \::/__/       \:\  /:/  /                  #
#   \:\/:/  /   ~~~~\:\  \             \:\/:/  /     \:\  \    \/__\:\  \        \::/  /   \:\/:/  /     \:\~~\        \:\  \        \:\/:/  /                   #
#    \::/  /         \:\__\             \::/  /       \:\__\        \:\__\       /:/  /     \::/  /       \:\__\        \:\__\        \::/  /                    #
#     \/__/           \/__/              \/__/         \/__/         \/__/       \/__/       \/__/         \/__/         \/__/         \/__/                     #
#      ___           ___           ___                    ___           ___                                   ___           ___           ___                    #
#     /\__\         /\  \         /\  \                  /\  \         /\  \                                 /\__\         /|  |         /\  \                   #
#    /:/ _/_       /::\  \       /::\  \                /::\  \       /::\  \       ___         ___         /:/  /        |:|  |        /::\  \                  #
#   /:/ /\__\     /:/\:\  \     /:/\:\__\              /:/\:\  \     /:/\:\__\     /\__\       /\__\       /:/  /         |:|  |       /:/\:\  \                 #
#  /:/ /:/  /    /:/  \:\  \   /:/ /:/  /             /:/  \:\  \   /:/ /:/  /    /:/  /      /:/__/      /:/  /  ___   __|:|  |      /:/ /::\  \   ___     ___  #
# /:/_/:/  /    /:/__/ \:\__\ /:/_/:/__/___          /:/__/ \:\__\ /:/_/:/  /    /:/__/      /::\  \     /:/__/  /\__\ /\ |:|__|____ /:/_/:/\:\__\ /\  \   /\__\ #
# \:\/:/  /     \:\  \ /:/  / \:\/:::::/  /          \:\  \ /:/  / \:\/:/  /    /::\  \      \/\:\  \__  \:\  \ /:/  / \:\/:::::/__/ \:\/:/  \/__/ \:\  \ /:/  / #
#  \::/__/       \:\  /:/  /   \::/~~/~~~~            \:\  /:/  /   \::/__/    /:/\:\  \      ~~\:\/\__\  \:\  /:/  /   \::/~~/~      \::/__/       \:\  /:/  /  #
#   \:\  \        \:\/:/  /     \:\~~\                 \:\/:/  /     \:\  \    \/__\:\  \        \::/  /   \:\/:/  /     \:\~~\        \:\  \        \:\/:/  /   #
#    \:\__\        \::/  /       \:\__\                 \::/  /       \:\__\        \:\__\       /:/  /     \::/  /       \:\__\        \:\__\        \::/  /    #
#     \/__/         \/__/         \/__/                  \/__/         \/__/         \/__/       \/__/       \/__/         \/__/         \/__/         \/__/     #
#                                                                                                                                                                #
#                                                                                                                        >> https://github.com/Optickal          #
##################################################################################################################################################################
        
       
'''



banner2 = r'''
#EXTINF:-1 tvg-logo="https://scontent-atl3-1.cdninstagram.com/v/t51.2885-19/105937352_265914024481562_7622129429491260210_n.jpg?stp=dst-jpg_s320x320&_nc_ht=scontent-atl3-1.cdninstagram.com&_nc_cat=102&_nc_ohc=zf11R_EmFHsAX_MSb9q&edm=ABfd0MgBAAAA&ccb=7-4&oh=00_AT8B_Bu6PSKwIOBvOvRtIPCTOSvILccpgTaAsLRNRcH3mg&oe=6242D5FA&_nc_sid=7bff83",[COLOR green] [B] Marvins Playlist [/B] [/COLOR]
https://
#EXTINF:-1 tvg-name="KroneHitTv" tvg-id="KHTV" group-title="Radio" tvg-logo="https://play-lh.googleusercontent.com/b3UZEQKoQGGXKAXY_qwijvDVDIEqfqJv-nXP1jN-f71WFVSc4aq8ciIpD0O7BWpgD1s",[COLOR yellow] KroneHit TV [/COLOR]
https://bitcdn-kronehit.bitmovin.com/v2/hls/chunklist_b3128000.m3u8
#EXTINF:-1 tvg-id="RTL102.5TV.it" tvg-logo="https://raw.githubusercontent.com/Tapiosinn/tv-logos/master/countries/italy/rtl-1025-it.png" group-title="Radio",RTL 102.5 HD
https://dd782ed59e2a4e86aabf6fc508674b59.msvdn.net/live/S97044836/tbbP8T1ZRPBL/playlist_video.m3u8
#EXTINF:-1 tvg-id="R101TV.it" tvg-chno="167" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/r101tv.png" group-title="Radio",R101 TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://live2-radio-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(er)/index.m3u8
#EXTINF:-1 tvg-id="Radio105TV.it" tvg-chno="66" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/radio105tv.png" group-title="Radio",Radio 105 TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://live2-radio-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(ec)/index.m3u8
#EXTINF:-1 tvg-id="DeejayTV.it" tvg-chno="69" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/deejaytv.png" group-title="Radio",Deejay TV
https://deejay-tv-lh.akamaized.net/i/DeejayTv_1@129866/master.m3u8
#EXTINF:-1 tvg-id="RadioItaliaTV.it" tvg-chno="70" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/radioitaliatv.png" group-title="Radio",RadioItaliaTV
https://radioitaliatv-lh.akamaihd.net/i/radioitaliatv_1@329645/master.m3u8
#EXTINF:-1 tvg-id="RadioKissKiss.it" tvg-chno="158" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/radiokisskisstv.png" group-title="Radio",RADIO KISS KISS TV
https://58d921499d3d3.streamlock.net/KissKissTV/KissKissTV.stream/playlist.m3u8
#EXTINF:-1 tvg-id="R101TV.it" tvg-chno="167" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/r101tv.png" group-title="Radio",R101 TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://live2-radio-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(er)/index.m3u8
#EXTINF:-1 tvg-id="RaiRadio2.it" tvg-chno="203" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/rairadio2visual.png" group-title="Radio",Rai Radio 2 Visual
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont=5674080
#EXTINF:-1 tvg-id="RTL102.5News.it" tvg-chno="233" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/rtl1025tv.png" group-title="Radio",RTL 102.5 News
https://dd782ed59e2a4e86aabf6fc508674b59.msvdn.net/live/S38122967/2lyQRIAAGgRR/playlist_video.m3u8
#EXTINF:-1 tvg-id="VirginRadio.it" tvg-chno="257" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/virginradiotv.png" group-title="Radio",VIRGIN RADIO
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://live2-radio-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(ew)/index.m3u8
#EXTINF:-1 tvg-id="RadioFrecciaTV.it" tvg-chno="258" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/radiofrecciatv.png" group-title="Radio",RADIOFRECCIA
https://dd782ed59e2a4e86aabf6fc508674b59.msvdn.net/live/S3160845/0tuSetc8UFkF/playlist_video.m3u8
#EXTINF:-1 tvg-id="rds" tvg-chno="265" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/rdssocialtv.png" group-title="Radio",RDS Social TV
https://stream.rdstv.radio/out/v1/ec85f72b87f04555aa41d616d5be41dc/index.m3u8
#EXTINF:-1 tvg-id="RadioZeta.it" tvg-chno="266" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/radiozetatv.png" group-title="Radio",RADIO ZETA
https://dd782ed59e2a4e86aabf6fc508674b59.msvdn.net/live/S9346184/XEx1LqlYbNic/playlist_video.m3u8
#EXTINF:-1 tvg-id="RadioCapitalTv.it"  tvg-chno="713" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/radiocapitaltv.png" group-title="Radio",Radio Capital TV
https://capital_tv-lh.akamaihd.net/i/CapitalTv_1@183098/master.m3u8
#EXTINF:-1 tvg-id="M2OTv.it" tvg-chno="715" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/radiom2otv.png" group-title="Radio",M2O TV
https://m2otv-lh.akamaihd.net/i/m2oTv_1@186074/master.m3u8
#EXTINF:-1 tvg-id="RadioMontecarlo.it" tvg-chno="772" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/radiomontecarlotv.png" group-title="Radio",Radio Montecarlo TV
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://live2-radio-mediaset-it.akamaized.net/content/hls_h0_clr_vos/live/channel(bb)/index.m3u8
#EXTINF:-1 tvg-id="RTVSanMarino.it" tvg-chno="831" tvg-logo="https://cdn.jsdelivr.net/gh/Tundrak/IPTV-Italia/logos/rtvsanmarino.png" group-title="Radio",RTV San Marino
https://d2hrvno5bw6tg2.cloudfront.net/smrtv-ch01/_definst_/smil:ch-01.smil/chunklist_b1692000_slita.m3u8
#EXTINF:-1 tvg-name="Ö3-VisualRadio" tvg-id="oe3.at" group-title="Musik" tvg-logo="https://raw.githubusercontent.com/jnk22/kodinerds-iptv/master/logos/radio/hitradiooe3.png",Ö3-VisualRadio
https://studiocam-oe3.mdn.ors.at/out/u/studiocam_oe3/q6a/manifest.m3u8
#EXTINF:-1 tvg-name="SWR3-VisualRadio" tvg-id="swr3.de" group-title="Musik" tvg-logo="https://raw.githubusercontent.com/jnk22/kodinerds-iptv/master/logos/radio/swr3.png",SWR3-VisualRadio
https://swrswr3vr-hls.akamaized.net/hls/live/2018683/swr3vr/master.m3u8
#EXTINF:-1 tvg-name="DASDING-VisualRadio" tvg-id="Dasding.de" group-title="Musik" tvg-logo="https://raw.githubusercontent.com/jnk22/kodinerds-iptv/master/logos/radio/dasding.png",DASDING-VisualRadio
https://swrdasdingvr-hls.akamaized.net/hls/live/2018681/dasdingvr/master.m3u8


#EXTINF:-1 tvg-name="Oberjoch Webcam" tvg-id="OJ" group-title="Webcam" tvg-logo="https://i.ibb.co/CPfTkDF/Bergbahnen-Hindelang-Oberjoch.png",[COLOR orange] Oberjoch Webcam Test 1[/COLOR]
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://ch-fra-n16.livespotting.com/vpu/d6se1ryf/edlyww6d_720.m3u8?session=eaebeef6-745e-4e4e-8c94-6cfcb3e24ed0
#EXTINF:-1 tvg-name="Oberjoch Webcam" tvg-id="OJ" group-title="Webcam" tvg-logo="https://i.ibb.co/CPfTkDF/Bergbahnen-Hindelang-Oberjoch.png",[COLOR orange] Oberjoch Webcam Test 2[/COLOR]
#EXTVLCOPT:http-user-agent=Mozilla/5.0
https://ch-fra-n16.livespotting.com/vpu/d6se1ryf/edlyww6d.m3u8?
#EXTINF:-1 group-title="Webcam" tvg-logo="https://www.damuels-mellau.at/bundles/clientwebsite/damuels_mellau/img/damuels_mellau_logo.png",Mellau Rosenstelle
https://stream.webcam-livestream.at/live/mellaurossstelle/index.m3u8
#EXTINF:-1 group-title="Webcam" tvg-logo="https://www.damuels-mellau.at/bundles/clientwebsite/damuels_mellau/img/damuels_mellau_logo.png",Mellau Rosenstelle Berg
https://stream.webcam-livestream.at/live/rossstelleberg/index.m3u8


#EXTINF:-1 group-title="Tomorrowland" tvg-logo="https://w7.pngwing.com/pngs/378/394/png-transparent-2018-tomorrowland-tomorrowworld-music-festival-logo-electronic-dance-music-design-purple-heart-logo.png",ONE WORLD TV #1
https://live-tml.freecaster.com/tomorrowland/96b89f93-ce21-492f-ab98-b56b84247175/96b89f93-ce21-492f-ab98-b56b84247175.isml/96b89f93-ce21-492f-ab98-b56b84247175-stereo=256000-video=5499968.m3u8
#EXTINF:-1 group-title="Tomorrowland" tvg-logo="https://w7.pngwing.com/pngs/378/394/png-transparent-2018-tomorrowland-tomorrowworld-music-festival-logo-electronic-dance-music-design-purple-heart-logo.png",ONE WORLD TV #2
https://live-tml.freecaster.com/tomorrowland/96b8a4bc-bc66-4519-9184-9b5d149d2d14/96b8a4bc-bc66-4519-9184-9b5d149d2d14.isml/96b8a4bc-bc66-4519-9184-9b5d149d2d14-stereo=256000-video=5499968.m3u8



#EXTINF:-1 tvg-name="Sky Radio 101 FM" radio="true" tvg-logo="https://raw.githubusercontent.com/jnk22/kodinerds-iptv/master/logos/radio/skyradio101fm.png",Sky Radio 101 FM
http://playerservices.streamtheworld.com/api/livestream-redirect/SKYRADIO.mp3
#EXTINF:-1 tvg-name="80s80s Radio" radio="true" tvg-logo="https://static-assets.iamrad.io/80s80s/1648022795461/4c68f9a343fe635641e064a1821bb125.svg",80s80s Radio
http://streams.80s80s.de/web/mp3-192/streams.80s80s.de/play.m3u


#EXTINF:-1 group-title="Honeypuu Twitch",HoneyPuu Twitch [COLOR orange] Test [/COLOR]
https://github.com/Optickal/Test/raw/master/Honeypuu.m3u8
#EXTINF:-1 group-title="Honeypuu Twitch",HoneyPuu Twitch 720p/60
https://video-weaver.fra05.hls.ttvnw.net/v1/playlist/CpkErfuCCqUBxDbLK18QsbFKvlvv4HRtM4twmCt7mZqK6Sgs88H5JOV69hRaKMirLDh3GFonHCgK1DaNuQ8sZw5EDatK1m89z5gFXY3QEsnVBEzUhS5exwUgyNBf8L0XzXR3t2ISRmUlVHNBDn2oz-W_2IsFBCyEXrQskMAKmMuzJ8cYatBnqtoQxAsoI92EluVx0jjZHo9jKRTKTjDypnhK1Dz45KnnswOs-DY6m9jdXb_cXhpurzUlJxVH-n1Ev7PL0nD9FZk8G4_kgaNtxnin6HqNzDxIFhDF6vmk4K2jc3E12O5gqVDnOU_1lEVNjsgdC1ksp47Duqp0tcc5xT4Z-UJaTSE4In08Q2FUMu-NceYv7pq0ap4u6RqRrfh0AEF0CbIubtK7AyeuZrkJBpkLjjRnS80Q4dkLH6xbzV5KzW3QMAWHuqJOdYFlK1ofSY_6E8wKilLx37j9kOqIptas10dRztuhmjwEHiQKxS38dASYb71FODcboHSVP-UvGykIO5NqH8RUGKw-ITAwEBmuPr2dGTKsHF8sJQEpWnURcEreoKT8cYubxtUT55RVJ7WXXfeX31sbEPwd7nwPfvpyOETDJ1lsQ5xdEDrU-RlorJFT3SWeysyUfyJUAZhSlob3UMI1sF18RqShnky-R0fzi-ODFbBAP-mmmNnbjA9cB-N4TfPRAEhsJSFSEA61kL3xDhkTRjgVriMbGgx2lTzJtwbzVrTukjogASoJZXUtd2VzdC0yMP0E.m3u8


'''





from datetime import datetime
import requests
import os
import sys

print()




windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/Optickal/OptickalTV-test/main/assets/info.m3u8')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/Optickal/OptickalTV-test/main/assets/info.m3u8')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")
    
    
print(banner1)

#print epg
print('#EXTM3U x-tvg-url="https://telerising.de/epg/easyepg-basic.gz"')
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M
dt_string = now.strftime("%d/%m/%Y %H:%M")
print("#EXTINF:-1 , Stand -", dt_string)
print("https://")

print(banner2)

#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
