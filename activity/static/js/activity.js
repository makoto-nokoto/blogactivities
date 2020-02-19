//var showloading = document.getElementById('showloading');
//$(header).style.display='none';
//$(main).style.display='none';
//$("#showloading").style.display='inline'
// 画面本体のdivを取得
//var contents = document.getElementById('contents');
$(function() {
     // ブラウザウィンドウの高さを取得する
    $('header,main,footer').css('display','none'); // コンテンツを非表示にする
//    $("#showloading").fadeIn(500);
    $('.spinner-grow .text-primary').css('display','block');//ローディング画像を表示
});
$(window).on('load', function () {
  //$(".sr-only").remove();
  $("#showloading").delay(500).fadeOut(500);
  $("header").delay(1000).fadeIn(1000);
  $("main").delay(1000).fadeIn(1000);
  $("footer").delay(1000).fadeIn(1000);
//  $('#showloading').style.display = 'none';
// contentsのdivを表示
//contents.classList.remove('hidden');
//});

  var num = 0;
  var imgElem = document.images['moving'];
  console.log(imgElem);

  var countup = function() {
    console.log(num++);
    imgElem.style.width = num + "%";
  }

  var time = setInterval(function() {
    console.log(imgElem.width);
    countup();
    if (num > 15) {
      clearInterval(time);
    }
  }, 1000);
});
