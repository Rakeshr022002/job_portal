let password_icon=document.getElementById("passwordicon");
let password=document.getElementById("password");

password_icon.onclick=function()
{
    if(password.type == "password")
        {
            password.type="text";
            password_icon.src="static/images/show eye.png";
        }
       else
        {
            password.type="password";
            password_icon.src="static/images/hidden eye.png";
        }
}

let con_password_icon=document.getElementById("conpasswordicon");
let con_password=document.getElementById("conpassword");

con_password_icon.onclick=function()
{
    if(con_password.type == "password")
        {
            con_password.type="text";
            con_password_icon.src="static/images/show eye.png";
        }
       else
        {
            con_password.type="password";
            con_password_icon.src="static/images/hidden eye.png";
        }
}


function clickcheckbox(){
    var checkbox=document.getElementById("checkbox");
    checkbox.checked =!checkbox.checked;
}