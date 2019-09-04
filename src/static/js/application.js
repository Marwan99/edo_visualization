$(document).ready(function() {
  //connect to the socket server.
  var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
  var numbers_received = [];
  // console.log("lol");
  //receive details from server
  socket.on('newnumber', function(msg)
  {
    // console.log("Received number" + msg.number);
    $('#log_x').html(msg.x.toString());
    $('#log_y').html(msg.y.toString());
    $('#log_z').html(msg.z.toString());

    Plotly.extendTraces('plot',{x:[[msg.x]], y:[[msg.y]], z:[[msg.z]]}, [0]);
  });

});
