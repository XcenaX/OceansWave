$(function() {
    $('#item1').hover(function() {
      
      $('#item1').css('background', '#253D92');
      $('#item1')[0].children[1].style.background = 'rgba(37, 61, 146, 0.5)';
    }, function() {
      $('#item1').css('background', '#FFB74B');
      $('#item1')[0].children[1].style.background = '#FFDDA9';
    });
});

$(function() {
  $('#item2').hover(function() {
    
    $('#item2').css('background', '#253D92');
    $('#item2')[0].children[1].style.background = 'rgba(37, 61, 146, 0.5)';
  }, function() {
    $('#item2').css('background', '#FFB74B');
    $('#item2')[0].children[1].style.background = '#FFDDA9';
  });
});

$(function() {
  $('#item3').hover(function() {
    
    $('#item3').css('background', '#253D92');
    $('#item3')[0].children[1].style.background = 'rgba(37, 61, 146, 0.5)';
  }, function() {
    $('#item3').css('background', '#FFB74B');
    $('#item3')[0].children[1].style.background = '#FFDDA9';
  });
});

$(function() {
  $('#item4').hover(function() {
    
    $('#item4').css('background', '#253D92');
    $('#item4')[0].children[1].style.background = 'rgba(37, 61, 146, 0.5)';
  }, function() {
    $('#item4').css('background', '#FFB74B');
    $('#item4')[0].children[1].style.background = '#FFDDA9';
  });
});

$(function() {
  var arrow = $("#hover-arrow")[0];
  setInterval(function(){
    if(arrow.style.marginTop == "60px"){
      arrow.style.marginTop = "40px";
    }else{
      arrow.style.marginTop = "60px";
    }
    
  }, 1000)
});

$(document).ready(function(){
  $('.scrollto a').on('click', function() {

    let href = $(this).attr('href');
    if(href[0] == "/"){
      href = href.substring(1);
    }
    console.log(href);
    $('html, body').animate({
        scrollTop: $(href).offset().top
    }, {
        duration: 370,   // по умолчанию «400» 
        easing: "linear" // по умолчанию «swing» 
    });
  
    return false;
  });
  $('#hover-arrow').on('click', function() {
    let href = $("#event").attr('id');

    $('html, body').animate({
        scrollTop: $("#"+href).offset().top
    }, {
        duration: 370,   // по умолчанию «400» 
        easing: "linear" // по умолчанию «swing» 
    });
    $("#hover-arrow")[0].remove();
    return false;
  });
});
