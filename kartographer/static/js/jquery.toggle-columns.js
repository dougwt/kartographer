(function($){
  ////////////////////////////////////////////////////////
  // Nifty csrftoken functions for ajax from django docs
  ////////////////////////////////////////////////////////
  // fetch csrftoken using jQuery
  getCookie = function(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
  csrfSafeMethod = function(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  ////////////////////////////////////////////////////////

  // Makes an AJAX POST request to store the updated preference
  set_pref = function(preference, value) {
    if (preference != "" && value != "") {
      var data = { preference:preference, value:value };
      var args = { type:"POST", url:"/ajax_set_pref/", data:data, complete:null };
      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        }
      });
      $.ajax(args);
    }
    else {
      // display an explanation of failure
    }
    return false;
  };

  remove_kart = function(character, kart, wheel, glider, $row) {
    if (character != "" && kart != "" && wheel != "" && glider != "" && $row != "") {

      // alert( "(" + character + ", " + kart + ", " + wheel + ", " + glider + ")");

      var data = { character:character, kart:kart, wheel:wheel, glider:glider };
      var args = { type:"POST", url:"/ajax_remove_kart/", data:data, complete:null };
      $.ajaxSetup({
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        }
      });
      $.ajax(args).done( function() {
        $row.remove();
      });
    }
    else {
      // display an explanation of failure
    }
    return false;
  }
  enable_toggleable_columns = function(column_prefs) {
    // column_prefs = column_prefs | null;

    ////////////////////////
    // INITIALIZE
    ////////////////////////

    // Preload commonly used jQuery objects
    // Priority columns
    var $priority = new Array();
    $priority[1] = $( "*[data-priority='1']" );
    $priority[2] = $( "*[data-priority='2']" );
    $priority[3] = $( "*[data-priority='3']" );

    // Table columns
    var $col = new Array();
    $col['name'] = $( "*[data-column='name']" );
    $col['speed_ground'] = $( "*[data-column='speed_ground']" );
    $col['speed_water'] = $( "*[data-column='speed_water']" );
    $col['speed_air'] = $( "*[data-column='speed_air']" );
    $col['speed_antigravity'] = $( "*[data-column='speed_antigravity']" );
    $col['acceleration'] = $( "*[data-column='acceleration']" );
    $col['weight'] = $( "*[data-column='weight']" );
    $col['handling_ground'] = $( "*[data-column='handling_ground']" );
    $col['handling_water'] = $( "*[data-column='handling_water']" );
    $col['handling_air'] = $( "*[data-column='handling_air']" );
    $col['handling_antigravity'] = $( "*[data-column='handling_antigravity']" );
    $col['traction'] = $( "*[data-column='traction']" );
    $col['miniturbo'] = $( "*[data-column='miniturbo']" );

    // Dropdown toggles
    var $toggle = new Array();
    $toggle['name'] = $( "#table-toggle-name" );
    $toggle['speed_ground'] = $( "#table-toggle-speed" );
    $toggle['speed_hidden'] = $( "#table-toggle-speed-hidden" );
    $toggle['acceleration'] = $( "#table-toggle-acceleration" );
    $toggle['weight'] = $( "#table-toggle-weight" );
    $toggle['handling_ground'] = $( "#table-toggle-handling" );
    $toggle['handling_hidden'] = $( "#table-toggle-handling-hidden" );
    $toggle['traction'] = $( "#table-toggle-traction" );
    $toggle['miniturbo'] = $( "#table-toggle-miniturbo" );
    $toggle['highlight_hidden'] = $( "#table-toggle-highlight-hidden" );
    $toggle['highlight_acceleration'] = $( "#table-toggle-highlight-acceleration" );

    // Bootstrap view breakpoints
    var screen_sm_min = 768;
    var screen_md_min = 992;
    var screen_lg_min = 1200;

    ////////////////////////
    // FUNCTIONS
    ////////////////////////

    // Toggle background color for secret stats
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

    // Changes a View preference's state to visible/selected
    function show_column(slug) {
      if (slug == 'speed_hidden') {
        $toggle['speed_hidden'].addClass("selected");
        $col['speed_water'].removeClass("hidden");
        $col['speed_air'].removeClass("hidden");
        $col['speed_antigravity'].removeClass("hidden");
      } else if (slug == 'handling_hidden') {
        $toggle['handling_hidden'].addClass("selected");
        $col['handling_water'].removeClass("hidden");
        $col['handling_air'].removeClass("hidden");
        $col['handling_antigravity'].removeClass("hidden");
      } else if (slug == 'highlight_hidden') {
        $toggle['highlight_hidden'].addClass("selected");
        $col['speed_water'].addClass('hidden-stat');
        $col['speed_air'].addClass('hidden-stat');
        $col['speed_antigravity'].addClass('hidden-stat');
        $col['handling_water'].addClass('hidden-stat');
        $col['handling_air'].addClass('hidden-stat');
        $col['handling_antigravity'].addClass('hidden-stat');
        $col['miniturbo'].addClass('hidden-stat');
      } else if (slug == 'highlight_acceleration') {
        $toggle['highlight_acceleration'].addClass("selected");
        $('#kart-list td[data-column="acceleration"]:contains(".25")').addClass('inefficient-1');
        $('#kart-list td[data-column="acceleration"]:contains(".5")').addClass('inefficient-2');
        $('#kart-list td[data-column="acceleration"]:contains(".75")').addClass('inefficient-3');
      } else {
        $toggle[slug].addClass("selected");
        $col[slug].removeClass("hidden");
      }
    }

    // Changes a View preference's state to hidden/unselected
    function hide_column(slug) {
      if (slug == 'speed_hidden') {
        $toggle['speed_hidden'].removeClass("selected");
        $col['speed_water'].addClass("hidden");
        $col['speed_air'].addClass("hidden");
        $col['speed_antigravity'].addClass("hidden");
      } else if (slug == 'handling_hidden') {
        $toggle['handling_hidden'].removeClass("selected");
        $col['handling_water'].addClass("hidden");
        $col['handling_air'].addClass("hidden");
        $col['handling_antigravity'].addClass("hidden");
      } else if (slug == 'highlight_hidden') {
        $toggle['highlight_hidden'].removeClass("selected");
        $col['speed_water'].removeClass('hidden-stat');
        $col['speed_air'].removeClass('hidden-stat');
        $col['speed_antigravity'].removeClass('hidden-stat');
        $col['handling_water'].removeClass('hidden-stat');
        $col['handling_air'].removeClass('hidden-stat');
        $col['handling_antigravity'].removeClass('hidden-stat');
        $col['miniturbo'].removeClass('hidden-stat');
      } else if (slug == 'highlight_acceleration') {
        $toggle['highlight_acceleration'].removeClass("selected");
        $('#kart-list td[data-column="acceleration"]:contains(".25")').removeClass('inefficient-1');
        $('#kart-list td[data-column="acceleration"]:contains(".5")').removeClass('inefficient-2');
        $('#kart-list td[data-column="acceleration"]:contains(".75")').removeClass('inefficient-3');
      } else {
        $toggle[slug].removeClass("selected");
        $col[slug].addClass("hidden");
      }
    }

    // Set the initial state of all columns
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
      load_pref('speed_ground', true);
      load_pref('speed_hidden', defaults['speed_hidden']);
      load_pref('acceleration', true);
      load_pref('weight', true)
      load_pref('handling_ground', true);
      load_pref('handling_hidden', defaults['handling_hidden']);
      load_pref('traction', true);
      load_pref('miniturbo', defaults['miniturbo']);
      load_pref('highlight_hidden', true);
      load_pref('highlight_acceleration', true);
    }

    ////////////////////////
    // onLoad begins here
    ////////////////////////

    // Initialize Columns onLoad
    initializeColumns();

    // Handle dropdown click toggle events
    // #table-toggle-name
    $toggle['name'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('name', 'false');
      } else {
        set_pref('name', 'true');
      }
      $(this).toggleClass("selected");
      $col['name'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-speed
    $toggle['speed_ground'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('speed_ground', 'false');
      } else {
        set_pref('speed_ground', 'true');
      }
      $(this).toggleClass("selected");
      $col['speed_ground'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-speed-hidden
    $toggle['speed_hidden'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('speed_hidden', 'false');
      } else {
        set_pref('speed_hidden', 'true');
      }
      $(this).toggleClass("selected");
      $col['speed_water'].toggleClass("hidden");
      $col['speed_air'].toggleClass("hidden");
      $col['speed_antigravity'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-acceleration
    $toggle['acceleration'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('acceleration', 'false');
      } else {
        set_pref('acceleration', 'true');
      }
      $(this).toggleClass("selected");
      $col['acceleration'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-weight
    $toggle['weight'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('weight', 'false');
      } else {
        set_pref('weight', 'true');
      }
      $(this).toggleClass("selected");
      $col['weight'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-handling
    $toggle['handling_ground'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('handling_ground', 'false');
      } else {
        set_pref('handling_ground', 'true');
      }
      $(this).toggleClass("selected");
      $col['handling_ground'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-handling-hidden
    $toggle['handling_hidden'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('handling_hidden', 'false');
      } else {
        set_pref('handling_hidden', 'true');
      }
      $(this).toggleClass("selected");
      $col['handling_water'].toggleClass("hidden");
      $col['handling_air'].toggleClass("hidden");
      $col['handling_antigravity'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-traction
    $toggle['traction'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('traction', 'false');
      } else {
        set_pref('traction', 'true');
      }
      $(this).toggleClass("selected");
      $col['traction'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-miniturbo
    $toggle['miniturbo'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('miniturbo', 'false');
      } else {
        set_pref('miniturbo', 'true');
      }
      $(this).toggleClass("selected");
      $col['miniturbo'].toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-highlight
    $toggle['highlight_hidden'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('highlight_hidden', 'false');
      } else {
        set_pref('highlight_hidden', 'true');
      }
      $(this).toggleClass("selected");
      toggleHighlightSecret();
      event.stopPropagation();
    });
    $toggle['highlight_acceleration'].click(function( event ) {
      if ($(this).hasClass("selected")) {
        set_pref('highlight_acceleration', 'false');
      } else {
        set_pref('highlight_acceleration', 'true');
      }
      $(this).toggleClass("selected");
      toggleHighlightAcceleration();
      event.stopPropagation();
    });
  };
})(jQuery);
