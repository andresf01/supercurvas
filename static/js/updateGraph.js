

// $(document).ready(function (){
//     $('#btn-graph').on('click', function(e){
//         e.preventDefault();
//         $.ajax({
//         beforeSend: function(){
//         },
//         url: './grafica',
//         type: 'GET',
//         // data: {},
//         // headers:  {"X-CSRFToken": getCookie("csrftoken")},
//         success: function(resp){
//             console.log('Success, resp:'+resp);
//             document.getElementById("grafica").innerHTML = ''+resp+'';
//         },
//         error: function(jqXHR, estado, error){
//             // Show that function is not correct
//             console.log('Error, err:'+error);
//         },
//         complete: function(jqXHR, estado){
//         },
//         timeout: 10000
            
//         });
              
//     });
// });

$(document).ready(function (){
    $('#btn-graph').on('click', function(e){
        e.preventDefault();
        var fun = $('#funcion').val();
        var iterations = $('#iterations').val();
        var lowerbound = $('#lowerbound').val();
        var upperbound = $('#upperbound').val();
        // console.log('fun:'+fun+';iterations:'+iterations+';lowerbound:'+lowerbound+';upperbound:'+upperbound);
        $( "#grafica" ).load( '/grafica/'+fun+'/'+iterations+'/'+lowerbound+'/'+upperbound, function( response, status, xhr ) {
            if ( status == "error" ) {
                var msg = "Sorry but there was an error: ";
                $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
            }
        });
        console.log('trying to get JSON');
        $.getJSON('./calcular/'+fun+'/'+iterations+'/'+lowerbound+'/'+upperbound, function(data){
            console.log('./calcular/'+fun+'/'+iterations+'/'+lowerbound+'/'+upperbound);
            $('#valorReal').text(data[0].valorReal);
            // Result t,s,r
            $('#tResult').text(data[1].valor);
            $('#sResult').text(data[2].valor);
            $('#rResult').text(data[3].valor);
            // Relative error t,s,r
            $('#tRelError').text(data[1].errorRe);
            $('#sRelError').text(data[2].errorRe);
            $('#rRelError').text(data[3].errorRe);
            // Absolute error t,s,r
            $('#tAbsError').text(data[1].errorAb);
            $('#sAbsError').text(data[2].errorAb);
            $('#rAbsError').text(data[3].errorAb);
        });
        // var objson = $.getJSON('./calcular/'+fun+'/'+iterations+'/'+lowerbound+'/'+upperbound);
        // console.log(objson[0]);
        
        // console.log(typeof(jsondata));
        // var obj = JSON.parse(jsondata);
        
        // console.log(obj[0].valorReal);
        // document.getElementById("grafica").innerHTML = '<object type="text/html" data="grafica?fun='+fun+'&iterations='+iterations+'&lowerbound='+lowerbound+'&upperbound='+upperbound+'" width=100% height=550px></object>';
    });
});


// <script>
	// document.getElementById("graph").innerHTML = '<object type="text/html" data="grafica" width=100% height=550px></object>';

	// function load_home() {
	// 	document.getElementById("graph").innerHTML = '<object type="text/html" data="grafica" width=100% height=550px></object>';
	// }
// </script>