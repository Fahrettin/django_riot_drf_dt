<dtable>
  <table id="tbl" onclick={ dosome } class="display" cellspacing="0" width="90%">
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

     dosome(e) {
       //console.log(e)
       console.log(this)
       if (e.target.tagName =='TD'){
          var datt = e.srcElement.parentElement.firstChild.innerText
          //console.log(datt)
          alert( 'You clicked on '+ datt +'\'s row' )
          
       }
      }
   
</script>
</dtable>
