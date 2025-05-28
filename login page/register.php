<?php
if (isset($_POST['submit'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $email = $_POST['email'];

    // Write data to CSV file
    $file = fopen("users.csv", "a");
    fputcsv($file, array($username, $password, $email));
    fclose($file);

    // Redirect back to the registration form
    header("Location: registration.html");
    exit();
}
?>