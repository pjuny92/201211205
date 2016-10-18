import urllib
response = urllib.urlopen('https://www.google.com/finance/historical?q=KRX%3AKOSPI200&ei=MDHrV5m8E4uo0ATC5YC4Dg')
_html = response.read()

from lxml import etree
_htmlTree = etree.HTML(_html)

result = etree.tostring(_htmlTree, pretty_print=True, method="html")

nodes1 = _htmlTree.xpath('//*[@class="lm"]/text()')
nodes2 = _htmlTree.xpath('//*[@class="rgt"]/text()')
nodes3 = _htmlTree.xpath('//*[@class="rgt rm"]/text()')
str1 = _htmlTree.xpath('//*[@class="bb lm lft"]/text()')
str2 = _htmlTree.xpath('//*[@class="rgt bb"]/text()')
str3 = _htmlTree.xpath('//*[@class="rgt bb rm"]/text()')

for y in range(1):
    m = 4*y
    print str1[y].strip(), str2[m].strip(), str2[m+1].strip(), str2[m+2].strip(), str2[m+3].strip(), str3[y]
for i in range(30):
    n =4*i
    print nodes1[i].strip(), nodes2[n].strip(), nodes2[n+1].strip(), nodes2[n+2].strip(), nodes2[n+3].strip(), nodes3[i]