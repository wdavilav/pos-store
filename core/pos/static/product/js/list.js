var product = {
    list: function () {
        $('#data').DataTable({
            autoWidth: false,
            destroy: true,
            data: [['1', 'LAVA WIMPLUS 900 GR TORONJA X12U', 'H993F200', 'DESINFECTANTE', 'No', '1.49', '1.79', '49', '1'], ['2', 'LAVA WIMPLUS 900 GR TUTIFRUTI X12U', '91301662', 'DESINFECTANTE', 'No', '1.49', '1.79', '54', '2'], ['3', 'TIPS AMB. BANO MANZANA X144U', '11011050040', 'DESINFECTANTE', 'No', '0.69', '0.82', '41', '3'], ['4', 'ESPONJA COLORES X3U ESTRELLA X40P', 'PT0401001', 'DESINFECTANTE', 'No', '0.41', '0.71', '60', '4'], ['5', 'MR. MUSCULO TANQUE X2U', '12669', 'DESINFECTANTE', 'No', '1.41', '2.71', '37', '5'], ['6', 'DESINF. WISE FLORAL GALON', '06DWFG', 'DESINFECTANTE', 'No', '1.41', '3.43', '55', '6'], ['7', 'SUAVIZANTE WISE PRIMAVERAL 430ML', 'SUAROPW430', 'DESINFECTANTE', 'No', '0.35', '0.55', '66', '7'], ['8', 'SCOTT CUID.COMPLETO GD P11/LL12 X5P', 'KC-9763', 'DESINFECTANTE', 'No', '4.45', '6.46', '19', '8'], ['9', 'DET. WISE 3 KL LIMON X6U', '06DW3L', 'DESINFECTANTE', 'No', '3.41', '4.52', '59', '9'], ['10', 'PROTEX FRESH', '02062', 'DESINFECTANTE', 'No', '1.39', '2.40', '51', '10'], ['11', 'FORMATEO DE COMPUTADORAS', 'FORMATEO85451', 'SERVICIOS', 'Si', '0.00', '15.00', '0', '11']]
        });
    }
};

$(function () {
    product.list();
});