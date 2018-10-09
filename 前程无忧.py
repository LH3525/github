from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(r'F:\Tools\Selenium3\chromedriver.exe')
driver.implicitly_wait(10)
driver.get('https://www.51job.com/')
#窗口最大化
driver.maximize_window()
#选择高级搜索
driver.find_element_by_css_selector("div.ush a[href*='51job.com']").click()
# 输入搜索关键词 python
driver.find_element_by_id('kwdselectid').send_keys('python')
driver.find_element_by_css_selector('div.tit').click()
#选择被选中的所有城市
driver.find_element_by_id('work_position_input').click()
cities = driver.find_elements_by_css_selector('#work_position_click_center_right_list_000000 em[class=on]')
for one in cities:
    one.click()
#选中杭州
driver.find_element_by_id('work_position_click_center_right_list_category_000000_080200').click()
#点击确定按钮
driver.find_element_by_id('work_position_click_bottom_save').click()
# 职能类别 选 计算机软件 -> 高级软件工程师
driver.find_element_by_id('funtype_click').click()
driver.find_element_by_id('funtype_click_center_right_list_category_0100_0100').click()
driver.find_element_by_id('funtype_click_center_right_list_sub_category_each_0100_0106').click()
driver.find_element_by_id('funtype_click_bottom_save').click()
#选择公司性质
driver.find_element_by_id('cottype_list').click()
driver.find_element_by_css_selector('#cottype_list span.li[data-value="01"]').click()
#选择工作年限
driver.find_element_by_id('workyear_list').click()
driver.find_element_by_css_selector("#workyear_list span.li[data-value='02']").click()
#点击搜索按钮
driver.find_element_by_css_selector("div[class='btnbox p_sou'] span:nth-child(1)").click()
#列表获取内容
jobs = driver.find_elements_by_css_selector('#resultList div[class=el]')
for job in jobs:
    fields = job.find_elements_by_tag_name('span')
    print('|'.join(field.text for field in fields))
driver.quit()
