Search = function() {

    this.focus = function(text, key) {

        text.each(function() {

            var text = $(this).html();
            $(this).html(text.replace(key, '<span id="search-key">' + key + '</span>'));

        });
    };

    this.init = () => {

        var obj = $('.search-effect .searck-key');
        var key = obj.html();
        var text = $('.search-effect .effect-add');

        try {

            key = key.split(' ');
            for (var i = 0; i < key.length; i++) this.focus(text, key[i]);

        } catch (exception) {

            this.focus(text, key);
        }

        obj.mouseover(function() {
            $('.search-effect #search-key').each(function() {
                $(this).addClass('search-style');
            });
        });

        obj.mouseout(function() {
            $('.search-effect #search-key').each(function() {
                $(this).removeClass('search-style');
            });
        });
    };

}