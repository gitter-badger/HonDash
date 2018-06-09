try {
   var autobahn = require('autobahn');
} catch (e) {
   // when running in browser, AutobahnJS will
   // be included without a module system
}

var connection = new autobahn.Connection({
   url: 'ws://127.0.0.1:8080/ws',
   realm: 'realm1'}
);

connection.onopen = function (session) {

    function onevent1(args) {
        for (var key in args[0]) { // for all values
            if (args[0][key]['tag'] != null) { // if it's associated to a frontend tag
                window[args[0][key]["tag"]]["refresh"](args[0][key]["value"]);
            }
        }
   }

   session.subscribe('com.app.idea', onevent1);
};



connection.open();
