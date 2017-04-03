Search = function() {

    this.focus = function(text, key) {

        text.each(function() {

            var text = $(this).html();
            $(this).html(text.replace(key, '<span id="search-key">' + key + '</span>'));

        });
    };

    this.init = (args) => {

        var obj = $(args + ' .searck-key');
        var key = obj.html();
        var text = $(args + ' .effect-add');

        try {

            key = key.split(' ');
            for (var i = 0; i < key.length; i++) {
                if (key[i].length > 1) {
                    this.focus(text, key[i]);
                }
            }

        } catch (exception) {

            this.focus(text, key);
        }

        obj.mouseover(function() {
            $(args + ' #search-key').each(function() {
                $(this).addClass('search-style');
            });
        });

        obj.mouseout(function() {
            $(args + ' #search-key').each(function() {
                $(this).removeClass('search-style');
            });
        });
    };

}