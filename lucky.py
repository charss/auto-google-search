from msedge.selenium_tools import Edge, EdgeOptions
import sys

print('Googling...') # Display text while downloading the Google page
page = ('https://google.com/search?q=' + ' '.join(sys.argv[1:]))
options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)
driver.get(page)
# stages = driver.find_element_by_xpath("//div[@class='yuRUbf']//a")
stages = driver.find_elements_by_css_selector(".yuRUbf > a")

# links = [elem.get_attribute('href') for elem in elems]
numOpen = min(5, len(stages))
for i in range(numOpen):
    # Open a new window
    x = stages[i].get_attribute('href')
    print(x)
    driver.execute_script("window.open('" + x + "','_blank');")
    # driver.execute_script("window.open('" + x + "', 'new window')")
    # driver.execute_script("window.open(%s);" % page)

    # Switch to the new window and open URL B
    # driver.get(stages[i].get_attribute('href'))
    # driver.switch_to.window(driver.window_handles[i + 1])
    # print(stages[i].get_attribute('href'))
    # driver.get(stages[i].get_attribute('href'))
   
