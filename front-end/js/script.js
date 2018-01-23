 function redirectIfNotLoggedIn()
 {

    if(localStorage.token)
    {
       activateProfileDiv();
       getUserSkills(); // get user skills and set the profile of user

    }else
    {
      activateLoginDiv();
    }

 }

function hideAllContent()
{
  $(".content").hide();
}

function activateProfileDiv()
{
  // activate profile div and hide others
  hideAllContent();
  $("#user-profile").show();
}
function activateLoginDiv()
{
  hideAllContent();
  $("#home-page").show();
}

function somethingWentWrongHandler()
{

   alert("Something went wrong , please try again !");
   redirectIfNotLoggedIn();
}

function clearLocalStorage()
{
  localStorage.clear();
}


function getUserSkills()
{
  var user = JSON.parse(localStorage.user);
  console.log("user pk : " + user.pk);
  if(!user)
  {
    somethingWentWrongHandler();
    return;
  }

   $.ajax({
        type: 'GET',
        url: 'http://127.0.0.1:8000/api/v1/user/skills/'+user.pk,
        beforeSend: function(xhr) {
          if (localStorage.token) {
            xhr.setRequestHeader('Authorization', 'JWT ' + localStorage.token);
          }
        },
        success: function(data) {
          alert('Hello ' + data );
        },
        error: function() {
            somethingWentWrongHandler();
        }
      });
}

 $(document).ready(function() {

    // pace plugin setup - ajax loader
    $(document).ajaxStart(function() { Pace.restart(); });

    redirectIfNotLoggedIn();

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

          //save JWT token
          localStorage.token = data.token;
          localStorage.user = JSON.stringify(data.user); 

          activateProfileDiv();
          getUserSkills();
        },
        error: function() {
          alert("Login Failed , please try again !");
        }
      });
    });

    $('#logout').click(function() {
        clearLocalStorage();
    });
  });