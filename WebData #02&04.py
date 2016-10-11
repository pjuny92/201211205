{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 웹데이터 #2: 웹파일을 가져와서 자료구조에 넣기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import urllib2\n",
    "url='http://archive.ics.uci.edu/ml/machine-learning-databases/horse-colic/horse-colic.data'"
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
    "res = urllib2.urlopen(url)"
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
    "data = res.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "res.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(25437, str)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(data), type(data)"
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
    "lines = data.splitlines()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "line = lines[0].split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "28"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(line)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "1\n",
      "530101\n",
      "38.50\n",
      "66\n",
      "28\n",
      "3\n",
      "3\n",
      "?\n",
      "2\n",
      "5\n",
      "4\n",
      "4\n",
      "?\n",
      "?\n",
      "?\n",
      "3\n",
      "5\n",
      "45.00\n",
      "8.40\n",
      "?\n",
      "?\n",
      "2\n",
      "2\n",
      "11300\n",
      "00000\n",
      "00000\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "for item in line:\n",
    "    print item"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "_data = list()\n",
    "for line in lines:\n",
    "    lineData = line.split()\n",
    "    #print lineData\n",
    "    _data.append(lineData)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'2'"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "_data[0][0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "str"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(_data[0][1])"
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
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "492\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "1.64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum = 0\n",
    "for i in _data:\n",
    "    sum +=int(i[1])\n",
    "print sum\n",
    "float (sum)/len(_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "38.50\n",
      "39.2\n",
      "38.30\n",
      "39.10\n",
      "37.30\n",
      "?\n",
      "37.90\n",
      "?\n",
      "?\n",
      "38.30\n",
      "38.10\n",
      "39.10\n",
      "37.20\n",
      "38.00\n",
      "38.2\n",
      "37.60\n",
      "?\n",
      "37.50\n",
      "37.60\n",
      "39.4\n"
     ]
    }
   ],
   "source": [
    "for i in range(0,20):\n",
    "    print _data[i][3]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 웹데이터 #4: 한국 포털사이트에서 노래제목을 검색"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### regex"
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
    "import urllib"
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
    "keyword = '비오는'\n",
    "url = 'http://music.naver.com/search/search.nhn?query='+keyword+'&x=0&y=0'"
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
   "execution_count": 21,
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
   "execution_count": 22,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "instance"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
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
   "execution_count": 24,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "pos = mydata.find('트랙 리스트')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'\\xed'"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mydata[pos]"
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
    "pos1 = mydata.find('_title title NPI=', pos)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27563"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mydata.find('title=', pos+20)"
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
    "f = open('mydata.txt', 'w')\n",
    "f.write(mydata)\n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import re"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "p = re.compile('title=\".*비.?오는.*\"')\n",
    "res = p.findall(mydata)"
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
      "title=\"검색어 입력\" value=\"비오는\" maxlength=\"50\" accesskey=\"s\"\n",
      "title=\"비오는날\" alt=\"비오는날\"\n",
      "title=\"비오는 금요일\" alt=\"비오는 금요일\"\n",
      "title=\"비 오는 거리\" ><span class=\"ellipsis\"\n",
      "title=\"1집 비오는 거리\" class=\"_album NPI=a:album,r:1,i:682\"><span class=\"ellipsis\"\n",
      "title=\"비오는 날 수채화\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 날 수채화 1 OST\" class=\"_album NPI=a:album,r:2,i:33001\"><span class=\"ellipsis\"\n",
      "title=\"비 오는 날\" ><span class=\"ellipsis\"\n",
      "title=\"비 오는 날\" class=\"_album NPI=a:album,r:3,i:656486\"><span class=\"ellipsis\"\n",
      "title=\"비오는날 (동요) (멜로디 MR)\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 밤에\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 거리\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 압구정\" ><span class=\"ellipsis\"\n",
      "title=\"김현주의 비오는 거리\" class=\"_album NPI=a:album,r:8,i:117082\"><span class=\"ellipsis\"\n",
      "title=\"비 오는 거리  (Feat. 핫펠트)\" ><span class=\"ellipsis\"\n",
      "title=\"뉴에이지 연가 : 비 오는 날의 거리, 추억, 그리고 아름다운 재즈 피아노(Pop 올드 팝, 클래식, 영화 OST 베스트 연주 음악)\" class=\"_album NPI=a:album,r:10,i:636985\"><span class=\"ellipsis\"\n",
      "title=\"비 오는 거리\" ><span class=\"ellipsis\"\n",
      "title=\"비 오는 거리\" class=\"_album NPI=a:album,r:11,i:442032\"><span class=\"ellipsis\"\n",
      "title=\"비 오는 날의 수채화\" ><span class=\"ellipsis\"\n",
      "title=\"비 오는 날\" ><span class=\"ellipsis\"\n",
      "title=\"비 오는 날\" class=\"_album NPI=a:album,r:13,i:651748\"><span class=\"ellipsis\"\n",
      "title=\"비오는 날은 푸르다\" ><span class=\"ellipsis\"\n",
      "title=\"비오는 날은 푸르다\" class=\"_album NPI=a:album,r:14,i:660894\"><span class=\"ellipsis\"\n",
      "title=\"Rain Cello : 비 오는 날, 첼로\" class=\"_album NPI=a:album,r:15,i:559967\"><span class=\"ellipsis\"\n",
      "title=\"비오는 금요일\"\n",
      "title=\"비오는 금요일\" alt=\"비오는 금요일\" class=\"NPI=a:artist,r:,i:271713\"\n",
      "title=\"비 오는 날\"\n",
      "title=\"비 오는 날\"\n",
      "title=\"비오는 카페\"\n",
      "title=\"유ㄹish.1 - 비오는 거리\"\n",
      "title=\"비 오는 날\"\n",
      "title=\"비오는 압구정\"\n",
      "title=\"비오는 날에\"\n",
      "title=\"비오는 거리 (Feat. 단비)\"\n",
      "title=\"비오는 날의 수채화\"\n",
      "title=\"[cover] 비오는 거리 - 줄리\"\n",
      "title=\"비 오는 날의 분수\"\n",
      "title=\"비 오는 날, 생각나는 그 노래\"\n",
      "title=\"비오는 날 [데모]\"\n",
      "title=\"비오는 밤에\"\n"
     ]
    }
   ],
   "source": [
    "for item in res:\n",
    "    print item"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
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
