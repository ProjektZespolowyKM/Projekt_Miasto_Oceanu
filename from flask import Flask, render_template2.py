<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rejestracja - Kres Oceanu</title>
</head>
<body>
    <h1>Rejestracja - Kres Oceanu</h1>
    <form action="/signup" method="post">
        <label for="username">Nazwa użytkownika:</label><br>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Hasło:</label><br>
        <input type="password" id="password" name="password" required><br><br>
        <input type="submit" value="Zarejestruj">
    </form>
</body>
</html>

