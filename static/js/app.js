$(document).ready(function() {
    let header = $('#header');
    let scrollPos = $(window).scrollTop();
    let intro = $('#intro');
    let introH = intro.innerHeight();

    $(window).on('scroll load', function() {
        scrollPos = $(this).scrollTop();
        if (scrollPos > introH) {
            header.addClass('fixed');
        } else {
            header.removeClass('fixed');
        }
    });

    $('#icon').on('click', function(event) {
        event.preventDefault();
        $('#navv_inner').toggleClass('active');
    });

    // Убираем блокировку перехода по ссылкам
    $('.navv__link').on('click', function() {
        // Можно добавить любую дополнительную логику здесь
        // Например, можно закрыть меню после перехода по ссылке
        $('#navv_inner').removeClass('active');
    });
});
