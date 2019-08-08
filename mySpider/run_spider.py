from scrapy import cmdline


cmdstr = " scrapy crawl itcast "
#cmdstr += " -o itcast.csv -t csv  "
cmdline.execute(cmdstr.split())
