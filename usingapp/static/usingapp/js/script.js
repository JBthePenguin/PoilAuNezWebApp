// NAVBAR

// Wave effect
(function ($) {
  var SCROLLING_NAVBAR_OFFSET_TOP = 50;
  $(window).on('scroll', function () {
    var $navbar = $('.navbar');
    if ($navbar.length) {
      if ($navbar.offset().top > SCROLLING_NAVBAR_OFFSET_TOP) {
        $('.scrolling-navbar').addClass('top-nav-collapse');
      } else {
        $('.scrolling-navbar').removeClass('top-nav-collapse');
      }
    }
  });
})(jQuery);


// ACTUS
function DisplayActu(img_url, title, text, author, title, creating_date, change_date) {
  $(".subheading").remove();
  $("#header_actus .card img.card-img-top").replaceWith("<img class='card-img-top' src=" + img_url + ">");
  $("#header_actus .card h4.card-title").text(title);
  $("#header_actus .card div.card-text").html(text);
  if (creating_date == change_date) {
    var word = "publiée";
  }
  else {
    var word = "modifiée";
  }
  $("#header_actus .card p.card-footer").html("<small>actualité " + word + " par " + author + " le " + change_date + "</small>");
}


//CAROUSEL
$('.bs-vertical-slider').carousel({
    interval: 3000
});

$('.carousel-item .embed-responsive .video-js').on('play', function (e) {
  $('#carousel-video').carousel('pause');
});

$('.carousel-item .embed-responsive .video-js').on('stop pause ended', function (e) {
    $("#carousel-video").carousel();
});


//GALERY
baguetteBox.run('.cards-gallery', { animation: 'slideIn'});


//CAPTCHA

$('#refresh-captcha').click(function () {
    $.getJSON("/captcha/refresh/", function (result) {
        $('.captcha').attr('src', result['image_url']);
        $('#id_captcha_0').val(result['key'])
    });
});