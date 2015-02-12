
var idCounter =0;
addToList = function(snapshot) {
  var cake = snapshot.val();
    console.log(snapshot.key());
    var name="commentarea"+idCounter;
  var listitem =
  '<tr><td>'+cake.date + " </td><td> " + cake.beforeDate + " </td><td> " +cake.name+' </td><td> ' +cake.taak+'</td><td><textarea class="'+name+'"></textarea></td></tr>';
  document.getElementById('cakes').innerHTML += listitem;
    $(name).keydown(function(event) {
        console.log("pressed something");
        if (event.keyCode == 13) {
            console.log("pressed enter at " + snapshot.key());
            snapshot.ref().child('first').set('Fred');
            snapshot.ref().child('last').set('Flintstone');
            snapshot.ref().set({ first: 'Fred', last: 'Flintstone' });
         }
    });
    idCounter+=1;
};

window.onload = function() {
  var ref = new Firebase('https://roosterstanna.firebaseio.com');
  ref.child('taken').on('child_added', addToList);
};