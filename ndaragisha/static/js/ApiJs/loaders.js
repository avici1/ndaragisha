/*function loadMainData() {
    $('#admissions_tbl').DataTable({
        "processing": true,
        "ajax": {
            "url": "http://127.0.0.1:8000/admissions/all/",
            dataSrc: ''
        },
        "columns": [
            {"data": "first_name"},
            {"data": "last_name"},
            {"data": "cell"},
            {"data": "sector"},
            {"data": "district"},
            {"data": "province"},


        ]
    });
    $('#admissions_tbl').tableExport();
}*/
function get_lost_items() {
    $.getJSON("http://127.0.0.1:8000/api/load/lost", function (data) {
        let option = '';
        $.each(data, function (key, value) {
            option += '<option value= "'+value.doc_id+'">'+value.doc_id+'</option>';
        });
        $("#options").append(option)
    })
}

window.onload = function () {
    get_lost_items();
};
