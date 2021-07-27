# 导入cmdline模块, 可以实现控制终端命令行
from scrapy import cmdline

# 使用execute()方法, 输入scrapy的命令
cmdline.execute(['scrapy', 'crawl', 'douban_movie'])