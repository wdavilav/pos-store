function alert_sweetalert(type, title, message, callback, timer) {
    if ($.isEmptyObject(message)) {
        html = '';
    }
    Swal.fire({
        icon: type,
        title: title,
        text: message,
        grow: true,
        showCloseButton: true,
        allowOutsideClick: true,
        timer: timer
    }).then((result) => {
        callback();
    });
}

function message_error(message) {
    var content = message;
    if (typeof (message) === "object") {
        content = JSON.stringify(message);
    }
    alert_sweetalert('error', 'Error', content, function () {
    }, 2000);
}

function submit_with_formdata(title, content, pathname, params, success) {
    $.confirm({
        // type: 'blue',
        theme: 'modern',
        title: title,
        icon: 'fas fa-info-circle',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: pathname,
                        data: params,
                        type: 'POST',
                        dataType: 'json',
                        headers: {
                            'X-CSRFToken': csrftoken
                        },
                        processData: false,
                        contentType: false,
                        beforeSend: function () {

                        },
                        success: function (request) {
                            if (!request.hasOwnProperty('error')) {
                                success(request);
                                return false;
                            }
                            message_error(request.error);
                        },
                        error: function (jqXHR, textStatus, errorThrown) {
                            message_error(errorThrown + ' ' + textStatus);
                        },
                        complete: function () {

                        }
                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    });
}

function enable_tooltip() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl, {
            boundary: '.table'
        });
    });
}

function dialog_action(title, content, success, cancel) {
    $.confirm({
        theme: 'modern',
        title: title,
        icon: 'fas fa-info-circle',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: "btn-primary",
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    success();
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {
                    cancel();
                }
            },
        }
    });
}

function validate_text_box(event, type) {
    var key = event.keyCode || event.which;
    var numbers = (key > 47 && key < 58) || key === 8;
    var numbers_spaceless = key > 47 && key < 58;
    var letters = !((key !== 32) && (key < 65) || (key > 90) && (key < 97) || (key > 122 && key !== 241 && key !== 209 && key !== 225 && key !== 233 && key !== 237 && key !== 243 && key !== 250 && key !== 193 && key !== 201 && key !== 205 && key !== 211 && key !== 218)) || key === 8;
    var letters_spaceless = !((key < 65) || (key > 90) && (key < 97) || (key > 122 && key !== 241 && key !== 209 && key !== 225 && key !== 233 && key !== 237 && key !== 243 && key !== 250 && key !== 193 && key !== 201 && key !== 205 && key !== 211 && key !== 218)) || key === 8;
    var decimals = ((key > 47 && key < 58) || key === 8 || key === 46);

    switch (type) {
        case "numbers":
            return numbers;
        case "numbers_spaceless":
            return numbers_spaceless;
        case "letters":
            return letters;
        case "numbers_letters":
            return numbers || letters;
        case "letters_spaceless":
            return letters_spaceless;
        case "decimals":
            return decimals;
    }
    return true;
}