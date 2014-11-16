(function($){

  ////////////////////////////////////////
  // enable_toggleable_list_columns
  ////////////////////////////////////////

  enable_toggleable_list_columns = function() {

    // Preload jQuery objects
    var $priority1 = $( "*[data-priority='1']" );
    var $priority2 = $( "*[data-priority='2']" );
    var $priority3 = $( "*[data-priority='3']" );

    var $col_speed_ground = $( "*[data-column='speed_ground']" );
    var $col_speed_water = $( "*[data-column='speed_water']" );
    var $col_speed_air = $( "*[data-column='speed_air']" );
    var $col_speed_antigravity = $( "*[data-column='speed_antigravity']" );
    var $col_acceleration = $( "*[data-column='acceleration']" );
    var $col_weight = $( "*[data-column='weight']" );
    var $col_handling_ground = $( "*[data-column='handling_ground']" );
    var $col_handling_water = $( "*[data-column='handling_water']" );
    var $col_handling_air = $( "*[data-column='handling_air']" );
    var $col_handling_antigravity = $( "*[data-column='handling_antigravity']" );
    var $col_traction = $( "*[data-column='traction']" );
    var $col_miniturbo = $( "*[data-column='miniturbo']" );

    var $toggle_speed = $( "#table-toggle-speed" );
    var $toggle_speed_hidden = $( "#table-toggle-speed-hidden" );
    var $toggle_acceleration = $( "#table-toggle-acceleration" );
    var $toggle_weight = $( "#table-toggle-weight" );
    var $toggle_handling = $( "#table-toggle-handling" );
    var $toggle_handling_hidden = $( "#table-toggle-handling-hidden" );
    var $toggle_traction = $( "#table-toggle-traction" );
    var $toggle_miniturbo = $( "#table-toggle-miniturbo" );
    var $toggle_highlight_secret = $( "#table-toggle-highlight-secret" );
    var $toggle_highlight_acceleration = $( "#table-toggle-highlight-acceleration" );

    // Bootstrap view breakpoints
    var $screen_sm_min = 768;
    var $screen_md_min = 992;
    var $screen_lg_min = 1200;

    function toggleHighlightSecret() {
      $col_speed_water.toggleClass('secret-stat');
      $col_speed_air.toggleClass('secret-stat');
      $col_speed_antigravity.toggleClass('secret-stat');
      $col_handling_water.toggleClass('secret-stat');
      $col_handling_air.toggleClass('secret-stat');
      $col_handling_antigravity.toggleClass('secret-stat');
      $col_miniturbo.toggleClass('secret-stat');
    }

    function toggleHighlightAcceleration() {
      $('td[data-column="acceleration"]:contains(".25")').toggleClass('inefficient-1');
      $('td[data-column="acceleration"]:contains(".50")').toggleClass('inefficient-2');
      $('td[data-column="acceleration"]:contains(".75")').toggleClass('inefficient-3');
    }

    function initializeColumns() {
      // Dropdown selections
      $toggle_speed.addClass("selected");
      $toggle_speed_hidden.removeClass("selected");
      $toggle_acceleration.addClass("selected");
      $toggle_weight.addClass("selected");
      $toggle_handling.addClass("selected");
      $toggle_handling_hidden.removeClass("selected");
      $toggle_traction.addClass("selected");
      $toggle_highlight_secret.addClass("selected");
      $toggle_highlight_acceleration.addClass("selected");

      // Prioritize columns based on screen size
      $priority1.removeClass("hidden");
      $priority2.addClass("hidden");
      $priority3.addClass("hidden");

      var $width = $( window ).width();

      if ($width > $screen_sm_min) {
        $priority2.removeClass("hidden");
        $toggle_miniturbo.addClass("selected");
      }
      if ($width > $screen_lg_min) {
        $priority3.removeClass("hidden");
        $toggle_speed_hidden.addClass("selected");
        $toggle_handling_hidden.addClass("selected");
      }

      // Secret stat highlights
      $col_speed_water.addClass('secret-stat');
      $col_speed_air.addClass('secret-stat');
      $col_speed_antigravity.addClass('secret-stat');
      $col_handling_water.addClass('secret-stat');
      $col_handling_air.addClass('secret-stat');
      $col_handling_antigravity.addClass('secret-stat');
      $col_miniturbo.addClass('secret-stat');
    }

    // Initialize Columns onLoad & onResize
    initializeColumns();
    $( window ).resize(function() {
      initializeColumns();
    });

    // #table-toggle-speed
    $toggle_speed.click(function( event ) {
      $(this).toggleClass("selected");
      $col_speed_ground.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-speed-hidden
    $toggle_speed_hidden.click(function( event ) {
      $(this).toggleClass("selected");
      $col_speed_water.toggleClass("hidden");
      $col_speed_air.toggleClass("hidden");
      $col_speed_antigravity.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-acceleration
    $toggle_acceleration.click(function( event ) {
      $(this).toggleClass("selected");
      $col_acceleration.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-weight
    $toggle_weight.click(function( event ) {
      $(this).toggleClass("selected");
      $col_weight.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-handling
    $toggle_handling.click(function( event ) {
      $(this).toggleClass("selected");
      $col_handling_ground.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-handling-hidden
    $toggle_handling_hidden.click(function( event ) {
      $(this).toggleClass("selected");
      $col_handling_water.toggleClass("hidden");
      $col_handling_air.toggleClass("hidden");
      $col_handling_antigravity.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-traction
    $toggle_traction.click(function( event ) {
      $(this).toggleClass("selected");
      $col_traction.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-miniturbo
    $toggle_miniturbo.click(function( event ) {
      $(this).toggleClass("selected");
      $col_miniturbo.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-highlight
    $toggle_highlight_secret.click(function( event ) {
      $(this).toggleClass("selected");
      toggleHighlightSecret();
      event.stopPropagation();
    });
    $toggle_highlight_acceleration.click(function( event ) {
      $(this).toggleClass("selected");
      toggleHighlightAcceleration();
      event.stopPropagation();
    });
  };

  ////////////////////////////////////////
  // enable_toggleable_components_columns
  ////////////////////////////////////////

  enable_toggleable_components_columns = function() {

    // Preload jQuery objects
    var $priority1 = $( "*[data-priority='1']" );
    var $priority2 = $( "*[data-priority='2']" );
    var $priority3 = $( "*[data-priority='3']" );

    var $col_name = $( "*[data-column='name']" );
    var $col_speed_ground = $( "*[data-column='speed_ground']" );
    var $col_speed_water = $( "*[data-column='speed_water']" );
    var $col_speed_air = $( "*[data-column='speed_air']" );
    var $col_speed_antigravity = $( "*[data-column='speed_antigravity']" );
    var $col_acceleration = $( "*[data-column='acceleration']" );
    var $col_weight = $( "*[data-column='weight']" );
    var $col_handling_ground = $( "*[data-column='handling_ground']" );
    var $col_handling_water = $( "*[data-column='handling_water']" );
    var $col_handling_air = $( "*[data-column='handling_air']" );
    var $col_handling_antigravity = $( "*[data-column='handling_antigravity']" );
    var $col_traction = $( "*[data-column='traction']" );
    var $col_miniturbo = $( "*[data-column='miniturbo']" );

    var $toggle_name = $( "#table-toggle-name" );
    var $toggle_speed = $( "#table-toggle-speed" );
    var $toggle_speed_hidden = $( "#table-toggle-speed-hidden" );
    var $toggle_acceleration = $( "#table-toggle-acceleration" );
    var $toggle_weight = $( "#table-toggle-weight" );
    var $toggle_handling = $( "#table-toggle-handling" );
    var $toggle_handling_hidden = $( "#table-toggle-handling-hidden" );
    var $toggle_traction = $( "#table-toggle-traction" );
    var $toggle_miniturbo = $( "#table-toggle-miniturbo" );
    var $toggle_highlight_secret = $( "#table-toggle-highlight-secret" );
    var $toggle_highlight_acceleration = $( "#table-toggle-highlight-acceleration" );

    // Bootstrap view breakpoints
    var $screen_sm_min = 768;
    var $screen_md_min = 992;
    var $screen_lg_min = 1200;

    function toggleHighlightSecret() {
      $col_speed_water.toggleClass('secret-stat');
      $col_speed_air.toggleClass('secret-stat');
      $col_speed_antigravity.toggleClass('secret-stat');
      $col_handling_water.toggleClass('secret-stat');
      $col_handling_air.toggleClass('secret-stat');
      $col_handling_antigravity.toggleClass('secret-stat');
      $col_miniturbo.toggleClass('secret-stat');
    }

    function toggleHighlightAcceleration() {
      $('td[data-column="acceleration"]:contains(".25")').toggleClass('inefficient-1');
      $('td[data-column="acceleration"]:contains(".50")').toggleClass('inefficient-2');
      $('td[data-column="acceleration"]:contains(".75")').toggleClass('inefficient-3');
    }

    function initializeColumns() {
      // Dropdown selections
      $toggle_name.removeClass("selected");
      $toggle_speed.addClass("selected");
      $toggle_speed_hidden.removeClass("selected");
      $toggle_acceleration.addClass("selected");
      $toggle_weight.addClass("selected");
      $toggle_handling.addClass("selected");
      $toggle_handling_hidden.removeClass("selected");
      $toggle_traction.addClass("selected");
      $toggle_highlight_secret.addClass("selected");
      $toggle_highlight_acceleration.addClass("selected");

      // Prioritize columns based on screen size
      $priority1.removeClass("hidden");
      $priority2.addClass("hidden");
      $priority3.addClass("hidden");

      var $width = $( window ).width();

      if ($width > $screen_sm_min) {
        $priority2.removeClass("hidden");
        $toggle_name.addClass("selected");
        $toggle_miniturbo.addClass("selected");
      }
      if ($width > $screen_lg_min) {
        $priority3.removeClass("hidden");
        $toggle_speed_hidden.addClass("selected");
        $toggle_handling_hidden.addClass("selected");
      }

      // Secret stat highlights
      $col_speed_water.addClass('secret-stat');
      $col_speed_air.addClass('secret-stat');
      $col_speed_antigravity.addClass('secret-stat');
      $col_handling_water.addClass('secret-stat');
      $col_handling_air.addClass('secret-stat');
      $col_handling_antigravity.addClass('secret-stat');
      $col_miniturbo.addClass('secret-stat');
    }

    // Initialize Columns onLoad & onResize
    initializeColumns();
    // $( window ).resize(function() {
    //   initializeColumns();
    // });

    // #table-toggle-name
    $toggle_name.click(function( event ) {
      $(this).toggleClass("selected");
      $col_name.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-speed
    $toggle_speed.click(function( event ) {
      $(this).toggleClass("selected");
      $col_speed_ground.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-speed-hidden
    $toggle_speed_hidden.click(function( event ) {
      $(this).toggleClass("selected");
      $col_speed_water.toggleClass("hidden");
      $col_speed_air.toggleClass("hidden");
      $col_speed_antigravity.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-acceleration
    $toggle_acceleration.click(function( event ) {
      $(this).toggleClass("selected");
      $col_acceleration.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-weight
    $toggle_weight.click(function( event ) {
      $(this).toggleClass("selected");
      $col_weight.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-handling
    $toggle_handling.click(function( event ) {
      $(this).toggleClass("selected");
      $col_handling_ground.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-handling-hidden
    $toggle_handling_hidden.click(function( event ) {
      $(this).toggleClass("selected");
      $col_handling_water.toggleClass("hidden");
      $col_handling_air.toggleClass("hidden");
      $col_handling_antigravity.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-traction
    $toggle_traction.click(function( event ) {
      $(this).toggleClass("selected");
      $col_traction.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-miniturbo
    $toggle_miniturbo.click(function( event ) {
      $(this).toggleClass("selected");
      $col_miniturbo.toggleClass("hidden");
      event.stopPropagation();
    });
    // #table-toggle-highlight
    $toggle_highlight_secret.click(function( event ) {
      $(this).toggleClass("selected");
      toggleHighlightSecret();
      event.stopPropagation();
    });
    $toggle_highlight_acceleration.click(function( event ) {
      $(this).toggleClass("selected");
      toggleHighlightAcceleration();
      event.stopPropagation();
    });
  };
})(jQuery);
