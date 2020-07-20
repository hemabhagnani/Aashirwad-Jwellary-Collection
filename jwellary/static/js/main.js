(function ($) {
 "use strict";
/*----------------------------
	wow js active
------------------------------ */
 new WOW().init();
/*----------------------------
	New Trend List owl active
------------------------------ */
  $(".new-trend-list").owlCarousel({
      autoPlay: false,
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,
      items : 3,
	  /* transitionStyle : "fade", */    /* [This code for animation ] */
	  navigationText:["<i class='flaticon-arrows-3'></i>","<i class='flaticon-arrows-4'></i>"],
      itemsDesktop : [1199,3],
	  itemsDesktopSmall : [991,2],
	  itemsTablet: [767,1],
	  itemsMobile : [479,1],
  });
/*----------------------------
	Featured Product List owl active
------------------------------ */
  $(".featured-product-list").owlCarousel({
      autoPlay: false,
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,
      items : 4,
	  /* transitionStyle : "fade", */    /* [This code for animation ] */
	  navigationText:["<i class='flaticon-arrows-3'></i>","<i class='flaticon-arrows-4'></i>"],
      itemsDesktop : [1199,4],
	  itemsDesktopSmall : [991,3],
	  itemsTablet: [767,2],
	  itemsMobile : [479,1],
  });

/*----------------------------
	Blog List owl active
------------------------------ */
  $(".blog-list").owlCarousel({
      autoPlay: false,
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,
      items : 3,
	  /* transitionStyle : "fade", */    /* [This code for animation ] */
	  navigationText:["<i class='flaticon-arrows-3'></i>","<i class='flaticon-arrows-4'></i>"],
      itemsDesktop : [1199,3],
	  itemsDesktopSmall : [991,2],
	  itemsTablet: [767,2],
	  itemsMobile : [479,1],
  });
/*----------------------------
	Bran List owl active
------------------------------ */
  $(".brand-list").owlCarousel({
      autoPlay: false,
	  slideSpeed:2000,
	  pagination:false,
	  navigation:true,
      items : 5,
	  /* transitionStyle : "fade", */    /* [This code for animation ] */
	  navigationText:["<i class='flaticon-arrows-3'></i>","<i class='flaticon-arrows-4'></i>"],
      itemsDesktop : [1199,5],
	  itemsDesktopSmall : [991,4],
	  itemsTablet: [767,3],
	  itemsMobile : [479,2],
  });
/*----------------------------
	Our Team List owl active
------------------------------ */
  $(".our-team-list").owlCarousel({
      autoPlay: false,
	  slideSpeed:2000,
	  pagination:false,
	  navigation:false,
      items : 4,
      itemsDesktop : [1199,4],
	  itemsDesktopSmall : [991,3],
	  itemsTablet: [767,3],
	  itemsMobile : [479,2],
  });
/*----------------------------
	Testimonial List owl active
------------------------------ */
  $(".testimonial-list").owlCarousel({
      autoPlay: false,
	  slideSpeed:2000,
	  pagination:true,
	  navigation:false,
      items : 1
  });

/*---------------------
	countdown
--------------------- */
	$('[data-countdown]').each(function() {
	  var $this = $(this), finalDate = $(this).data('countdown');
	  $this.countdown(finalDate, function(event) {
		$this.html(event.strftime('<span class="cdown days"><span class="time-count">%-D</span> <p>Days</p></span> <span class="cdown hour"><span class="time-count">%-H</span> <p>Hour</p></span> <span class="cdown minutes"><span class="time-count">%M</span> <p>Min</p></span> <span class="cdown second"> <span><span class="time-count">%S</span> <p>Sec</p></span>'));
	  });
	});
/*--------------------------
	scrollUp
---------------------------- */
	$.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });
/*----------------------------
	price-slider active
------------------------------ */
	  $( "#slider-range" ).slider({
	   range: true,
	   min: 99,
	   max: 500,
	   values: [ 99, 999 ],
	   slide: function( event, ui ) {
		$( "#amount" ).val(ui.values[ 0 ] + " - "+ ui.values[ 1 ] );
	   }
	  });
	  $( "#amount" ).val($( "#slider-range" ).slider( "values", 0 ) +
	   " - " + $( "#slider-range" ).slider( "values", 1 ) );
/*----------------------------------
	Create an account toggle function
 ----------------------------------*/
	 $( '#ship-box' ).on('click', function() {
        $( '#ship-box-info' ).slideToggle(1000);
     });

/*---------------------
	venobox
--------------------- */
    $('.venobox').venobox();


/*----------------------------
	Input Plus Minus Button
------------------------------ */
    $(".cart-plus-minus").append('<div class="dec qtybutton">-</div><div class="inc qtybutton">+</div>');
    $(".qtybutton").on("click", function() {
        var $button = $(this);
        var oldValue = $button.parent().find("input").val();
        if ($button.text() == "+") {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don't allow decrementing below zero
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        $button.parent().find("input").val(newVal);
    });
/*---------------------
	Faq page Accrodian
--------------------- */
	 $('.collapse').on('shown.bs.collapse', function(){
		$(this).parent().find(".flaticon-square-1").removeClass("flaticon-square-1").addClass("flaticon-square");
		}).on('hidden.bs.collapse', function(){
		$(this).parent().find(".flaticon-square").removeClass("flaticon-square").addClass("flaticon-square-1");
		});
/*----------------------------
	jQuery MeanMenu
------------------------------ */
	jQuery('nav#dropdown').meanmenu();

})(jQuery);