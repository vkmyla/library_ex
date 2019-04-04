//bk_table config
$(document).ready(function() {
    var dt_table = $('#bk_table').dataTable({
        order: [[ 0, "desc" ]],
        columnDefs: [
            {
                name: 'title',
                orderable: true,
                searchable: true,
                targets: [0]
            },
            {
                name: 'author',
                orderable: true,
                searchable: true,
                targets: [1]
            },
            {
                name: 'misc',
                orderable: false,
                searchable: false,
                targets: [2, 3]
            }

        ],
        searching: true,
        processing: true
        // serverSide: true,
        // stateSave: true,
        // ajax: TESTMODEL_LIST_JSON_URL
    });
});
