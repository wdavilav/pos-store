var product = {
    list: function () {
        $('#data').DataTable({
            autoWidth: false,
            destroy: true,
            //data: [['1', 'LAVA WIMPLUS 900 GR TORONJA X12U', 'H993F200', 'DESINFECTANTE', 'No', '1.49', '1.79', '49', '1'], ['2', 'LAVA WIMPLUS 900 GR TUTIFRUTI X12U', '91301662', 'DESINFECTANTE', 'No', '1.49', '1.79', '54', '2'], ['3', 'TIPS AMB. BANO MANZANA X144U', '11011050040', 'DESINFECTANTE', 'No', '0.69', '0.82', '41', '3'], ['4', 'ESPONJA COLORES X3U ESTRELLA X40P', 'PT0401001', 'DESINFECTANTE', 'No', '0.41', '0.71', '60', '4'], ['5', 'MR. MUSCULO TANQUE X2U', '12669', 'DESINFECTANTE', 'No', '1.41', '2.71', '37', '5'], ['6', 'DESINF. WISE FLORAL GALON', '06DWFG', 'DESINFECTANTE', 'No', '1.41', '3.43', '55', '6'], ['7', 'SUAVIZANTE WISE PRIMAVERAL 430ML', 'SUAROPW430', 'DESINFECTANTE', 'No', '0.35', '0.55', '66', '7'], ['8', 'SCOTT CUID.COMPLETO GD P11/LL12 X5P', 'KC-9763', 'DESINFECTANTE', 'No', '4.45', '6.46', '19', '8'], ['9', 'DET. WISE 3 KL LIMON X6U', '06DW3L', 'DESINFECTANTE', 'No', '3.41', '4.52', '59', '9'], ['10', 'PROTEX FRESH', '02062', 'DESINFECTANTE', 'No', '1.39', '2.40', '51', '10'], ['11', 'FORMATEO DE COMPUTADORAS', 'FORMATEO85451', 'SERVICIOS', 'Si', '0.00', '15.00', '0', '11']]
            data: [{"id": 1, "name": "LAVA WIMPLUS 900 GR TORONJA X12U", "code": "H993F200", "category": {"id": 1, "name": "DESINFECTANTE"}, "is_service": false, "price": 1.49, "pvp": 1.79, "stock": 49}, {"id": 2, "name": "LAVA WIMPLUS 900 GR TUTIFRUTI X12U", "code": "91301662", "category": {"id": 1, "name": "DESINFECTANTE"}, "is_service": false, "price": 1.49, "pvp": 1.79, "stock": 54}, {"id": 3, "name": "TIPS AMB. BANO MANZANA X144U", "code": "11011050040", "category": {"id": 1, "name": "DESINFECTANTE"}, "is_service": false, "price": 0.69, "pvp": 0.82, "stock": 41}, {"id": 4, "name": "ESPONJA COLORES X3U ESTRELLA X40P", "code": "PT0401001", "category": {"id": 1, "name": "DESINFECTANTE"}, "is_service": false, "price": 0.41, "pvp": 0.71, "stock": 60}, {"id": 5, "name": "MR. MUSCULO TANQUE X2U", "code": "12669", "category": {"id": 1, "name": "DESINFECTANTE"}, "is_service": false, "price": 1.41, "pvp": 2.71, "stock": 37}, {"id": 6, "name": "DESINF. WISE FLORAL GALON", "code": "06DWFG", "category": {"id": 1, "name": "DESINFECTANTE"}, "is_service": false, "price": 1.41, "pvp": 3.43, "stock": 55}, {"id": 7, "name": "SUAVIZANTE WISE PRIMAVERAL 430ML", "code": "SUAROPW430", "category": {"id": 1, "name": "DESINFECTANTE"}, "is_service": false, "price": 0.35, "pvp": 0.55, "stock": 66}, {"id": 8, "name": "SCOTT CUID.COMPLETO GD P11/LL12 X5P", "code": "KC-9763", "category": {"id": 1, "name": "DESINFECTANTE"}, "is_service": false, "price": 4.45, "pvp": 6.46, "stock": 19}, {"id": 9, "name": "DET. WISE 3 KL LIMON X6U", "code": "06DW3L", "category": {"id": 1, "name": "DESINFECTANTE"}, "is_service": false, "price": 3.41, "pvp": 4.52, "stock": 59}, {"id": 10, "name": "PROTEX FRESH", "code": "02062", "category": {"id": 1, "name": "DESINFECTANTE"}, "is_service": false, "price": 1.39, "pvp": 2.4, "stock": 51}, {"id": 11, "name": "FORMATEO DE COMPUTADORAS", "code": "FORMATEO85451", "category": {"id": 2, "name": "SERVICIOS"}, "is_service": true, "price": 0.0, "pvp": 15.0, "stock": 0}],
            columns: [
                { data: 'id' },
                { data: 'name' },
                { data: 'code' },
                { data: 'category.id' },
                { data: 'is_service' },
                { data: 'price' },
                { data: 'pvp' },
                { data: 'stock' },
                { data: 'id' }
            ]
        });
    }
};

$(function () {
    product.list();
});