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
            ]
        });
    }
};

$(function () {
    product.list();
});