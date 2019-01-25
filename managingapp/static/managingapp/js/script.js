$('#form-part').hide();

// Ajax request to choose the good form 
function DisplayForm(url, object_id, csrf_token) {
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'object_id': object_id,
            'csrfmiddlewaretoken': csrf_token
        },
        success: function (data) {
            // append form to template html
            $('#form-ajax').html(data);
            if (object_id == 'add') {
                $('#btn-form-add-mod').html('Ajouter');
            }
            else {
                $('#btn-form-add-mod').html('Modifier');
            }
            $('#form-part').show();
            $('html, body').animate(
                {scrollTop: $('#form-part').offset().top },
                'slow'
            );
        },
        error: function(xhr, status, e) {
            alert(status, e);
        }
    });
}

function DeleteConfirm(kind, object_id) {
    r = confirm("Confirmer")
    if (r == true) {
        url = "/manager/" + kind + "/delete/" + object_id;
        $.get(url, function(data){
            alert(data);
            location.reload();
        });
    }
}
