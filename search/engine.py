# -*- encode:utf8 -*-

__author__ = 'SHENOISZ'

from django.template.defaultfilters import slugify
import re

class Engine(object):

    obj = []
    method = False

    # for method get
    def remove(self, q):
        return slugify(q).replace('-', ' ').replace('+', ' ').replace('_', ' ')

    def loop(self,obj=[], fields=[], q='', items=[]):

        search = q.lower() if self.method else self.remove(q)
        end = len(search)
        start = 0

        start_ = 0
        end_ = end
        alterne = 0

        while search:

            total = len(items)

            if total <= 0:

                if search[:end] == '' or search[start:] == '' or search[start_:end_] == '':
                    items = []
                    break

                if alterne == 0:
                    items = self.items(obj, fields, search[:end])
                    end -= 1
                    alterne = 1

                elif alterne == 1:    
                    items = self.items(obj, fields, search[start:])
                    start += 1
                    alterne = 2 

                else: 
                    items = self.items(obj, fields, search[start_:end_])
                    start_ += 1
                    end_ -= 1
                    alterne = 0

            else:
                break

        return items              
            

    def items(self, obj=[], fields=[], q=''):

        novo = []
        count = len(fields)

        try:
            search = q.split(' ')
        except:
            search = [q]          

        for s in obj:

            found = False
            level = 0
            founded = count

            for f in fields:

                text = getattr(s, f)
                sear_count = 0

                for sear in search:
                    
                    if len(sear) < 3:
                        try:
                            sear_count += 1
                            sear = sear + search[sear_count]
                            regex = re.compile(sear)

                            if re.findall(regex, text.lower() if self.method else self.remove(text)):
                                founded -= 1
                                found = True
                        except:
                            pass
                    else:      
                        regex = re.compile(sear)
                        if re.findall(regex, text.lower() if self.method else self.remove(text)):
                            founded -= 1
                            found = True

                if found:
                    s.relevence = founded + level
                    s.save()
                    novo.append(s)
                    found = False
                    founded = 0
                    break 

                level += count    


        novo = sorted(novo, key=lambda x : x.relevence)        
        return novo

    def search(self, obj=None, fields=[], q='', order_by=None, limit=None, method='post', filter={}):

        if method == 'post':
            self.method = True

        if order_by and limit:
            if filter:
                self.obj = obj.objects.filter(**filter).order_by(order_by)[:limit]
            else:    
                self.obj = obj.objects.all().order_by(order_by)[:limit]
        else:  
            if filter:
                self.obj = obj.objects.filter(**filter)
            else:    
                self.obj = obj.objects.all()

        if q == '':
            return self.obj
        return self.loop(self.obj, fields, q,items=self.items(self.obj, fields, q))        