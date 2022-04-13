$(window).on('load', function(){
    setTimeout(function(){
        $('#wipe').hide();
        $('#main_content,header,footer').show();
    }, 3000);
    $('#wipe').removeClass("d-none");
    $('#main_content,header,footer').hide();
    $('body').css({
        'width': '100%',
        'height': '100%',
        'cursor': "url('https://github.com/devarshatgithub/Python-Programming/blob/main/src/feather.cur'), auto"
    });
    $('embed').css({
        'height': 'fit-content'
    });
    $('kbd').css({
        'color': 'green',
        'background-color': '#e1e1e1'
    });
    $('.pop').css({
        'border': 'none',
        'background-color': 'transparent',
        'padding-top': '0',
        'padding-bottom': '0',
        'color': 'rgb(34, 91, 165)',
        'text-decoration': 'underline'
    });
    $('.placeholder').css({
        'font-size': 'small'
    });
    $('.modal-content').css({
        'width': 'fit-content',
        'height': 'fit-content'
    });
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    })
});
