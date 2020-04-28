jQuery(document).ready(function ($) {

  // make code pretty
  window.prettyPrint && prettyPrint();


  $('.accordion').on('show', function (e) {
    $(e.target).prev('.accordion-heading').find('.accordion-toggle').addClass('active');
    $(e.target).prev('.accordion-heading').find('.accordion-toggle i').removeClass('icon-caret-right');
    $(e.target).prev('.accordion-heading').find('.accordion-toggle i').addClass('icon-caret-down');
  });

  $('.accordion').on('hide', function (e) {
    $(this).find('.accordion-toggle').not($(e.target)).removeClass('active');
    $(this).find('.accordion-toggle i').not($(e.target)).removeClass('icon-aret-down');
    $(this).find('.accordion-toggle i').not($(e.target)).addClass('icon-caret-right');
  });


  (function () {

    var $menu = $('nav'),
      optionsList = '<option value="" selected>Go to..</option>';

    $menu.find('li').each(function () {
      var $this = $(this),
        $anchor = $this.children('a'),
        depth = $this.parents('ul').length - 1,
        indent = '';

      if (depth) {
        while (depth > 0) {
          indent += ' - ';
          depth--;
        }

      }
      $(".nav li").parent().addClass("bold");

      optionsList += '<option value="' + $anchor.attr('href') + '">' + indent + ' ' + $anchor.text() + '</option>';
    }).end()
      .after('<select class="selectmenu">' + optionsList + '</select>');

    $('select.selectmenu').on('change', function () {
      window.location = $(this).val();
    });

  })();

  //to top
  $().UItoTop({
    easingType: 'easeOutQuart'
  });

  //add some elements with animate effect
  $(".features").hover(
    function () {
      $(this).find('.icon').addClass("animated fadeInUp");
      $(this).find('a.btn').addClass("animated fadeInRight");
      $(this).find('.features_content').addClass("animated fadeInDown");
    },
    function () {
      $(this).find('.icon').removeClass("animated fadeInUp");
      $(this).find('a.btn').removeClass("animated fadeInRight");
      $(this).find('.features_content').removeClass("animated fadeInDown");
    }
  );

  $(".cta-box").hover(
    function () {
      $(this).find('.cta a').addClass("animated wiggle");
    },
    function () {
      $(this).find('.cta a').removeClass("animated wiggle");
    }
  );

  $("a[data-pretty^='prettyPhoto']").prettyPhoto({
    social_tools: false
  });
  //portfolio hover
  $('ul.da-thumbs > li').hoverdir();

  $(".da-animate a").mouseover(function () {
    $(".da-thumbs li article", this).stop().animate({
      "padding-top": "10p%"
    }, {
      queue: false,
      duration: 500
    }, "slow");
  });
  $(".da-animate a").mouseout(function () {
    $(".da-thumbs li article", this).stop().animate({
      "padding-top": "25p%"
    }, "slow");
  });

  $('ul.nav li.dropdown').hover(function () {
    $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeIn();
  }, function () {
    $(this).find('.dropdown-menu').stop(true, true).delay(200).fadeOut();
  });



  // flexslider
  $('.flexslider').flexslider({
    animation: "fade",
    controlNav: false
  });

  //testmonial slider
  $('.testmonial_slider').flexslider({
    animation: "fade",
    controlsContainer: " ",
    pauseOnHover: true,
    slideshowSpeed: 7000,
    animationSpeed: 600,
    easing: "swing",
    direction: "horizontal",
    controlNav: true,
    directionNav: false,
    smoothHeight: true,
    startAt: 0,
    slideshow: true
  });

  $('#images').refineSlide({
    transition: 'random',
    autoPlay: true,
    useThumbs: false

  });

  // custom js for cases_in_australia page.
  $('#update-cases').click(function () {
    $('#update-cases-modal').modal('toggle');
  });

  $('#council-search').change(
    function() {
      // Declare variables
      var input, filter, tr, th, td, i, txtValue;
      input = document.getElementById('council-search');
      filter = input.value.toUpperCase();
      th = document.getElementById("results");
      tr = th.getElementsByTagName('tr');

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
        td = tr[i].children[6];
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  );

  $('#postcode-search').keyup(
    function() {
      // Declare variables
      var input, filter, tr, th, td, i, txtValue;
      input = document.getElementById('postcode-search');
      filter = input.value.toUpperCase();
      th = document.getElementById("results");
      tr = th.getElementsByTagName('tr');

      // Loop through all list items, and hide those who don't match the search query
      for (i = 1; i < tr.length; i++) {
          td = tr[i].children[2];
          txtValue = td.textContent || td.innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
              tr[i].style.display = "";
          } else {
              tr[i].style.display = "none";
          }
      }
    }
  );
});
