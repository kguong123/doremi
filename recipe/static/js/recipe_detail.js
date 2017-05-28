function checkMobileDevice() {
      var mobileKeyWords = new Array('Android', 'iPhone', 'iPod', 'BlackBerry', 'Windows CE', 'SAMSUNG', 'LG', 'MOT', 'SonyEricsson');
      for (var info in mobileKeyWords) {
          if (navigator.userAgent.match(mobileKeyWords[info]) != null) {
              return true;

          }
      }
      return false;
  }

  $(function () {
    
    var msie6 = $.browser == 'msie' && $.browser.version < 7;
    var device = checkMobileDevice();
      
      if (device){
        $('#comment').removeClass('fixed');
      }
      else{
        if (!msie6) {
          var top = $('#comment').offset().top - parseFloat($('#comment').css('margin-top').replace(/auto/, 0));
          $(window).scroll(function (event) {
            // what the y position of the scroll is
            var y = $(this).scrollTop();
            
            // whether that's below the form
            if (y >= top) {
              // if so, ad the fixed class
              $('#comment').addClass('fixed');
            } else {
              // otherwise remove it
              $('#comment').removeClass('fixed');
            }
          });
        }  
      }  
  });