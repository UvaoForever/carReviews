document.getElementById('addComment').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем перезагрузку страницы
    console.log('Работает');

    // Получаем данные пользователя из формы
    const userData = {
        login: document.getElementsByName('login').value,
        password: document.getElementsByName('password').value
    };

    // Отправляем POST-запрос для получения токена
    axios.post('http://localhost:8000/api/token/', userData)
        .then(response => {
            // Здесь будет токен пользователя
            const accessToken = response.data.access;
            const refreshToken = response.data.refresh;

            console.log('Access Token:', accessToken);
            console.log('Refresh Token:', refreshToken);

            // Теперь вы можете использовать accessToken для дальнейших запросов
        })
        .catch(error => {
            console.error('Error getting the token:', error);
        });
});