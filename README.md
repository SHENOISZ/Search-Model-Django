# Search-Model-Django
Search Model Django is a little searching in fields with rank


### Using

engine = Engine()
<br>

`
more importance ------------------------> less
`
<br>
fields=['name', 'slug','text']

fields=['name', 'slug']

fields=['text', 'slug']

obj = engine.search(obj=Model, fields=fields, q=search, method='post')

return render(request, 'index.html', {'obj': obj})

### More Options

obj = engine.search(obj=Model, fields=fields, q=search, method='post', filter={'name':'shenoisz'})

obj = engine.search(obj=Model, fields=fields, q=search, method='post', order_by='-views', limit=20)

obj = engine.search(obj=Model, fields=fields, q=search, method='post', order_by='-views', limit=20, filter={'name':'shenoisz'})

return render(request, 'index.html', {'obj': obj})

<br><br>

## Javascript plugin(required jQuery)
```
<link href="/static/css/search.css" rel="stylesheet">

<script src="/static/js/search.js"></script>
```

![CSCore Logo](https://raw.githubusercontent.com/SHENOISZ/Search-Model-Django/master/screeshots/search-01.png)

![CSCore Logo](https://raw.githubusercontent.com/SHENOISZ/Search-Model-Django/master/screeshots/search-02.png)
