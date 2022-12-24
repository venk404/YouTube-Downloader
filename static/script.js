jQuery(document).ready(function(){
    $('#all_middle_div').hide();
    $("#thumbnail").hide();
    $("#loader").hide();
});



function showVideo() {
    var videoUrl = document.getElementById("videoUrl").value
    if (document.getElementById("videoUrl").value == "") {
        alert("please paste the youtube link");
        $('#all_middle_div').hide();
        $("#loader").hide();
        return false;
    } 
        $("#loader").show();
     
    
        setTimeout(async () => {
            let regex = /(youtu.*be.*)\/(watch\?v=|embed\/|v|shorts|)(.*?((?=[&#?])|$))/gm;
           
            
             //this scrolldown
            
            let result = regex.test(videoUrl);
            if(!result)
            {
                alert("Youtube Link Format Is Incorrect")
                $('#all_middle_div').hide();
                $("#loader").hide();
                $('#videoUrl').val('');
                return false;
            }
            // var myWord = 'shorts';
            // if(new RegExp('\\b' + myWord + '\\b').test(videoUrl)){
                $('#all_middle_div').show();
                $("#thumbnail").show();
                var entry1 = $('#videoUrl').val();
            $.ajax({
                url: '/api/thumbnail', 
                type: 'GET',
                async:false,
                data:{entry1_id: entry1},
                datatype:'json',
                contentType:'json',
                success: function(response){
                    document.getElementById("thumbnail").src=response[0];
                    document.getElementById("titletext").innerHTML = response[1];
        
        
                }
            })
            fillformat();
            $('html,body').animate({scrollTop: document.body.scrollHeight},"slow"); 
  
}, 0);
    
    
}



function fillformat()
{
    var entry1 = $('#videoUrl').val();
    $.ajax({
        url: '/api/fillformat', 
        type: 'GET',
        async:false,
        data:{entry1_id: entry1},
        datatype:'json',
        contentType:'json',
        success: function(response){
            $('#format').find('option').not(':first').remove();
            $.each(response, function (index, value) {
                $('#format').append($('<option/>', { 
                    value: value,
                    text : index, 
                }));
              });
              $("#loader").hide();
  
        }     
});
}


function download()
{ 
    
        if (document.getElementById("format").value == 'Select Video Format') {   //use this method for return false
            alert("Please Select Format");
            return false;
        }
        p1_value = $('#format').val(); // Or wherever the value is coming from...
        p2_value = $('#videoUrl').val();
        url = "/api/download?entry_id=" + p1_value + "&entry1_id=" + p2_value;
        window.location.href = url;                       
    
    
}








