$(document).ready(function() {


  function registrar(){
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8000/login/signup/",
      data: {
        login:'bruna',
        email:'brua@',
        senha: '123',
        tipoUser: 'Consumidor',
      },
      success: function(result) {
        console.log(result);
      },
      error: function(result) {
        console.log(result);
      }
    });
  }

  function logar(){
    $.ajax({
      type: "GET",
      url: "http://127.0.0.1:8000/login/signin/",
      data: {
        login:'bruna',
        senha: '123',
      },
      success: function(result) {
        console.log(result);
      },
      error: function(result) {
        console.log(result);
      }
    });
  }


  $('#signup').click(function() {
    registrar();
  });

  $('#signin').click(function() {
    ();
  });

});
