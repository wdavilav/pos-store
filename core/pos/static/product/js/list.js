var product = {
    list: function () {
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
                data: {
                    'action': 'search'
                },
                dataSrc: ""
            },
            columns: [
                {data: 'id'},
                {data: 'name'},
                {data: 'code'},
                {data: 'category.name'},
                {data: 'is_service'},
                {data: 'price'},
                {data: 'pvp'},
                {data: 'stock'},
                {data: 'id'}
            ],
            // ordering: false,
            columnDefs: [
                {
                    targets: [-5],
                    class: 'text-center',
                    render: function (data, type, row) {
                        if (data) {
                            return '<span class="badge bg-primary rounded-pill">Si</span>';
                        }
                        return '<span class="badge bg-info rounded-pill">No</span>';
                    },
                },
                {
                    targets: [-4, -3],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '$' + data;
                    },
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    render: function (data, type, row) {
                        if (data < 5) {
                            return '<span class="badge bg-danger rounded-pill">' + data + '</span>';
                        }
                        return '<span class="badge bg-success rounded-pill">' + data + '</span>';
                    },
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
            rowCallback: function (row, data, index) {
                if (data.stock < 5) {
                    // $(row).addClass('low-stock');
                    $(row).addClass('low-stock');
                }
            }
        });
    }
};

$(function () {
    product.list();
});