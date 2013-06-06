$(function() {
    // enable tooltips
    $('[rel=tooltip]').tooltip();

    // toggle info
    $('.btn-more').on('click', function() {
        var $more = $(this).parent().siblings('.chapter-more');
        if ($more.is(':visible')) {
            $more.fadeOut('fast');
            $(this).html('<i class="icon-angle-down"></i>');
        }
        else {
            $more.fadeIn('fast');
            $(this).html('<i class="icon-angle-up"></i>');
        }

        return false;
    });

    // on row click, toggle info
    $('li').on('click', function() {
        $(this).find('.btn-more').click();
    });
});
