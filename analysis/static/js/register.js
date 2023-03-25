$( document ).ready(function() {
    $('#name').keyup(function () {
        name_chek();

    });
    function name_chek(){
        var name = $('#name').val();
        var letter = /^[A-Za-z]+$/;
        if (name == '') {
            $('#name_val').html("<b>***Enter the name***</b>");
            return false;
        }
        else if (!letter.test(name)) {
            $('#name_val').html("<b>***Number and special symbol are not allow***</b>");
            return false;
        }
        else if (name.length < 5 || name.length > 50) {
            $('#name_val').html("<b>***Name Chacater is between 5 and 50***</b>");
            return false;
        }
        else{
            $('#name_val').html(" ");
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
    $('#experience').keyup(function () {
        experience_chek();

    });
    function experience_chek(){
        var experience= $('#experience').val();
        var letter=/^[0-9]+$/;
        if (experience == '') {
            $('#experience_val').html("<b>***Enter the experience***</b>");
            return false;
        }
        else if (!letter.test(experience)) {
            $('#experience_val').html("<b>***Experience not valid***</b>");
            return false;
        }
        else if(experience.length>2){
            $('#experience_val').html("<b>***Experience length must be 2 digit*** </b>");
            return false;
        }
        else{
            $('#experience_val').html(" ");
            return true;
        }
    }
    $('#position').keyup(function () {
        position_chek();

    });
    function position_chek(){
        var position= $('#position').val();
        var letter=/^[A-Za-z]+$/;
        if (position == '') {
            $('#position_val').html("<b>***Enter the  Position***</b>");
            return false;
        }
        else if (!letter.test(position)) {
            $('#position_val').html("<b>***Position Not Valid***</b>");
            return false;
        }
        else if(position.length<=5){
            $('#position_val').html("<b>***Enter Valid Position***</b>");
            return false;
        }
        else{
            $('#position_val').html(" ");
            return true;
        }
    }
    $("#save_btn").on("click",function(){
       name_err=name_chek()
       email_err=email_chek()
       experience_err=experience_chek()
       position_err=position_chek()
       if (name_err && email_err && experience_err && position_err){
         return true

       }
       else{
         return false
       }         
    })
});

