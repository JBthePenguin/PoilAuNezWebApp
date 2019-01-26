$('#form-part').hide();
$('#display-message').hide();

// Ajax request to choose and display the good form 
function DisplayForm(url, object_id, csrf_token) {
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'action': 'display_form',
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

// Ajax request to display the good message
function DisplayMessage(message_id, csrf_token) {
    $.ajax({
        type: 'POST',
        url: "/manager/message/",
        data: {
            'action': 'display_message',
            'message_id': message_id,
            'csrfmiddlewaretoken': csrf_token
        },
        success: function (data) {
            // append message to template html
            $('#contact_name').html(data['contact_name']);
            $('#contact_email').html(data['contact_email']);
            $('#date').html(data['date']);
            $('#subject').html(data['subject']);
            $('#content').html(data['content']);
            $('#display-message').show();            
            $('html, body').animate(
                {scrollTop: $('#display-message').offset().top },
                'slow'
            );
        },
        error: function(xhr, status, e) {
            alert(status, e);
        }
    });
}

// Confirm delete before Ajax request to do it
function DeleteConfirm(url, object_id, csrf_token) {
    r = confirm("Confirmer")
    if (r == true) {
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'action': 'delete',
                'object_id': object_id,
                'csrfmiddlewaretoken': csrf_token
            },
            success: function (data) {
                alert(data);
                location.reload();
            },
            error: function(xhr, status, e) {
            alert(status, e);
            }
        });
    }
}
