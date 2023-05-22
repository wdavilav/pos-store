var tblSale;
var input_date_range;

var sale = {
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
        tblSale = $('#data').DataTable({
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
            order: [[0, 'desc']],
            columns: [
                {data: "id"},
                {data: "client.names"},
                {data: "date_joined"},
                {data: "subtotal"},
                {data: "total_iva"},
                {data: "total_dscto"},
                {data: "total"},
                {data: "cash"},
                {data: "change"},
                {data: "id"},
            ],
            columnDefs: [
                {
                    targets: [-2, -3, -4, -5, -6, -7],
                    class: 'text-center',
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-8],
                    class: 'text-center',
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    render: function (data, type, row) {
                        var buttons = '<a rel="detail" data-bs-toggle="tooltip" title="Detalle" class="btn btn-success btn-sm"><i class="fas fa-boxes"></i></a> ';
                        buttons += '<a href="' + pathname + 'delete/' + row.id + '/" data-bs-toggle="tooltip" title="Eliminar" class="btn btn-danger btn-sm"><i class="fas fa-trash"></i></a> ';
                        buttons += '<a href="' + pathname + 'print/invoice/' + row.id + '/" target="_blank" data-bs-toggle="tooltip" title="Imprimir" class="btn btn-secondary btn-sm"><i class="fas fa-print"></i></a>';
                        return buttons;
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

    $('#data tbody')
        .off()
        .on('click', 'a[rel="detail"]', function () {
            $('.tooltip').remove();
            var tr = tblSale.cell($(this).closest('td, li')).index();
            var row = tblSale.row(tr.row).data();
            $('#tblProducts').DataTable({
                autoWidth: false,
                destroy: true,
                ajax: {
                    url: pathname,
                    type: 'POST',
                    headers: {
                        'X-CSRFToken': csrftoken
                    },
                    data: {
                        'action': 'search_detail_products',
                        'id': row.id
                    },
                    dataSrc: ""
                },
                columns: [
                    {data: "product.short_name"},
                    {data: "price_with_vat"},
                    {data: "cant"},
                    {data: "subtotal"},
                    {data: "total_dscto"},
                    {data: "total"},
                ],
                columnDefs: [
                    {
                        targets: [-1, -2, -3, -5],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return '$' + data.toFixed(2);
                        }
                    },
                    {
                        targets: [-4],
                        class: 'text-center',
                        render: function (data, type, row) {
                            return data;
                        }
                    }
                ],
                initComplete: function (settings, json) {

                }
            });
            $('#myModalDetail').modal('show');
        })

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
            sale.list(false);
        });

    $('.drp-buttons').hide();

    sale.list(false);

    $('.btnSearchAll').on('click', function () {
        sale.list(true);
    });
});