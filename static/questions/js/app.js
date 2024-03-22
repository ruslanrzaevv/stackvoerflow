$(function(){
    let header = $('#header');
    let scrollPos = $(window).scrollTop();
    let intro = $('#intro'); // Добавлено определение переменной intro
    let introH = intro.innerHeight(); // Исправлено определение высоты элемента

    $(window).on('scroll load', function (){
        scrollPos = $(this).scrollTop();
        if (scrollPos > introH) {
            header.addClass('fixed');
        } else {
            header.removeClass('fixed');
        }
    });
});
