
var SESSION_EXPIRE_STATUS ="Signature has expired."; //TO_DO change to status number overriding defsult django text
var HOST = "http://softxide.pythonanywhere.com";
var TTL_DEDICATED_SKILLS = 1000; // total number of top votes skills which should have dedicated rows



function setUpProfileSkills(data)
{
  // sort the skills data as per total number of upvotes in descending order
  data.sort(function(skill_a,skill_b)
    {
      return  skill_b.skill_upvotes.length - skill_a.skill_upvotes.length;
    })

    var i = 0 ,ttl_skills = data.length;

    var html="";

    while( i < ttl_skills && i < TTL_DEDICATED_SKILLS)
    {
      html +="<div class = 'skill-dedicated-row'> \
                       <span class = 'upvote-count' id = 'skill-id-"+data[i].skill_id+"'>"+data[i].skill_upvotes.length + "</span><span class = 'row-skill-name'>" +data[i].skill_name + "</span>\
                       <hr class = 'skill-row-hr'>";

       // for each skill get the user who upvoted it  
        html += " <div class = 'user-who-upvoted'>";
       //TO_DO handle dom if user upvoting skill exceeds the width of row

       for(var j = 0 ; j < data[i].skill_upvotes.length; ++j)
       {
         html+="<img class = 'userupvote-by' id = 'user-"+data[i].skill_upvotes[j].upvote_by
             +"' data-user-info= '" + data[i].skill_upvotes[j].upvote_by_username +  "' src = '"+data[i].skill_upvotes[j].upvote_by_user_image+"' >"
         
                    
       }

      
      html+="   </div><!-- user who upvoted ends here --> \
             </div> <!-- skill-dedicated-row ends here -->";       

      ++i;
    } 

    $(".skills-section").append(html);
}


 function redirectIfNotLoggedIn()
 {
    // get user skills and set the profile of user
    if(localStorage.token)
    {
       getUserSkills(function(data)
       {
          activateProfileDiv();
          showDOMElementsAsPerSession(true);
          setUpProfileSkills(data);
       }); 


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
  // delete user skill rows
  $(".skill-dedicated-row").remove();
  $("#user-profile").show();
  //update username of profile 
  var user = JSON.parse(localStorage.user);
  $("#profile-heading").text("What " +user.username + " is good at");

}
function activateLoginDiv()
{
  hideAllContent();
  $("#home-page").show();
}

function somethingWentWrongHandler()
{

  $.alert({
    title: 'Alert!',
    content: 'Something went wrong , please try again !',
    useBootstrap: false
  });
   redirectIfNotLoggedIn();
}

function clearLocalStorage()
{
  localStorage.clear();
}

/**************  end point calls ***************************/

//get user skills with upvote info
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
        url: HOST+'/api/v1/user/skill/upvotes/'+user.pk,
        beforeSend: function(xhr) {
          if (localStorage.token) {
            xhr.setRequestHeader('Authorization', 'JWT ' + localStorage.token);
          }
        },
        success: function(data) {
          if(callback)
            callback(data);
        },
        error: function(data) {

            if(!data.responseJSON  || data.responseJSON.detail === SESSION_EXPIRE_STATUS)
            {

                $.alert({
                  title: 'Logged out !',
                  content: 'Please login again !',
                  useBootstrap: false
                });
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
         $.alert({
                  title: 'Alert',
                  content: 'Please provide all details',
                  useBootstrap: false
                });
        return;
      }

      $.ajax({
        type: "POST",
        url: HOST+"/rest-auth/login/",
        data: {
          username: username,
          password: password
        },
        success: function(data) {

          //save JWT token
          localStorage.token = data.token;
          localStorage.user = JSON.stringify(data.user); 

          //callback after getting user skills

          getUserSkills( function (data){
              activateProfileDiv();
              showDOMElementsAsPerSession(true);
              setUpProfileSkills(data);
          } );
        },
        error: function() {
           $.alert({
                  title: 'Log in failed ',
                  content: 'Please login again !',
                  useBootstrap: false
                });
        }
      });
    });

    $('#logout').click(function() {
        clearLocalStorage();
        activateLoginDiv();
        showDOMElementsAsPerSession(false);
    });

  
  });