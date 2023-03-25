$( document ).ready(function() {
    $('#firstname').keyup(function () {
        firstname_chek();

    });
    function firstname_chek(){
        var firstname = $('#firstname').val();
        var letter = /^[A-Za-z]+$/;
        if (firstname == '') {
            $('#firstname_val').html("<b>***Enter the name***</b>");
            return false;
        }
        else if (!letter.test(firstname)) {
            $('#firstname_val').html("<b>***Number and special symbol are not allow***</b>");
            return false;
        }
        else if (firstname.length < 5 || firstname.length > 50) {
            $('#firstname_val').html("<b>***Firstname Chacater is between 5 and 50***</b>");
            return false;
        }
        else{
            $('#firstname_val').html(" ");
            return true;
        }
    }
    $('#lastname').keyup(function () {
        lastname_chek();

    });
    function lastname_chek(){
        var lastname = $('#lastname').val();
        var letter = /^[A-Za-z]+$/;
        if (lastname == '') {
            $('#lastname_val').html("<b>***Enter the lastname***</b>");
            return false;
        }
        else if (!letter.test(lastname)) {
            $('#lastname_val').html("<b>***Number and special symbol are not allow***</b>");
            return false;
        }
        else if (lastname.length < 5 || lastname.length > 50) {
            $('#lastname_val').html("<b>***Lastname Chacater is between 5 and 50***</b>");
            return false;
        }
        else{
            $('#lastname_val').html(" ");
            return true;
        }
    }
    $('#username').keyup(function () {
        username_chek();

    });
    function username_chek(){
        var username = $('#username').val();
        var letter = /^(?=.*[0-9])(?=.*[_@])[a-zA-Z0-9_@]{5,10}$/;
        if (username == '') {
            $('#username_val').html("<b>***Enter the username***</b>");
            return false;
        }
        else if (!letter.test(username)) {
            $('#username_val').html("<b>***Alpha and Numeric Character Compulsory and length between 5 to 10***</b>");
            return false;
        }
        else{
            $('#username_val').html(" ");
            return true;
        }
    }
    $('#email').keyup(function () {
        email_chek();

    });
    function email_chek(){
        var email= $('#email').val();
        var letter= /^[a-zA-Z0-9.]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        if (email == '') {
            $('#email_val').html("<b>***Enter the email***</b>");
            return false;
        }
        else if (!letter.test(email)) {
            $('#email_val').html("<b>***Email Not Valid***</b>");
            return false;
        }
        else{
            $('#email_val').html(" ");
            return true;
        }
    }
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
        var firstname=firstname_chek();
        var lastname=lastname_chek();
        var username = username_chek();
        var email = email_chek();
        var password = password_chek();
        var confirmpassword = confirmpassword_chek();
        if (firstname == true && lastname == true && email == true && username == true && password == true && confirmpassword == true){
            return true;

        }
        else{
            return false;
        }
    })
    
});