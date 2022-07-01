<?php
$conn = new mysqli('db', 'sql', 'password', 'admin_site');

// select query
if ($_SERVER["REQUEST_METHOD"] == "GET") {
    $user = $_GET['user'];
    $pass = $_GET['pass'];
    $sql = "SELECT id FROM users WHERE username = '$user' AND password = '$pass'";
    $result = mysqli_query($conn,$sql);
    $count = mysqli_num_rows($result);
    if($count != 0) {
        echo "Logged in!";
    } else {
        echo "Incorrect username or password!";
    }
}
?>
