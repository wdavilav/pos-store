var input_date_range;
var user_access = {
    list: function (all) {
        var parameters = {
            'action': 'search',
            'start_date': input_date_range.data('daterangepicker').startDate.format('YYYY-MM-DD'),
            'end_date': input_date_range.data('daterangepicker').endDate.format('YYYY-MM-DD'),
        };
        if (all) {
            parameters['start_date'] = '';
            parameters['end_date'] = '';
        }
        $('#data').DataTable({
            autoWidth: false,
            destroy: true,
            deferRender: true,
            ajax: {
                url: pathname,
                type: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: parameters,
                dataSrc: ""
            },
            columns: [
                {data: "id"},
                {data: "user.username"},
                {data: "date_joined"},
                {data: "hour"},
                {data: "remote_addr"},
                {data: "http_user_agent"},
                {data: "login_attempt"},
                {data: "id"},
            ],
            columnDefs: [
                {
                    targets: [-3, -4, -5, -6, -7],
                    class: 'text-center',
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        var name = row.login_attempt.name;
                        if (row.login_attempt.id === 'success') {
                            return '<span class="badge bg-primary rounded-pill">' + name + '</span>';
                        }
                        return '<span class="badge bg-danger rounded-pill">' + name + '</span>';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '<a href="' + pathname + 'delete/' + row.id + '/" data-bs-toggle="tooltip" title="Eliminar" class="btn btn-danger btn-sm"><i class="fas fa-trash"></i></a>';
                    }
                },
            ],
            rowCallback: function (row, data, index) {

            },
            initComplete: function (settings, json) {
                enable_tooltip();
            }
        });
    }
};

$(function () {

    input_date_range = $('input[name="date_range"]');

    input_date_range
        .daterangepicker({
                language: 'auto',
                startDate: new Date(),
                locale: {
                    format: 'YYYY-MM-DD',
                },
                autoApply: true,
            }
        )
        .on('change.daterangepicker apply.daterangepicker', function (ev, picker) {
            user_access.list(false);
        });

    $('.drp-buttons').hide();

    $('.btnSearchAll').on('click', function () {
        user_access.list(true);
    });

    user_access.list(false);
});