#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/30 12:22
# @Author  : nanganglei
# @File    : footer-check.py

import sys
import re
reload(sys)
sys.setdefaultencoding("utf-8")
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

dict_footer_pc = {'网页首页sogou':'https://www.sogou.com/',
               '网页结果页':'https://www.sogou.com/web?query=%E4%B8%AD%E5%9B%BD&_asf=www.sogou.com&_ast=&amp;w=01019900&p=40040100&ie=utf8&from=index-login&s_from=index&sut=17197&amp;sst0=1514607794820&;lkt=0%2C0%2C0&sugsuv=00F32BB90A8198405A3B5D6930502119&amp;sugtime=1514607794820',
               # '网页首页sogo':'https://www.sogo.com/',
               # '小说首页':'https://yd.sogou.com/h5/index?gf=evrnew-d-p-i',
               #  '小说结果页':'https://yd.sogou.com/h5/search?query=china&gf=evrdh-d1-pidx-i&uID=PL_nlYC-OnhgThRK&sgid=25-11826340-AVpDnXh5mSlIV9UE8jk65d8',
               #  '应用首页':'http://as.sogo.com/index',
               #  '应用结果页':'http://as.sogo.com/so?w=1459&uID=PZm68XWSn4euHQuu&pid=34&query=china',
               '微信首页':'http://weixin.sogou.com/',
                '知识首页':'http://zhishi.sogou.com/',
                '知识结果页':'http://www.sogou.com/sogou?query=chian&interation=196636&chuidq=28&pid=sogou-wsse-926c11cc055de9b8&ie=utf8&w=01015002&sut=1535&sst0=1514611395044&lkt=0%2C0%2C0&amp;sugsuv=00F32BB90A8198405A3B5D6930502119&sugtime=1514611395044&amp;oq=&ri=0&sourceid=sugg&;suguuid=&amp;p=40040108',
                '微信结果页':'http://weixin.sogou.com/weixin?type=2&query=china&ie=utf8&s_from=input&amp;_sug_=y&amp;_sug_type_=&w=01019900&sut=678&sst0=1514608357450&lkt=1%2C1514608357347%2C1514608357347',
                '知乎首页':'http://zhihu.sogou.com/',
                '知乎结果页':'http://zhihu.sogou.com/zhihu?query=china&ie=utf8&w=&amp;sut=712&amp;sst0=1514608390251&amp;lkt=1%2C1514608390148%2C1514608390148',
                '新闻首页':'http://news.sogou.com/',
                '新闻结果页':'http://news.sogou.com/news?query=china&mode=1&w=01029901&sut=766&sst0=1514608443918&lkt=1%2C1514608443810%2C1514608443810',
                '明医首页':'http://mingyi.sogou.com/mingyi?ie=utf8&fr=common_index_nav&query=',
                '明医结果页':'http://mingyi.sogou.com/mingyi?query=china&_asf=www.sogou.com&_ast=&w=01019900&p=40040100&amp;ie=utf8&amp;sut=736&amp;sst0=1514608507968&;lkt=0%2C0%2C0',
                '英文首页':'http://english.sogou.com/',
                '英文结果页':'http://english.sogou.com/english?query=china&;_asf=www.sogou.com&_ast=&w=01019900&;p=40040100&amp;b_o_e=1&amp;ie=utf8&amp;sut=723&amp;sst0=1514608568366&amp;lkt=0%2C0%2C0',
                '翻译':'http://fanyi.sogou.com/',
                '图片首页':'http://pic.sogou.com/?p=40030500&;w=',
                '图片结果页':'http://pic.sogou.com/pics?query=china&w=05009900&p=40030500&_asf=pic.sogou.com&_ast=1514608669&sc=index&sut=1880&sst0=1514608668805',
                '视频首页':'http://m.v.sogou.com/?el=/vw/v?v=5&amp;w=1276',
                '视频结果页':'http://v.sogou.com/?query=&ie=utf8&p=40030600',
                '问问首页':'http://wenwen.sogou.com/?ch=videosearch',
                 '词典首页':'http://dict.sogou.com/',
                '词典结果页':'http://dict.sogou.com/cidian?v=5&;uID=PL_nlYC-OnhgThRK&amp;w=2153&;ie=utf8&;keyword=china',
                '学术首页':'http://scholar.sogou.com/xueshu',
                '学术结果页':'http://scholar.sogou.com/xueshu?keyword=china',
                '购物首页':'http://gouwu.sogou.com',
                '购物结果页':'http://gouwu.sogou.com/shop?ie=utf8&amp;query=china&p=40251501',
                '百科首页':'http://baike.sogou.com/Home.v?p=40051203',
                '百科结果页':'http://baike.sogou.com/v456899.htm',
                }

dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13G36  Safari/601.1")
dcap["phantomjs.page.settings.userAgent"] = (
    # "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
    # "Mozilla/5.0 (Linux; U; Android 7.0; zh-cn; HUAWEI MLA-TL10 Build/HUAWEIMLA-TL10) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/7.6 Mobile Safari/537.36"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36"
)
driver = webdriver.PhantomJS(desired_capabilities=dcap)

# querys_file = open('vue', 'r')
# querys = querys_file.readlines()
# num = len(querys)


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
    for key in dict_footer_pc:
        # print key
        url_tem =  dict_footer_pc[key]
        driver.get(url_tem)
        time.sleep(1)
        content = driver.page_source
        # content_lower = content.lower()
        cases = re.findall('201[78]\D.{,55}sogou',content,re.IGNORECASE|re.S)
        # print key,url_tem
        lenlen = len(cases)
        if lenlen < 1:
            print "pc-----" + key + "： " + "warning warning warning NO 2017/8 SOGOU!"
        else:
            print "pc-----" + key + "： " + cases[-1]




getFromA_jude()
# querys_file.close()
driver.close()
driver.quit()