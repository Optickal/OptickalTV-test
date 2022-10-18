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


#EXTINF:-1 group-title="Honeypuu Twitch",HoneyPuu Twitch 1080p/60
https://video-weaver.fra05.hls.ttvnw.net/v1/playlist/CpsEC_XGF0ujSoa-DLvMmENxm_2KTL1HUA2SmmPmTKTL1Mt67ArXZiaZzvDq4xkCKi7tHzcRDeMtq8_r796apIxSTDAHjYIXtDsF6KtXRiQ-cJr0i6Vg7cEC2rTiZEyNVZuOChfXNJ_wnd449gfFcjLm9zvkNOkMbGfHT176TjzIeM2lspk5lL4KeF7_7zoSNkWUfwfkGiuR2irKqjWawvULwulQ3UgVUpxw-sp9P4Ls7TKe7N24kFhf7RXOwYsauj8Qy0-HXzhnMEDoaTabderelJI9GaOt9pAp5g9U-3Dv7Fb_8QkjY6-QnKpda5YlmP9FVRzJ2tzLfVbUFa-leuS6JbLwji_O5U5atmm5HlPUjwovDnqZtlK_RiPKkTLLc0j81nbR4PpmZcK1YaLw0iyFh9TQZLunIhBU2I1uG4-7K2s_dXZ2LQOiiyU6G8ZxbQo-3ASq8OOwlWVKf_3ijT72kLLsnjQVgxGQJFiV13LpBVvyUoXplqiWk7_zL5dD62DiN-XCIii2GngHR3C5L06eaPOq6t1mGzrVdaGUL68ERnNRv-7izS_CpwirBOrLMitUuYhDaSSTwQDzsza5lrOIiMIh0t4vHEo22b-ljyTdgb-o820wyLa7Bw9-y-2NmuR23tE1L7yz7Ejqz5pl3tJtypH_gcz2a7gcXsSJP0hlDls9wXL6XdZZZm9U_Zp5_PPnzbtc2hqcfmAmkvgaDIHnG-MJwTHx4MbnMCABKglldS13ZXN0LTIw-QQ.m3u8
#EXTINF:-1 group-title="Honeypuu Twitch",HoneyPuu Twitch 720p/60
https://video-weaver.fra05.hls.ttvnw.net/v1/playlist/CpkEXnx2OZ4i65KEK7oVBw3lgGhE51_lPKZl6WnTBdOqJ44EegL8_o0elkyNzeNoeAjf_Q3hBRFh20_1FG7rnZ1D-esvgPCQ8XPupIBcVDCgfGQiQctteLwJjAaOyw12Z9q-cxaaGwhJ07SPvfPBindrvKsiOxg_tT2Nf_0FBKX2Oy6mtJtYPBZZ2bdYHkCUjuvf01LkT6lxVfybL5zpdxoovWH2xefL2rJNu4m64UGfl3u_WJ4WgdX5ZlAQAGEODnbs32-MGNlrHqSpUG_qMqpc6gQAbrFqo89LieNcD5AEUF1oG9uwdJu3V3-jSPpPbnz2hMYQ09Bt7Pl3-vcHWE0AshOBESPUlVDfm4fAnm-oqkje1Qmwwy3qCTbx2Mdd0cAG2-lbmho2d0eH_4VFuTdRu3jXxH_-f11OuIx5sqUJYm-tU_y6LJl2krOcah45aB6Y_m3QNt-7Hv23UVAt1XuAOkLd1kOQq-OWx0imGmnFscn-w5dSONVZmcCnJk1DMcUdgEiD0vImhp_nRmwVm_-63NjCBWg3vdq_9CMCJ9Ru4_WMPGXoxP9bq14PtN606aBJdfpYWpNOmVw3-3ddCFq5_ntL-hWl0CgkCGD51uHjEqoHO6pH_Tbk-zbSGr0uzAqQWCpGFsGn7jmWCF2EIoDnIkPxPpr-FjUCyo7m70m022NFiE545OXCATcW8fv9fO5Gf0MwvMhKaDbjGgxIj-9u22rpxScLvOkgASoJZXUtd2VzdC0yMPkE.m3u8
#EXTINF:-1 group-title="Honeypuu Twitch",HoneyPuu Twitch 480p
https://video-weaver.fra05.hls.ttvnw.net/v1/playlist/CpkEeEf6n68oyQ0ri7CMu_5SruF4W0YtgXm0-nFyjfTEbENkOnuGlK7DIXl05ERXbYgL3cW1Jn2cqRpPIlp0DK6lY3mqwYXVQNSHYJwzmJmr1mneMkXKffkDqOjfZahtU00ncJGjMiKQEcfMi3kpLUPR9hvvsaifQOvRuFnIF3ssMWoqXPFdH81nTJB75oj8vdp81bDG6BdnP1U4kA8uu2hFCpoyrDlBzCA0YCZgfazCLdjTZGFVnUv00aqV4a1JplR0Jiu_0Sn6c3c34Ylaf_7xTxrtBZd_fkuwOAF02Y7FCJ_NEtU2rSjJL61PBDU0wgQaiaArMbjC8OBuQupfrQWsXBbeqGZXNZhxynWi7bzk6JnqFVdxJWe81SsUol7uWOt4RmZ0Thp4sHxXI7apMIeSY1zKe7pgiGzjHOfE8f7pXem8_qqqRx01NZehbxdn7ZmAO2g9FkjGvfbEYFMPwzuhyWeOn8he_ii87rsxZI8pNYpFKZt660-0JiiDeu28XUDJYByLeSA9K4CHSYJn2k7ZNF_0kmZIlk-sEJOFoxfG5dWBLdhcAFRw2G8hPrYw1PLuxBeNRf6lEiMKU7EZPt3XYpqFCcuju5WPfxbmjnall3Mazwyr69zwV4mckG-AzX3HfNdm-HvwDTfXrSV2tSV-h3KiUwLL6YCWU1PULkMJNepWpjneTgjztd0xHwl-9DxnGlZ_tXuthxAgGgzBxGog9QGEk9X3Sx4gASoJZXUtd2VzdC0yMPkE.m3u8




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
