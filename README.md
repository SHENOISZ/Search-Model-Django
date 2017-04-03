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
### Add class in html:
```
    <!-- add class search-effect -->
<div class="row search-effect">
    <div class="col-lg-12">
                                <!-- add class searck-key -->
        <h1>Buscar por: <span class="text-info searck-key">Notebook</span></h1>
        <ul>
            <!-- add class effect-add -->
            <li class="effect-add">Good notebook</li>
            <li class="effect-add">Notebook black core i3</li>
            <li class="effect-add">publish: April - 2 - 2017</li>
        </ul>
    </div>
</div>
```
### Starting the plugin:
```
<script>
    //initialize search effect
    var search = new Search();
    search.init();
</script>
```

![CSCore Logo](https://raw.githubusercontent.com/SHENOISZ/Search-Model-Django/master/screeshots/search-01.png)

![CSCore Logo](https://raw.githubusercontent.com/SHENOISZ/Search-Model-Django/master/screeshots/search-02.png)
