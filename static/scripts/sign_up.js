function EmailFoucs() {
    $("#EmailLable").addClass("login-lable-top"); 
}

function EmailBlur() {
    let email = $("#Email").val();  
    if(email == ""){
        $("#EmailLable").removeClass("login-lable-top");
    }
}

function FirstNameFoucs() {
    $("#FirstNameLable").addClass("login-lable-top");
}

function FirstNameBlur() {
    let firstName = $("#FirstName").val();
    if(firstName == ""){
        $("#FirstNameLable").removeClass("login-lable-top");
    }
}

function LastNameFoucs() {
    $("#LastNameLable").addClass("login-lable-top");
}

function LastNameBlur() {
    let lastName = $("#LastName").val();
    if(lastName == ""){
        $("#LastNameLable").removeClass("login-lable-top");
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
    let firstName = $("#FirstName").val();
    let lastName = $("#LastName").val();
    let email = $("#Email").val();
    let password = $("#Password").val();
    let allow = true;
    if(firstName == ""){
        $("#FirstNameError").removeClass("login-error-hide");
        allow = false;
    }
    else{
        $("#FirstNameError").addClass("login-error-hide");
    }

    if(lastName == ""){
        $("#LastNameError").removeClass("login-error-hide");
        allow = false;
    }
    else{
        $("#LastNameError").addClass("login-error-hide");
    }

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
        document.getElementById('Register_Form').submit();
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