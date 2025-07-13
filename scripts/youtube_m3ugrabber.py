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
#EXTINF:-1 group-title="Webcam" tvg-logo="https://www.visitjesolo.it/sites/default/files/styles/600_360/public/schstr/restyling-logo-comino-01_0.png" tvg-id="", [COLOR teal] Camping Jesolo International [/COLOR]
https://hls.youtb.workers.dev/channel/UCDB_gbIJPzzT7xg__hSfqSw.m3u8
#EXTINF:-1 tvg-name="KroneHitTv" tvg-id="KHTV" group-title="Radio" tvg-logo="https://play-lh.googleusercontent.com/b3UZEQKoQGGXKAXY_qwijvDVDIEqfqJv-nXP1jN-f71WFVSc4aq8ciIpD0O7BWpgD1s",[COLOR yellow] KroneHit TV [/COLOR]
https://bitcdn-kronehit.bitmovin.com/v2/hls/chunklist_b3128000.m3u8
#EXTINF:-1 tvg-id="RTL102.5TV.it" tvg-logo="https://raw.githubusercontent.com/Tapiosinn/tv-logos/master/countries/italy/rtl-1025-it.png" group-title="Radio",RTL 102.5 HD
https://dd782ed59e2a4e86aabf6fc508674b59.msvdn.net/live/S97044836/tbbP8T1ZRPBL/playlist_video.m3u8

#EXTINF:-1 tvg-id="RadioCompany.it" tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCbyuF3vnqQkKOzY0xFAv3AoDgT24j5EaDTw&usqp=CAU" group-title="Radio",Radio Company TV HD
https://company.fluid.stream/CompanyTV/smil:Company_ALL.smil/playlist.m3u8



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

#EXTINF:-1 group-title="TV", ARD HD
https://mcdn.daserste.de/daserste/de/master.m3u8


#EXTINF:-1 group-title="Twitch" tvg-logo="https://scontent-lax3-1.cdninstagram.com/v/t51.2885-15/184761410_264224142070921_752288161223085036_n.jpg?stp=dst-jpg_s200x200&_nc_cat=1&ccb=1-7&_nc_sid=8ae9d6&_nc_ohc=zW3BMrFzKisAX9vSca4&_nc_oc=AQlrjHT1QsIxjNOr5MMqwMhpzyPvecdUufkLR7GwV-r80-ayyfqlmIF7tzZwiyiYVD4&_nc_ht=scontent-lax3-1.cdninstagram.com&oh=00_AfA_VEoVr9bvrz_VpMGlww7sTeHxtrvQaegpdSXhVSELjg&oe=636CDA19",HoneyPuu Twitch [COLOR orange] 720p/60fps [/COLOR]
https://video-weaver.fra05.hls.ttvnw.net/v1/playlist/CpgEgxoEIkgoOYYx5izEWupyLz_v9DwtHlD9Rjd9245t8dSuCZ8s_IYuQkPPuxfpfD3_VZQQPB2R09g7gi9qf0oW7stBUmYYANnTjfAgqmSiwzE9ctrTeJ9bsCFDLzpIWv74G2RhqpEWcJpEqy08NYz8UvbWl3xpLzdxjRmv8lsFflcn8zS5b99aSUodr0_8uGImJY_FhDnZZZnrAKKo6Ue3Tno8lOLsemVu1PIT4ido4bskaKw5gRuXfs7pL5HKvxSNDJN0y5D0bR5sk9ccOl6Td4yjLk9Jbl1z_UTuhi8r7ocxjSoZYSFasbWHLYa98Gz_3ZFAFlzg1-t2lucA46NHQRBIbdfGZwPhUYOhUh1yo6qCdufJaomZPC50872mliLJSYdWM99HNB7-Wnpbsev6z4yzkDCl1NG4u6sd3bJzMdvoK9UtCjIaQ2nBHTBmroMcUksa_sIdc7vVlYhTB0zCgsLUNWqZA1MmMUmcpS0cNmLV6vzc5HKKvuQUl77NO7kubOMfBy89e1GA9clVkaUglerPbWyKQz_pxOO-htaugdVmGFSLz-Ai4Yr_FfPIK3JIZ_SrPSTeponvOu5KlbdpKtaaTbQyeVbZuClWM95TiAzBkrcEeXqLX9T-rZGgax-KpUmvDgxA-_apJ4aAKR8At5gyceIlNIoiyPQtXgZ6gGlLqYAPXIeVDx34lYrhTaMr9sFH03obYCEaDLfic4zSz0mr1tlRdCABKglldS13ZXN0LTIwiwU.m3u8

#EXTINF:-1 group-title="Twitch" tvg-logo="https://static.wikia.nocookie.net/youtube/images/3/3b/BastiGHG-Neues-Kanallogo.png/revision/latest?cb=20210908235206&path-prefix=de",BastiGHG Twitch [COLOR orange] 720p/60fps [/COLOR]
https://video-weaver.fra05.hls.ttvnw.net/v1/playlist/CpUEnslHXAdmCEgblSYBSuedA26nqlqPlafQ0HJKHu7XokJJAWVT4KidS7KuLHpjpgcEZvuy_KUJxr_SNv7Ykpa6gusa4YtgBQpaYWVoBXMp4VDwuYgnR382MWy3pPQ53Cr3RFamulHceLBDUUr57LQkQukOxbe-8vpzDV329rO4yAgHpvqyBwtCjMzOuXETkzsTk6af_rK48bOtgU8RBAlgysEDUvnrsC7u341SRGWCjqNJUTRL4g3a-M9tCJ1Ammm_0MFIICScSIMLDzzlNGFcM6b-jsVVCkLGwT5JCkJz3k7dYcRIdq_cfb9RFZ-vcU4rZ_nL7oCPgUEFu7lw-g700uOnB5XK-rGLlcCPuJ2yoNX_kElW2s6qfu1iQW_fYdSK9irxBsca1vcELEbso4hTWZzLYXRPvI2QLxAKKcr7bRzxMX_GN_VOeyXbSS4DL6ntC7cmSthmtFWHWNf4T66ZztlK5nng3pCcelgulobDrzDa0deHk03hBr_uMsQLKyEfNMkyqLa3R5FpNYdtjkMm9sgFbRc4PAEE5vf5Ge9jfUFfSy0Hk0qYeDN47PQd4sVOfkBFbXfi0VdZSDXlIkgrMRkLBykncLknO7r-i31mvgvumjvVV9MuYQnfgcYaIBweAh2HqAHtKx1dBEYaxQJgRmmzdCYXwNv1gtYiQ_hIm_ReH4NAlJSuHy6nAdN5ukdM9bL2J5QaDGbNP6XjBA_kqB7hbyABKglldS13ZXN0LTIwiwU.m3u8

#EXTINF:-1 group-title="Twitch" tvg-logo="",unsympathisch_TV Twitch [COLOR orange] 720p/60fps [/COLOR]
https://video-weaver.prg03.hls.ttvnw.net/v1/playlist/CpMEc_ZjPyec0IpmtvoPH3LiNLuDPsltIGIPeY2TqoIwTbLwau2XC4m08MrrTzbLBUtWj4532vEJe-vK4KjusZ29bqc_KB4IgBsuoenfTXkHhC_7NRwnIbQQRzrTubbNvRyLqBjcBvmx10JUXWRunu4y5u3z9eV66j6C2KeLjZ1CkmUWHN2cvqtA-mxVtlvujtErUJu77wVIAayUUZE3K2DpoIwa66Ev15_m9rLtSTaJ6eNlt3J4yApIMgCdU7HdVaj8sz1faD9NF5GNaIWjK-I6VJ-WC58DcMMrGIyzADWQymVKWf2xaN0xAhuFGbsA5P7N3yhHuYwn85UPaZ2VwNgoitH7fck3WJiXK5nxWHYu74vHNxi0bsDeihqQPhWXKYK89YwJbfXrasAh1AXvF3dngjstAcqFesCaEQKWAzLDfZkgQUqh6wzhjZwJxZ_mb9-C6DAf_1gAziLzy85kZTTOLMfEgon5fCuTqcbcUZG65mTY5ucmmQQKgHGOvNgk_eDrblwTPrIRpck197hPa0dhgu61sQB69yvWXNIc9DQJzj9qNthchHHn5G1AuxIQxgGB-9NQUPs5bYQXaxdqFQ1K99Ve_KKxneHn_nQm7iy0njKVKfp2D8bMktWrTlpVjeKJDAN-imfXZF1ioP-zv5IRxxuiwCusBOjMsGON9jVpuAr_mVerltc_VQD1EOb_5MNBA1_YGgxKlUydKO98bB6mem8gASoJZXUtd2VzdC0yMIcF.m3u8

#EXTINF:-1 group-title="Airpower" tvg-logo="https://de.m.wikipedia.org/wiki/AirPower#/media/Datei%3AAirpower-Logo.svg",Airpower 2024 Facebook Live
https://www.facebook.com/video/playback/playlist.m3u8?v=2268751570142407&a=0

#EXTINF:-1 group-title="Airpower" tvg-logo="https://de.m.wikipedia.org/wiki/AirPower#/media/Datei%3AAirpower-Logo.svg",Airpower 2024 Live
https://egress-stkpl568letoqb1mdwrq0.live.streamer.wpstream.net/ev_wps_54054_wwwair1592b4_74484_1725685105/hls/1et7l1zj3a7hpl8h.m3u8

'''






from datetime import datetime
import requests
import os
import sys
from bs4 import BeautifulSoup

print()

windows = False
if 'win' in sys.platform:
    windows = True

# ===== JESOLO-WEBCAM M3U8 GRABBER =====
def get_jesolo_m3u8():
    jesolo_url = "https://www.skylinewebcams.com/de/webcam/italia/veneto/venezia/spiaggia-di-jesolo.html"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        resp = requests.get(jesolo_url, headers=headers, timeout=10)
        soup = BeautifulSoup(resp.text, "html.parser")
        for script in soup.find_all("script"):
            if script.string and "live.m3u8" in script.string:
                start = script.string.find("https://hd-auth.skylinewebcams.com")
                end = script.string.find(".m3u8", start)
                if start != -1 and end != -1:
                    m3u8_url = script.string[start:end+5]
                    return m3u8_url
    except Exception as e:
        return None
    return None

# Jesolo-Link einfügen
jesolo_stream = get_jesolo_m3u8()
if jesolo_stream:
    print('#EXTINF:-1 group-title="Webcams" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/6/69/Jesolo_Beach_icon.png" tvg-id="jesolo.webcam", Jesolo Beach Live')
    print(jesolo_stream)
else:
    print('#EXTINF:-1 group-title="Webcams", Jesolo Beach (nicht erreichbar)')
    print('https://raw.githubusercontent.com/Optickal/OptickalTV-test/main/assets/info.m3u8')

# ===== DEIN BESTEHENDER CODE =====
def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/Optickal/OptickalTV-test/main/assets/info.m3u8')
                return
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

print('#EXTM3U x-tvg-url="https://telerising.de/epg/easyepg-basic.gz"')

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M")
print("#EXTINF:-1 , Stand -", dt_string)
print("https://")

# ✅ Angepasst: Datei im Root lesen (nicht ../)
with open('youtube_channel_info.txt') as f:
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