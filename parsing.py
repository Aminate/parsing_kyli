


import requests
from bs4 import BeautifulSoup



#ПАРСИНГ САЙТА КУЛИКОВСКОЙ

url = 'https://site.kulikov.com' #на переменнной url ссылка сайта
response = requests.get('https://site.kulikov.com/katalog/tovary_kdk/torty/korzhevye/').text
soup = BeautifulSoup(response, 'lxml')

d = soup.find('div', class_="product-item").find('h3').find('a').text  #обращаюсь к названию торта
print(d.strip())   #Торт "Эстерхази" (0,650 кг)

price =soup.find('div',class_="product-item-info-container product-item-price-container").find('span',class_="product-item-price-current").text
print(price.strip()) #говорю что хочу в виде str и прощу убрать пустые пробелы
image =soup.find('div',class_="product-item").find('a').find('span',class_="product-item-image-alternative").get('style') #обраща
# -юсь к фотке торта

p = image.split()[1] 
p2 = p[5:]
p3 = p2[:-3]
print(url + p3)   #тут короче махинация как я удалю в ссылке фото ненужные элементы по индексу

url_ = 'https://site.kulikov.com'
response =requests.get('https://site.kulikov.com/katalog/tovary_kdk/vypechka/kruassany_i_sdobnaya_vypechka/').text
soup = BeautifulSoup(response,'lxml')
d2 = soup.find('div', class_="product-item").find('h3').find('a').text
print(d2.strip())
price=soup.find('div',class_="product-item-info-container product-item-price-container").find('span',class_="product-item-price-current").text
print(price.strip())
image1 =soup.find('div',class_="product-item").find('a',class_="product-item-image-wrapper").find('span',class_="product-item-image-alternative").get('style')
# print(image1)
a =image1.split()[1]
a2 =a[5:]
a3 =a2[:-3]
print(url_+ a3)
























#вывод:
# Торт "Эстерхази" (0,650 кг)
# 990 сом
# https://site.kulikov.com/upload/iblock/65f/d98zllbe0i20xzx7ybxjaszqbcmp14to/%D0%AD%D1%81%D1%82%D0%B5%D1%80%D1%85%D0%B0%D0%B7%D0%B8%20%281%29.png
# АМИНА МОЛОДЕЦ!!!!!!!!!


# def get_html(url):
#     response = requests.get(url)
#     return response.text


# def get_total_pages(html):
#     soup = BeautifulSoup(html, 'lxml') #обращение к библиотеке
#     tort_ul = soup.find('div', class_="product-item").find('h3').find('a').text
#     return tort_ul
# # print(get_total_pages())

										

									
				
#     # print(response.status_code) #при принте вышла 200 значит все отлично 
    
# def main():
#     cake_url = 'https://site.kulikov.com/katalog/tovary_kdk/torty/korzhevye/'
#     get_total_pages(get_html(cake_url))

# main()
