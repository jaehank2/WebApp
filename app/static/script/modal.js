$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    // $('#task-modal').on('show.bs.modal', function (event) {
    //     const button = $(event.relatedTarget) // Button that triggered the modal
    //     const taskID = button.data('source') // Extract info from data-* attributes
    //     const content = button.data('content') // Extract info from data-* attributes

    //     const modal = $(this)
    //     if (taskID === 'New Task') {
    //         modal.find('.modal-title').text(taskID)
    //         $('#task-form-display').removeAttr('taskID')
    //     } else {
    //         modal.find('.modal-title').text('Edit Task ' + taskID)
    //         $('#task-form-display').attr('taskID', taskID)
    //     }

    //     if (content) {
    //         modal.find('.form-control').val(content);
    //     } else {
    //         modal.find('.form-control').val('');
    //     }
    // })


    $('#submit-task').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: tID ? '/edit/' + tID : '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#submit-task-input').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#submit-edit').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val())
        $.ajax({
            type: 'POST',
            url: '/edit',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#submit-edit-input').val()
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#submit-search').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val())
        console.log("search")
        $.ajax({
            type: 'POST',
            url: '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': $('#submit-search-input').val()
            }),
            success: function (res) {
                console.log(res.response)
                window.open('http://127.0.0.1:5000/search', '_blank');
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#submit-advanced-query').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        $.ajax({
            type: 'POST',
            url: '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': 'advanced'
            }),
            success: function (res) {
                console.log(res.response)
                window.open('http://127.0.0.1:5000/advanced', '_blank');
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.remove').click(function () {
        const remove = $(this)
        $.ajax({
            type: 'POST',
            url: '/delete/' + remove.data('source'),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    // $('.state').click(function () {
    //     const state = $(this)
    //     const tID = state.data('source')
    //     const new_state
    //     if (state.text() === "In Progress") {
    //         new_state = "Complete"
    //     } else if (state.text() === "Complete") {
    //         new_state = "Todo"
    //     } else if (state.text() === "Todo") {
    //         new_state = "In Progress"
    //     }

    //     $.ajax({
    //         type: 'POST',
    //         url: '/edit/' + tID,
    //         contentType: 'application/json;charset=UTF-8',
    //         data: JSON.stringify({
    //             'status': new_state
    //         }),
    //         success: function (res) {
    //             console.log(res)
    //             location.reload();
    //         },
    //         error: function () {
    //             console.log('Error');
    //         }
    //     });
    // });

});