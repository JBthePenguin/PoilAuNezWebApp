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
function DisplayActu1() {
  $(".subheading").remove();
  $("#header_actus .card img.card-img-top").replaceWith("<img class='card-img-top' src='img/actu1.png'>");
  $("#header_actus .card h4.card-title").replaceWith("<h4 class='card-title text-center'><span>Ze magical hysteric tour 2018</span></h4>");
  $("#header_actus .card p.card-text").replaceWith("<p class='card-text text-left'>Bienvenue au Zekistan où la compagnie Poil au nez propose un spectacle tout public le vendredi 28 décembre 2018 à 16h, dans la salle Paradiso à Sarrancolin. Entrée 4€ pour les adultes et 2€ pour les enfants.</p>");
  $("#header_actus .card p.card-footer").replaceWith("<p class='card-footer text-right'><small>actualité publiée par Zek le 10/12/18</small></p>");
}

function DisplayActu2() {
  $(".subheading").remove();
  $("#header_actus .card img.card-img-top").replaceWith("<img class='card-img-top' src='img/alapoursuite.png'>");
  $("#header_actus .card h4.card-title").replaceWith("<h4 class='card-title text-center'><span>A la poursuite d'une histoire</span></h4>");
  $("#header_actus .card p.card-text").replaceWith("<p class='card-text text-left'>La compagnie Poil au nez sera en représentation du 3 au 7 octobre 2018 au Palais des sports de Los Angeles à 20h. Entrée 3$</p>");
  $("#header_actus .card p.card-footer").replaceWith("<p class='card-footer text-right'><small>actualité publiée par Zek le 02/09/18</small></p>");
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
