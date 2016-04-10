""" Created by Jieyi on 3/5/16. """

__all__ = ['authority', 'autoMailer', 'internet', 'io_operation', 'mail', 'mailer']

debug_log = False

# Country language.
lang_list = ['Select a language', 'English', 'Tradition Chinese', 'Simple Chinese', 'Korea']
atta_lang_list = [None, '', 'chinese', 'chinese', '']
# Attachments name list.
attachment_list = ['Detail Map.png', 'Map.png', 'From the Kansai Int.pdf', 'GARBAGE.pdf',
                   'Home Utensils.pdf', 'Rule for email.pdf', 'Self Check.pdf']
# The links which will be changed in the content.
content_link_title = ['< Japan Guide >', '< Weather Forecast in Osaka >',
                      '< Shuttle bus station at KIX to / from the Rinku Premium Outlet Shopping Mall >',
                      '< Shuttle Bus Timetable Between KIX and the Rinku Premium Outlet Mall >',
                      '< USJ >', '< KAIYUKAN AQUARIUM 海遊館 >']
# Other county language website.
content_link = {lang_list[1]: ['http://www.japan-guide.com/e/e2361.html',
                               'http://meteocast.net/forecast/jp/osaka/',
                               'http://www.kansai-airport.or.jp/en/index.asp',
                               'http://www.kate.co.jp/en/',
                               'http://www.usj.co.jp/e/',
                               'http://www.kaiyukan.com/language/eng/'],
                lang_list[2]: ['http://tw.japan-guide.com/',
                               'http://cn.meteocast.net/forecast/jp/osaka/',
                               'http://www.kansai-airport.or.jp/tw/index.asp',
                               'http://www.kate.co.jp/tcn/',
                               'http://www.usj.co.jp/tw/',
                               'http://www.kaiyukan.com/language/chinese_traditional/'],
                lang_list[3]: ['http://cn.japan-guide.com/',
                               'http://cn.meteocast.net/forecast/jp/osaka/',
                               'http://www.kansai-airport.or.jp/cn/index.asp',
                               'http://www.kate.co.jp/scn/',
                               'http://www.usj.co.jp/cn/',
                               'http://www.kaiyukan.com/language/chinese_simplified/'],
                lang_list[4]: ['http://kr.japan-guide.com/',
                               'http://ko.meteocast.net/forecast/jp/osaka/',
                               'http://www.kansai-airport.or.jp/kr/index.asp',
                               'http://www.kate.co.jp/kr/',
                               'http://www.usj.co.jp/kr/',
                               'http://www.kaiyukan.com/language/korean/']}

c = '''
Hello **name**,

Please kindly acknowledge to receipt of this email with attachments.
Be sure to do not forget to download or print out the apartment address, the location maps, and check in flow for your comfortable stay.


See you soon!

Mariko


< Mariko's Private Info. >
Mobile;
+81-90-7494-8047  (81 is Japanese country number)

LINE user ID;
marikondkawanaka

WECHAT user ID;
marikondkawanaka

# LINE and WECHAT #
LINE or WECHAT response is faster than Airbnb's, so if you want to use LINE or WECHAT with me, let's do it! When you find me, please send me a test message with your name. I usually don't use WECHAT very much, but if you don't have LINE, we can touch by WECHAT.


< Guest Support >
Let me inform you that it's difficult for me to help you all the time as like searching something (attractions, shopping, product... etc.) I hope that you could search them by yourself first before you ask me any questions.


< Free Pocket Wifi Service >
Portable wifi device is provided. You can use wifi in everywhere in free while you are in Japan!
Japanese pocket wifi has flow limitation of the usage. If you use internet over 2GB in three days, Internet speed will be very slow. After three days you use it beyond the limitation, the speed of Internet will be recovered.


< Mariko's Guidebook >
You can check my guidebook about neighbors such as convenience store, supermarkets, food, or clinic in my Airbnb page. Therefore, you should see my guidebook in Airbnb App. If you see my page  by browser, you will not be able to  see it.


< Address in Japanese >
大阪市浪速区日本橋4-5-18
Room 405


< The Nearest Train Station From the Apartment  (by walk) >
＊Nankai Line Namba Stn.; around 10 min.
＊Subway Sakaisuji Line Ebisucho Stn.; around 4 min.
＊Subway Sakaisuji Line Nipponbashi Stn; around 10 min.
＊Subway Midosuji Line Namba Stn; around 12 min.


< Discount Season for Shoppers >
Winter; from January 1st. or 2nd. to the end of January or the end of February
Summer; from the end of June or July 1st. to the end of July or the end of August
＊High brands or cosmetic brands are not sold in discount price


< Train Timetable and Searching Route >
http://www.rome2rio.com/


< JR Bullet Train "Sinkansen" Timetable >
http://english.jr-central.co.jp/info/timetable/


< Japan Guide >
http://tw.japan-guide.com/


< Weather Forecast in Osaka >
＊The rainy season in Osaka; from June to July for 1 month or from July to August for 1 month.


< Shuttle bus station at KIX to / from the Rinku Premium Outlet Shopping Mall >


< Shuttle Bus Timetable Between KIX and the Rinku Premium Outlet Mall >


< Connecting Shuttle Bus Stop at KIX for Rinku Premium Outlet >
＊From KIX, take a bus at No. S12 at KIX terminal 1.
＊The bus fare between KIX and the Outlet Mall is ¥200 per person for one way at this moment.
＊Seat-load time is 15-20min around.


< Connecting  Between the Rinku Premium Outlet Mall and Namba Stn. >
＊Walk 6 min. between the outlet and Rinku Town Stn. You need to take Nankai Line, not JR Line.
＊The fare is ¥760 for one-way.

< USJ >

# USJ Information #
＊Harry Potter is the most popular attraction in USJ now. USJ say waiting time is over 2 hours on weekdays, over 3 hours is on weekends, national holidays, and school day off.
＊If you want to enjoy Harry Potter, you had better to get a ”numbered ticket” to confirm your entering. You can get the ticket as using the self ticketing machine inside the park (It is on the way to Harry Potter from the park entrance). For that, you had better to go USJ in the morning as long as you can, and line up for opening the park entrance.
＊For other popular attractions such as Hollywood Dream the Ride, Amazing Spiderman, Evangelion 4D, etc...,USJ say  waiting time is 2-2.5 hours on weekdays. 2.5-3 hours on weekends and national holidays.
＊Express 3 Tickets, Express 5 Tickets, and Express 7 Tickets  help you to save time for waiting.
    (You cannot enjoy Harry Potter with Express 3.)
＊If you want to get the Express ticket, you need to buy it in advance. USJ website tells you detail.
＊Even for getting the park entrance ticket, sometimes guests make a long line in front of ticket center. So that, at least I suggest you to buy the park entrance ticket in advance. (See USJ website.)
＊USJ business hour is flexible, it depends on seasons as like summer season or winter season. Also it is different at Halloween season, X'mas season, weekend & national holidays. They sometimes open the gate 1 hour earlier when guests make a long lining for opening the entrance.
＊USJ offers children price, senior price, and disability price.
＊Depends on attractions, there are age limit. (See USJ website.)


< The Best Way to Go USJ by Train >
1). Take the train Hanshin Line from Namba Stn. to Nishikujo Stn.
2). Change train at Nishikujo Stn.
3). Take the train JR Yumesaki Line Nishikujo Stn. to Universal City Stn.
＊It takes around 30-40 min. door to door.
＊The fare is ¥360 for one-way at this moment.
＊There is children fare, senior fare, and disability fare. You can ask train staff.


< Access for Kyoto >
Plan A:
1) Walk to Namba and take Midosuji subway from Namba Stn. to Umeda Stn.
2) Change train at Umeda to JR Tokaido Line. Osaka Stn. (Midosuji Umeda Stn. and JR Osaka Stn. are same station)
3) Take JR Tokaido Line from Osaka Stn. to Kyoto Stn.
＊It takes around 60-70 min. from door to door by Midosuji Line and JR Tokaido Line.
＊The fare is ¥800 for one-way at this moment.
＊There is children fare, senior fare, and disability fare. You can ask train staff.


Plan B:
1) Walk to Ebisucho Stn. and take Sakaisuji subway from Ebisucho Stn. to Kitahama Stn.
2) Change train at Kitahama Stn to Keihan Line.
3) Take Keihan Line from Kitahama Stn. to Gion-Shijo Stn.
＊It takes around 70 min. from door to door by Midosuji Line and Keihan Line.
＊The fare is ¥650 for one-way at this moment.
＊There is children fare, senior fare, and disability fare. You can ask train staff.



< KAIYUKAN AQUARIUM 海遊館 >

1. There is the city bus stop between TAKASHIMAYA Department Store and MARUI Department Store.
2. The bus line is No. 60.
3. Final destination "TEMPOZAN 天保山" is the nearest bus stop from KAIYUKAN.
4. Seat-lod time is around 30-40 min. (It takes around 50-60 min. door to door)
5. From TEMPOZAN to KAIYUKAN, it takes 3min. by walk.
＊The fare is ¥210 for one-way at this moment. You had better to prepare ¥100 coins and ¥10 coins for pay.
＊There is a children fare for under age 11 children.
＊I suggest you to use the bus for KAIYUKAN, it's more convenient and cheaper than train.
'''
