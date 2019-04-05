//bk_table config
$(document).ready(function() {
    var dt_table = $('#bk_table').dataTable({
        order: [[ 1, "desc" ]],
        columns: [
                 {data: null, defaultContent: '', title: '', searchable: false,
                   orderable: false}
                 ],
        columnDefs: [
            {
                ordarable: false,
                targets: 0,
                className: 'select-checkbox',
                checkboxes: {selectRow: true}
            },
            {
                name: 'title',
                orderable: true,
                searchable: true,
                targets: [1]
            },
            {
                name: 'author',
                orderable: true,
                searchable: true,
                targets: [2]
            },
            {
                name: 'misc',
                orderable: false,
                searchable: false,
                targets: [3, 4]
            }
        ],
        select: {
          style: 'multi'
        },
        order: [[1, 'asc']],
        searching: true,
        processing: true
        // serverSide: true,
        // stateSave: true,
        // ajax: TESTMODEL_LIST_JSON_URL
    });
});
