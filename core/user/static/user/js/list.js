var user = {
    list: function () {
        $('#data').DataTable({
            autoWidth: false,
            destroy: true,
            ajax: {
                url: pathname,
                type: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken
                },
                data: {
                    'action': 'search'
                },
                dataSrc: ""
            },
            columns: [
                {"data": "id"},
                {"data": "names"},
                {"data": "username"},
                {"data": "is_active"},
                {"data": "image"},
                {"data": "groups"},
                {"data": "id"},
            ],
            columnDefs: [
                {
                    targets: [-5],
                    class: 'text-center',
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<img alt="" class="img-fluid mx-auto d-block" src="' + data + '" width="20px" height="20px">';
                    }
                },
                {
                    targets: [-4],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        if (data) {
                            return '<span class="badge rounded-pill bg-success">Activo</span>';
                        }
                        return '<span class="badge rounded-pill bg-danger">Inactivo</span>';
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        var content = '';
                        row.groups.forEach(function (value, index, array) {
                            content += '<span class="badge rounded-pill bg-secondary">' + value.name + '</span> ';
                        });
                        return content;
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        var buttons = '<a href="' + pathname + 'update/' + row.id + '/" data-bs-toggle="tooltip" title="Editar" class="btn btn-warning btn-sm"><i class="fas fa-edit"></i></a> ';
                        buttons += '<a href="' + pathname + 'delete/' + row.id + '/" data-bs-toggle="tooltip" title="Eliminar" class="btn btn-danger btn-sm"><i class="fas fa-trash"></i></a>';
                        return buttons;
                    }
                },
            ],
            initComplete: function (settings, json) {
                enable_tooltip();
            }
        });
    }
};

$(function () {
    user.list();
});

