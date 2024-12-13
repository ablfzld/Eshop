function EmailFoucs() {
    $("#EmailLable").addClass("login-lable-top"); 
}

function EmailBlur() {
    let email = $("#Email").val();  
    if(email == ""){
        $("#EmailLable").removeClass("login-lable-top");
    }
}

function PasswordFoucs() {
    $("#PasswordLable").addClass("login-lable-top"); 
}

function PasswordBlur() {
    let email = $("#Password").val();  
    if(email == ""){
        $("#PasswordLable").removeClass("login-lable-top");
    }
}


function FormSubmit() {
    let email = $("#Email").val();
    let password = $("#Password").val();
    let allow = true;
    if(email == ""){
        $("#EmailError").removeClass("login-error-hide");
        allow = false;
    }
    else{
        $("#EmailError").addClass("login-error-hide");
    }

    if(password == ""){
        $("#PasswordError").removeClass("login-error-hide");
        allow = false;
    }
    else{
        $("#PasswordError").addClass("login-error-hide");
    }

    if(allow){
        document.getElementById('Login_Form').submit();
    }
}

var passtype = "password";
function ShowPassword() {
    if(passtype == 'password')
    {
        $("#Password").get(0).type="text";
        passtype = "text";
    }
    else
    {
        $("#Password").get(0).type="password";
        passtype = "password";
    }
}