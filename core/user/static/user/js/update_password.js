$(function () {
    $('.btnShowPassword').on('click', function () {
        var i = $(this).find('i');
        var input = $(this).closest('.input-group').find('input');
        if (i.hasClass('fa fa-eye-slash')) {
            i.removeClass();
            i.addClass('fa fa-eye');
            input.attr('type', 'password');
        } else {
            i.removeClass();
            i.addClass('fa fa-eye-slash');
            input.attr('type', 'text');
        }
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        var form = $(this)[0];
        submit_with_formdata('Notificación', '¿Estas seguro de realizar la siguiente acción?', pathname, new FormData(form), function () {
            location.href = $(form).attr('data-url');
        });
    });
});