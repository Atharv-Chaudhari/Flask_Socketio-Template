# Flask_Socketio-Template

Update Content on Frontend Asynchronously using socket


Alternate way to perform such tasks is using ajax 

POST data to flask without reloading frontend page :-
#todo-form is id of form on frontend
```js
    <script type="text/javascript">
        $(document).on('submit', '#todo-form', function (e) {
            console.log('data from frontend');
            e.preventDefault();
            $.ajax({
                type: 'POST',
                url: '/',
                data: {
                    todo: $("#todo").val()
                },
                success: function () {
                    console.log('data sent to flask');
                }
            })
        });
    </script>
```

GET data from flask to Frontend without reloading page :- 

```js 
    function yourFunction() {
            fetch(`/result`)
                .then(function (response) {
                    return response.text();
                }).then(function (text) {
                    console.log('GET response text:');
                    text = JSON.parse(text);
                 }
     }
```

Above stuff will take data only once which may even work before flask sends data so we have to add timeout

```js 
    function yourFunction() {
            fetch(`/result`)
                .then(function (response) {
                    return response.text();
                }).then(function (text) {
                    console.log('GET response text:');
                    text = JSON.parse(text);
                 }
     }
     function getdata(){
            setTimeout( function() { yourFunction(); }, 4000);
        }
```

we can call getdata() function onload in body tag so it will try to get data after 4 sec of loading page or somewhere else like clicking button so data will be retrieved after 4 sec of clicking on button

If we have to retrive data after every 4 sec then
```js 
    function yourFunction() {
            fetch(`/result`)
                .then(function (response) {
                    return response.text();
                }).then(function (text) {
                    console.log('GET response text:');
                    text = JSON.parse(text);
                 }
          setTimeout(yourFunction, 4000);
     }
```


Reference :- https://stackoverflow.com/questions/43599537/python-flask-date-update-real-time
