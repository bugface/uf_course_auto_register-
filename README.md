# README #
### What is this repository for? ###
The script can inform you when there is a course available as your requirement

### How do I get set up? ###
requirment: python 3.5, selenium package, chrome-driver
the script tested only in linux environment, you might need to tweak the code to fit for other OS

### Who do I talk to? ###
alexgre@ufl.edu

### if you do not want to see the real desktop use code below ###
```python
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

browser = webdriver.Firefox()
browser.get('http://www.google.com')
print browser.title
browser.quit()

display.stop()
```
