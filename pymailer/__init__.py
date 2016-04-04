""" Created by Jieyi on 3/5/16. """

__all__ = ['authority', 'autoMailer', 'internet', 'io_operation', 'mail', 'mailer']

debug_log = True

# Country language.
lang_list = ['Select a language', 'English', 'Tradition Chinese', 'Simple Chinese', 'Korea']
atta_lang_list = [None, '', 'chinese', 'chinese', '']
# Attachments name list.
attachment_list = ['Detail Map.png', 'Map.png', 'Kansai Int Access.pdf', 'GARBAGE.pdf',
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
