<dtable>
  <table id="tbl" class="display" cellspacing="0" width="90%">
    <thead>
      <tr>
        <th each={tbl_columns}> {columnName} </th>
      </tr>
    </thead>
  </table>
    <script>
    var self = this
    tbl_columns =[
                {columnName:"name"},
                {columnName:"position"},
                {columnName:"office"},
                {columnName:"age"},
                {columnName:"startdate"}
            ]

    self.on('mount', function() {
    $('#tbl').DataTable( {
        ajax: {
            url: '/api/staff/',
            dataSrc: ''
              },
        columns: [
            { "data": "name" },
            { "data": "position" },
            { "data": "office" },
            { "data": "age" },
            { "data": "startdate" }]
    })
})
   
</script>
</dtable>
