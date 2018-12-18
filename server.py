# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import json
import urllib.request

from urllib.parse import quote
import  string
from house_reg import HouseReg
#
class MainHandler(tornado.web.RequestHandler):
    
    api='ca287984c2f81377402c2ccd303c2be0'
    m={}    
    def location(self,city,district,community):
        add=city+district+community
        if add in self.m:
            return self.m[add]
        url='https://restapi.amap.com/v3/geocode/geo?address='+add+'&output=json&key='+self.api
        url = quote(url, safe = string.printable)
        print(url)
        resu = urllib.request.urlopen(url)
        
        js=resu.read()
        l=json.loads(js)
        lo=l['geocodes'][0]['location']
        ll=lo.split(',')
        res=(float(ll[0]),float(ll[1]))
        self.m[add]=res
        return res
    
    def get(self):
        city=self.get_argument('city','北京市')
        district = self.get_argument('district','海淀区')
        community=self.get_argument('community','北航') #小区
        lng,lat=self.location(city,district,community)
        square = float(self.get_argument('square','100'))
        living = int(self.get_argument('living',0))
        drawing = int(self.get_argument('drawing',0))
        kitchen = int(self.get_argument('kitchen',0))
        bath = int(self.get_argument('bath',0))
        floor = int(self.get_argument('floor',0))
        btype = int(self.get_argument('btype',0))
        ctime = int(self.get_argument('ctime',0))
        rcondition = int(self.get_argument('rcondition',0))
        struc = int(self.get_argument('struc',0))
        elevator = int(self.get_argument('elevator',0))
        five = int(self.get_argument('five',0))
        subway = int(self.get_argument('subway',0))
        arg=[lng,lat,square,living,drawing,kitchen,
             bath,floor,btype,ctime,rcondition,struc,elevator,
             five,subway]
        self.write(str(reg.result(arg)))

        


if __name__ == "__main__":
    reg=HouseReg()
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8124)
    tornado.ioloop.IOLoop.current().start()
