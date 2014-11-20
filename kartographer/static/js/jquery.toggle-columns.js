(function($){
  enable_toggleable_columns = function(column_prefs) {
    // column_prefs = column_prefs | null;

    // Preload jQuery objects
    var $priority = new Array();
    $priority[1] = $( "*[data-priority='1']" );
    $priority[2] = $( "*[data-priority='2']" );
    $priority[3] = $( "*[data-priority='3']" );

    var $col = new Array();
    $col['name'] = $( "*[data-column='name']" );
    $col['speed'] = $( "*[data-column='speed_ground']" );
    $col['speed_water'] = $( "*[data-column='speed_water']" );
    $col['speed_air'] = $( "*[data-column='speed_air']" );
    $col['speed_antigravity'] = $( "*[data-column='speed_antigravity']" );
    $col['acceleration'] = $( "*[data-column='acceleration']" );
    $col['weight'] = $( "*[data-column='weight']" );
    $col['handling'] = $( "*[data-column='handling_ground']" );
    $col['handling_water'] = $( "*[data-column='handling_water']" );
    $col['handling_air'] = $( "*[data-column='handling_air']" );
    $col['handling_antigravity'] = $( "*[data-column='handling_antigravity']" );
    $col['traction'] = $( "*[data-column='traction']" );
    $col['miniturbo'] = $( "*[data-column='miniturbo']" );

    var $toggle = new Array();
    $toggle['speed'] = $( "#table-toggle-speed" );
    $toggle['speed_hidden'] = $( "#table-toggle-speed-hidden" );
    $toggle['acceleration'] = $( "#table-toggle-acceleration" );
    $toggle['weight'] = $( "#table-toggle-weight" );
    $toggle['handling'] = $( "#table-toggle-handling" );
    $toggle['handling_hidden'] = $( "#table-toggle-handling-hidden" );
    $toggle['traction'] = $( "#table-toggle-traction" );
    $toggle['miniturbo'] = $( "#table-toggle-miniturbo" );
    $toggle['highlight_hidden'] = $( "#table-toggle-highlight-hidden" );
    $toggle['highlight_acceleration'] = $( "#table-toggle-highlight-acceleration" );
    $toggle['name'] = $( "#table-toggle-name" );

    // Bootstrap view breakpoints
    var screen_sm_min = 768;
    var screen_md_min = 992;
    var screen_lg_min = 1200;

    // Toggles background color for secret stats
    function toggleHighlightSecret() {
      $col['speed_water'].toggleClass('hidden-stat');
      $col['speed_air'].toggleClass('hidden-stat');
      $col['speed_antigravity'].toggleClass('hidden-stat');
      $col['handling_water'].toggleClass('hidden-stat');
      $col['handling_air'].toggleClass('hidden-stat');
      $col['handling_antigravity'].toggleClass('hidden-stat');
      $col['miniturbo'].toggleClass('hidden-stat');
    }

    // Toggles background color for inefficient acceleration values
    function toggleHighlightAcceleration() {
      $('td[data-column="acceleration"]:contains(".25")').toggleClass('inefficient-1');
      $('td[data-column="acceleration"]:contains(".50")').toggleClass('inefficient-2');
      $('td[data-column="acceleration"]:contains(".75")').toggleClass('inefficient-3');
    }

    function show_column(slug) {
      $toggle[slug].addClass("selected");

      if (slug == 'speed_hidden') {
        $col['speed_water'].removeClass("hidden");
        $col['speed_air'].removeClass("hidden");
        $col['speed_antigravity'].removeClass("hidden");
      }
      else if (slug == 'handling_hidden') {
        $col['handling_water'].removeClass("hidden");
        $col['handling_air'].removeClass("hidden");
        $col['handling_antigravity'].removeClass("hidden");
      } else {
        $col[slug].removeClass("hidden");
      }
    }

    function hide_column(slug) {
      $toggle[slug].removeClass("selected");

      if (slug == 'speed_hidden') {
        $col['speed_water'].addClass("hidden");
        $col['speed_air'].addClass("hidden");
        $col['speed_antigravity'].addClass("hidden");
      }
      else if (slug == 'handling_hidden') {
        $col['handling_water'].addClass("hidden");
        $col['handling_air'].addClass("hidden");
        $col['handling_antigravity'].addClass("hidden");
      } else {
        $col[slug].addClass("hidden");
      }
    }

    // Set the initial state for columns
    function initializeColumns() {

      function load_pref(name, default_show) {
        if (column_prefs[name] == true) {
          // alert(name + ' true');
          show_column(name);
        } else if (column_prefs[name] == false) {
          // alert(name + ' false');
          hide_column(name);
        } else if (default_show) {
          // alert(name + ' default show');
          show_column(name);
        } else {
          // alert(name + ' default hide');
          hide_column(name);
        }
      }

      // Prioritize columns based on screen size
      $priority[1].removeClass("hidden");
      $priority[2].addClass("hidden");
      $priority[3].addClass("hidden");

      var $width = $( window ).width();

      if ($width > screen_sm_min) {
        show_column('name');
        show_column('miniturbo');
      }
      if ($width > screen_lg_min) {
        show_column('speed_hidden');
        show_column('handling_hidden');
      }

      // Determine default state based on screen width
      var defaults = new Array();
      defaults['name'] = false;
      defaults['miniturbo'] = false;
      defaults['speed_hidden'] = false;
      defaults['handling_hidden'] = false;

      if ($width > screen_sm_min) {
        defaults['name'] = true;
        defaults['miniturbo'] = true;
      }
      if ($width > screen_lg_min) {
        defaults['speed_hidden'] = true;
        defaults['handling_hidden'] = true;
      }

      // Override screen defaults based on parameters
      load_pref('name', defaults['name']);
      load_pref('speed', true);
      load_pref('speed_hidden', defaults['speed_hidden']);
      load_pref('acceleration', true);
      load_pref('weight', true)
      load_pref('handling', true);
      load_pref('handling_hidden', defaults['handling_hidden']);
      load_pref('traction', true);
      load_pref('miniturbo', defaults['miniturbo']);

      // handle_pref('highlight_hidden');
      // handle_pref('highlight_acceleration', false);

      // Secret stat highlights
      $col['speed_water'].addClass('hidden-stat');
      $col['speed_air'].addClass('hidden-stat');
      $col['speed_antigravity'].addClass('hidden-stat');
      $col['handling_water'].addClass('hidden-stat');
      $col['handling_air'].addClass('hidden-stat');
      $col['handling_antigravity'].addClass('hidden-stat');
      $col['miniturbo'].addClass('hidden-stat');
    }

    // Execution begins here

    // Initialize Columns onLoad
    initializeColumns();

    // Handle dropdown click toggle events
    // #table-toggle-name
    $toggle['name'].click(function( event ) {
      $(this).toggleClass("selected");
      $col['name'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-speed
    $toggle['speed'].click(function( event ) {
      $(this).toggleClass("selected");
      $col['speed_ground'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-speed-hidden
    $toggle['speed_hidden'].click(function( event ) {
      $(this).toggleClass("selected");
      $col['speed_water'].toggleClass("hidden");
      $col['speed_air'].toggleClass("hidden");
      $col['speed_antigravity'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-acceleration
    $toggle['acceleration'].click(function( event ) {
      $(this).toggleClass("selected");
      $col['acceleration'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-weight
    $toggle['weight'].click(function( event ) {
      $(this).toggleClass("selected");
      $col['weight'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-handling
    $toggle['handling'].click(function( event ) {
      $(this).toggleClass("selected");
      $col['handling_ground'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-handling-hidden
    $toggle['handling_hidden'].click(function( event ) {
      $(this).toggleClass("selected");
      $col['handling_water'].toggleClass("hidden");
      $col['handling_air'].toggleClass("hidden");
      $col['handling_antigravity'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-traction
    $toggle['traction'].click(function( event ) {
      $(this).toggleClass("selected");
      $col['traction'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-miniturbo
    $toggle['miniturbo'].click(function( event ) {
      $(this).toggleClass("selected");
      $col['miniturbo'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-highlight
    $toggle['highlight_hidden'].click(function( event ) {
      $(this).toggleClass("selected");
      toggleHighlightSecret();
      event.stopPropagation();
    });
    $toggle['highlight_acceleration'].click(function( event ) {
      $(this).toggleClass("selected");
      toggleHighlightAcceleration();
      event.stopPropagation();
    });
  };
})(jQuery);
