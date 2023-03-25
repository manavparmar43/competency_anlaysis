
$('#password').keyup(function () {
    password_chek();
});
function password_chek() {
    var password = $('#password').val();
    var pattern = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{5,10}$/;

    if (password == '') {
        $('#password_val').html("<b>***Enter the password***</b>");
        return false;
    }
    else if (password.length < 8 || password.length > 20) {
        $('#password_val').html("<b>***Password Chacater is between 5 and 10***</b>");
        return false;
    }
    else if (!pattern.test(password)) {
        $('#password_val').html("<b>***Alpha and Numeric Character Compulsory*** </b>");
        return false;
    }
    else {
        $('#password_val').html("");
        return true;
    }


}
$('#confirmpassword').keyup(function () {
    confirmpassword_chek();
});
function confirmpassword_chek() {
    var confirmpassword = $('#confirmpassword').val();
    var password = $('#password').val();


    if (confirmpassword == '') {
        $('#confirmpassword_val').html("<b>***Enter the Confirmpassword***</b>");
        return false;


    }
    else if (password != confirmpassword) {
        $('#confirmpassword_val').html("<b>***Password not match*** </b>");
        return false;
    }

    else {
        $('#confirmpassword_val').html("");
        return true;
    }


}
$('#save').on('click',function () {
    var password = password_chek();
    var confirmpassword = confirmpassword_chek();
    if ( password == true && confirmpassword == true){
        return true;

    }
    else{
        return false;
    }
})



