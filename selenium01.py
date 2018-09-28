from selenium import webdriver
driver = webdriver.Chrome(r'F:\Tools\Selenium3\chromedriver.exe')
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')
Weather = driver.find_element_by_id("forecastID")
place = Weather.text
CityWeather = place.split('℃\n')
Temperature = int(100)
curcity = []
for one in CityWeather:
    one = one.replace('℃','')
    city = one.split('\n')[0]
    TemMin = int(one.split('/')[1])
    if TemMin < Temperature:
        Temperature = TemMin
        Temperature = Temperature
        curcity = [city]
    elif TemMin == Temperature:
        curcity.append(city)
print('最低气温:%s℃ 当前城市:%s'%(Temperature,''.join(curcity)))
# driver.quit()


