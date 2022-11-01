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





#EXTINF:-1 group-title="Twitch" tv-logo="https://instazoom.cc/img/21/1667339957970320455873777.jpg",HoneyPuu Twitch [COLOR orange] 720p/60fps [/COLOR]
https://video-weaver.prg03.hls.ttvnw.net/v1/playlist/CpgE_qMU4MlvD24qe19wU7xC27rt1mkEtGtqlNoo8f4QOcBQk_9eOKudKaXFxzUuryQL5G978EYBhcnRshzJLcbs4GAYXjeh3HyeClIoPPYco59yGRWhtlVa2u9p4B-HfP3jjH-BDKmpC6lGPBqxHd9sNROevyPL_NeqLBM8clKOn8w0YfPeV5vsolPwgvllNXv60hOtD3VfahOS3wNzAaPOOAwbLThyz_ds5Sh1fCdOwCJWt3Sh-fpd3Q_SPYwXlszLWIOL7L5t2DDmqb6KiMqydTzFdyGUVMvuJ0wrNnOC3cQn2cX43iipfS0eA2s8P7OZd2qfKiMoW6hsY4pkUUFwyEF7Gb3lecrWg4HXjwQ-wyWrUHKX0ay3APN13Hw0wnd0ICdMBdMsvwmqj3cwHy4O28G3ttOmoR0a9qOnE9qkvOD1lhW4FjsAIFv1Sfz4pR32qgsjDEdbRrDfp1dnk3J0X-rt1u-lkgxwqrb3WwM3X0yUgS2bbTfA_jtPAm3kGDeU9TSkMC8s3SERg25aL5xKzh9C11QP_yJasqHd4wBZ_ZMw-I7RaaWRHHZ4-A4-dKvPW2NxoNRYpdSn2rs3iTNrp-zkdaTv3-Q_D5ZYURiUWMbTL6ZDiVWkPYbDTx_hjot2EXzfZAo8CLWAh6p5mTrnxYHXXk6i1aGdOQyHBqDkBY1L85fKMGiQja3_EfQMhwyorKodoPBY_pkaDN9qhtFFeeWTS2oGQiABKglldS13ZXN0LTIwhwU.m3u8

#EXTINF:-1 group-title="Twitch" tv-logo="https://static.wikia.nocookie.net/youtube/images/3/3b/BastiGHG-Neues-Kanallogo.png/revision/latest?cb=20210908235206&path-prefix=de",BastiGHG Twitch [COLOR orange] 720p/60fps [/COLOR]
https://video-weaver.fra05.hls.ttvnw.net/v1/playlist/CpYEjXTQOrLwwl5T7tsuhhKdak0Pg7q_hshfSNRAaaZhQPfArhF3jHGTubT235nFqioyEi0GNDXM_aQIYZHDSUxLiJBcSvYYq1383hSc8Xae6-nnetiGC3V7jcbmDCaI5YvUdUD3gMIxqiXNYqaL5tJRLSMTCiXSUICWYsx6BL__qim4Sq0vxYBC4a88AvImj1ZeaJpvsqjHDpzBH6p6pfLFc4H6L4oQH_VjSofeGMh1aKnmRYuab6A1Sahooh_hoTYeEa79G0blV4hrRpBar4sg7l0WEII5zRwTk4yQ_2IkvxLOCtnADMnNfHMPNMUbslgFIOA9Kz20HnUiMVQ_EythTlQIIdkx8jm_P--wdUwjn4Xvs0UHLlIdvez1z465nEeCad9OD26IspDBNlXYQPQSTcC2p-ZNGJVMUFm1Nup5GxyHqk1mzvBvIE8JusUuU4-RpnCiBOmIS-QkuIxSeODChPx_9w7TfbQmC5z3136lHaU52Nu4m_1GfJAcDscw71iXkO5Jllsxj-xZyo_wchET__0Uxly2Jvr4IvDPtHhHtQZix0H5DoTtTaLfstanCOTlpDUFX3_kn6sVCGWOyFcVr-SvtL-1txg_5-261xHq7gjg5dvBh0MIEGQkiWU1n-nYg_UZtxAgUsi-wsifDOXEDrV2vtlqXiDJjVyx_9imvq7oZWQerwmskEWWcA0WERSKgiYtJO3aGgxCzpb6XXTugjqaqqAgASoJZXUtd2VzdC0yMIcF.m3u8

#EXTINF:-1 group-title="Twitch" tv-logo="",unsympathisch_TV Twitch [COLOR orange] 720p/60fps [/COLOR]
https://video-weaver.prg03.hls.ttvnw.net/v1/playlist/CpMEc_ZjPyec0IpmtvoPH3LiNLuDPsltIGIPeY2TqoIwTbLwau2XC4m08MrrTzbLBUtWj4532vEJe-vK4KjusZ29bqc_KB4IgBsuoenfTXkHhC_7NRwnIbQQRzrTubbNvRyLqBjcBvmx10JUXWRunu4y5u3z9eV66j6C2KeLjZ1CkmUWHN2cvqtA-mxVtlvujtErUJu77wVIAayUUZE3K2DpoIwa66Ev15_m9rLtSTaJ6eNlt3J4yApIMgCdU7HdVaj8sz1faD9NF5GNaIWjK-I6VJ-WC58DcMMrGIyzADWQymVKWf2xaN0xAhuFGbsA5P7N3yhHuYwn85UPaZ2VwNgoitH7fck3WJiXK5nxWHYu74vHNxi0bsDeihqQPhWXKYK89YwJbfXrasAh1AXvF3dngjstAcqFesCaEQKWAzLDfZkgQUqh6wzhjZwJxZ_mb9-C6DAf_1gAziLzy85kZTTOLMfEgon5fCuTqcbcUZG65mTY5ucmmQQKgHGOvNgk_eDrblwTPrIRpck197hPa0dhgu61sQB69yvWXNIc9DQJzj9qNthchHHn5G1AuxIQxgGB-9NQUPs5bYQXaxdqFQ1K99Ve_KKxneHn_nQm7iy0njKVKfp2D8bMktWrTlpVjeKJDAN-imfXZF1ioP-zv5IRxxuiwCusBOjMsGON9jVpuAr_mVerltc_VQD1EOb_5MNBA1_YGgxKlUydKO98bB6mem8gASoJZXUtd2VzdC0yMIcF.m3u8




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
