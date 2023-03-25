$( document ).ready(function() {
    $("#save").on('click',function(){
        var data = [];
        for (let i = 1; i < 80; i+=2) {
            $.each($(`input[name='ques_${i}']:checked`), function(){            
                data.push($(this).val());
                
            });
        }
        
        if (data.length == 40) {
            return true;
        }
        else{
            $('#question_val').html("<br><b>***PLEASE FILL THE ALL QUESTION***</b>");
            return false;
        }
    });
    
    
});