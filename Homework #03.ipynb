{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 한국 포털 사이트에서 노래제목을 검색"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### css selector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import lxml.html\n",
    "from lxml.cssselect import CSSSelector"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import urllib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "keyword = '비오는'\n",
    "url = 'http://music.naver.com/search/search.nhn?query='+keyword+'&x=0&y=0'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "http://music.naver.com/search/search.nhn?query=비오는&x=0&y=0\n"
     ]
    }
   ],
   "source": [
    "print url"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "f = urllib.urlopen(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "mydata = f.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "html = lxml.html.fromstring(mydata)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sel = CSSSelector('#content > div:nth-child(4) \\\n",
    "    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \\\n",
    "    > table > tbody > tr > td.name > a.title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "results = sel(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "비 오는 거리\n",
      "비오는 날 수채화\n",
      "비 오는 날\n",
      "비오는거리\n",
      "비 오는 거리\n",
      "비오는 날 (Inst.)\n",
      "비오는날 (동요) (멜로디 MR)\n",
      "비오는 거리\n",
      "비 오는 거리  (Feat. 핫펠트)\n",
      "비오는 압구정\n",
      "One More Time\n",
      "Yesterday (비틀즈 예스터 데이 : CF `시몬스침대`)\n",
      "비오는 밤에\n",
      "비오는 남산\n",
      "비 오는 날의 수채화\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    print item.text_content()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sel = CSSSelector('table[summary] > tbody > ._tracklist_move > .name > a.title')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<Element a at 0x422ea48>,\n",
       " <Element a at 0x4284778>,\n",
       " <Element a at 0x42847c8>,\n",
       " <Element a at 0x4284818>,\n",
       " <Element a at 0x4284868>,\n",
       " <Element a at 0x42848b8>,\n",
       " <Element a at 0x4284908>,\n",
       " <Element a at 0x4284958>,\n",
       " <Element a at 0x42849a8>,\n",
       " <Element a at 0x42849f8>,\n",
       " <Element a at 0x4284a48>,\n",
       " <Element a at 0x4284a98>,\n",
       " <Element a at 0x4284ae8>,\n",
       " <Element a at 0x4284b38>,\n",
       " <Element a at 0x4284b88>]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sel(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sel = CSSSelector('table[summary] > tbody > ._tracklist_move')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "results = sel(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_selName = CSSSelector('.name > a.title')\n",
    "_selArtist = CSSSelector('._artist.artist')\n",
    "_selAlbum = CSSSelector('.album > a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_name=_selName(results[1])\n",
    "_artist=_selArtist(results[1])\n",
    "_album=_selAlbum(results[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이승훈 --- 비 오는 거리 --- 1집 비오는 거리\n",
      "강인원 --- 비오는 날 수채화 --- 비오는 날 수채화 1 OST\n",
      "오소연 --- 비 오는 날 --- 비 오는 날\n",
      "유레이 --- 비오는거리 --- 비오는 거리\n",
      "소울스타 (SoulstaR) --- 비 오는 거리 --- 비 오는 거리\n",
      "김민우 --- 비오는 날 (Inst.) --- 비오는 날\n",
      "동요시대 --- 비오는날 (동요) (멜로디 MR) --- 동요 MR반주 5\n",
      "서영은 --- 비오는 거리 --- 1집 Romantic 1\n",
      "베이빌론(Babylon) --- 비 오는 거리  (Feat. 핫펠트) --- BETWEEN US\n",
      "브라운 아이즈 --- 비오는 압구정 --- 2집 Reason 4 Breathing?\n",
      "Richard Marx --- One More Time --- 김현주의 비오는 거리\n",
      "Romantisch Jazzkapelle --- Yesterday (비틀즈 예스터 데이 : CF `시몬스침대`) --- 뉴에이지 연가 : 비 오는 날의 거리, 추억, 그리고 아름다운 재즈 피아노(Pop 올드 팝, 클래식, 영화 OST 베스트 연주 음악)\n",
      "루드 페이퍼(Rude Paper) --- 비오는 밤에 --- 1집 Paper Spectrum\n",
      "조영순 --- 비오는 남산 --- 무진장 트롯트 골든 1＆2\n",
      "SG 워너비 --- 비 오는 날의 수채화 --- Classic Odyssey\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    #print lxml.html.tostring(item)\n",
    "    _name=_selName(item)\n",
    "    _artist=_selArtist(item)\n",
    "    _album=_selAlbum(item)\n",
    "    if _name:\n",
    "        print _artist[0].text_content().strip(),\n",
    "        print \"---\",\n",
    "        print _name[0].text_content(),\n",
    "        print \"---\",\n",
    "        print _album[0].text_content()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## ip주소에서 지역정보 알아내기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import json\n",
    "import urllib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ipdata = urllib.urlopen('http://freegeoip.net/json/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'{\"ip\":\"1.233.142.175\",\"country_code\":\"KR\",\"country_name\":\"Republic of Korea\",\"region_code\":\"11\",\"region_name\":\"Seoul\",\"city\":\"Seoul\",\"zip_code\":\"\",\"time_zone\":\"Asia/Seoul\",\"latitude\":37.5985,\"longitude\":126.9783,\"metro_code\":0}\\n'"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ipdata.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def getCountry(ipAddress):\n",
    "    response = urllib.urlopen(\"http://freegeoip.net/json/\"+ipAddress).read().decode('utf-8')\n",
    "    responseJson = json.loads(response)\n",
    "    return responseJson.get(\"country_code\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "KR\n"
     ]
    }
   ],
   "source": [
    "print(getCountry(\"1.233.142.175\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 국제학회 목록을 크롤링하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import lxml.html\n",
    "from lxml.cssselect import CSSSelector\n",
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "r = requests.get('https://www.ieee.org/conferences_events/index.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "html = lxml.html.fromstring(r.text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sel = CSSSelector('div.content-c > div:nth-child(1) > div > div:nth-child(2)')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "results = sel(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "print len(results)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    print item.get('href')\n",
    "    print item.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<div><p></p><p><a target=\"\" href=\"http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=39212&amp;WT.mc_id=con_hi-poct_16\">2016 IEEE Healthcare Innovation Point-Of-Care Technologies Conference (HI-POCT)</a><br> Cancun, Mexico | 9 - 11 November 2016&#160;</p> <p><a target=\"\" href=\"http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=38831&amp;WT.mc_id=con_sgc_16\">2016 IEEE International Conference on Smart Grid Communications (SmartGridComm) </a><br> Sydney, Australia | 6 - 9 November 2016</p> <p><a target=\"\" href=\"http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=38386&amp;WT.mc_id=con_itsc_16\">2016 IEEE 19th International Conference on Intelligent Transportation Systems (ITSC)</a><br> Rio de Janeiro, Brazil | 1 - 4 November 2016</p> <p><a target=\"\" href=\"http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=39005&amp;WT.mc_id=con_milcom_16\">MILCOM 2016 - 2016 IEEE Military Communications Conference (MILCOM)</a><br>Baltimore, MD, USA | 1 - 3 November 2016</p></div>\r\n",
      "\t\t\t\t\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    print lxml.html.tostring(item)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sel = CSSSelector('#inner-container > div.content-gray > div.content-lc \\\n",
    "        > div.content-lc-bottom > div.content-c > div:nth-child(1) > div \\\n",
    "        > div p > br')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<a target=\"\" href=\"http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=39212&amp;WT.mc_id=con_hi-poct_16\">2016 IEEE Healthcare Innovation Point-Of-Care Technologies Conference (HI-POCT)</a>\n",
      "<a target=\"\" href=\"http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=38831&amp;WT.mc_id=con_sgc_16\">2016 IEEE International Conference on Smart Grid Communications (SmartGridComm) </a>\n",
      "<a target=\"\" href=\"http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=38386&amp;WT.mc_id=con_itsc_16\">2016 IEEE 19th International Conference on Intelligent Transportation Systems (ITSC)</a>\n",
      "<a target=\"\" href=\"http://www.ieee.org/conferences_events/conferences/conferencedetails/index.html?Conf_ID=39005&amp;WT.mc_id=con_milcom_16\">MILCOM 2016 - 2016 IEEE Military Communications Conference (MILCOM)</a>\n",
      "<a href=\"#top\">top of page</a>\n",
      "<a target=\"_blank\" href=\"mailto:ieee-mce@ieee.org\">ieee-mce@ieee.org</a>\n",
      "<a target=\"\" href=\"mailto:mcminfo@ieee.org\">mce-sales@ieee.org</a>\n",
      "<a target=\"\" href=\"/conferences_events/conferences/organizers/index.html?WT.mc_id=lp_ce_rfc\">Resources for conference organizers</a>\n",
      "<a href=\"#top\">top of page</a>\n",
      "<a href=\"#top\">top of page</a>\n",
      "<a href=\"#top\">top of page</a>\n",
      "<a href=\"#top\">top of page</a>\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    print lxml.html.tostring(item)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "sel = CSSSelector('div.box-c-indent p > a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "results = sel(html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[<Element a at 0x4635638>, <Element a at 0x4635a98>, <Element a at 0x4635458>, <Element a at 0x4635408>, <Element a at 0x46354f8>, <Element a at 0x4635548>, <Element a at 0x4635598>, <Element a at 0x46355e8>, <Element a at 0x4635688>, <Element a at 0x4635728>, <Element a at 0x4635778>, <Element a at 0x46357c8>]\n"
     ]
    }
   ],
   "source": [
    "print results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2016 IEEE Healthcare Innovation Point-Of-Care Technologies Conference (HI-POCT)\n",
      "2016 IEEE International Conference on Smart Grid Communications (SmartGridComm) \n",
      "2016 IEEE 19th International Conference on Intelligent Transportation Systems (ITSC)\n",
      "MILCOM 2016 - 2016 IEEE Military Communications Conference (MILCOM)\n",
      "top of page\n",
      "ieee-mce@ieee.org\n",
      "mce-sales@ieee.org\n",
      "Resources for conference organizers\n",
      "top of page\n",
      "top of page\n",
      "top of page\n",
      "top of page\n"
     ]
    }
   ],
   "source": [
    "for item in results:\n",
    "    print item.text_content()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 프리미어리그 크롤링"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "url = 'http://www.bbc.co.uk/sport/football/premier-league/results'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import requests"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "r = requests.get(url)\n",
    "_html = r.text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "209042"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(_html)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "78319"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "_html.find('table-stats')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def getIndicesOfAllTableStats(string, query):\n",
    "    listindex=list()\n",
    "    offset=0\n",
    "    i = string.find(query, offset)\n",
    "    while i >= 0:\n",
    "        listindex.append(i)\n",
    "        i = string.find(query, i + 1)\n",
    "    return listindex"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "param1 = _html\n",
    "param2 = 'table-stats'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[78319, 83365, 89435, 91426, 93403, 95399, 104542, 109601, 115677, 117658, 119641, 121625, 130771, 133797, 142906, 145926, 154015, 156004, 157984, 160991, 180503]\n"
     ]
    }
   ],
   "source": [
    "_indices=getIndicesOfAllTableStats(param1, param2)\n",
    "print _indices"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "from scrapy.selector import Selector\n",
    "_res=Selector(text=_html).xpath(\"//table[@class='table-stats']/tbody/tr[@class='report']/td[@class='match-details']/p\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<p>\n",
      "                <span class=\"team-home teams\">\n",
      "                                        <a href=\"/sport/football/teams/manchester-united\">Man Utd</a>                </span>\n",
      "                  <span class=\"score\"> <abbr title=\"Score\"> 1-1 </abbr> </span>                  <span class=\"team-away teams\">\n",
      "                    <a href=\"/sport/football/teams/stoke-city\">Stoke</a>                </span>\n",
      "                                            </p>\n"
     ]
    }
   ],
   "source": [
    "print _res[0].extract()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Man Utd 1-1 1 1 Stoke\n",
      "Leicester 0-0 0 0 Southampton\n",
      "Tottenham 2-0 2 0 Man City\n",
      "Burnley 0-1 0 1 Arsenal\n",
      "Swansea 1-2 1 2 Liverpool\n",
      "Hull 0-2 0 2 Chelsea\n",
      "Sunderland 1-1 1 1 West Brom\n",
      "Watford 2-2 2 2 Bournemouth\n",
      "West Ham 1-1 1 1 Middlesbrough\n",
      "Everton 1-1 1 1 Crystal Palace\n",
      "Burnley 2-0 2 0 Watford\n",
      "West Ham 0-3 0 3 Southampton\n",
      "Man Utd 4-1 4 1 Leicester\n",
      "Bournemouth 1-0 1 0 Everton\n",
      "Liverpool 5-1 5 1 Hull\n",
      "Middlesbrough 1-2 1 2 Tottenham\n",
      "Stoke 1-1 1 1 West Brom\n",
      "Sunderland 2-3 2 3 Crystal Palace\n",
      "Swansea 1-3 1 3 Man City\n",
      "Arsenal 3-0 3 0 Chelsea\n",
      "Watford 3-1 3 1 Man Utd\n",
      "Crystal Palace 4-1 4 1 Stoke\n",
      "Southampton 1-0 1 0 Swansea\n",
      "Tottenham 1-0 1 0 Sunderland\n",
      "Hull 1-4 1 4 Arsenal\n",
      "Leicester 3-0 3 0 Burnley\n",
      "Man City 4-0 4 0 Bournemouth\n",
      "West Brom 4-2 4 2 West Ham\n",
      "Everton 3-1 3 1 Middlesbrough\n",
      "Chelsea 1-2 1 2 Liverpool\n",
      "Sunderland 0-3 0 3 Everton\n",
      "Swansea 2-2 2 2 Chelsea\n",
      "Man Utd 1-2 1 2 Man City\n",
      "Arsenal 2-1 2 1 Southampton\n",
      "Bournemouth 1-0 1 0 West Brom\n",
      "Burnley 1-1 1 1 Hull\n",
      "Middlesbrough 1-2 1 2 Crystal Palace\n",
      "Stoke 0-4 0 4 Tottenham\n",
      "West Ham 2-4 2 4 Watford\n",
      "Liverpool 4-1 4 1 Leicester\n",
      "West Brom 0-0 0 0 Middlesbrough\n",
      "Man City 3-1 3 1 West Ham\n",
      "Tottenham 1-1 1 1 Liverpool\n",
      "Chelsea 3-0 3 0 Burnley\n",
      "Crystal Palace 1-1 1 1 Bournemouth\n",
      "Everton 1-0 1 0 Stoke\n",
      "Leicester 2-1 2 1 Swansea\n",
      "Southampton 1-1 1 1 Sunderland\n",
      "Watford 1-3 1 3 Arsenal\n",
      "Hull 0-1 0 1 Man Utd\n",
      "Sunderland 1-2 1 2 Middlesbrough\n",
      "West Ham 1-0 1 0 Bournemouth\n",
      "Stoke 1-4 1 4 Man City\n",
      "Burnley 2-0 2 0 Liverpool\n",
      "Swansea 0-2 0 2 Hull\n",
      "Tottenham 1-0 1 0 Crystal Palace\n",
      "Watford 1-2 1 2 Chelsea\n",
      "West Brom 1-2 1 2 Everton\n",
      "Leicester 0-0 0 0 Arsenal\n",
      "Man Utd 2-0 2 0 Southampton\n",
      "Chelsea 2-1 2 1 West Ham\n",
      "Bournemouth 1-3 1 3 Man Utd\n",
      "Arsenal 3-4 3 4 Liverpool\n",
      "Hull 2-1 2 1 Leicester\n",
      "Burnley 0-1 0 1 Swansea\n",
      "Crystal Palace 0-1 0 1 West Brom\n",
      "Everton 1-1 1 1 Tottenham\n",
      "Middlesbrough 1-1 1 1 Stoke\n",
      "Southampton 1-1 1 1 Watford\n",
      "Man City 2-1 2 1 Sunderland\n"
     ]
    }
   ],
   "source": [
    "for entry in _res:\n",
    "    home_team = entry.xpath(\"span[@class='team-home teams']/a/text()\").extract()\n",
    "    score = entry.xpath(\"span[@class='score']/abbr/text()\").extract()\n",
    "    away_team = entry.xpath(\"span[@class='team-away teams']/a/text()\").extract()\n",
    "    if home_team and score and away_team:\n",
    "        home_team = home_team[0].strip()\n",
    "        score = score[0].strip()\n",
    "        home_goals = int(score.split('-')[0])\n",
    "        away_goals = int(score.split('-')[1])\n",
    "        away_team = away_team[0].strip()\n",
    "    print home_team, score, home_goals, away_goals, away_team"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [Root]",
   "language": "python",
   "name": "Python [Root]"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
