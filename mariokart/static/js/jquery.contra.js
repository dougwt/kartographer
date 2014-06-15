/*! jQuery Contra v1.0
 * http://jonraasch.com/blog/jquery-contra-plugin
 *
 * Copyright (c) 2009 Jon Raasch (http://jonraasch.com/)
 * Licensed under the MIT License (see http://dev.jonraasch.com/contra/docs#licensing)
 */
 
(function($) {
    $.contra = function( callback, opts ) {
        function checkIt( key ) {
            if ( key == opts.code[currStep] ) {
                currStep++;
                if ( currStep >= opts.code.length ) callback();
            }
            else currStep = 0;
        };
        
        if ( typeof callback != 'function' ) return false;
        
        var currStep = 0,
        
        opts = opts || {};
        opts.scope = opts.scope || $(document);

        // each array item is a step in the code
        opts.code = opts.code || [
            38,
            38,
            40,
            40,
            37,
            39,
            37,
            39,
            66,
            65,
            13
        ];
        
        opts.scope.keyup(function(ev) {
            checkIt( ev.which || ev.keyCode );
        });
    };
    
    $.fn.contra = function( callback, opts ) {
        var opts = opts || {};
        opts.scope = $(this);
        
        $.contra( callback, opts );
    };

})(jQuery);