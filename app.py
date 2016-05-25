from download import download
from scroll import scroll

brightness = 50

d = download()
scroll = scroll(brightness)
shop = "pimoroni"
val = d.get_total_stock(shop)
while (val!=0 or val==0):
  print(str(val)+ " in stock, at: " + shop)
  scroll.show(val)
  time.sleep(60.0)
