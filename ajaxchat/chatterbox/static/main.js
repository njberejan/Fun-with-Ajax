var $statements = $('#statements');

$.get('/api/chatterbox/', function(statements){
  statements.results.forEach(function(statement){
    console.log(statement)
    var $li = $('<li>');
    $li.text(statement.text)
    $li.appendTo($statements);
  })
});

// document.write($statements)
