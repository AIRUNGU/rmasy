var attempt=3; //variable to the number of attempts
//Below function executes on click of login button.
function validate(form){
		if(form.username.value=="test" && form.password.value=="123"){
			alert("Login successfully");
			window.location="home.html"; //Redirecting to other page. return false
		} else {
			attempt--; //Decrementing by one.
			alert("You have"+attempt+"attempt;");
			//Disabling the fields after 3 attempts
				if(attempt==0){
					document.getElementById("username").disabled=true;
					document.getElementById("password").disabled=true;
					document.getElementById("submit").disabled=true;
					return false;

				}
		}

}