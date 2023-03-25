

$('#edit').on('click',function(){
    $('#firstname').removeAttr('readonly');
    $('#firstname').removeAttr('style');
    $('#firstname').removeAttr('title');
    $('#lastname').removeAttr('readonly');
    $('#lastname').removeAttr('style');
    $('#lastname').removeAttr('title');
    $('#username').removeAttr('readonly');
    $('#username').removeAttr('style');
    $('#username').removeAttr('title');
    $('#email').removeAttr('readonly');
    $('#email').removeAttr('style');
    $('#email').removeAttr('title');
    $('#choice').removeAttr('disabled');
    $('#choice').removeAttr('style');
    $('#choice').css({"height": "50px", "width": "100%", "border-radius":"4px" ,"background-color": "white", "border-color": "lightgrey"})
    $('#choice').removeAttr('title');
    $('#edit_div').html("");
    $('#edit_div').append(` <button class="btn btn--radius-2 btn--blue" type="submit"id="save">Save</button>`)
}); 
