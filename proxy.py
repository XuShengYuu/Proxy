import requests
from requests.exceptions import RequestException 
from lxml import etree
import random

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def get_proxy_page(ip_url):
    try:
        ip_response = requests.get(ip_url,headers=headers)
        if ip_response.status_code ==200:
            return ip_response.text
        return None
    except RequestException:
        return None

def parse_ip_page(ip_html):
    ip_list = []
    r = etree.HTML(ip_html)
    ips = r.xpath('//*[@id="ip_list"]/tr/td[2]/text()')
    # ip_pattern = re.compile('<tr class="odd".*?<td>(.*?)</td>.*?</tr>',re.S)
    # ips = re.findall(pattern,ip_html)
    # print(ips)
    for ip in ips:
	    try:
	        proxy = {'http':ip}
	        text_url = 'https://www.baidu.com/'
	        res = requests.get(url=text_url,proxies=proxy,headers=headers,timeout=1)
	        ip_list.append(ip)
	    except BaseException as e:
	        print(e)
    # print(ip_list)
    proxies= {'http':random.choice(ip_list)}    
    return proxies
    
# def get_random_ip(ip_list):
#     proxy_list = []
#     for ip in ip_list:
#         proxy_list.append('http://' + ip)
#     proxy_ip = random.choice(proxy_list)
#     proxies = {'http': proxy_ip}
#     return proxies

def main():
	ip_url ='http://www.xicidaili.com/nn/'
	ip_html = get_proxy_page(ip_url)
	parse_ip_page(ip_html)
	proxies = parse_ip_page(ip_html)
	# proxies = get_random_ip(ip_list)
	print(proxies)
	# print(ip_html)   




if __name__ == '__main__':
	main()
	# text_proxy(proxy)