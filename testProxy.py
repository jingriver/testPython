import urllib2
proxy = urllib2.ProxyHandler({'http': 'http://xyang@jc1prxy3.global.knight.com:8080'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
print urllib2.urlopen("http://www.google.com/").read()
