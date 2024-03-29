from pyquery import PyQuery as pq

html = '''<div class=‘content’>
    <ul id = 'haha'>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul></div>'''

doc = pq(html)
li = doc('.item-0.active')
print(li)
# 删除classactive
print(li.removeClass('active'))
# 增加class属性haha
print(li.addClass('haha'))