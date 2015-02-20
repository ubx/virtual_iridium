import urllib, urllib2

import re


def sendPOST(url, data):
    #url = 'http://localhost:8080/rockblock'
    values = dict(imei='300234010753370', momsn='12345', transmit_time='2-10-10 10:41:50',
                  iridium_latitude='52.3867', iridium_longitude='0.2938', iridium_cep='8', data=data)
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    rsp = urllib2.urlopen(req)
    content = rsp.read()
    # print result
    pat = re.compile('Title:.*')
    print pat.search(content).group()


if __name__ == "__main__":
    sendPOST('http://localhost:8080/rockblock', 'Aaaaaaaaaaaaaaaaaaaaaaaaaaaa')