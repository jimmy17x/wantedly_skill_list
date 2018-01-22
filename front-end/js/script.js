 $(document).ready(function() {

    $('#knklkjlkljk').click(function() {
      $.ajax({
        type: 'GET',
        url: '/api/profile',
        beforeSend: function(xhr) {
          if (localStorage.token) {
            xhr.setRequestHeader('Authorization', 'JWT ' + localStorage.token);
          }
        },
        success: function(data) {
          alert('Hello ' + data.name + '! You have successfully accessed to /api/profile.');
        },
        error: function() {
          alert("Sorry, you are not logged in.");
        }
      });
    });

    //login function 
    $('#log-in').click(function() {

      var username = $("#username").val();
      var password = $("#password").val();

      if(!username || !password)
      {
        alert("Please enter username and password");
        return;
      }

      $.ajax({
        type: "POST",
        url: "http://localhost:8000/rest-auth/login/",
        data: {
          username: username,
          password: password
        },
        success: function(data) {
          localStorage.token = data.token;
          alert('Got a token from the server! Token: ' + data.token);
        },
        error: function() {
          alert("Login Failed , please try again !");
        }
      });
    });
    $('#logout').click(function() {
      localStorage.clear();
    });
  });