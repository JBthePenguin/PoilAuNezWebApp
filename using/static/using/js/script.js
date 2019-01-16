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
  $("#header_actus .card p.card-text").text(text);
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
    interval: 2000
});


//GALERY
baguetteBox.run('.cards-gallery', { animation: 'slideIn'});


//FORM ADMIN ACTU

function AddActu() {
  $('#mod-actu1-form').hide();
  $('#mod-actu2-form').hide();
  $('#add-actu-form').show();
}

function ModifyActu1() {
  $('#add-actu-form').hide();
  $('#mod-actu2-form').hide();
  $('#mod-actu1-form').show();
}

function ModifyActu2() {
  $('#add-actu-form').hide();
  $('#mod-actu1-form').hide();
  $('#mod-actu2-form').show();
}

function AddPhoto() {
  $('#mod-photo-form').hide();
  $('#add-photo-form').show();
}

function ModifyPhoto() {
  $('#add-photo-form').hide();
  $('#mod-photo-form').show();
}

function AddVideo() {
  $('#mod-video-form').hide();
  $('#add-video-form').show();
}

function ModifyVideo() {
  $('#add-video-form').hide();
  $('#mod-video-form').show();
}

function DisplayMessage() {
  $("#display-message").show();
}
