# Flask_Socketio-Template

Update Content on Frontend Asynchronously using socket


Alternate way to perform such tasks is using ajax 
POST data to flask without reloading frontend page :-
```js
    <script type="text/javascript">
        $(document).on('submit', '#todo-form', function (e) {
            console.log('Code Received at ajax');
            e.preventDefault();
            $.ajax({
                type: 'POST',
                url: '/',
                data: {
                    todo: $("#todo").val()
                },
                success: function () {
                    console.log('Code sent to flask');
                    // alert("Code Added To Redeem");
                }
            })
        });
    </script>
```js
