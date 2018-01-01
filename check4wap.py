#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/14 16:46
# @Author  : nanganglei
# @File    : run4zhongke.py


import sys
import re
reload(sys)
sys.setdefaultencoding("utf-8")
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

dict_footer_wap = {'网页首页sogou':'http://m.sogou.com/',
               '网页结果页':'http://m.sogou.com/web/searchList.jsp?uID=PL_nlYC-OnhgThRK&amp;v=5&from=index&amp;w=1274&;t=1514600976675&s_t=1514601033136&s_from=index&keyword=+china&pg=webSearchList&amp;suguuid=2e845a91-9463-4eb1-86af-3885ff60a4f6&sugsuv=AAH9vcBXHQAAAAqQY78OAQAAZAM%3D&sugtime=1514601033136',
               # '网页首页sogo':'https://m.sogo.com/?prs=9&rfh=1',
               '小说首页':'https://yd.sogou.com/h5/index?gf=evrnew-d-p-i',
                '小说结果页':'https://yd.sogou.com/h5/search?query=china&gf=evrdh-d1-pidx-i&uID=PL_nlYC-OnhgThRK&sgid=25-11826340-AVpDnXh5mSlIV9UE8jk65d8',
                '应用首页':'http://m.sogou.com/app/ios/so',
                '应用结果页':'http://m.sogou.com/app/ios/so?query=china&uID=PL_nlYC-OnhgThRK&v=5&w=1817',
                '知识首页':'http://zhishi.sogou.com/',
                '知识结果页':'https://m.sogou.com/web/sl?keyword=chia&uID=PL_nlYC-OnhgThRK&v=5&pid=sogou-waps-0baf163c24ed14b5&t=1514612185243&;s_t=1514612207271&channel=zhishi&channel=zhishi&;usetab=1',
               # '微信首页':'http://weixin.sogou.com/',
                '微信结果页':'http://weixin.sogou.com/weixinwap?query=china&amp;type=2&;ie=utf8&;_sug_=y&;_sug_type_=&s_from=input',
                '知乎首页':'http://zhihu.sogou.com/wap',
                '知乎结果页':'http://zhihu.sogou.com/zhihuwap?query=china&ie=utf8&w=2136&s_t=1514601513891',
                # '新闻首页':'http://news.sogou.com/?v=5&w=1276',
                '新闻结果页':'http://m.sogou.com/web/sl?query=china&p=42040301&s_t=1514601573043&channel=news',
                '明医首页':'http://mingyi.sogou.com/?fr=common_index_nav',
                '明医结果页':'http://mingyi.sogou.com/mingyi?keyword=china&;uID=PL_nlYC-OnhgThRK&amp;s_from=index&v=5&amp;t=1514601605248&s_t=1514601652371&pg=mingyiSearch',
                '英文首页':'http://english.sogou.com/?fr=common_index_nav',
                '英文结果页':'http://english.sogou.com/english?keyword=china&amp;uID=PL_nlYC-OnhgThRK&amp;v=5&from=eng_index&t=1514601665377&amp;s_t=1514601686419&;b_o_e=1',
                # '翻译':'http://fanyi.sogou.com/?fr=common_index_nav',
                '图片首页':'http://pic.sogou.com/pic/index.jsp?v=5&w=1276',
                '图片结果页':'http://pic.sogou.com/pic/searchList.jsp?uID=PL_nlYC-OnhgThRK&v=5&;statref=index_form_1&amp;keyword=%E5%88%98%E5%BE%B7%E5%8D%8E',
                '视频首页':'http://m.v.sogou.com/?el=/vw/v?v=5&amp;w=1276',
                '视频结果页':'http://m.v.sogou.com/v?query=111111111&w=06009900',
                '问问首页':'http://wenwen.sogou.com/?ch=fromwapsearch.index',
                 '词典首页':'http://dict.sogou.com/cidian',
                '词典结果页':'http://dict.sogou.com/cidian?v=5&;uID=PL_nlYC-OnhgThRK&amp;w=2153&;ie=utf8&;keyword=china',
                '学术首页':'http://scholar.sogou.com/xueshu',
                '学术结果页':'http://scholar.sogou.com/xueshu?keyword=china',
                '购物首页':'http://wap.gouwu.sogou.com/index.htm#filter=87',
                '购物结果页':'http://wap.gouwu.sogou.com/search?query=china&amp;sourceid=si_tbtn&ie=utf-8',
                '百科首页':'http://baike.sogou.com/m',
                '百科结果页':'http://baike.sogou.com/m/fullLemma?key=china',
                }

dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36  Safari/601.1")
dcap["phantomjs.page.settings.userAgent"] = (
    # "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    # "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI MLA-TL10 Build/HUAWEIMLA-TL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36"
    "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko)"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)



my_headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36',
              'Accept-Encoding' : 'gzip, deflate, br',
              'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
              'Referer':'https://wap.sogou.com/web/searchList.jsp?uID=V5npvumGTk-3uIl0&v=5&amp;dp=1&w=1278&t=1508233127824&s_t=1508233130135&amp;s_from=result_up&;htprequery=c&keyword=%e5%9c%a3%e5%a2%9f'}


def print_current_time():
    timeTemp = time.time()
    timeTempNext = time.localtime(timeTemp)
    timeNow = time.strftime("%Y-%m-%d-%H-%M-%S", timeTempNext)  #转化为当前时间
    return timeNow




def getFromA_jude():
    for key in dict_footer_wap:
        # print key
        url_tem =  dict_footer_wap[key]
        driver.get(url_tem)
        content = driver.page_source
        cases = re.findall('201[78]\D.{,50}sogou',content,re.IGNORECASE|re.S)

        lenlen = len(cases)
        if lenlen < 1:
            print "wap-----" + key + "： " + "warning warning warning NO 2017/8SOGOU!"
        else:
            print "wap-----" + key + "： " + cases[-1]




getFromA_jude()

driver.close()
driver.quit()