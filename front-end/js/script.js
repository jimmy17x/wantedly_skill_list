
var SESSION_EXPIRE_STATUS ="Signature has expired."; //TO_DO change to status number overriding defsult django text
var HOST = "http://127.0.0.1:8000";

 function redirectIfNotLoggedIn()
 {

    if(localStorage.token)
    {
       activateProfileDiv();
       getUserSkills(); // get user skills and set the profile of user

    }else
    {
      activateLoginDiv();
      showDOMElementsAsPerSession(false);
    }

 }
   function showDOMElementsAsPerSession(isVisible)
    {
      $('#logout').hide();

      if(isVisible)
      {
         $('#logout').show();
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

/**************  end point calls ***************************/
function getUserSkills(callback)
{
  var user = JSON.parse(localStorage.user);
  if(!user)
  {
    somethingWentWrongHandler();
    return;
  }

   $.ajax({
        type: 'GET',
        url: HOST+'/api/v1/user/skills/'+user.pk,
        beforeSend: function(xhr) {
          if (localStorage.token) {
            xhr.setRequestHeader('Authorization', 'JWT ' + localStorage.token);
          }
        },
        success: function(data) {
          if(callback)
            callback();
        },
        error: function(data) {

            if(data.responseJSON.detail === SESSION_EXPIRE_STATUS)
            {
                alert("You have been logged out , please login again");
                activateLoginDiv();
                clearLocalStorage();
                return;
            }

            somethingWentWrongHandler();
        }
      });
}


/**************  end point calls  ends here***************************/


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

          //callback after getting user skills
          getUserSkills( function (){
              activateProfileDiv();
              showDOMElementsAsPerSession(true)
          } );
        },
        error: function() {
          alert("Login Failed , please try again !");
        }
      });
    });

    $('#logout').click(function() {
        clearLocalStorage();
        activateLoginDiv();
        showDOMElementsAsPerSession(false);
    });

  
  });