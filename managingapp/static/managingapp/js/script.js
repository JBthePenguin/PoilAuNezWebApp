$('#form-part').hide();

// Ajax request to choose the good form 
function DisplayForm(actu_id, csrf_token) {
    $.ajax({
        type: 'POST',
        url: '/manager/actus/',
        data: {
            'delete': false,
            'actu_id': actu_id,
            'csrfmiddlewaretoken': csrf_token
        },
        success: function (data) {
            // append form to template html
            $('#form-ajax').html(data);
            if (actu_id == 'add') {
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

function DeleteConfirm(actu_id) {
    r = confirm("Confirmer")
    if (r == true) {
        url = "/manager/actus/delete_actu/" + actu_id;
        $.get(url, function(data){
            alert(data);
            location.reload();
        });
    }
}
